"""Standardized 300 DPI folio ingestion for Altshiller-Court's College Geometry."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from PIL import Image

DEFAULT_ROOT_PDF_NAME = "College Geometry_ An Introduction to the M - Nathan Altshiller-Court.pdf"


def ensure_source_pdf(repo_root: Path) -> Path:
    """Ensure ``resources/college_geometry/pdfs/college_geometry.pdf`` exists.

    Copies from the root Dover PDF if not yet present in ``pdfs/``, leaving the
    root file intact.
    """
    target_pdf = repo_root / "resources" / "college_geometry" / "pdfs" / "college_geometry.pdf"
    if target_pdf.is_file():
        return target_pdf

    root_pdf = repo_root / DEFAULT_ROOT_PDF_NAME
    if not root_pdf.is_file():
        pdfs = sorted(repo_root.glob("*.pdf"))
        if not pdfs:
            raise FileNotFoundError(
                f"Source PDF not found at {target_pdf} or in {repo_root}."
            )
        root_pdf = pdfs[0]

    target_pdf.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root_pdf, target_pdf)
    return target_pdf


def load_structure_map(volume_dir: Path) -> dict[str, Any]:
    """Load ``structure_map.json`` from ``resources/college_geometry/``."""
    map_path = volume_dir / "structure_map.json"
    if not map_path.is_file():
        raise FileNotFoundError(f"Structure map not found: {map_path}")
    return json.loads(map_path.read_text(encoding="utf-8"))


def ingest_folios(
    repo_root: Path,
    dpi: int = 300,
    force: bool = False,
) -> dict[str, Any]:
    """Render all 334 PDF pages at ``dpi`` and route into chapter directories.

    Cover folios (``0001`` and ``0334``) preserve full RGB color; interior text
    and diagram folios (``0002``–``0333``) are saved as crisp 8-bit grayscale PNGs
    with zero loss of line stroke or anti-aliasing fidelity.
    """
    pdf_path = ensure_source_pdf(repo_root)
    volume_dir = repo_root / "resources" / "college_geometry"
    structure = load_structure_map(volume_dir)
    folios = structure["folios"]

    if not force:
        missing = [
            f for f in folios
            if not (volume_dir / f["chapter_dir"] / f"{f['folio']}.png").is_file()
        ]
        if not missing:
            return {
                "total_folios": len(folios),
                "extracted": 0,
                "skipped_existing": len(folios),
                "pdf_path": str(pdf_path),
            }

    for ch in structure["chapters"]:
        (volume_dir / ch["dir"]).mkdir(parents=True, exist_ok=True)

    extracted = 0
    with tempfile.TemporaryDirectory(dir=str(volume_dir)) as tmp_dir:
        tmp_prefix = Path(tmp_dir) / "page"
        cmd = [
            "pdftoppm",
            "-png",
            "-r",
            str(dpi),
            str(pdf_path),
            str(tmp_prefix),
        ]
        subprocess.run(cmd, check=True)

        for entry in folios:
            folio_id = entry["folio"]
            pdf_page = int(entry["pdf_page"])
            chapter_dir = entry["chapter_dir"]
            dest_png = volume_dir / chapter_dir / f"{folio_id}.png"

            if dest_png.is_file() and not force:
                continue

            candidates = [
                Path(tmp_dir) / f"page-{pdf_page:03d}.png",
                Path(tmp_dir) / f"page-{pdf_page:04d}.png",
                Path(tmp_dir) / f"page-{pdf_page}.png",
            ]
            raw_png = next((c for c in candidates if c.is_file()), None)
            if raw_png is None:
                raise FileNotFoundError(f"Rendered page {pdf_page} not found in {tmp_dir}")

            if entry.get("is_cover", False):
                shutil.move(str(raw_png), str(dest_png))
            else:
                with Image.open(raw_png) as im:
                    gray = im.convert("L")
                    gray.save(dest_png, format="PNG", optimize=True)
            extracted += 1

    return {
        "total_folios": len(folios),
        "extracted": extracted,
        "skipped_existing": len(folios) - extracted,
        "pdf_path": str(pdf_path),
    }
