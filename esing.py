#!/usr/bin/env python

import os
import random


filename = 'output.ssml.txt'
with open(filename, 'w') as f:
    for i in xrange(0, 40):
        word = random.choice("The quick brown fox jumped over the lazy dog".split())
        #pitch = random.choice([x * 20 for x in xrange(1, 9)])
        pitch = int(i * 3.2)
        f.write('<prosody pitch="%sHz">%s</prosody>\n' % (pitch, word))

os.system('cat %s' % filename)

os.system('espeak -m -f %s' % filename)
