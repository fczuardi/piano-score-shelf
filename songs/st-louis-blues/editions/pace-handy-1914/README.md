# St. Louis Blues — Pace & Handy 1914 Memphis edition

This directory contains a work-in-progress transcription of the six-page Pace & Handy Music Co. issue preserved by the Gaylord Music Library at Washington University in St. Louis. The source was published in Memphis in 1914; its music occupies scan pages 2–5. The uncompressed MusicXML file is the canonical digital score, and the MuseScore file is the editable working copy.

The first music page of the source (scan page 2), comprising the opening piano introduction and measures 9–18 with three lyric verses, has been transcribed and reviewed. The remaining measures are placeholders and will be replaced as transcription continues.

## Transcription workflow

1. Work directly from witness A, the Washington University scans under `../../inputs/`.
2. Enter one printed system at a time in `st-louis-blues-pace-handy-1914.mscz`.
3. Save the MuseScore file, then run `just edition-sync st-louis-blues pace-handy-1914` to refresh the canonical MusicXML.
4. Compare every measure with witness A. Consult Brown's 1918 issue only when a reading is unclear, and record that consultation.
5. Record corrections, alternatives, and unresolved readings as `[[decisions]]` entries in `EDITION.toml`.
6. Use `just edition-build st-louis-blues pace-handy-1914` to generate review derivatives when useful.
7. Before declaring the edition complete, review the entire score visually and aurally and replace the WIP scope and status in the manifest.

## CC0 scope and source rights

Fabricio C Zuardi intends to dedicate the transcription, engraving, editorial apparatus, and digital files to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/), to the extent that he owns copyright or related rights in them.

That dedication cannot waive third-party rights. The underlying 1914 music and lyrics are public domain in the United States but may remain protected in life-plus-70 jurisdictions through December 31, 2028. Fonts and software components retain their own licenses. The scanned cover artwork is source evidence and is not incorporated into the CC0 engraving.

The legacy identification of the Washington University copy as an apparent first edition is documented on the main song page. This edition title identifies the known publisher, place, and date without claiming that the physical copy belongs to a particular printing or impression.
