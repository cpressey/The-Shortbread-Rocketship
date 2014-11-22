#!/usr/bin/env python

import os
from optparse import OptionParser
import random
import json


def random_pop(l):
    d = random.randint(0, len(l) - 1)
    return l.pop(d)


PATTERNS = [
    'X',
    'X X',
    ' X X ',
    ' X ',
    'X X ',
    ' X X',
]


def make_scene(available):
    keys = available.keys()

    layers = []
    used_patterns = set()

    for x in xrange(0, 4):
        type_ = random.choice(keys)
        pattern = None
        while pattern is None or pattern in used_patterns:
            pattern = random.choice(PATTERNS)
        layers.append({
            'type': type_,
            'sample': random.choice(available[type_]),
            'pattern': pattern
        })
        used_patterns.add(pattern)

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

    scenes = []
    for scene_num in xrange(1, 16):
        scene = make_scene(available)
        scenes.append(scene)

    print json.dumps(scenes)


if __name__ == '__main__':
    import sys
    main(sys.argv)
