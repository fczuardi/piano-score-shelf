# St. Louis Blues — transcription of the Handy Bros. ukulele edition

This directory contains a complete transcription of the Handy Bros. scenic-cover ukulele edition preserved in IMSLP #716402. Its publication date is unverified; 1914 dates the underlying composition, not necessarily this edition. The uncompressed MusicXML file is the canonical interchange score, and the MuseScore file is the editable engraving source. PDF, SVG, and MIDI files are generated derivatives.

The primary witness is the four score pages of the undated Handy Bros. scenic-cover issue preserved under `../../inputs/`. Brown University Library's 1918 Pace & Handy issue is the first collation witness. [`EDITION.toml`](EDITION.toml) records the exact artifact identifiers, editorial policy, output names, and every future intervention.

## Transcription workflow

1. Enter one printed system at a time in MuseScore using the primary witness.
2. Save the editable score as `st-louis-blues-handy-bros-ukulele.mscz`, then run `just edition-sync st-louis-blues handy-bros-ukulele` to refresh the canonical uncompressed `st-louis-blues-handy-bros-ukulele.musicxml`. This command uses MuseScore's headless converter because the 4.7 Linux GUI export dialog may fail to open.
3. Compare every measure against the primary scan, then consult witness B only where the reading is unclear.
4. Record corrections, alternatives, and unresolved readings as `[[decisions]]` entries in `EDITION.toml`.
5. Run `just edition-build` to generate PDF, synthesized MP3, per-page SVG, and MIDI derivatives.
6. Open the generated MusicXML and MIDI independently and listen through the entire score before changing the edition status to `reviewed`.

## Attribution and source status

Transcribed by Fabricio C Zuardi, 2026, from the Handy Bros. edition preserved in IMSLP #716402. Source edition's publication date and rights in its additions remain unverified. Fonts retain their own licenses.

The edition is published as complete. Its manifest records the transcription history, editorial policy, witnesses, and interventions.

Brown's 1918 score differs musically and is intended as the source of a separate future transcription.
