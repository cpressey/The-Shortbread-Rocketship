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
(because sox stops at the incorrect header.  workaround, use avconv to
make wav file sources for them)

Sources Used
------------

TODO: get URLs for these, confirm that they're all in the public domain

### choral

*   181681__searchingbird__turdus-merula.mp3
*   202111__felix-blume__two-bulls-singing-in-the-desert-of-arizona.wav
*   206029__wjoojoo__stanley-singing.flac
*   252904__kijjaz__20141025-two-girls-singing-and-dancing-in-a-house.wav
*   Big_Bill_Broonzy_-_17_-_Baby_Please_Dont_Go.mp3
*   Eliseo_and_Company-A_Festa_E_Munte_Virgine-Columbia-E4019_64kb.mp3
*   Enrico_Caruso,_Bessie_Abott,_Louise_Homer,_Antonio_Scotti,_Giuseppe_Verdi,_Bella_figlia_dell'_amore_(Rigoletto)_unrestored.ogg
*   Enrico_Caruso_-_Nellie_Melba_-_La_Boheme_-_O_soave_fanciulla.ogg
*   Hmv-db3903-2ea8403.ogg
*   JoeMccoy-EvilDevilWomanBlues.ogg
*   La_bohème,_O_Mimì,_tu_più_non_torni_(Caruso,_Scotti).ogg
*   La_Donna_E_Mobile_Rigoletto.ogg
*   Marie_Rappold_performing_O_Patria_Mia_from_Aida.ogg
*   Mozart-Abendempfindungchant.ogg
*   Mozart-Exultate.ogg
*   Nicola_Zerola,_Giuseppe_Verdi,_La_fatal_pietra_(Aida)_unrestored.ogg
*   No_Pagliaccio_non_son.ogg
*   Psalters_-_01_-_Banner.mp3
*   Puccini_La_Boheme_Vecchia_zimarra.ogg
*   Puccini_-_Melba_-_Adieu_de_Mimi_(La_Boheme)_-_1926.ogg
*   Puccini_-_Melba_-_Donde_lieta_usci_(La_Bohème)_-_1907.ogg
*   Puccini_Mi_chiamano_Mimì_par_Claudia_Muzio.ogg
*   Triumphal_March_from_Aida.ogg
*   Verdi_-_Melba_-_Caro_Nome_(Rigoletto).ogg
*   Verdi_-_Rigoletto_-_Smirnov.ogg
*   Verdi_Rigoletto_Sobinov.ogg

### orch

TODO: add the source code that generated 'witide_generated_strings'

*   140329__p-howe__lillibulleroflute.wav
*   145514__zabuhailo__plasticpipeflute2.wav
*   162765__dorhel__symphony-orchestra-tuning-before-concert.wav
*   165546__luckyv1303__six-studies-in-english-folk-song-iii.mp3
*   165547__luckyv1303__six-studies-in-english-folk-song-ii.mp3
*   165548__luckyv1303__six-studies-in-english-folk-song-i.mp3
*   165549__luckyv1303__saint-seans-sonata-for-clarinet.mp3
*   202724__tonant__brassbandwarmup.wav
*   202786__tonant__orchestratuning.wav
*   Lloyd_Rodgers_-_03_-_shakeout_-_steve_moshier.mp3
*   The_United_States_Army_Old_Guard_Fife_and_Drum_Corps_-_20_-_Monteverdis_Toccata_from_LOrfeo.mp3
*   The_USAF_Concert_Band_and_Singing_Sergeants_-_10_-_Winter_Vivaldis_Four_Seasons.mp3
*   witide_generated_strings.wav

### piano

*   Felipe_Sarro_-_11_-_C_Schumann_Scherzo_in_C_minor_Op_14.mp3
*   John_H_Glover-Kind_-_10_-_I_Do_Like_To_Be_Beside_The_Seaside_1907_piano_roll.mp3
*   Nathan_Eckel_-_01_-_Sonata_in_G_Minor_Didone_Abbandonata_op50_no3_-_I_Largo_Allegro.mp3
*   Nathan_Eckel_-_02_-_Sonata_in_G_Minor_Didone_Abbandonata_op50_no3_-_II_Adagio_dolente.mp3
*   Nathan_Eckel_-_03_-_Sonata_in_G_Minor_Didone_Abbandonata_op50_no3_-_III_Allegro_agitato_e_con_disperazione.mp3
*   Paul_Pitman_-_04_-_Preludes_Book_2_-_La_puerta_del_Vino.mp3
*   Paul_Pitman_-_06_-_Preludes_Book_2_-_.mp3
*   Scott_Joplin_-_09_-_Original_Rags_1900_piano_roll.mp3
*   ScottJoplin-FiggyFrank1908incomplete.mp3
*   ScottJoplin-JosephLamb1908.mp3
*   ScottJoplin-OriginalRagspianoRoll1900.mp3
*   ScottJoplin-PianoRollBlues1900.mp3
*   ScottJoplin-PineappleRag1908.mp3
*   ScottJoplin-RagtimeDance1906.mp3
*   Scott_Joplin_-_Ragtime_Dance.mp3

### short

These are all off [freesound.org](http://freesound.org/).  Some I had to
doctor to make sure they were more than 2 seconds long.  (I added PAD11
to their names.)

*   145515__zabuhailo__plasticpipeflute1-PAD11.mp3
*   152509__minian89__jet-engine.wav
*   159135__cms4f__flute-play-c-16.wav
*   188286__pepv__bird8.wav
*   235463__jcdecha__wind-chimes-single.wav
*   244795__jarredgibb__war-of-the-worlds-horn-2.wav
*   84414__emilpetersen__vand.aif
*   90741__bigdumbweirdo__orch-hit.wav

### speech

Some of these are from [librivox.org](http://librivox.org)
and some from [archive.org](http://archive.org)
Some I cut down in size because they were so huge (I added CHUNK11 to their
names.)

*   amorporanexins_azevedo-CHUNK11.mp3
*   Anne_island_18_montgomery.ogg
*   OnReleasingtheWatergateTapes.mp3
*   populargovernment_01_macmechan_64kb-CHUNK11.mp3
*   PressConferenceontheRiotsattheDemocraticConvention.mp3
*   ResignationAddress-1974.mp3
*   trespicos_19_alarcon_64kb.mp3.wav
