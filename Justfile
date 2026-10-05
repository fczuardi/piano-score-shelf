default:
    @just --list

# Build derived content and launch the local Zola development server
serve:
    python3 scripts/build.py
    zola serve

# Export PDF, SVG pages, and MIDI from a modern edition's canonical MusicXML
edition-build song="st-louis-blues" edition="modern-1914":
    python3 scripts/build_edition.py {{song}} {{edition}}

# Refresh canonical MusicXML after saving the MuseScore working file
edition-sync song="st-louis-blues" edition="modern-1914":
    python3 scripts/build_edition.py {{song}} {{edition}} --sync-only

# List audio inputs for a Content ID experiment without writing files
content-id-list song="st-louis-blues":
    python3 scripts/content_id_videos.py --song {{song}} --list

# Create local test videos and initialize a results page; no uploads
content-id-videos song="st-louis-blues":
    python3 scripts/content_id_videos.py --song {{song}}
