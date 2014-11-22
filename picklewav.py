#!/usr/bin/env python

import os
from optparse import OptionParser
import sys
from tempfile import mkstemp


from longwave import Wav, OutputWav


def main(argv):
    optparser = OptionParser(__doc__)
    optparser.add_option("--pickle-dir", default='pickle')
    (options, args) = optparser.parse_args(argv[1:])

    for filename in args:
        dirname = os.path.dirname(filename)
        os.system('mkdir -p "%s"' % options.pickle_dir)
        outfile = os.path.join(
            options.pickle_dir, os.path.basename(filename) + ".pickle"
        )
        if os.path.exists(outfile):
            print outfile, 'already exists, SKIPPING'
            continue

        (temp_fd, temp_filename) = mkstemp(suffix='.wav')
        os.close(temp_fd)
        command = 'sox "%s" -r 16k -b 16 "%s"' % (
            filename, temp_filename,
        )
        print command
        os.system(command)
        if False:
            os.system('totem %s' % temp_filename)

        print temp_filename, '->', outfile
        w = Wav.load(temp_filename)
        w.dump()
        w.pickle(outfile)
        os.unlink(temp_filename)


if __name__ == '__main__':
    import sys
    main(sys.argv)
