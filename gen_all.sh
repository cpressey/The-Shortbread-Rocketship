#!/bin/sh

./smarts.py > opera.json
for SCENE in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
  ./carpet.py opera.json $SCENE --minutes=8 --output-name="Scene_$SCENE"
done