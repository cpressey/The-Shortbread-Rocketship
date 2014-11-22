#!/usr/bin/env python

from array import array
import cPickle as pickle
import gc
import math
import mmap
import operator
from optparse import OptionParser
import random
import struct
import sys
import wave

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x


class BackingStore(object):
    pass


class ArrayLevelBackingStore(BackingStore):
    def __init__(self, size=0, data=None):
        if data is None:
            data = [0.0] * size
        self.map = array('d', data)

    def __setitem__(self, x, level):
        self.map[x] = level

    def __getitem__(self, x):
        return self.map[x]

    def __len__(self):
        return len(self.map)

    def rotate(self, samples):
        self.map = self.map[-samples:] + self.map[0:-samples]

    def concat(self, store):
        assert isinstance(store, ArrayLevelBackingStore)
        # returns a new BackingStore
        return ArrayLevelBackingStore(data=self.map + store.map)


class ListLevelBackingStore(BackingStore):
    def __init__(self, size=0, data=None):
        if data is None:
            data = [0.0] * size
        self.map = data

    def __setitem__(self, x, level):
        self.map[x] = level

    def __getitem__(self, x):
        return self.map[x]

    def __len__(self):
        return len(self.map)

    def rotate(self, samples):
        self.map = self.map[-samples:] + self.map[0:-samples]

    def concat(self, store):
        assert isinstance(store, ListLevelBackingStore)
        # returns a new BackingStore
        return ListLevelBackingStore(data=self.map + store.map)


class MmapLevelBackingStore(BackingStore):
    def __init__(self, size=0, data=None):
        self.size = size
        if size > 0:
            self.map = mmap.mmap(-1, size * 8)
        else:
            self.map = ()

    def __setitem__(self, x, level):
        p = x * 8
        self.map[p:p+8] = struct.pack('d', level)

    def __getitem__(self, x):
        p = x * 8
        return struct.unpack('d', self.map[p:p+8])[0]

    def __len__(self):
        return self.size

    def rotate(self, samples):
        blocksize = samples * 8
        back = self.map[-blocksize:]
        self.map[blocksize:] = self.map[:-blocksize]
        self.map[:blocksize] = back

    def concat(self, store):
        # returns a BackingStore, which may be new.
        if len(self) == 0:
            return store
        n = MmapLevelBackingStore(self.size + len(store))
        for i in xrange(0, self.size):
            n[i] = self[i]
        for i in xrange(self.size, len(store)+self.size):
            n[i] = store[i-self.size]
        return n


class BaseWav(object):
    pass


class Wav(BaseWav):

    def __init__(self, **kwargs):
        self.framerate = kwargs.get('framerate', 44100)
        self.sampwidth = kwargs.get('sampwidth', 2)
        self.nchannels = kwargs.get('nchannels', 2)
        self.storage = kwargs.get('storage', ListLevelBackingStore)
        nframes = kwargs.get('nframes', 0)
        self.levels = self.storage(size=nframes)

    @property
    def nframes(self):
        return len(self.levels)

    @property
    def framesize(self):
        return self.nchannels * self.sampwidth

    @property
    def duration(self):
        return self.nframes / float(self.framerate)

    @classmethod
    def load(cls, filename, **kwargs):
        inp = wave.open(filename)
        kwargs['framerate'] = inp.getframerate()
        kwargs['sampwidth'] = inp.getsampwidth()
        if kwargs['sampwidth'] != 2:
            raise NotImplementedError
        kwargs['nchannels'] = inp.getnchannels()
        nframes = inp.getnframes()
        kwargs['nframes'] = nframes
        wav = Wav(**kwargs)
        frames = inp.readframes(nframes)

        print 'decoding %s frames (%s)...' % (
            nframes, len(frames)
        )
        for x in tqdm(xrange(0, nframes)):
            p = x * wav.framesize
            chanwords = []
            for chan in xrange(0, wav.nchannels):
                chanwords.append(
                    frames[p + wav.sampwidth * chan:p + wav.sampwidth * (chan+1)]
                )
            chanlevels = [
                struct.unpack('<h', word)[0] / 32767.0
                for word in chanwords
            ]
            level = sum(chanlevels) / (wav.nchannels * 1.0)
            wav.levels[x] = level

        inp.close()
        return wav

    @classmethod
    def unpickle(cls, filename):
        with open(filename, 'r') as f:
            return pickle.load(f)

    def save(self, filename):
        out = wave.open(filename, 'w')
        out.setframerate(self.framerate)
        out.setsampwidth(self.sampwidth)
        out.setnchannels(self.nchannels)
        out.setnframes(1)  # len(self.levels)

        print 'rendering %s levels...' % len(self.levels)
        assert self.sampwidth == 2
        frames = []
        for x in tqdm(xrange(0, len(self.levels))):
            for c in xrange(0, self.nchannels):
                frames.append(struct.pack('<h', int(self.levels[x] * 32767)))

        out.writeframes(''.join(frames))
        out.close()

    def pickle(self, filename):
        with open(filename, 'w') as f:
            pickle.dump(self, f)

    def dump(self):
        print 'framerate:', self.framerate
        print 'sampwidth:', self.sampwidth
        print 'nchannels:', self.nchannels
        print 'nframes:', self.nframes
        #print inp.getnchannels() * inp.getnframes() * inp.getsampwidth()  # near filesize
        print 'framesize:', self.framesize
        print 'duration:', self.duration, 'seconds'

    # mutators

    def downsample(self, framerate):
        step = self.framerate / float(framerate)
        new_size = int(len(self.levels) / step)
        levels = self.storage(size=new_size)
        for x in xrange(0, new_size):
            levels[x] = self.levels[int(x * step)]
        self.framerate = framerate
        self.levels = levels

    def scale_amplitude(self, factor):
        for x in xrange(0, len(self.levels)):
            self.levels[x] = self.levels[x] * factor

    def fade_sine(self):
        factor = math.pi / len(self.levels)
        for x in xrange(0, len(self.levels)):
            self.levels[x] *= math.sin(x * factor)

    def extend(self, wav):
        assert self.sampwidth == wav.sampwidth
        assert self.framerate == wav.framerate
        #assert self.nchannels
        self.levels = self.levels.concat(wav.levels)

    def amplify(self):
        min_level = 0.0
        max_level = 0.0
        for level in levels:
            min_level = min(min_level, level)
            max_level = max(max_level, level)

        max_abs_level = max(max_level, math.abs(min_level))
        amp_level = 1 / max_abs_level
        print amp_level, '%%%%%%'
        self.scale_amplitude(amp_level)

    def rotate(self, dur):
        # take dur seconds off the back, move to the front
        samples = int(float(dur) * self.framerate)
        self.levels.rotate(samples)

    def blank(self, pos, dur):
        pos = int(float(pos) * self.framerate)
        samples = int(float(dur) * self.framerate)
        for i in xrange(pos, pos+samples):
            self.levels[i] = 0.0

    # return new wavs

    def random_crop(self, seconds):
        samples = int(float(seconds) * self.framerate)
        start = random.randint(0, len(self.levels) - samples)
        
        new = Wav(
            storage=self.storage,
            framerate=self.framerate,
            sampwidth=self.sampwidth,
            nchannels=self.nchannels,
            nframes=samples,
        )

        for x in xrange(start, start+samples):
            new.levels[x-start] = self.levels[x]

        return new


class OutputWav(BaseWav):

    def __init__(self, filename, **kwargs):
        self.framerate = kwargs.get('framerate', 44100)
        self.sampwidth = kwargs.get('sampwidth', 2)
        self.nchannels = kwargs.get('nchannels', 2)
        self.storage = kwargs.get('storage', ListLevelBackingStore)

        self.filename = filename
        out = wave.open(filename, 'w')
        out.setframerate(self.framerate)
        out.setsampwidth(self.sampwidth)
        out.setnchannels(self.nchannels)
        out.setnframes(1)  # len(self.levels)
        self.out = out

    def close(self):
        self.out.close()

    def extend(self, wav):
        self.extend_levels(wav.levels)

    def extend_levels(self, levels):
        #print 'rendering %s levels...' % len(levels)

        frames = []
        for x in xrange(0, len(levels)):
            for c in xrange(0, self.nchannels):
                frames.append(struct.pack('<h', int(levels[x] * 32767)))
            if len(frames) > 10000:
                self.out.writeframes(''.join(frames))
                frames = []        

        self.out.writeframes(''.join(frames))

    def extend_silence(self, dur):
        samples = int(float(dur) * self.framerate)
        zeroframe = struct.pack('<h', 0)

        frames = []
        for x in xrange(0, samples):
            for c in xrange(0, self.nchannels):
                frames.append(zeroframe)
            if len(frames) > 10000:
                self.out.writeframes(''.join(frames))
                frames = []        

        self.out.writeframes(''.join(frames))

    def mix(self, wavs):
        for wav in wavs:
            assert wav.nframes == wavs[0].nframes
            #assert wav.sampwidth == wavs[0].sampwidth
            assert wav.framerate == wavs[0].framerate

        levels = []
        num = float(len(wavs))
        for x in xrange(0, n.nframes):
            #level = reduce(operator.mul, [w.levels[x] for w in wavs], 1)
            level = reduce(operator.add, [w.levels[x] for w in wavs], 1) / num
            level = min(1.0, level)
            level = max(-1.0, level)
            levels.append(level)
        
        self.extend_levels(levels)
