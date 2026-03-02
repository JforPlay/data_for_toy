"""Convert PNG images to WebP format across the repository.

Walks the repo recursively, converts .png files to .webp, and deletes
the originals on success. Skips excluded directories.
"""

import argparse
import os
import sys
import time

from PIL import Image


EXCLUDED_DIRS = {"output_expressions", "missingno", "paintingface"}


def convert_png_to_webp(png_path, quality, lossless):
    """Convert a single PNG file to WebP. Returns True on success."""
    webp_path = os.path.splitext(png_path)[0] + ".webp"
    img = Image.open(png_path)
    img.save(webp_path, "WEBP", quality=quality, lossless=lossless)
    os.remove(png_path)
    return webp_path


def main():
    parser = argparse.ArgumentParser(
        description="Convert PNG images to WebP format."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Root directory to walk (default: current directory)",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=80,
        help="WebP quality 1-100 (default: 80, ignored if --lossless)",
    )
    parser.add_argument(
        "--lossless",
        action="store_true",
        help="Use lossless WebP compression",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be converted without actually converting",
    )
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    converted = 0
    failed = 0
    skipped_dirs = 0
    start = time.time()

    for dirpath, dirnames, filenames in os.walk(root):
        # Prune excluded directories in-place so os.walk doesn't descend
        before = len(dirnames)
        dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
        skipped_dirs += before - len(dirnames)

        # Also skip hidden directories (e.g. .git, .claude)
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]

        for fname in filenames:
            if not fname.lower().endswith(".png"):
                continue

            png_path = os.path.join(dirpath, fname)

            if args.dry_run:
                print(f"[DRY RUN] {png_path}")
                converted += 1
                continue

            try:
                webp_path = convert_png_to_webp(
                    png_path, args.quality, args.lossless
                )
                converted += 1
                print(f"[OK] {png_path} -> {webp_path}")
            except Exception as e:
                failed += 1
                print(f"[FAIL] {png_path}: {e}", file=sys.stderr)

    elapsed = time.time() - start
    print(f"\n--- Summary ---")
    print(f"Converted: {converted}")
    print(f"Failed:    {failed}")
    print(f"Excluded dirs pruned: {skipped_dirs}")
    print(f"Time: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
