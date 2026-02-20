# GEMINI.md - Project Context

## Project Overview
This is a **Non-Code Project** (Asset Repository) that stores various game assets (images, icons, backgrounds, etc.) for the **altoy** fan project (https://github.com/JforPlay/altoy). The assets are sourced from the game **Azur Lane** and are primarily used to power a fan-made viewer for story, skin, and game information in Korean.

## Directory Overview
The repository is structured into numerous folders, each containing a specific category of game assets. Most assets are in `.png` format, often named with game IDs or descriptive English/Pinyin/Romanized names.

### Key Directories and Contents
- **`activitybanner/`**: UI banners for game activities and events.
- **`aircrafticon/`**: Icons for different aircraft types and equipment.
- **`bg/` & `commonbg/`**: Game backgrounds used in various scenes.
- **`dorm3d.../`**: Assets related to the "Dorm 3D" feature (collections, icons, memories, photos).
- **`educate.../`**: Assets for the "Education" (Secret Shipyard/Childhood) system, including avatars, pictures, and props.
- **`output_expressions/`**: Large collection of character facial expressions and "painting" faces, organized by character ID.
- **`item/` & `props/`**: Icons for game items, currencies, and miscellaneous props.
- **`spweapon/`**: Icons for "Special Weapons" (Unique Augments), named by weapon ID.
- **`loadingbg/`**: Loading screen images.
- **`emoji/`**: Game chat emojis.
- **`mangapic/`**: Images from in-game manga or comics.
- **`voteships/`**: Assets related to popularity polls/voting events.

### Key Files
- **`README.md`**: Contains a disclaimer regarding asset usage, project links, and credits to the original developers (Manjuu, Yostar, etc.).
- **`output_expressions/expression_manifest.json`**: (Likely) A mapping or metadata file for the expressions stored in the subdirectories.

## Usage
The contents of this directory are intended to be served as static assets for the `altoy` web application. Developers or tools interacting with this repository should:
1.  Reference assets using their relative paths (e.g., `spweapon/10000.png`).
2.  Be aware that many files are named based on internal game IDs.
3.  Respect the copyright and disclaimer mentioned in `README.md`.

## Note on Development
This repository does not contain source code for building or running an application. It is a data-only repository. Updates typically involve adding new assets extracted from the game client or updating existing ones.
