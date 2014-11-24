#!/bin/sh

./smarts.py > opera.json || exit 1
for SCENE in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
  ./carpet.py opera.json $SCENE $*
done
