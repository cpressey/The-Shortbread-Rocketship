#!/usr/bin/env python

import os
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

from longwave import Wav, OutputWav, ListLevelBackingStore
from reprowave import dual_carpet


WAVS = {}

def rand_wave(dirname):
    return random.choice(
        [x for x in os.listdir(dirname) if x.endswith('.pickle')]
    )


OUTPUT_RATE = None


def load_wav(filename):
    global WAVS
    if filename in WAVS:
        return WAVS[filename]

    print "loading", filename, "..."
    assert filename.endswith('.pickle')
    w = Wav.unpickle(filename)
    assert w.sampwidth == 2
    assert w.framerate == OUTPUT_RATE
    w.dump()
    WAVS[filename] = w
    return w


def random_pop(l):
    d = random.randint(0, len(l) - 1)
    return l.pop(d)


def main(argv):
    global OUTPUT_RATE
    optparser = OptionParser(__doc__)
    optparser.add_option("--minutes", default=8)
    optparser.add_option("--output-rate", default=16000)
    #optparser.add_option("--snippet-duration", default=2.0)
    #optparser.add_option("--pattern", default='X')
    optparser.add_option("--output-filename", "-o", default='output.wav')
    (options, args) = optparser.parse_args(argv[1:])

    OUTPUT_RATE = int(options.output_rate)

    dirs = args

    # TODO: handle each of these slightly specially
    master_dir = 'sources/RDY'
    types = ('choral', 'orch', 'speech', 'piano', 'short')

    patterns = [
        'X',
        'X X',
        ' X X ',
        ' X ',
        'X X ',
        ' X X',
    ]

    layer_names = []
    for layer_num in xrange(0, 4):
        print 'LAYER', layer_num
        type_dir = random.choice(types)
        type_dir = 'short'
        dirname = os.path.join(master_dir, type_dir, 'pickle')
        wavename = rand_wave(dirname)
        fullwavename = os.path.join(dirname, wavename)
        wav = load_wav(fullwavename)

        pattern = random_pop(patterns)
        print fullwavename, '-> "%s"' % pattern
        
        #snippet_dur = float(options.snippet_duration)
        snippet_dur = 2.0
        repetitions = int(options.minutes) * int(60.0 / snippet_dur)

        layer_name = 'layer%s.wav' % layer_num
        dual_carpet(
            [wav], layer_name,
            repetitions, snippet_dur, pattern,
            framerate=OUTPUT_RATE
        )
        layer_names.append(layer_name)

    if len(layer_names) > 1:
        os.system('sox --norm -m %s %s' % (
            ' '.join(layer_names), options.output_filename
        ))
    else:
        os.system('mv %s %s' % (layer_names[0], options.output_filename))
    lame_name = options.output_filename + '.mp3'
    os.system('lame %s %s' % (options.output_filename, lame_name))
    os.system('ls -lh %s' % lame_name)
    os.system('totem %s' % lame_name)


if __name__ == '__main__':
    import sys
    main(sys.argv)
