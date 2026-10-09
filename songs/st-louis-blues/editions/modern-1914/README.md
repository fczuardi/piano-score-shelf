# St. Louis Blues — transcription of the Handy Bros. ukulele edition

This directory contains a work-in-progress transcription of the Handy Bros. scenic-cover ukulele edition preserved in IMSLP #716402. Its publication date is unverified; 1914 dates the underlying composition, not necessarily this edition. The uncompressed MusicXML file is the canonical digital score. MuseScore, PDF, SVG, and MIDI files are working or generated derivatives.

The primary witness is the four score pages of the undated Handy Bros. scenic-cover issue preserved under `../../inputs/`. Brown University Library's 1918 Pace & Handy issue is the first collation witness. [`EDITION.toml`](EDITION.toml) records the exact artifact identifiers, editorial policy, output names, and every future intervention.

## Transcription workflow

1. Enter one printed system at a time in MuseScore using the primary witness.
2. Save the editable score as `st-louis-blues.mscz`, then run `just edition-sync` to refresh the canonical uncompressed `st-louis-blues.musicxml`. This command uses MuseScore's headless converter because the 4.7 Linux GUI export dialog may fail to open.
3. Compare every measure against the primary scan, then consult witness B only where the reading is unclear.
4. Record corrections, alternatives, and unresolved readings as `[[decisions]]` entries in `EDITION.toml`.
5. Run `just edition-build` to generate PDF, per-page SVG, and MIDI derivatives.
6. Open the generated MusicXML and MIDI independently and listen through the entire score before changing the edition status to `reviewed`.

## Licensing boundary

To the extent possible under law, the project's transcription, engraving, metadata, and editorial contributions are dedicated to the public domain under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). This dedication applies only to rights held by the transcriber. Copyright status of additions in the source edition has not been verified; third-party rights are unaffected. Fonts retain their own licenses.

The edition is published as a work in progress. Its manifest records the currently completed scope; PDF and MIDI release derivatives will follow after the musical text has been completed and reviewed.

The legacy directory name `modern-1914` is retained for link compatibility and does not date the source edition. Brown's 1918 score differs musically and is intended as the source of a separate future transcription.
