#!/usr/bin/env python

import sys
import wave

for filename in sys.argv[1:]:
    print filename
    w = wave.open(filename)

    print w.getframerate()
    print w.getsampwidth()
    print w.getnchannels()
    print w.getnframes()
    print w.getnchannels() * w.getnframes() * w.getsampwidth()
    print

    # frames = w.readframes(1)
    # print len(frames)  # = w.getnchannels() * w.getsampwidth()
    # print map(ord, frames)
    
    w.close()
