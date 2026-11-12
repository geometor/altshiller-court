"""Verification tests for Chapter I Semantic Ink-to-Vector SVGs and per-item interactive wiring."""

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
DOCSRC_CG_DIR = REPO_ROOT / "docsrc" / "college_geometry"
DOCSRC_CH01_DIR = DOCSRC_CG_DIR / "ch01-geometric-constructions"
DOCS_CG_DIR = REPO_ROOT / "docs" / "college_geometry"
DOCS_CH01_DIR = DOCS_CG_DIR / "ch01-geometric-constructions"

EXPECTED_SVG_LOCATIONS: dict[str, str] = {
    "0023.g1.svg": "b-general-method/005-problem",
    "0024.g1.svg": "b-general-method/006-problem",
    "0025.g1.svg": "b-general-method/007-problem",
    "0026.g1.svg": "b-general-method/008-problem",
    "0026.g2.svg": "b-general-method/008-problem",
    "0027.g1.svg": "b-general-method/009-problem",
    "0028.g1.svg": "b-general-method/009-problem",
    "0031.g1.svg": "c-geometric-loci/011-important-loci/locus-07",
    "0032.g1.svg": "c-geometric-loci/011-important-loci/locus-08",
    "0033.g1.svg": "c-geometric-loci/011-important-loci/locus-10",
    "0034.g1.svg": "c-geometric-loci/011-important-loci/locus-11",
    "0035.g1.svg": "c-geometric-loci/011-important-loci/locus-12",
    "0037.g1.svg": "c-geometric-loci/012-problem",
    "0038.g1.svg": "c-geometric-loci/013-problem",
    "0038.g2.svg": "c-geometric-loci/013-problem",
    "0039.g1.svg": "c-geometric-loci/014-problem",
    "0040.g1.svg": "d-indirect-elements/015-problem",
    "0041.g1.svg": "d-indirect-elements/017-problem",
    "0043.g1.svg": "d-indirect-elements/018-problem",
    "0044.g1.svg": "d-indirect-elements/019-problem",
    "0045.g1.svg": "d-indirect-elements/020-problem",
    "0046.g1.svg": "d-indirect-elements/022-problem",
}

G_ROLE_RE = re.compile(r":g:`([^`]+)`")
EQ_ROLE_RE = re.compile(r":eq:`([^`]+)`")


def test_svg_xml_schema_co_location_and_overlap_verification() -> None:
    """Verify all 22 Chapter I SVGs have no py_file keys, co-locate with their owning item, and hit >= 95% overlap."""
    compile_edition(REPO_ROOT)

    for json_path in sorted(CH01_RES_DIR.glob("*.json")):
        data = json.loads(json_path.read_text(encoding="utf-8"))
        for g in data.get("graphics", []):
            assert "py_file" not in g, f"Forbidden py_file key in {json_path.name}"
            assert "geometry" in g, f"Missing geometry dict in {json_path.name}"
            assert g.get("svg_file", "").endswith(".svg"), f"Missing svg_file in {json_path.name}"

    docsrc_svgs = sorted(DOCSRC_CG_DIR.rglob("*.svg"))
    assert len(docsrc_svgs) == 22

    for svg_name, rel_item_dir in EXPECTED_SVG_LOCATIONS.items():
        res_svg = CH01_RES_DIR / svg_name
        doc_svg = DOCSRC_CH01_DIR / rel_item_dir / svg_name
        assert res_svg.is_file(), f"Missing resource SVG: {res_svg}"
        assert doc_svg.is_file(), f"Expected co-located docsrc SVG at {doc_svg}"

        root = ET.fromstring(res_svg.read_text(encoding="utf-8"))
        assert "euclid-graphic" in root.attrib.get("class", "")
        assert root.attrib.get("data-graphic-id") == res_svg.stem

    report = verify_all_svgs(RESOURCES_DIR)
    assert report["verified_count"] == 22
    assert report["min_overlap_score"] >= 95.0, f"Overlap below 95%: {report}"
    for item in report["results"]:
        assert item["overlap_score"] >= 95.0, f"Low overlap on {item['svg_file']}: {item}"


def test_self_contained_g_and_eq_role_resolution() -> None:
    """Verify every :g: and :eq: role resolves globally AND strictly locally on each compiled item page."""
    compile_edition(REPO_ROOT)

    all_keys: set[str] = set()
    for svg_path in sorted(CH01_RES_DIR.glob("*.svg")):
        all_keys.update(build_svg_ref_keyset(svg_path))
    assert len(all_keys) >= 260

    g_count = 0
    eq_count = 0

    # 1. Check all resource folios against global SVG keyset
    for rst_path in sorted(RESOURCES_DIR.glob("*/*.rst")):
        text = rst_path.read_text(encoding="utf-8")
        default_gid = f"{rst_path.stem.split('.')[0]}.g1"
        for m in G_ROLE_RE.finditer(text):
            display, target = parse_geom_role_text(m.group(1))
            assert display, f"Empty :g: display in {rst_path}"
            for part in [p.strip() for p in target.split(";") if p.strip()]:
                cand_keys = parse_geometor_ref_keys(part, default_gid)
                assert any(k in all_keys for k in cand_keys), f"Broken :g: `{part}` in {rst_path}"
                g_count += 1
        for m in EQ_ROLE_RE.finditer(text):
            display, spec = parse_eq_role_text(m.group(1))
            assert display, f"Empty :eq: display in {rst_path}"
            sides = [s.strip() for s in re.split(r"[=,;]", spec) if s.strip()]
            assert len(sides) >= 2
            for side in sides:
                cand_keys = parse_geometor_ref_keys(side, default_gid)
                assert any(k in all_keys for k in cand_keys), f"Broken :eq: `{side}` in {rst_path}"
            eq_count += 1

    # 2. Check every compiled docsrc page strictly against SVGs co-located in its OWN directory
    for rst_path in sorted(DOCSRC_CG_DIR.rglob("*.rst")):
        text = rst_path.read_text(encoding="utf-8")
        local_svgs = sorted(rst_path.parent.glob("*.svg"))
        local_keys: set[str] = set()
        for lsvg in local_svgs:
            local_keys.update(build_svg_ref_keyset(lsvg))
        default_gid = local_svgs[0].stem if local_svgs else "none.g1"

        for m in G_ROLE_RE.finditer(text):
            display, target = parse_geom_role_text(m.group(1))
            assert display
            assert local_svgs, f":g: role `{m.group(1)}` on page without local SVG: {rst_path}"
            for part in [p.strip() for p in target.split(";") if p.strip()]:
                cand_keys = parse_geometor_ref_keys(part, default_gid)
                assert any(k in local_keys for k in cand_keys), (
                    f"Cross-item or broken :g: `{part}` on {rst_path} (local SVGs={[s.name for s in local_svgs]})"
                )

        for m in EQ_ROLE_RE.finditer(text):
            display, spec = parse_eq_role_text(m.group(1))
            assert display
            assert local_svgs, f":eq: role `{m.group(1)}` on page without local SVG: {rst_path}"
            for side in [s.strip() for s in re.split(r"[=,;]", spec) if s.strip()]:
                cand_keys = parse_geometor_ref_keys(side, default_gid)
                assert any(k in local_keys for k in cand_keys), (
                    f"Cross-item or broken :eq: `{side}` on {rst_path} (local SVGs={[s.name for s in local_svgs]})"
                )

    assert g_count >= 350
    assert eq_count >= 25


def test_folio_scanner_svg_detection_and_clean_rst_rendering() -> None:
    """Verify FolioScanner detects all 22 SVGs in folios 0020-0052 and produces zero Docutils System Messages."""
    publish_src = REPO_ROOT.parents[1] / "photon-platform" / "publish" / "src"
    if publish_src.is_dir() and str(publish_src) not in sys.path:
        sys.path.insert(0, str(publish_src))
    scanner_mod = pytest.importorskip("photon_platform.publish.folio_review.scanner")
    scanner = scanner_mod.FolioScanner(REPO_ROOT)
    stats = scanner.get_summary_stats()
    assert stats["total_folios"] == 334
    assert stats["total_graphics"] == 22
    assert stats["total_svgs"] == 22

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
        if 20 <= item["folio_int"] <= 52:
            for g in detail["graphics"]:
                assert g["svg_exists"] is True, f"Missing SVG for {item['folio']}.{g['id']}"
                assert g["py_exists"] is False, f"Unexpected .py for {item['folio']}.{g['id']}"
                assert g["in_md_format"] == "svg", (
                    f"Expected .. picture:: *.svg in {item['folio']}.rst, got {g['in_md_format']}"
                )
                ch01_svg_graphics += 1

    assert ch01_svg_graphics == 22


def test_published_html_collections_and_inline_svgs() -> None:
    """Verify built HTML collection cards include inline SVG thumbnails and leaf pages inline all 22 SVGs."""
    if not (DOCS_CG_DIR / "index.html").is_file():
        return

    # Verify collection index pages render inline .euclid-graphic SVG thumbnails on cards
    for coll_rel in (
        "b-general-method/index.html",
        "c-geometric-loci/011-important-loci/index.html",
        "d-indirect-elements/index.html",
    ):
        coll_html = (DOCS_CH01_DIR / coll_rel).read_text(encoding="utf-8")
        assert "euclid-graphic" in coll_html, f"Expected inline SVG thumbnails on {coll_rel}"

    # Verify every expected Chapter I SVG is inlined on its exact built leaf item HTML page
    for svg_name, rel_item_dir in EXPECTED_SVG_LOCATIONS.items():
        gid = svg_name[:-4]
        item_html_path = DOCS_CH01_DIR / rel_item_dir / "index.html"
        comm_html_path = DOCS_CH01_DIR / rel_item_dir / "commentary.html"
        assert item_html_path.is_file(), f"Missing built item HTML: {item_html_path}"
        assert comm_html_path.is_file(), f"Missing built commentary HTML: {comm_html_path}"
        html_text = item_html_path.read_text(encoding="utf-8")
        assert f'data-graphic-id="{gid}"' in html_text, (
            f"Missing inlined SVG {gid} in {item_html_path}"
        )
        assert 'class="geom-ref"' in html_text
        assert "enunciation" in html_text
        assert "geometor_interactive.js" in html_text
