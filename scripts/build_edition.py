#!/usr/bin/env python3
"""Export a modern score edition from its canonical MusicXML file."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("song", nargs="?", default="st-louis-blues")
    parser.add_argument("edition", nargs="?", default="modern-1914")
    parser.add_argument("--sync-only", action="store_true")
    args = parser.parse_args()

    directory = ROOT / "songs" / args.song / "editions" / args.edition
    manifest_path = directory / "EDITION.toml"
    if not manifest_path.exists():
        raise SystemExit(f"edition manifest not found: {manifest_path.relative_to(ROOT)}")

    data = tomllib.loads(manifest_path.read_text())
    executable = shutil.which("musescore") or shutil.which("mscore")
    if not executable:
        raise SystemExit("MuseScore is required. On this system: sudo pacman -S musescore")
    environment = os.environ.copy()
    environment["QT_QPA_PLATFORM"] = "offscreen"

    canonical = directory / data["edition"]["canonical_file"]
    if args.sync_only:
        working = directory / data["edition"]["working_file"]
        if not working.exists():
            raise SystemExit(f"MuseScore working file not found: {working.relative_to(ROOT)}")
        subprocess.run(
            [executable, "--export-to", str(canonical), str(working)],
            check=True,
            env=environment,
        )
        return
    if not canonical.exists():
        raise SystemExit(
            f"canonical score not found: {canonical.relative_to(ROOT)}\n"
            "Run `just edition-sync` after saving the MuseScore working file."
        )

    outputs = data["outputs"]
    build = directory / "build"
    pages = build / "pages"
    pages.mkdir(parents=True, exist_ok=True)
    targets = [
        directory / outputs["pdf"],
        directory / outputs["midi"],
        directory / f'{outputs["svg_prefix"]}.svg',
    ]
    for target in targets:
        subprocess.run(
            [executable, "--export-to", str(target), str(canonical)],
            check=True,
            env=environment,
        )


if __name__ == "__main__":
    main()
