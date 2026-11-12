"""Verification tests for the GEOMETOR • altshiller-court Digital Scriptorium."""

from __future__ import annotations

import json
import re
from pathlib import Path

from geometor.altshiller_court.compile_edition import (
    apparatus_slug,
    compile_edition,
    get_edition_status,
)
from geometor.altshiller_court.ingest import load_structure_map

REPO_ROOT = Path(__file__).resolve().parents[1]
RESOURCES_DIR = REPO_ROOT / "resources" / "college_geometry"
DOCSRC_ROOT = REPO_ROOT / "docsrc"
DOCSRC_DIR = DOCSRC_ROOT / "college_geometry"

PERSON_RE = re.compile(r":person:`([^`]+)`")
CITE_RE = re.compile(r":cite:`([^`]+)`")
TERM_RE = re.compile(r":term:`([^`]+)`")
ANCHOR_DEF_RE = re.compile(r"^\.\.\s+_([A-Za-z0-9_.\-]+):", flags=re.MULTILINE)
REF_ROLE_RE = re.compile(r":ref:`([^`]+)`")


def test_structure_map_integrity() -> None:
    """Verify the 334-folio structure map, pagination invariant, and 699 articles."""
    smap = load_structure_map(RESOURCES_DIR)
    assert smap["work"]["pdf_pages"] == 334
    assert smap["work"]["total_articles"] == 699

    folios = smap["folios"]
    assert len(folios) == 334
    assert folios[0]["folio"] == "0001"
    assert folios[-1]["folio"] == "0334"

    chapters = smap["chapters"]
    assert len(chapters) == 13
    assert chapters[0]["dir"] == "00_frontmatter"
    assert chapters[1]["sections"][-1]["title"] == "Review Exercises (1–67)"
    assert chapters[-1]["dir"] == "12_index"

    # Unbroken pagination law: PDF Folio = Printed Page + 19 for body & backmatter
    by_folio = {entry["folio"]: entry for entry in folios}
    assert by_folio["0020"]["printed_page"] == "1"
    assert by_folio["0040"]["printed_page"] == "21"
    assert by_folio["0052"]["printed_page"] == "33"
    assert by_folio["0312"]["printed_page"] == "293"
    assert by_folio["0314"]["printed_page"] == "295"
    assert by_folio["0332"]["printed_page"] == "313"

    # Blank versos
    for blank_folio in ("0005", "0009", "0015", "0019", "0313", "0333"):
        assert by_folio[blank_folio]["is_blank"] is True


def test_edition_status_and_assets() -> None:
    """Verify extracted 300 DPI scans, 65 Frontmatter + Ch. I + Ch. III folios, 32 crops, and 32 SVGs."""
    status = get_edition_status(REPO_ROOT)
    assert status["total_folios"] == 334
    assert status["scans_present"] == 334
    assert status["rst_transcribed"] == 65
    assert status["notes_present"] == 65
    assert status["folios_with_graphics"] == 29
    assert status["diagram_crops"] == 32
    assert status["svg_diagrams"] == 32
    assert status["verified_reviews"] == 65


def test_apparatus_registries_and_role_resolution() -> None:
    """Ensure every :person:, :cite:, and :term: role in resources/ and docsrc/ resolves cleanly."""
    compile_edition(REPO_ROOT)

    persons = json.loads((RESOURCES_DIR / "persons.json").read_text(encoding="utf-8"))
    citations = json.loads((RESOURCES_DIR / "citations.json").read_text(encoding="utf-8"))
    glossary = json.loads((RESOURCES_DIR / "glossary.json").read_text(encoding="utf-8"))
    reviews = json.loads((RESOURCES_DIR / "folio_reviews.json").read_text(encoding="utf-8"))

    assert len(persons) >= 67
    assert len(citations) >= 31
    assert len(glossary) >= 57
    assert "datum" in glossary
    assert len(reviews) == 65

    person_slugs = {apparatus_slug(k) for k in persons}
    cite_slugs = {apparatus_slug(k) for k in citations}
    term_slugs = {apparatus_slug(k) for k in glossary}

    def extract_slug(raw: str) -> str:
        match = re.search(r"<([^>]+)>", raw)
        key = match.group(1).strip() if match else raw.strip()
        return apparatus_slug(key)

    all_rst = sorted(RESOURCES_DIR.glob("*/*.rst")) + sorted(DOCSRC_DIR.rglob("*.rst"))
    for rst_path in all_rst:
        content = rst_path.read_text(encoding="utf-8")
        for m in PERSON_RE.finditer(content):
            slug = extract_slug(m.group(1))
            assert slug in person_slugs, f"Unresolved :person:`{m.group(1)}` in {rst_path}"
        for m in CITE_RE.finditer(content):
            slug = extract_slug(m.group(1))
            assert slug in cite_slugs, f"Unresolved :cite:`{m.group(1)}` in {rst_path}"
        for m in TERM_RE.finditer(content):
            slug = extract_slug(m.group(1))
            assert slug in term_slugs, f"Unresolved :term:`{m.group(1)}` in {rst_path}"


def test_euclid_style_collection_hierarchy_and_xrefs() -> None:
    """Verify multi-level Book -> Chapters -> Sections -> Items -> Loci hierarchy, hero SVGs, clean titles, and 100% :ref: resolution."""
    summary = compile_edition(REPO_ROOT)
    assert summary["units_compiled"] == 13
    assert summary["sections_compiled"] == 55
    assert summary["items_compiled"] == 94
    assert summary["transcribed_folios"] == 65
    assert summary["verified_folios"] == 65
    assert summary["svgs_compiled"] == 32
    assert summary["svgs_copied"] == 49
    assert summary["graphics_copied"] == 98

    # Zero legacy monolithic *-en.rst or *-commentary.rst files anywhere in docsrc/college_geometry/
    assert list(DOCSRC_DIR.rglob("*-en.rst")) == []
    assert list(DOCSRC_DIR.rglob("*-commentary.rst")) == []

    # Verify zero bare `[A-Z]. ` section/item titles that trigger Docutils (INFO/1) Enumerated list warnings
    bare_letter_title_re = re.compile(r"^:title:\s+[A-Z](?:\.[a-z])?\.\s+", flags=re.MULTILINE)
    for rst_path in sorted(DOCSRC_DIR.rglob("*.rst")):
        rst_txt = rst_path.read_text(encoding="utf-8")
        assert not bare_letter_title_re.search(rst_txt), f"Bare lettered title in {rst_path}"
        assert "Folio Allocation in This Section" not in rst_txt, f"Stub table left in {rst_path}"

    # Verify every Chapter landing page carries hero.svg + .. picture:: hero.svg
    smap = load_structure_map(RESOURCES_DIR)
    for ch in smap["chapters"]:
        ch_dir = DOCSRC_DIR / ch["slug"]
        assert (ch_dir / "hero.svg").is_file(), f"Missing chapter hero.svg in {ch_dir}"
        ch_idx = (ch_dir / "index.rst").read_text(encoding="utf-8")
        assert ".. picture:: hero.svg" in ch_idx

    # Book root collection + apparatus
    root_index = (DOCSRC_DIR / "index.rst").read_text(encoding="utf-8")
    assert ".. collection::" in root_index
    assert ":type: chapter" in root_index
    for apparatus_file in ("bibliography.rst", "persons.rst", "glossary.rst", "scan-inventory.rst"):
        assert (DOCSRC_DIR / apparatus_file).is_file()

    # Frontmatter chapter + 6 leaf items
    fm_dir = DOCSRC_DIR / "frontmatter"
    assert ":type: item" in (fm_dir / "index.rst").read_text(encoding="utf-8")
    assert (fm_dir / "commentary.rst").is_file()
    for fm_slug in (
        "01-cover",
        "02-title-and-dedication",
        "03-preface",
        "04-contents",
        "05-to-the-instructor",
        "06-to-the-student",
    ):
        assert (fm_dir / fm_slug / "index.rst").is_file()
        assert (fm_dir / fm_slug / "commentary.rst").is_file()

    # Chapter I sections, § 11 Locus sub-collection, §§ 15-22, and Review Exercises 1-67
    ch01_dir = DOCSRC_DIR / "ch01-geometric-constructions"
    assert [p.name for p in ch01_dir.glob("*.svg")] == ["hero.svg"]
    assert list(ch01_dir.glob("*.png")) == []
    assert ":type: section" in (ch01_dir / "index.rst").read_text(encoding="utf-8")
    assert (ch01_dir / "commentary.rst").is_file()

    for sec_slug in (
        "a-preliminaries",
        "b-general-method",
        "c-geometric-loci",
        "d-indirect-elements",
        "review-exercises",
    ):
        assert (ch01_dir / sec_slug / "hero.svg").is_file()
        sec_idx = (ch01_dir / sec_slug / "index.rst").read_text(encoding="utf-8")
        assert ".. picture:: hero.svg" in sec_idx
        assert ".. collection::" in sec_idx
        assert ":type: item" in sec_idx

    loci_dir = ch01_dir / "c-geometric-loci" / "011-important-loci"
    assert ":type: locus" in (loci_dir / "index.rst").read_text(encoding="utf-8")
    for n in range(1, 13):
        assert (loci_dir / f"locus-{n:02d}" / "index.rst").is_file()
        assert (loci_dir / f"locus-{n:02d}" / "commentary.rst").is_file()

    # Verify Chapter III transcribed sections (Preliminaries, Circumcircle incl. Problem of Pappus § 84, Medians)
    ch03_dir = DOCSRC_DIR / "ch03-properties-of-the-triangle"
    for ch03_sec in ("a-preliminaries", "b-the-circumcircle", "c-medians"):
        assert (ch03_dir / ch03_sec / "hero.svg").is_file()
        s_idx = (ch03_dir / ch03_sec / "index.rst").read_text(encoding="utf-8")
        assert ".. picture:: hero.svg" in s_idx
        assert ":type: item" in s_idx
    pappus_item = ch03_dir / "b-the-circumcircle" / "084-the-problem-of-pappus" / "index.rst"
    assert pappus_item.is_file()
    assert "0082.g1.svg" in pappus_item.read_text(encoding="utf-8")

    # Verify complete § 15 (no editorial continuation truncation) and Review Exercises 1-67
    art15_text = (ch01_dir / "d-indirect-elements" / "015-problem" / "index.rst").read_text(encoding="utf-8")
    assert ".. folio:: 0040" in art15_text
    assert ".. folio:: 0041" in art15_text
    assert "Editorial Continuation" not in art15_text
    assert "mediators <mediator>" in art15_text

    loci_rev_text = (ch01_dir / "review-exercises" / "03-loci" / "index.rst").read_text(encoding="utf-8")
    assert "67." in loci_rev_text
    assert ".. folio:: 0052" in loci_rev_text

    # Verify 100% of :ref: targets across docsrc/ resolve to a unique defined .. _label:
    defined_labels: dict[str, Path] = {}
    docsrc_rst_files = [
        p for p in sorted(DOCSRC_ROOT.rglob("*.rst")) if "modules/api/" not in p.as_posix()
    ]
    for rst_path in docsrc_rst_files:
        txt = rst_path.read_text(encoding="utf-8")
        for m in ANCHOR_DEF_RE.finditer(txt):
            lbl = m.group(1).lower()
            assert lbl not in defined_labels, (
                f"Duplicate anchor `{lbl}` in {rst_path} and {defined_labels[lbl]}"
            )
            defined_labels[lbl] = rst_path

    for rst_path in docsrc_rst_files:
        txt = rst_path.read_text(encoding="utf-8")
        for m in REF_ROLE_RE.finditer(txt):
            raw = m.group(1)
            tm = re.search(r"<([^>]+)>", raw)
            target = (tm.group(1) if tm else raw).strip().lower()
            assert target in defined_labels, f"Broken :ref:`{raw}` in {rst_path}"
