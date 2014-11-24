#!/usr/bin/env python

import os
from optparse import OptionParser
import random
import json


def random_pop(l):
    d = random.randint(0, len(l) - 1)
    return l.pop(d)


TYPES = (
    'choral', 'orch', 'speech', 'piano', 'short'
)

PATTERNS = [
    'X',
    'X X',
    ' X X ',
    ' X ',
    'X X ',
    ' X X',
]


def expand_pattern(base, expansion):
    new = ''
    for char in base:
        if char == ' ':
            new += ' ' * len(expansion)
        else:
            new += expansion
    return new


def make_scene(sample_library):

    layers = []
    used_patterns = set()

    for x in xrange(0, 4):
        if x == 0:
            type_ = 'choral'
        else:
            type_ = random.choice(TYPES)
            while not sample_library[type_]:
                type_ = random.choice(TYPES)

        pattern = None
        while pattern is None or pattern in used_patterns:
            pattern = random.choice(PATTERNS)
            if random.randint(1, 2) == 2:
                pattern = expand_pattern(pattern, random.choice(PATTERNS))

        try:
            sample = random_pop(sample_library[type_])
        except ValueError:
            print "No more samples of type %s available!!!" % type_
            raise

        layers.append({
            'type': type_,
            'sample': sample,
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

    sample_library = {}  # type -> list of filename

    for type_ in TYPES:
        type_dir = os.path.join(master_dir, type_)
        for filename in os.listdir(type_dir):
            full_filename = os.path.join(type_dir, filename)
            sample_library.setdefault(type_, []).append(full_filename)

    scenes = []
    for scene_num in xrange(1, 16):
        scene = make_scene(sample_library)  # will delete from sample_library
        scenes.append(scene)

    print json.dumps(scenes)


if __name__ == '__main__':
    import sys
    main(sys.argv)
