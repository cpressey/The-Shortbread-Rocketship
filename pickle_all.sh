#!/bin/sh -x

for T in choral piano orch speech short; do
    ./picklewav.py --pickle-dir=pickle/$T sources/RDY/$T/*.*
done
