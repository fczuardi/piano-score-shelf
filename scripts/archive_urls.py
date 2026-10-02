#!/usr/bin/env python3
"""List source URLs or submit them to the Wayback Machine."""

import argparse
from pathlib import Path
import tomllib
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def sources():
    for manifest in sorted((ROOT / "songs").glob("*/inputs/CREDITS.toml")):
        data = tomllib.loads(manifest.read_text())
        for source in data.get("sources", []):
            yield manifest.relative_to(ROOT), source
        for index, lead in enumerate(data.get("leads", []), 1):
            yield manifest.relative_to(ROOT), {
                "id": f"lead-{index}",
                "url": lead["url"],
            }


def submit_wayback(url):
    request = Request(
        "https://web.archive.org/save/" + url,
        headers={"User-Agent": "piano-score-shelf provenance bot/1.0"},
        method="POST",
    )
    with urlopen(request, timeout=120) as response:
        location = response.headers.get("Content-Location") or response.geturl()
        if location.startswith("/"):
            location = "https://web.archive.org" + location
        return location


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--list", action="store_true", help="print the queue without making requests")
    action.add_argument("--wayback", action="store_true", help="submit every source URL to Save Page Now")
    args = parser.parse_args()
    failed = False
    for manifest, source in sources():
        prefix = f"{manifest}: {source['id']}"
        if args.list:
            print(f"{prefix}\n  {source['url']}")
            continue
        try:
            print(f"{prefix}\n  {submit_wayback(source['url'])}")
        except (HTTPError, URLError, TimeoutError) as error:
            failed = True
            print(f"{prefix}\n  ERROR: {error}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
