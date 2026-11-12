"""Verification tests for Chapter I Semantic Ink-to-Vector SVGs and interactive text wiring."""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

from geometor.altshiller_court.compile_edition import compile_edition
from geometor.altshiller_court.svg_compiler import (
    build_svg_ref_keyset,
    parse_eq_role_text,
    parse_geom_role_text,
    parse_geometor_ref_keys,
    verify_all_svgs,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RESOURCES_DIR = REPO_ROOT / "resources" / "college_geometry"
CH01_RES_DIR = RESOURCES_DIR / "01_geometric_constructions"
DOCSRC_CH01_DIR = REPO_ROOT / "docsrc" / "college_geometry" / "ch01-geometric-constructions"
DOCS_CH01_HTML = (
    REPO_ROOT
    / "docs"
    / "college_geometry"
    / "ch01-geometric-constructions"
    / "ch01-geometric-constructions-en.html"
)

EXPECTED_CH01_SVGS = (
    "0023.g1.svg",
    "0024.g1.svg",
    "0025.g1.svg",
    "0026.g1.svg",
    "0026.g2.svg",
    "0027.g1.svg",
    "0028.g1.svg",
    "0031.g1.svg",
    "0032.g1.svg",
    "0033.g1.svg",
    "0034.g1.svg",
    "0035.g1.svg",
    "0037.g1.svg",
    "0038.g1.svg",
    "0038.g2.svg",
    "0039.g1.svg",
    "0040.g1.svg",
)

G_ROLE_RE = re.compile(r":g:`([^`]+)`")
EQ_ROLE_RE = re.compile(r":eq:`([^`]+)`")


def test_svg_xml_schema_and_overlap_verification() -> None:
    """Verify all 17 Chapter I SVGs exist, have no py_file keys, parse cleanly, and hit >= 95% ink overlap."""
    compile_edition(REPO_ROOT)

    for json_path in sorted(CH01_RES_DIR.glob("*.json")):
        data = json.loads(json_path.read_text(encoding="utf-8"))
        for g in data.get("graphics", []):
            assert "py_file" not in g, f"Forbidden py_file key in {json_path.name}"
            assert "geometry" in g, f"Missing geometry dict in {json_path.name}"
            assert g.get("svg_file", "").endswith(".svg"), f"Missing svg_file in {json_path.name}"

    for svg_name in EXPECTED_CH01_SVGS:
        res_svg = CH01_RES_DIR / svg_name
        doc_svg = DOCSRC_CH01_DIR / svg_name
        assert res_svg.is_file(), f"Missing resource SVG: {res_svg}"
        assert doc_svg.is_file(), f"Missing docsrc SVG: {doc_svg}"

        root = ET.fromstring(res_svg.read_text(encoding="utf-8"))
        assert "euclid-graphic" in root.attrib.get("class", "")
        assert root.attrib.get("data-graphic-id") == res_svg.stem

    report = verify_all_svgs(RESOURCES_DIR)
    assert report["verified_count"] == 17
    assert report["min_overlap_score"] >= 95.0, f"Overlap below 95%: {report}"
    for item in report["results"]:
        assert item["overlap_score"] >= 95.0, f"Low overlap on {item['svg_file']}: {item}"


def test_interactive_g_and_eq_role_resolution() -> None:
    """Verify every :g: and :eq: target across resources/ and docsrc/ resolves against build_svg_ref_keyset."""
    compile_edition(REPO_ROOT)

    all_keys: set[str] = set()
    for svg_path in sorted(CH01_RES_DIR.glob("*.svg")):
        all_keys.update(build_svg_ref_keyset(svg_path))
    assert len(all_keys) >= 200

    rst_files = sorted(RESOURCES_DIR.glob("*/*.rst")) + sorted(
        (REPO_ROOT / "docsrc" / "college_geometry").rglob("*.rst")
    )

    g_count = 0
    eq_count = 0

    for rst_path in rst_files:
        text = rst_path.read_text(encoding="utf-8")
        default_gid = f"{rst_path.stem.split('.')[0]}.g1"

        for m in G_ROLE_RE.finditer(text):
            raw = m.group(1)
            display, target = parse_geom_role_text(raw)
            assert display, f"Empty :g: display in {rst_path}: {raw}"
            parts = [p.strip() for p in target.split(";") if p.strip()]
            assert parts, f"Empty :g: target in {rst_path}: {raw}"
            for part in parts:
                cand_keys = parse_geometor_ref_keys(part, default_gid)
                assert cand_keys, f"Unparseable :g: target `{part}` in {rst_path.name}"
                assert any(k in all_keys for k in cand_keys), (
                    f"Broken :g: reference `{part}` (candidates={cand_keys}) in {rst_path}"
                )
                g_count += 1

        for m in EQ_ROLE_RE.finditer(text):
            raw = m.group(1)
            display, spec = parse_eq_role_text(raw)
            assert display, f"Empty or malformed :eq: display in {rst_path}: {raw}"
            sides = [s.strip() for s in re.split(r"[=,;]", spec) if s.strip()]
            assert len(sides) >= 2, f":eq: requires at least 2 operands in {rst_path}: {raw}"
            for side in sides:
                cand_keys = parse_geometor_ref_keys(side, default_gid)
                assert cand_keys, f"Unparseable :eq: operand `{side}` in {rst_path.name}"
                assert any(k in all_keys for k in cand_keys), (
                    f"Broken :eq: operand `{side}` (candidates={cand_keys}) in {rst_path}"
                )
            eq_count += 1

    assert g_count >= 250
    assert eq_count >= 20


def test_folio_scanner_svg_detection_and_clean_rst_rendering() -> None:
    """Verify FolioScanner detects all 17 SVGs in RST and produces zero Docutils System Messages."""
    publish_src = REPO_ROOT.parents[1] / "photon-platform" / "publish" / "src"
    if publish_src.is_dir() and str(publish_src) not in sys.path:
        sys.path.insert(0, str(publish_src))
    scanner_mod = pytest.importorskip("photon_platform.publish.folio_review.scanner")
    scanner = scanner_mod.FolioScanner(REPO_ROOT)
    stats = scanner.get_summary_stats()
    assert stats["total_folios"] == 334
    assert stats["total_graphics"] >= 17
    assert stats["total_svgs"] >= 17

    ch01_svg_graphics = 0
    for item in scanner.scan(force=True):
        if not item["has_md"] and not item["has_notes"]:
            continue
        detail = scanner.get_folio_detail(item["volume"], item["folio"])
        assert detail is not None
        assert "System Message:" not in detail["md_html"], (
            f"Docutils System Message in {item['folio']}.rst:\n{detail['md_html']}"
        )
        assert "System Message:" not in detail["notes_html"], (
            f"Docutils System Message in {item['folio']}.notes.rst:\n{detail['notes_html']}"
        )
        if 20 <= item["folio_int"] <= 40:
            for g in detail["graphics"]:
                assert g["svg_exists"] is True, f"Missing SVG for {item['folio']}.{g['id']}"
                assert g["py_exists"] is False, f"Unexpected .py for {item['folio']}.{g['id']}"
                assert g["in_md_format"] == "svg", (
                    f"Expected .. picture:: *.svg in {item['folio']}.rst, got {g['in_md_format']}"
                )
                ch01_svg_graphics += 1

    assert ch01_svg_graphics == 17


def test_published_html_inlines_all_17_interactive_svgs() -> None:
    """Verify built HTML contains all 17 inlined euclid-graphic SVGs, interactive spans, and JS."""
    if not DOCS_CH01_HTML.is_file():
        return
    html_text = DOCS_CH01_HTML.read_text(encoding="utf-8")
    for svg_name in EXPECTED_CH01_SVGS:
        gid = svg_name[:-4]
        assert f'data-graphic-id="{gid}"' in html_text, f"Missing inlined SVG {gid} in built HTML"

    inline_svgs = re.findall(r'<svg\b[^>]*class="[^"]*euclid-graphic[^"]*"', html_text)
    assert len(inline_svgs) == 17
    assert 'class="geom-ref"' in html_text
    assert 'class="geom-eq-ref"' in html_text
    assert "enunciation" in html_text
    assert "assertion" in html_text
    assert "geometor_interactive.js" in html_text
