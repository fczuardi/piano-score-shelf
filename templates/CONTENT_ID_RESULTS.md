# {{song}} Content ID experiment results

This experiment records which recordings and synthesized performances receive YouTube claims, which organizations claim them, and the matched passages and restrictions. No videos have been uploaded by the preparation script. A claim is an observation of YouTube's system, not a determination of copyright ownership; no claim observed is not a finding of permission.

## Experiment setup

- Prepared batch and manifest: `build/manifest.json`
- Channel: To fill in
- Upload dates and timezone: To fill in
- Visibility: Private
- Country of observation: To fill in
- Audio treatment: Original speed, pitch, and duration; AAC encoding at 192 kbps, without normalization or added audio.
- Video treatment: 1280 × 720 landscape title card at 2 frames per second.
- Modern score playback: Record score commit, soundfont, tempo, exported staves, and repeat settings when tested. Keep the audio export's hash from the manifest.

The manifest and individual JSON records preserve audio/video hashes, duration, encoding settings, and the FFmpeg version. WAV and MP3 transfers of the same performance are separate test cases, not independent performances.

## Source decoding observations

{{diagnostics}}

## Cases

Use one video per case. Retain dated observations rather than replacing an earlier outcome.

| Case | Audio source | Latest observed status | Video link | Last checked UTC |
| --- | --- | --- | --- | --- |
{{cases}}

Status values: Not uploaded; Checks pending; No claim observed; Claimed; Processing failed; Taken down. Use “No claim observed” only after checking Studio and recording when the check occurred.

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

No results recorded yet.

## Platform references

- [Private and unlisted visibility](https://support.google.com/youtube/answer/157177?hl=en)
- [Finding claimants and interpreting claims](https://support.google.com/youtube/answer/6013276?hl=en)
