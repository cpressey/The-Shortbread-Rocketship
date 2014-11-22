#!/usr/bin/env python

import gc
from optparse import OptionParser
import os
import random
import sys

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x

from longwave import Wav, OutputWav, ListLevelBackingStore


def carpet(wavs, output_wav, repetitions, snippet_dur=2.0, pattern='X'):
    for c in tqdm(xrange(0, repetitions)):

        pattern_pos = int((c / float(repetitions)) * len(pattern))
        if pattern[pattern_pos] == ' ':
            output_wav.extend_silence(snippet_dur)
        else:
            w = random.choice(wavs)
            d = w.random_crop(snippet_dur)
            d.fade_sine()
            output_wav.extend(d)
        if c % 100 == 0:
            gc.collect()


def dual_carpet(wavs, output_filename, repetitions, snippet_dur, pattern,
                sampwidth=2, framerate=8000):
    o = OutputWav(
        output_filename + '1.wav',
        nchannels=1,
        sampwidth=sampwidth,
        framerate=framerate,
    )
    carpet(wavs, o, repetitions, snippet_dur=snippet_dur, pattern=pattern)
    o.close()

    o = OutputWav(
        output_filename + '2.wav',
        nchannels=1,
        sampwidth=sampwidth,
        framerate=framerate,
    )
    o.extend_silence(1.0)
    carpet(wavs, o, repetitions, snippet_dur=snippet_dur, pattern=pattern)

    o.close()

    os.system('sox --norm -m %s %s %s' % (
        output_filename + '1.wav', output_filename + '2.wav', output_filename
    ))
    os.unlink(output_filename + '1.wav')
    os.unlink(output_filename + '2.wav')


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--offset", default=0)
    optparser.add_option("--output-filename", "-o", default='output.wav')
    optparser.add_option("--output-rate", default=8000)
    optparser.add_option("--minutes", default=8)
    optparser.add_option("--snippet-duration", default=2.0)
    optparser.add_option("--pattern", default='X')
    (options, args) = optparser.parse_args(argv[1:])

    wavs = []
    for filename in args:
        print "loading", filename, "..."
        assert filename.endswith('.pickle')
        w = Wav.unpickle(filename)
        assert w.sampwidth == 2
        assert w.framerate == int(options.output_rate)
        w.dump()
        wavs.append(w)

    o = OutputWav(
        options.output_filename,
        nchannels=1,
        sampwidth=wavs[0].sampwidth,
        framerate=wavs[0].framerate,
    )

    snippet_dur = float(options.snippet_duration)
    
    repetitions = int(options.minutes) * int(60.0 / snippet_dur)

    offset = float(options.offset)
    if offset > 0.0:
        o.extend_silence(offset)

    carpet(wavs, o, repetitions, snippet_dur=snippet_dur, pattern=options.pattern)

    o.close()


if __name__ == '__main__':
    main(sys.argv)
