"""Command-line interface for the Altshiller-Court Digital Scriptorium pipeline."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

from .compile_edition import compile_edition, get_edition_status
from .graphics import extract_all_graphics
from .ingest import ingest_folios
from .svg_compiler import compile_all_svgs, verify_all_svgs


def _default_repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def build_parser() -> argparse.ArgumentParser:
    """Construct the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="altshiller-court",
        description="Digital Scriptorium & Book Codex pipeline for Nathan Altshiller-Court's College Geometry (1952).",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=_default_repo_root(),
        help="Path to the geometor/altshiller-court repository root.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_ingest = sub.add_parser("ingest", help="Extract standardized 300 DPI folio PNGs from source PDF.")
    p_ingest.add_argument("--dpi", type=int, default=300, help="Rasterization DPI (default: 300).")
    p_ingest.add_argument("--force", action="store_true", help="Re-extract existing folio PNGs.")

    sub.add_parser("graphics", help="Crop and normalize light/dark diagram PNGs from <NNNN>.json files.")
    sub.add_parser("svg", help="Compile formal <NNNN>.json geometry definitions into interactive SVGs.")
    p_verify = sub.add_parser("verify-svg", help="Verify SVG ink overlap against 300 DPI diagram crops.")
    p_verify.add_argument(
        "--overlays",
        type=Path,
        default=None,
        help="Optional directory to write RGB overlap diagnostic PNGs.",
    )
    sub.add_parser("compile", help="Compile de-paginated 2-Track Book Codex and apparatus into docsrc/.")
    sub.add_parser("status", help="Show archival scan, transcription, graphics, SVG, and review counts.")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for ``altshiller-court`` CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)
    repo_root: Path = args.root.resolve()

    if args.command == "ingest":
        result = ingest_folios(repo_root, dpi=args.dpi, force=args.force)
    elif args.command == "graphics":
        result = extract_all_graphics(repo_root / "resources" / "college_geometry")
    elif args.command == "svg":
        result = compile_all_svgs(repo_root / "resources" / "college_geometry")
    elif args.command == "verify-svg":
        result = verify_all_svgs(
            repo_root / "resources" / "college_geometry",
            overlay_dir=args.overlays,
        )
    elif args.command == "compile":
        result = compile_edition(repo_root)
    elif args.command == "status":
        result = get_edition_status(repo_root)
    else:
        parser.error(f"Unknown command: {args.command}")
        return 2

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
