# Content ID audio experiments

Prepare one local title-card video per recording and document observations in a results page. This tool does not upload videos or access your YouTube account.

Requires Python 3, FFmpeg with `libx264`, AAC, and `drawtext`, and FFprobe. No Python packages are needed.

List the default St. Louis Blues recordings:

```sh
just content-id-list
```

Render all recordings and initialize the results page:

```sh
just content-id-videos
```

Videos and hashes are written under `experiments/content-id/st-louis-blues/build/`. The editable page is `experiments/content-id/st-louis-blues/RESULTS.md`. Both WAV and MP3 transfers are kept as distinct cases. Re-running verifies and reuses matching outputs; it never overwrites an existing results page. Add new cases to that page when extending a batch.

To prepare selected recordings or an audio export from MuseScore:

```sh
python3 scripts/content_id_videos.py path/to/recording.wav path/to/score-playback.wav
```

Use `--output` for a separate batch directory and `--results` for a separate results page. The manifest describes the inputs selected for that invocation; individual video records from earlier invocations remain in the output directory. Use `--overwrite` to regenerate selected videos explicitly.

Export your modern score to WAV or FLAC in MuseScore before adding it. Record its score commit, playback settings, and whether unfinished piano measures are included. The tool preserves timing and pitch, but encodes audio to AAC for the MP4 container.

Upload the resulting MP4s manually as Private videos. In Studio, complete the Checks step and record each claim's details and dated follow-up observations in the results page. The reusable page template is `templates/CONTENT_ID_RESULTS.md`. Prepared videos and local evidence belong in the ignored build directory; edit and commit the results page when ready.

Run `python3 scripts/build.py` after editing a results page. The site build reads the canonical results file and creates a page at `/experiments/content-id/st-louis-blues/`; generated pages are ignored by Git. Rendering the site requires Zola. This command does not publish the site.

Individual records retain FFmpeg decoding diagnostics. Review any reported source errors before treating the rendered video as a faithful transfer.
