"""Bounding-box figure cropper and dark-mode inverter for College Geometry folios.

Compatible natively with ``publish folio`` (``photon_platform.publish.folio_review``),
reading ``<NNNN>.json`` definitions of the form::

    {
      "folio": "0023",
      "page": "4",
      "graphics": [
        {
          "id": "g1",
          "type": "diagram",
          "file": "0023.g1.png",
          "bbox": [x, y, w, h],
          "caption": "Fig. 1 — Construction of a circle touching a line at a given point and passing through an external point.",
          "white_point": 238
        }
      ]
    }

Generates both ``<NNNN>.<gid>.png`` (clean white-point normalized light-mode diagram)
and ``<NNNN>.<gid>.inverted.png`` (crisp dark-mode diagram).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageOps


def normalize_diagram_crop(crop: Image.Image, white_point: int = 238) -> Image.Image:
    """Normalize paper background >= ``white_point`` to pure white while preserving ink."""
    gray = crop.convert("L")
    lut = [255 if i >= white_point else round(i * 255.0 / white_point) for i in range(256)]
    clean_gray = gray.point(lut)
    return clean_gray.convert("RGB")


def extract_graphics_for_json(json_path: Path) -> list[Path]:
    """Extract all calibrated graphics defined in ``json_path`` from ``<folio>.png``."""
    data: dict[str, Any] = json.loads(json_path.read_text(encoding="utf-8"))
    folio = str(data.get("folio") or json_path.stem)
    scan_path = json_path.parent / f"{folio}.png"
    if not scan_path.is_file():
        raise FileNotFoundError(f"Folio scan not found: {scan_path}")

    written: list[Path] = []
    with Image.open(scan_path) as img:
        img_w, img_h = img.size
        for g in data.get("graphics", []):
            bbox = g.get("bbox")
            if not bbox or len(bbox) != 4:
                continue
            x, y, w, h = [int(v) for v in bbox]
            x1 = max(0, min(img_w - 1, x))
            y1 = max(0, min(img_h - 1, y))
            x2 = max(x1 + 1, min(img_w, x + w))
            y2 = max(y1 + 1, min(img_h, y + h))

            gid = str(g.get("id") or "g1")
            if gid.isdigit():
                gid = f"g{gid}"
            out_file = str(g.get("file") or f"{folio}.{gid}.png")
            out_path = json_path.parent / out_file
            stem_base = out_path.name[:-4] if out_path.name.endswith(".png") else out_path.stem
            inv_path = json_path.parent / f"{stem_base}.inverted.png"

            white_point = int(g.get("white_point") or 238)
            raw_crop = img.crop((x1, y1, x2, y2))
            clean_rgb = normalize_diagram_crop(raw_crop, white_point=white_point)
            inverted_rgb = ImageOps.invert(clean_rgb)

            clean_rgb.save(out_path, format="PNG", optimize=True)
            inverted_rgb.save(inv_path, format="PNG", optimize=True)
            written.extend([out_path, inv_path])

    return written


def extract_all_graphics(volume_dir: Path) -> dict[str, Any]:
    """Extract graphics across all ``<NNNN>.json`` files in ``resources/college_geometry/``."""
    json_files = sorted(
        p for p in volume_dir.glob("*/*.json")
        if p.stem.isdigit() and len(p.stem) == 4
    )
    total_crops = 0
    processed_folios: list[str] = []
    for jp in json_files:
        outputs = extract_graphics_for_json(jp)
        if outputs:
            processed_folios.append(jp.stem)
            total_crops += len(outputs) // 2

    return {
        "folios_with_graphics": len(processed_folios),
        "diagrams_extracted": total_crops,
        "files_written": total_crops * 2,
        "folios": processed_folios,
    }
