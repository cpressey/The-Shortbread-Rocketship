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
    ' X ',
    'X X',
    'X X ',
    ' X X',
    ' XX ',
    ' X X ',
    'X X X',
    'XX XX',
    ' XXX ',
]


def expand_pattern(base, expansion):
    new = ''
    for char in base:
        if char == ' ':
            new += ' ' * len(expansion)
        else:
            new += expansion
    return new


PREFIX = 'The Shortbread Rocketship'
def make_scene(num, sample_library):

    layers = []
    used_patterns = set()

    for x in xrange(0, 4):
        # >===> pick type
        if x == 0:
            type_ = 'choral'
        else:
            type_ = random.choice(TYPES)
            while not sample_library.get(type_, []):
                type_ = random.choice(TYPES)

        # >===> pick sample of that type
        try:
            sample = random_pop(sample_library[type_])
        except ValueError:
            print "No more samples of type %s available!!!" % type_
            raise

        # >===> pick pattern
        if x == 3:
            pattern = 'X'
        else:
            pattern = None
            while pattern is None or pattern in used_patterns:
                pattern = random.choice(PATTERNS)
                if random.randint(1, 3) < 3:
                    pattern = expand_pattern(pattern, random.choice(PATTERNS))

        layers.append({
            'type': type_,
            'sample': sample,
            'pattern': pattern
        })
        used_patterns.add(pattern)

    scene = (num % 5) + 1
    act = (num / 5) + 1
    ROMAN = ['0', 'I', 'II', 'III', 'IV', 'V']

    return {
        'name': '%02d. %s--Act %s Scene %s' % (num, PREFIX, ROMAN[act], ROMAN[scene]),
        'layers': layers
    }


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--master-dir", default='pickle')
    optparser.add_option("--acts", default=3)
    optparser.add_option("--scenes-per-act", default=5)
    optparser.add_option("--exclude-samples-from", default=None)
    optparser.add_option("--dump-available-samples", default=False, action='store_true')
    (options, args) = optparser.parse_args(argv[1:])

    master_dir = options.master_dir

    num_acts = int(options.acts)
    scenes_per_act = int(options.scenes_per_act)

    exclude = set()
    if options.exclude_samples_from is not None:
        with open(options.exclude_samples_from, 'r') as f:
            for scene in json.loads(f.read()):
                for layer in scene['layers']:
                    exclude.add(layer['sample'])

    sample_library = {}  # type -> list of filename

    for type_ in TYPES:
        type_dir = os.path.join(master_dir, type_)
        for filename in os.listdir(type_dir):
            full_filename = os.path.join(type_dir, filename)
            if full_filename in exclude:
                #print "EXCLUDING", full_filename
                continue
            sample_library.setdefault(type_, []).append(full_filename)

    if options.dump_available_samples:
        from pprint import pprint
        pprint(sample_library)
        sys.exit(0)

    scenes = []
    for num in xrange(0, num_acts * scenes_per_act):
        # this function will delete some samples from sample_library dict
        scene = make_scene(num, sample_library)
        scenes.append(scene)

    print json.dumps(scenes)


if __name__ == '__main__':
    import sys
    main(sys.argv)
