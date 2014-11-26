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
*   Pick samples at random — ones that haven't been used yet.
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

If the input sample is "short", don't carpet it, just shotgun it randomly
around.  Or not, running outta time.

Sources Used
------------

Note, not all of these may have actually been used!  These are all the
possible sound files that were selected from.

TODO: get URLs for these, confirm that they're all in the public domain

### choral

*   [searchingbird turdus-merula.mp3](http://freesound.org/people/searchingbird/sounds/181681/) CC0
*   [felix-blume two-bulls-singing-in-the-desert-of-arizona.wav](http://freesound.org/people/felix.blume/sounds/202111/) CC0
*   [Stanley Singing](http://freesound.org/people/wjoojoo/sounds/206029/) CC0
*   [20141025 Two Girls Singing and Dancing in a House](http://freesound.org/people/kijjaz/sounds/252904/) CC0
*   [Big_Bill_Broonzy - 17 - Baby Please Don't Go.mp3](http://freemusicarchive.org/music/big_bill_broonzy/~/bigbillbroonzy-babypleasedontgo1) PD mark
*   [Eliseo_and_Company-A_Festa_E_Munte_Virgine-Columbia-E4019_64kb.mp3](https://archive.org/details/Eliseo_and_Company-A_Festa) ca. 1920, assumed PD
*   [Enrico_Caruso,_Bessie_Abott,_Louise_Homer,_Antonio_Scotti,_Giuseppe_Verdi,_Bella_figlia_dell'_amore_(Rigoletto)_unrestored.ogg](http://commons.wikimedia.org/wiki/File:Enrico_Caruso,_Bessie_Abott,_Louise_Homer,_Antonio_Scotti,_Giuseppe_Verdi,_Bella_figlia_dell%27_amore_%28Rigoletto%29_unrestored.ogg) — PD mark
*   [Enrico_Caruso_-_Nellie_Melba_-_La_Boheme_-_O_soave_fanciulla.ogg](http://commons.wikimedia.org/wiki/File:Enrico_Caruso_-_Nellie_Melba_-_La_Boheme_-_O_soave_fanciulla.ogg) — PD mark
*   [Hmv-db3903-2ea8403.ogg](http://commons.wikimedia.org/wiki/File:Hmv-db3903-2ea8403.ogg) — PD mark
*   [JoeMccoy-EvilDevilWomanBlues.ogg](https://archive.org/details/KansasJoeMccoy-EvilDevilWomanBlues) PD tag
*   [La_bohème,_O_Mimì,_tu_più_non_torni_(Caruso,_Scotti).ogg](http://en.wikipedia.org/wiki/File:La_boh%C3%A8me,_O_Mim%C3%AC,_tu_pi%C3%B9_non_torni_%28Caruso,_Scotti%29.ogg) — PD mark
*   [La_Donna_E_Mobile_Rigoletto.ogg](http://commons.wikimedia.org/wiki/File:La_Donna_E_Mobile_Rigoletto.ogg) — PD mark
*   [Marie_Rappold_performing_O_Patria_Mia_from_Aida.ogg](http://commons.wikimedia.org/wiki/File:Marie_Rappold_performing_O_Patria_Mia_from_Aida.ogg) -- 1916, public domain
*   [Mozart-Abendempfindungchant.ogg](https://archive.org/details/Abendempfindung) tagged PD
*   [Mozart-Exultate.ogg](https://archive.org/details/MozartExultate) tagged PD
*   [Nicola_Zerola,_Giuseppe_Verdi,_La_fatal_pietra_(Aida)_unrestored.ogg](http://commons.wikimedia.org/wiki/File:Nicola_Zerola,_Giuseppe_Verdi,_La_fatal_pietra_%28Aida%29_unrestored.ogg) — PD mark
*   [No_Pagliaccio_non_son.ogg](http://commons.wikimedia.org/wiki/File:No_Pagliaccio_non_son.ogg) — PD mark
*   [Psalters_-_01_-_Banner.mp3](http://freemusicarchive.org/music/Psalters/us_vs_us/01_Banner_vbr) — PD mark
*   [Puccini_La_Boheme_Vecchia_zimarra.ogg](http://commons.wikimedia.org/wiki/File:Puccini_La_Boheme_Vecchia_zimarra.ogg) — PD mark
*   [Puccini_-_Melba_-_Adieu_de_Mimi_(La_Boheme)_-_1926.ogg](http://commons.wikimedia.org/wiki/File:Puccini_-_Melba_-_Adieu_de_Mimi_%28La_Boheme%29_-_1926.ogg) — PD mark
*   [Puccini_-_Melba_-_Donde_lieta_usci_(La_Bohème)_-_1907.ogg](http://commons.wikimedia.org/wiki/File:Puccini_-_Melba_-_Donde_lieta_usci_%28La_Boh%C3%A8me%29_-_1907.ogg) — PD mark
*   [Puccini_Mi_chiamano_Mimì_par_Claudia_Muzio.ogg](http://commons.wikimedia.org/wiki/File:Puccini_Mi_chiamano_Mim%C3%AC_par_Claudia_Muzio.ogg) — PD mark
*   [Triumphal_March_from_Aida.ogg](http://commons.wikimedia.org/wiki/File:Triumphal_March_from_Aida.ogg) — PD (USMC) -- note, miscategorized (not choral)
*   [Verdi_-_Melba_-_Caro_Nome_(Rigoletto).ogg](http://commons.wikimedia.org/wiki/File:Verdi_-_Melba_-_Caro_Nome_%28Rigoletto%29.ogg) — PD mark
*   [Verdi_-_Rigoletto_-_Smirnov.ogg](http://commons.wikimedia.org/wiki/File:Verdi_-_Rigoletto_-_Smirnov.ogg) — PD mark
*   [Verdi_Rigoletto_Sobinov.ogg](http://commons.wikimedia.org/wiki/File:Verdi_Rigoletto_Sobinov.ogg)

### orch

TODO: add the source code that generated 'witide_generated_strings'

The ones that start with numbers are all from
[freesound.org](http://freesound.org/) and should not be hard to find
to confirm that they're in the public domain.

*   140329__p-howe__lillibulleroflute.wav
*   145514__zabuhailo__plasticpipeflute2.wav
*   162765__dorhel__symphony-orchestra-tuning-before-concert.wav
*   165546__luckyv1303__six-studies-in-english-folk-song-iii.mp3
*   165547__luckyv1303__six-studies-in-english-folk-song-ii.mp3
*   165548__luckyv1303__six-studies-in-english-folk-song-i.mp3
*   165549__luckyv1303__saint-seans-sonata-for-clarinet.mp3
*   202724__tonant__brassbandwarmup.wav
*   202786__tonant__orchestratuning.wav
*   [Lloyd_Rodgers_-_03_-_shakeout_-_steve_moshier.mp3](http://freemusicarchive.org/music/Lloyd_Rodgers/Cartesian_Reunion_Memorial_Orchestra_1242/shakeout_-_steve_moshier) — PD mark
*   [The_United_States_Army_Old_Guard_Fife_and_Drum_Corps_-_20_-_Monteverdis_Toccata_from_LOrfeo.mp3](http://freemusicarchive.org/music/The_United_States_Army_Old_Guard_Fife_and_Drum_Corps/Celebrating_50_Years/20) — PD mark
*   [The_USAF_Concert_Band_and_Singing_Sergeants_-_10_-_Winter_Vivaldis_Four_Seasons.mp3](http://freemusicarchive.org/music/The_USAF_Concert_Band_and_Singing_Sergeants/Best_Of_Breitband_Vol_1/10_USAFB_-_Winter_Vivaldi_Four_Seasons) — PD mark
*   witide_generated_strings.wav

### piano

*   [Felipe_Sarro_-_11_-_C_Schumann_Scherzo_in_C_minor_Op_14.mp3](http://freemusicarchive.org/music/Felipe_Sarro/Best_Of_Breitband_Vol_1/11_Felipe_Sarro_-_C_Schumann_Scherzo_in_C_minor_Op_14) -- public domain
*   [John_H_Glover-Kind_-_10_-_I_Do_Like_To_Be_Beside_The_Seaside_1907_piano_roll.mp3](http://freemusicarchive.org/music/John_H_Glover-Kind/Frog_Legs_Ragtime_Era_Favorites/10_-_john_h_glover-kind_-_i_do_like_to_be_beside_the_seaside) — PD mark
*   [Nathan_Eckel_-_01_-_Sonata_in_G_Minor_Didone_Abbandonata_op50_no3_-_I_Largo_Allegro.mp3](http://freemusicarchive.org/music/Nathan_Eckel/Muzio_Clementis_Sonata_in_G_Minor-Didone_Abbandonata/Sonata_in_G_Minor_Didone_Abbandonata_op50_no3_-_I_Introduzione_Largo_patetico_e_sostenuto_-_I_Allegro_ma_con_espressione) -- PD
*   [Nathan_Eckel_-_02_-_Sonata_in_G_Minor_Didone_Abbandonata_op50_no3_-_II_Adagio_dolente.mp3](http://freemusicarchive.org/music/Nathan_Eckel/Muzio_Clementis_Sonata_in_G_Minor-Didone_Abbandonata/Sonata_in_G_Minor_Didone_Abbandonata_op50_no3_-_II_Adagio_dolente) -- PD
*   [Nathan_Eckel_-_03_-_Sonata_in_G_Minor_Didone_Abbandonata_op50_no3_-_III_Allegro_agitato_e_con_disperazione.mp3](http://freemusicarchive.org/music/Nathan_Eckel/Muzio_Clementis_Sonata_in_G_Minor-Didone_Abbandonata/Sonata_in_G_Minor_Didone_Abbandonata_op50_no3_-_III_Allegro_agitato_e_con_disperazione) -- PD
*   Paul_Pitman_-_04_-_Preludes_Book_2_-_La_puerta_del_Vino.mp3
*   Paul_Pitman_-_06_-_Preludes_Book_2_-_.mp3
*   Scott_Joplin_-_09_-_Original_Rags_1900_piano_roll.mp3
*   [ScottJoplin-FiggyFrank1908incomplete.mp3](https://archive.org/details/ScottJoplin) PD
*   [ScottJoplin-JosephLamb1908.mp3](https://archive.org/details/ScottJoplin) PD
*   [ScottJoplin-OriginalRagspianoRoll1900.mp3](https://archive.org/details/ScottJoplin) PD
*   [ScottJoplin-PianoRollBlues1900.mp3](https://archive.org/details/ScottJoplin) PD
*   [ScottJoplin-PineappleRag1908.mp3](https://archive.org/details/ScottJoplin) PD
*   [ScottJoplin-RagtimeDance1906.mp3](https://archive.org/details/ScottJoplin) PD
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

Some of these are from [librivox.org](http://librivox.org) (which puts
everything into the public domain)
and some from [archive.org](http://archive.org).

Some I cut down in size because they were so huge (I added CHUNK11 to their
names.)

Also, some of the books-on-tape had incorrect MP3 headers, which `sox`
was just choking on, so I had to convert them to WAV with `avconv` first.

*   amorporanexins_azevedo-CHUNK11.mp3 — librivox
*   [Anne_island_18_montgomery.ogg](https://librivox.org/anne-of-the-island-by-lucy-maud-montgomery/)
*   [OnReleasingtheWatergateTapes.mp3](https://archive.org/details/Greatest_Speeches_of_the_20th_Century) author is "public domain"
*   [populargovernment_01_macmechan_64kb-CHUNK11.mp3](https://librivox.org/the-winning-of-popular-government-by-archibald-macmechan/)
*   [PressConferenceontheRiotsattheDemocraticConvention.mp3](https://archive.org/details/Greatest_Speeches_of_the_20th_Century) author is "public domain"
*   [ResignationAddress-1974.mp3](https://archive.org/details/Greatest_Speeches_of_the_20th_Century) author is "public domain"
*   trespicos_19_alarcon_64kb.mp3.wav — librivox
