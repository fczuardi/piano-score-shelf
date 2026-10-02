default:
    @just --list

# Build derived content and launch the local Zola development server
serve:
    python3 scripts/build.py
    zola serve
