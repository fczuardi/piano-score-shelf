# St. Louis Blues Content ID experiment results

This experiment records which recordings and synthesized performances receive YouTube claims, which organizations claim them, and the matched passages and restrictions. No videos have been uploaded by the preparation script. A claim is an observation of YouTube's system, not a determination of copyright ownership; no claim observed is not a finding of permission.

## Experiment setup

- Prepared batch and manifest: `build/manifest.json`
- Channel: To fill in
- Upload date: 2026-10-05, as reported by the uploader; local timezone America/Sao_Paulo. Exact times not recorded.
- Visibility: Private
- Country of observation: To fill in
- Audio treatment: Original speed, pitch, and duration; AAC encoding at 192 kbps, without normalization or added audio.
- Video treatment: 1280 × 720 landscape title card at 2 frames per second.
- Modern score playback: Record score commit, soundfont, tempo, exported staves, and repeat settings when tested. Keep the audio export's hash from the manifest.

The manifest and individual JSON records preserve audio/video hashes, duration, encoding settings, and the FFmpeg version. WAV and MP3 transfers of the same performance are separate test cases, not independent performances.

The modern WIP case uses the combined `/var/home/fcz/Music/st-louis-blues.flac` export (136.404 seconds). Its metadata contains placeholder artist and year tags; these are not evidence of authorship or date. Playback soundfont, tempo, and repeat settings have not yet been recorded. The preparation record includes the current working score hash, without assuming it proves the exact export revision.

## Source decoding observations

FFmpeg reported invalid MP3 packets in `usaf-band-st-louis-blues-march-1997.mp3` and `usaf-falconaires-st-louis-blues-1996.mp3`. Their individual JSON records retain the diagnostics. All ten rendered audio streams are within 0.04 seconds of their source duration; this duration check does not establish that damaged packets decoded faithfully. Review these two cases before interpreting their results.

## Cases

Use one video per case. Retain dated observations rather than replacing an earlier outcome.

| Case | Audio source | Latest observed status | Video link | Last checked UTC |
| --- | --- | --- | --- | --- |
| bessie-smith-louis-armstrong-st-louis-blues-1925-69ba59d6fda3 | bessie-smith-louis-armstrong-st-louis-blues-1925.mp3 | Claimed | [YouTube](https://youtu.be/azvvYfk_4jA) | — |
| dadvid-kemp-recorder-arrangement-synthesized-4e8e68bcbc29 | dadvid-kemp-recorder-arrangement-synthesized.mp3 | No automatic claim reported | — | — |
| ferera-paaluhi-st-louis-blues-1925-gutenberg-46e8049358eb | ferera-paaluhi-st-louis-blues-1925-gutenberg.mp3 | No automatic claim reported | — | — |
| original-dixieland-jazz-band-st-louis-blues-1921-loc-01203bf2e379 | original-dixieland-jazz-band-st-louis-blues-1921-loc.mp3 | Claimed | [YouTube](https://youtu.be/rj6Gal2dgGs) | — |
| original-dixieland-jazz-band-st-louis-blues-1921-808f119cf86d | original-dixieland-jazz-band-st-louis-blues-1921.wav | Claimed | [YouTube](https://youtu.be/Y0y-dzWPzRY) | — |
| ted-lewis-jazz-band-st-louis-blues-1922-loc-68fb9ae116e2 | ted-lewis-jazz-band-st-louis-blues-1922-loc.mp3 | No automatic claim reported | — | — |
| ted-lewis-jazz-band-st-louis-blues-1922-2415c38f5f4a | ted-lewis-jazz-band-st-louis-blues-1922.wav | No automatic claim reported | — | — |
| usaf-band-st-louis-blues-march-1994-a80ecebc8515 | usaf-band-st-louis-blues-march-1994.mp3 | Claimed | [YouTube](https://youtu.be/YRooPMqk9u4) | — |
| usaf-band-st-louis-blues-march-1997-e57e500bea9c | usaf-band-st-louis-blues-march-1997.mp3 | Claimed | [YouTube](https://youtu.be/x6kuD9IF5lA) | — |
| usaf-falconaires-st-louis-blues-1996-92c4c498a92b | usaf-falconaires-st-louis-blues-1996.mp3 | Claimed | [YouTube](https://youtu.be/Qv_Mqk2Pgo8) | — |
| st-louis-blues-wip-synthesized-af18b74fb812 | Modern WIP synthesized playback, combined score | No automatic claim reported | — | — |

Status values: No automatic claim reported; Not uploaded; Checks pending; No claim observed; Claimed; Processing failed; Taken down. Use “No claim observed” only after checking Studio and recording when the check occurred.

## Pending recording candidates

- **Jimmy Joy and St. Anthony Hotel Orchestra (1925)** — OKeh 40539, matrix 9377, take A. [UCSB catalog record](https://adp.library.ucsb.edu/index.php/matrix/detail/2000201513); [UCSB’s U.S. public-domain assessment](https://www.library.ucsb.edu/1925-recordings-digitized-ucsb-entering-public-domain-january-1-2026). Audio currently unavailable: UCSB’s player and direct MP3 returned HTTP 403 on October 5, 2026. No audio obtained, video prepared, or upload made. Pending acquisition of the recording before creating a test case.

## Results reported so far

As reported by the uploader in conversation on 2026-10-05, **6 of 11 videos received automatic claims**. All eleven were uploaded on 2026-10-05, as reported by the uploader. The other five have no automatic claim reported; exact check times and completion of checks have not been documented. The six claimed videos have been matched to URLs using uploader-supplied yt-dlp title output. Exact upload/check times, claim coverage outside blocked territories, and individual dispute submission dates remain to be recorded.

| Case | Matched recording and artist as displayed | Claimants and represented label | Matched interval | Shown impact |
| --- | --- | --- | --- | --- |
| Bessie Smith 1925 | The St. Louis Blues — Bessie Smith | SME, on behalf of Legacy Recordings | 0:00–3:10 | Blocked in Russia; potential earnings limitation |
| USAF Band 1994 | St. Louis Blues March — Glenn Miller & Si Zentner | The Orchard Music, on behalf of Ten12 Entertainment | 0:14–4:18 | Potential earnings limitation; no block shown |
| Falconaires 1996 | St. Louis Blues March — Glenn Miller Orchestra | PONYCANYON, UMG, on behalf of GRP | 0:13–4:09 | Potential earnings limitation; no block shown |
| USAF Band 1997 | St. Louis Blues — Memphis Belle Orchestra | WMG, on behalf of Prestige Elite USA | 0:09–3:35 | Potential earnings limitation; no block shown |
| Original Dixieland 1921 WAV, 808f119cf86d | St. Louis Blues — Original Dixieland Jazz Band | SME, on behalf of Bluebird | 0:00–3:16 | Blocked in Russia; potential earnings limitation |
| Original Dixieland 1921 MP3, 01203bf2e379 | Not independently documented in a screenshot | SME, on behalf of Bluebird, confirmed by uploader | Not documented | Russia block reported by uploader; other impacts not documented |

The first five entries are transcribed from uploader-supplied Studio screenshots. The MP3 claim is based on the uploader's confirmation. “Copyright – Audio” is the displayed type in the screenshots; it does not itself establish which underlying rights are asserted. A Russia block does not establish that the claim is limited to Russia.

The uploader plans to wait for the first Russia/Bluebird/SME dispute before disputing the second Dixieland upload. Which case was disputed first, submission date, and current dispute status remain to be confirmed. Prepared dispute wording for other cases is not evidence that a dispute was submitted.

## Observation template

Copy this section for each check. Add one row per claim; a video may have multiple claimants or territory-specific policies.

### Case and check date

- Case ID:
- Video URL:
- Uploaded at UTC:
- Checked at UTC:
- Checks completion status:
- Observed status:
- Studio screenshot or saved evidence file:

| Claimant as displayed | Matched title | Claim type as displayed | Matched start and end | Policy or restriction | Territories |
| --- | --- | --- | --- | --- | --- |
| To fill in | To fill in | To fill in | To fill in | To fill in | To fill in |

Record fields exactly as Studio displays them. Use “Not shown” for unavailable details. Keep screenshots locally; remove account identifiers before adding evidence to this public repository. Record the observed country separately from any worldwide policy shown by Studio.

Notes:

## Comparisons and interpretation

Summarize observed differences between transfers of the same historical performance, different recordings, and your own synthesized playback. Distinguish a claim naming a recording from a publishing/composition claim when Studio provides that information. Leave unclear claims unclassified.

Six claims have been reported. No conclusion about the validity of the claims or non-US rights has been established. The two Dixieland cases test different formats of the same LOC transfer.

## Platform references

- [Private and unlisted visibility](https://support.google.com/youtube/answer/157177?hl=en)
- [Finding claimants and interpreting claims](https://support.google.com/youtube/answer/6013276?hl=en)
