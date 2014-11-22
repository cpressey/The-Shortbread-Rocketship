#!/usr/bin/env python

import json
import os
from optparse import OptionParser
import random
import sys
import wave

try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x

from longwave import Wav, OutputWav, ListLevelBackingStore
from reprowave import dual_carpet


OUTPUT_RATE = None
WAVS = {}


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


def main(argv):
    global OUTPUT_RATE
    optparser = OptionParser(__doc__)
    optparser.add_option("--minutes", default=8)
    optparser.add_option("--output-rate", default=16000)
    optparser.add_option("--master-dir", default='pickle')
    #optparser.add_option("--snippet-duration", default=2.0)
    optparser.add_option("--output-name", "-o", default='output')
    (options, args) = optparser.parse_args(argv[1:])

    OUTPUT_RATE = int(options.output_rate)

    scheme = json.loads(open(args[0], 'r').read())
    scene_num = int(args[1])
    assert scene_num >= 1
    scene = scheme[scene_num-1]

    layer_names = []
    for (layer_num, layer) in enumerate(scene['layers']):
        print 'LAYER', layer_num

        dirname = os.path.join(options.master_dir, layer['type'])
        wavename = layer['sample']
        fullwavename = os.path.join(dirname, wavename)
        wav = load_wav(fullwavename)

        pattern = layer['pattern']
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
        os.system('sox --norm -m %s %s.wav' % (
            ' '.join(layer_names), options.output_name
        ))
        for layer_name in layer_names:
            os.unlink(layer_name)
    else:
        os.system('mv %s %s.wav' % (layer_names[0], options.output_name))

    lame_name = options.output_name + '.mp3'
    os.system('lame %s.wav %s' % (options.output_name, lame_name))
    os.system('ls -lh %s' % lame_name)
    os.unlink('%s.wav' % options.output_name)
    os.system('totem %s' % lame_name)


if __name__ == '__main__':
    import sys
    main(sys.argv)
