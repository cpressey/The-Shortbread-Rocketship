#!/usr/bin/env python

import os
from optparse import OptionParser
import random
import json


def rand_wave(dirname):
    return random.choice(
        [x for x in os.listdir(dirname) if x.endswith('.pickle')]
    )


def random_pop(l):
    d = random.randint(0, len(l) - 1)
    return l.pop(d)


def make_scene(available, patterns):
    keys = available.keys()

    layers = []
    for x in xrange(0, 4):
        layers.append({
            'sample': random.choice(available[random.choice(keys)]),
            'pattern': random.choice(patterns)
        })

    return {
        'layers': layers
    }


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--master-dir", default='pickle')
    (options, args) = optparser.parse_args(argv[1:])

    master_dir = options.master_dir
    types = ('choral', 'orch', 'speech', 'piano', 'short')
    
    available = {}
    for t in types:
        available[t] = os.listdir(os.path.join(master_dir, t))

    patterns = [
        'X',
        'X X',
        ' X X ',
        ' X ',
        'X X ',
        ' X X',
    ]

    scenes = []
    for scene_num in xrange(1, 16):
        scene = make_scene(available, patterns)
        scenes.append(scene)

    print json.dumps(scenes)


if __name__ == '__main__':
    import sys
    main(sys.argv)
