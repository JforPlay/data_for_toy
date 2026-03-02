# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **static asset repository** (no source code) that stores game assets for the [altoy](https://github.com/JforPlay/altoy) fan project — a Korean-language viewer for Azur Lane story, skin, and game information. Updates align with Korean game patches (e.g., "KR 8.4.92").

All assets are copyrighted by Manjuu, Xiamen Yongshi, Yostar Inc, and X.D. Global Limited. This repo is non-commercial.

## Repository Structure

~40,000 PNG files organized by game feature, with assets typically named by internal game numeric IDs (e.g., `100011.png`).

### Largest / Most Important Directories

- **`output_expressions/`** (~24,500 files) — Character art and facial expressions, organized into subdirectories per character ID. Each contains a `painting.png` (full art) and `painting_face_*.png` variants.
- **`equips/`** — Equipment/gear icons
- **`props/`** — Miscellaneous prop icons
- **`bg/`** — Scene background images
- **`island/`** — Island feature assets (7 subdirectories: charicon, drawawardicon, dressicon, furnitureicon, goodsicon, invitation, photoframe)
- **`emoji/`** — Chat emojis
- **`spweapon/`** — Special Weapon (Unique Augment) icons
- **`dorm3d*/`** (5 dirs) — Dorm 3D feature assets
- **`educate*/`** (6 dirs) — Education/Secret Shipyard system assets

### Key Data File

**`output_expressions/expression_manifest.json`** (~62,000 lines) — Maps character IDs to expression metadata:
```json
{
  "CHARACTER_ID": {
    "faces": ["0", "1", "2"],       // expression variant indices
    "box": [x, y, width, height],   // bounding box for face region
    "size": [width, height]          // full image dimensions
  }
}
```

## Working With This Repository

- There are no build steps, tests, or linting — this is a data-only repo.
- Assets are referenced by relative path from the repo root (e.g., `spweapon/10000.png`).
- Commits follow the pattern: `update data KR X.Y.Z` for patch updates, or descriptive messages for structural changes.
- The repo is ~35GB; git operations can be slow.
