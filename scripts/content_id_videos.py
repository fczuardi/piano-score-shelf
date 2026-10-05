#!/usr/bin/env python3
"""Prepare local audio-only Content ID test videos and a results page."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]
AUDIO_SUFFIXES = {'.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aiff', '.aif'}
SETTINGS = {'width': 1280, 'height': 720, 'fps': 2, 'video_codec': 'libx264',
            'crf': 28, 'audio_codec': 'aac', 'audio_bitrate': '192k', 'version': 1}


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def run(command):
    return subprocess.check_output(command, text=True).strip()


def relative(path):
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def case_id(path, digest):
    stem = re.sub(r'[^a-z0-9]+', '-', path.stem.lower()).strip('-') or 'audio'
    return f'{stem[:90]}-{digest[:12]}'


def probe(path):
    data = json.loads(run(['ffprobe', '-v', 'error', '-show_format', '-show_streams',
                           '-of', 'json', str(path)]))
    audio = [s for s in data['streams'] if s['codec_type'] == 'audio']
    if len(audio) != 1:
        raise ValueError(f'Expected one audio stream: {path}')
    duration = float(data['format']['duration'])
    if not 0 < duration < float('inf'):
        raise ValueError(f'Invalid duration: {path}')
    return duration, {key: audio[0].get(key) for key in
                      ('codec_name', 'sample_rate', 'channels', 'channel_layout')}


def prepare(path, output, ffmpeg_version, overwrite):
    audio_hash = sha256(path)
    ident = case_id(path, audio_hash)
    video = output / f'{ident}.mp4'
    record_path = output / f'{ident}.json'
    duration, stream = probe(path)
    if video.exists() and record_path.exists() and not overwrite:
        record = json.loads(record_path.read_text())
        if (record.get('audio_sha256') == audio_hash and record.get('settings') == SETTINGS
                and record.get('video_sha256') == sha256(video)):
            print(f'Reusing {video.name}', flush=True)
            return record
    if (video.exists() or record_path.exists()) and not overwrite:
        raise ValueError(f'Existing output does not match its record: {video}. Use --overwrite.')
    with tempfile.TemporaryDirectory(prefix='content-id-') as temporary:
        temp = Path(temporary)
        # A text file avoids interpreting filenames as FFmpeg filter expressions.
        (temp / 'title.txt').write_text(f'Content ID audio experiment\n\n{path.stem}\n\n{audio_hash[:12]}', encoding='utf-8')
        partial = output / f'{ident}.partial.mp4'
        command = ['ffmpeg', '-hide_banner', '-loglevel', 'error', '-nostdin', '-y',
                   '-f', 'lavfi', '-i', 'color=c=0x18202b:s=1280x720:r=2',
                   '-i', str(path), '-map', '0:v:0', '-map', '1:a:0',
                   '-vf', 'drawtext=expansion=none:textfile=title.txt:fontcolor=white:fontsize=20:line_spacing=14:x=(w-text_w)/2:y=(h-text_h)/2',
                   '-t', str(duration), '-c:v', 'libx264', '-preset', 'ultrafast',
                   '-tune', 'stillimage', '-crf', '28', '-pix_fmt', 'yuv420p',
                   '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', str(partial)]
        print(f'Rendering {path.name}', flush=True)
        try:
            encoded = subprocess.run(command, cwd=temp, capture_output=True, text=True)
            if encoded.returncode:
                raise ValueError(f'FFmpeg failed for {path.name}: {encoded.stderr}')
            diagnostics = encoded.stderr.strip()
            if diagnostics:
                print(f'Encoding diagnostics for {path.name}:\n{diagnostics}', flush=True)
            partial.replace(video)
        finally:
            partial.unlink(missing_ok=True)
    record = {'case_id': ident, 'audio_file': relative(path), 'audio_sha256': audio_hash,
              'audio_duration_seconds': duration, 'source_audio': stream,
              'video_file': video.name, 'video_sha256': sha256(video),
              'settings': SETTINGS, 'ffmpeg_version': ffmpeg_version,
              'created_at_utc': datetime.now(timezone.utc).isoformat(),
              'command': command, 'encoding_diagnostics': diagnostics,
              'youtube_video_id': None, 'observations': []}
    record_path.write_text(json.dumps(record, indent=2) + '\n')
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('audio', nargs='*', type=Path, help='Audio paths; default: all recordings for --song')
    parser.add_argument('--song', default='st-louis-blues')
    parser.add_argument('--output', type=Path, help='Video/manifest directory')
    parser.add_argument('--results', type=Path, help='Results page; existing pages are preserved')
    parser.add_argument('--list', action='store_true', help='List inputs without writing anything')
    parser.add_argument('--overwrite', action='store_true', help='Re-render existing video outputs')
    args = parser.parse_args()
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.song):
        parser.error('--song must be a lowercase song slug')
    for path in args.audio:
        if path.suffix.lower() not in AUDIO_SUFFIXES:
            parser.error(f'Unsupported audio input: {path}')
    paths = args.audio or sorted((ROOT / 'songs' / args.song / 'inputs').glob('*'))
    paths = sorted({p.resolve() for p in paths if p.suffix.lower() in AUDIO_SUFFIXES})
    if not paths:
        parser.error('No audio inputs found')
    for path in paths:
        if not path.is_file():
            parser.error(f'Audio input not found: {path}')
    if args.list:
        for path in paths:
            print(relative(path))
        return
    for executable in ('ffmpeg', 'ffprobe'):
        if not shutil.which(executable):
            parser.error(f'{executable} is required')
    output = (args.output or ROOT / 'experiments' / 'content-id' / args.song / 'build').resolve()
    results = (args.results or output.parent / 'RESULTS.md').resolve()
    output.mkdir(parents=True, exist_ok=True)
    version = run(['ffmpeg', '-version']).splitlines()[0]
    try:
        records = [prepare(path, output, version, args.overwrite) for path in paths]
    except (ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f'{error}\n')
    try:
        revision = run(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'])
        dirty = bool(run(['git', '-C', str(ROOT), 'status', '--porcelain']))
    except subprocess.CalledProcessError:
        revision, dirty = None, None
    manifest = {'prepared_at_utc': datetime.now(timezone.utc).isoformat(),
                'repository_commit': revision, 'repository_has_uncommitted_changes': dirty,
                'cases': records}
    (output / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
    if not results.exists():
        template = (ROOT / 'templates' / 'CONTENT_ID_RESULTS.md').read_text()
        rows = '\n'.join(f'| {r["case_id"]} | {Path(r["audio_file"]).name.replace(chr(124), chr(92) + chr(124)).replace(chr(10), ' ')} | Not uploaded | — | — |'
                         for r in records)
        credits = ROOT / 'songs' / args.song / 'inputs' / 'CREDITS.toml'
        title = tomllib.loads(credits.read_text())['work']['title'] if credits.exists() else args.song.replace('-', ' ').title()
        flagged = [Path(r['audio_file']).name for r in records if r.get('encoding_diagnostics')]
        diagnostics = ('FFmpeg reported source decoding errors for: ' + ', '.join(flagged) + '. Review these cases before interpreting their results.') if flagged else 'No source decoding errors reported for this batch.'
        text = template.replace('{{song}}', title).replace('{{cases}}', rows).replace('{{diagnostics}}', diagnostics)
        results.parent.mkdir(parents=True, exist_ok=True)
        results.write_text(text)
        print(f'Created results page: {results}')
    else:
        print(f'Preserved results page: {results}')
    print(f'Prepared {len(records)} videos. Manifest: {output / "manifest.json"}')


if __name__ == '__main__':
    main()
