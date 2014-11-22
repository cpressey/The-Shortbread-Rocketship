The Shortbread Rocketship
=========================

### A Cut-Up Opera ###

A generated opera in three acts, for
[NaOpGenMo](https://github.com/cpressey/NaOpGenMo).

Note
----

This repository is a mess.

Strategy
--------

There are three forty-minute acts.  Each act consists of five eight-minute
scenes.

For each scene, repeat the following four times:

*   Pick a pattern.   
*   The pattern will specify a number of samples.  The pattern will
    also specify where to "carpet" them.
*   Pick samples at random (ones you haven't used before?)
*   Execute the pattern, for 8 minutes long, to a WAV file.

Mix all four WAV files to produce the scene.

"Carpet" means:

*   Extract 2-second long snippet from longer work, apply sine wave amplitude
    to it (make edges less harsh), paste it into all parts of the score dictated
    by the pattern.
*   Then do the same thing with a 1-second offset, so they overlap.
*   Then mix the two.

Patterns look like `"X X"` which means "the first and final third but not
the middle third".

TODO
----

What kinds of patterns are there?

Are there patterns that should always be used?

If the input sample is "short", don't carpet it, just shotgun it randomly
around.

The chosen samples for at least one layer should include a "choral"
sample (though these might also include just speaking.)

Why are my e-books not pickling correctly?!?
