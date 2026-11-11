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
DOCSRC_DIR = REPO_ROOT / "docsrc" / "college_geometry"

PERSON_RE = re.compile(r":person:`([^`]+)`")
CITE_RE = re.compile(r":cite:`([^`]+)`")
TERM_RE = re.compile(r":term:`([^`]+)`")


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
    assert chapters[-1]["dir"] == "12_index"

    # Unbroken pagination law: PDF Folio = Printed Page + 19 for body & backmatter
    by_folio = {entry["folio"]: entry for entry in folios}
    assert by_folio["0020"]["printed_page"] == "1"
    assert by_folio["0040"]["printed_page"] == "21"
    assert by_folio["0312"]["printed_page"] == "293"
    assert by_folio["0314"]["printed_page"] == "295"
    assert by_folio["0332"]["printed_page"] == "313"

    # Blank versos
    for blank_folio in ("0005", "0009", "0015", "0019", "0313", "0333"):
        assert by_folio[blank_folio]["is_blank"] is True


def test_edition_status_and_assets() -> None:
    """Verify extracted 300 DPI scans, gold-standard transcriptions, crops, and reviews."""
    status = get_edition_status(REPO_ROOT)
    assert status["total_folios"] == 334
    assert status["scans_present"] == 334
    assert status["rst_transcribed"] >= 40
    assert status["notes_present"] >= 40
    assert status["folios_with_graphics"] >= 15
    assert status["diagram_crops"] >= 17
    assert status["verified_reviews"] >= 40


def test_apparatus_registries_and_role_resolution() -> None:
    """Ensure every :person:, :cite:, and :term: role in folio RST resolves cleanly."""
    persons = json.loads((RESOURCES_DIR / "persons.json").read_text(encoding="utf-8"))
    citations = json.loads((RESOURCES_DIR / "citations.json").read_text(encoding="utf-8"))
    glossary = json.loads((RESOURCES_DIR / "glossary.json").read_text(encoding="utf-8"))
    reviews = json.loads((RESOURCES_DIR / "folio_reviews.json").read_text(encoding="utf-8"))

    assert len(persons) >= 67
    assert len(citations) >= 31
    assert len(glossary) >= 55
    assert len(reviews) >= 40

    person_slugs = {apparatus_slug(k) for k in persons}
    cite_slugs = {apparatus_slug(k) for k in citations}
    term_slugs = {apparatus_slug(k) for k in glossary}

    def extract_slug(raw: str) -> str:
        match = re.search(r"<([^>]+)>", raw)
        key = match.group(1).strip() if match else raw.strip()
        return apparatus_slug(key)

    for rst_path in sorted(RESOURCES_DIR.glob("*/*.rst")):
        content = rst_path.read_text(encoding="utf-8")
        for m in PERSON_RE.finditer(content):
            slug = extract_slug(m.group(1))
            assert slug in person_slugs, f"Unresolved :person:`{m.group(1)}` in {rst_path.name}"
        for m in CITE_RE.finditer(content):
            slug = extract_slug(m.group(1))
            assert slug in cite_slugs, f"Unresolved :cite:`{m.group(1)}` in {rst_path.name}"
        for m in TERM_RE.finditer(content):
            slug = extract_slug(m.group(1))
            assert slug in term_slugs, f"Unresolved :term:`{m.group(1)}` in {rst_path.name}"


def test_compile_edition_codex_units() -> None:
    """Verify 2-Track Book Codex compilation produces all 13 units and apparatus pages."""
    summary = compile_edition(REPO_ROOT)
    assert summary["units_compiled"] == 13
    assert summary["apparatus"]["citations"] >= 31
    assert summary["apparatus"]["persons"] >= 67
    assert summary["apparatus"]["glossary"] >= 55

    for apparatus_file in (
        "index.rst",
        "bibliography.rst",
        "persons.rst",
        "glossary.rst",
        "scan-inventory.rst",
    ):
        assert (DOCSRC_DIR / apparatus_file).exists()

    ch01_en = DOCSRC_DIR / "ch01-geometric-constructions" / "ch01-geometric-constructions-en.rst"
    ch01_comm = (
        DOCSRC_DIR / "ch01-geometric-constructions" / "ch01-geometric-constructions-commentary.rst"
    )
    assert ch01_en.exists()
    assert ch01_comm.exists()

    en_text = ch01_en.read_text(encoding="utf-8")
    assert ":layout: book" in en_text
    assert ".. _ch01-geometric-constructions-en:" in en_text
    assert ".. folio:: 0020" in en_text
    assert ".. picture:: 0023.g1.png" in en_text
    assert ".. picture:: 0040.g1.png" in en_text
