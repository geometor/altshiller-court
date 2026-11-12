"""Folio depagination and item-per-page decomposition for *College Geometry*.

Transforms atomic diplomatic folio files (``<NNNN>.rst`` and ``<NNNN>.notes.rst``)
into structured chapter sections, leaf items, and sub-collections (such as the
twelve fundamental loci of ``§ 11``) with co-located ``.euclid-graphic`` SVGs and
paired ``commentary.rst`` companion tracks.
"""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

HEADING_CHARS = {"=", "-", "~", "^", '"', "+"}

ARTICLE_INLINE_RE = re.compile(r"^\*\*(\d+)\.\s+([^*]+?)\.\*\*\s*(.*)$", flags=re.DOTALL)
PROBLEM_ENUN_RE = re.compile(r"^(\s*)\*\*(\d+)\.\s+Problem\.\*\*\s+", flags=re.MULTILINE)
LOCUS_ENUN_RE = re.compile(r"^(\s*)LOCUS\s+(\d+)\.\s+", flags=re.MULTILINE)
PICTURE_RE = re.compile(r"^\.\.\s+picture::\s+(\S+)", flags=re.MULTILINE)
GEOM_GID_RE = re.compile(r"(\d{4}\.g\d+):")
ENUM_ITEM_RE = re.compile(r"^(\d+)\.\s+", flags=re.MULTILINE)


@dataclass
class FolioBlock:
    """A single top-level RST block carrying its source folio provenance."""

    text: str
    folios: list[tuple[str, str]] = field(default_factory=list)

    @property
    def primary_folio(self) -> tuple[str, str]:
        """Return ``(folio_id, page_str)`` where this block begins."""
        return self.folios[0]


@dataclass
class CodexItem:
    """A single compiled leaf page (or ``§ 11`` locus sub-collection) with commentary."""

    slug: str
    title: str
    anchor: str
    item_type: str  # "item" or "locus"
    order: int
    canonical_id: str
    blocks: list[FolioBlock] = field(default_factory=list)
    children: list[CodexItem] = field(default_factory=list)
    child_collection_type: str | None = None
    excerpt: str | None = None

    def all_folios(self) -> list[tuple[str, str]]:
        """Ordered unique ``(folio_id, page_str)`` pairs spanned by this item and its children."""
        seen: set[str] = set()
        result: list[tuple[str, str]] = []
        for blk in self.blocks:
            for fid, pstr in blk.folios:
                if fid not in seen:
                    seen.add(fid)
                    result.append((fid, pstr))
        for child in self.children:
            for fid, pstr in child.all_folios():
                if fid not in seen:
                    seen.add(fid)
                    result.append((fid, pstr))
        return result


@dataclass
class CodexSection:
    """A chapter section container holding intro blocks and ordered ``CodexItem`` children."""

    slug: str
    code: str
    title: str
    anchor: str
    canonical_id: str
    order: int
    overview: str
    intro_blocks: list[FolioBlock] = field(default_factory=list)
    items: list[CodexItem] = field(default_factory=list)


def parse_folio_rst(rst_path: Path) -> tuple[dict[str, str], str]:
    """Parse ``:key: value`` metadata header and RST body from a ``<NNNN>.rst`` file."""
    lines = rst_path.read_text(encoding="utf-8").splitlines()
    meta: dict[str, str] = {}
    idx = 0
    while idx < len(lines) and lines[idx].strip():
        m = re.match(r"^:([^:]+):\s*(.*)$", lines[idx])
        if m:
            meta[m.group(1).strip()] = m.group(2).strip()
        idx += 1
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    body = "\n".join(lines[idx:]).strip()
    return meta, body


def demote_headings(text: str, map_chars: dict[str, str]) -> str:
    """Rewrite RST underline characters according to ``map_chars``."""
    out_lines = text.splitlines()
    for i in range(1, len(out_lines)):
        prev = out_lines[i - 1].strip()
        cur = out_lines[i].strip()
        if prev and len(cur) >= len(prev) and len(set(cur)) == 1:
            ch = cur[0]
            if ch in map_chars:
                out_lines[i] = map_chars[ch] * len(prev)
    return "\n".join(out_lines)


def strip_top_heading(body: str, underline_char: str = "=") -> str:
    """Remove top RST heading underlined with ``underline_char`` if present."""
    lines = body.splitlines()
    if (
        len(lines) >= 2
        and lines[0].strip()
        and set(lines[1].strip()) == {underline_char}
        and len(lines[1].strip()) >= len(lines[0].strip())
    ):
        rest = lines[2:]
        while rest and not rest[0].strip():
            rest.pop(0)
        return "\n".join(rest)
    return body


def heading_info(block_text: str) -> tuple[str, str] | None:
    """If ``block_text`` is a 2-line RST heading, return ``(title, underline_char)``."""
    lines = block_text.strip().splitlines()
    if len(lines) == 2:
        title = lines[0].strip()
        under = lines[1].strip()
        if title and len(under) >= len(title) and len(set(under)) == 1 and under[0] in HEADING_CHARS:
            return title, under[0]
    return None


def _ends_mid_sentence(block: str) -> bool:
    """Return True if a plain paragraph block ends without sentence-closing punctuation."""
    stripped = block.strip()
    if not stripped or stripped.startswith(("..", "|")):
        return False
    if heading_info(stripped) is not None:
        return False
    last_char = stripped[-1]
    return last_char not in {".", ":", ";", "?", "!", "”", '"', ")", "*"}


def _is_plain_continuation_paragraph(block: str) -> bool:
    """Return True if ``block`` can continue an incomplete sentence across a figure or page turn."""
    stripped = block.strip()
    if not stripped or stripped.startswith(("..", "|")):
        return False
    if heading_info(stripped) is not None:
        return False
    return not re.match(
        r"^(?:\d+\.\s+|\*\*\d+\.|LOCUS\s+\d+|ANALYSIS\.|CONSTRUCTION\.|PROOF\.|DISCUSSION\.|CONVERSELY\.|\*Note\.\*)",
        stripped,
    )


def extract_depaginated_blocks(
    folio_entries: list[tuple[str, str, dict[str, str], str]],
    strip_chapter_heading: bool = False,
    demote_frontmatter: bool = False,
) -> list[FolioBlock]:
    """Convert consecutive folios into ``FolioBlock`` items, reflowing mid-sentence splits."""
    stream: list[FolioBlock] = []

    for idx, (folio_id, page_str, meta, raw_body) in enumerate(folio_entries):
        if meta.get("status", "ok") == "blank":
            continue
        body = raw_body
        if demote_frontmatter:
            body = demote_headings(body, {"=": "-", "-": "~"})
        elif strip_chapter_heading and idx == 0:
            body = strip_top_heading(body, "=")

        raw_blocks = [b.rstrip() for b in re.split(r"\n\s*\n(?=\S)", body.strip()) if b.strip()]
        for b_text in raw_blocks:
            stream.append(FolioBlock(text=b_text, folios=[(folio_id, page_str)]))

    # Reflow sentences split across floated .. picture:: blocks and/or folio turns
    i = 0
    while i < len(stream):
        if _ends_mid_sentence(stream[i].text):
            j = i + 1
            while j < len(stream) and stream[j].text.lstrip().startswith(".. picture::"):
                j += 1
            if j < len(stream) and _is_plain_continuation_paragraph(stream[j].text):
                stream[i].text = stream[i].text + " " + stream[j].text.lstrip()
                for fpair in stream[j].folios:
                    if fpair not in stream[i].folios:
                        stream[i].folios.append(fpair)
                stream.pop(j)
                continue
        i += 1

    return stream


def render_blocks_with_folios(blocks: list[FolioBlock]) -> str:
    """Render ``FolioBlock`` list to RST, emitting ``.. folio::`` milestones at folio transitions."""
    out: list[str] = []
    seen_folios: set[str] = set()
    active_folio: str | None = None

    for blk in blocks:
        start_fid, start_page = blk.primary_folio
        if start_fid != active_folio and start_fid not in seen_folios:
            out.append(f".. folio:: {start_fid}\n   :page: {start_page}")
            seen_folios.add(start_fid)
            active_folio = start_fid

        out.append(blk.text)

        for extra_fid, extra_page in blk.folios[1:]:
            if extra_fid not in seen_folios:
                out.append(f".. folio:: {extra_fid}\n   :page: {extra_page}")
                seen_folios.add(extra_fid)
                active_folio = extra_fid

    return "\n\n".join(out)


CH01_SECTION_META: dict[str, tuple[str, str, str, str]] = {
    "A. PRELIMINARIES": (
        "a-preliminaries",
        "A",
        "A. Preliminaries",
        (
            "Notation conventions for polygons, circles, triangle cevians, and circum-/inradii (§ 1), "
            "ten foundational Euclidean ruler-and-compass constructions (§ 2) with 24 elementary "
            "construction exercises, and verbal restatement discipline (§ 3)."
        ),
    ),
    "B. GENERAL METHOD OF SOLUTION OF CONSTRUCTION PROBLEMS": (
        "b-general-method",
        "B",
        "B. General Method of Solution of Construction Problems",
        (
            "Pappus's four-stage analytic method—Analysis, Construction, Proof, and Discussion (§ 4)—"
            "illustrated through five worked construction problems (§§ 5–9, Figs. 1–7), practical "
            "drafting and discussion guidelines (§ 10), and 14 exercises."
        ),
    ),
    "C. GEOMETRIC LOCI": (
        "c-geometric-loci",
        "C",
        "C. Geometric Loci",
        (
            "The method of intersecting geometric loci (§ 11), twelve fundamental linear and circular "
            "loci including the capable arc and Apollonian circle (Loci 1–12, Figs. 8–12), worked locus "
            "constructions (§§ 12–14, Figs. 13–16), and 27 locus and construction exercises."
        ),
    ),
    "D. INDIRECT ELEMENTS": (
        "d-indirect-elements",
        "D",
        "D. Indirect Elements",
        (
            "Auxiliary-triangle constructions introducing indirect metric and angular data—perimeter "
            "2p, side sums and differences b ± c, altitude sums and differences h_b ± h_c, and two-element "
            "data (§§ 15–22, Figs. 17–22)—with 46 graded and supplementary exercises."
        ),
    ),
    "REVIEW EXERCISES": (
        "review-exercises",
        "Review",
        "Review Exercises",
        (
            "Sixty-seven synthesis problems spanning Chapter I: Constructions (1–27), deductive "
            "Propositions (28–58), and Geometric Loci (59–67) across Folios 0048–0052 (pp. 29–33)."
        ),
    ),
}


def _exercise_range_suffix(blocks: list[FolioBlock]) -> str:
    nums: list[int] = []
    for blk in blocks:
        for m in ENUM_ITEM_RE.finditer(blk.text):
            nums.append(int(m.group(1)))
    if nums:
        return f" ({nums[0]}–{nums[-1]})"
    return ""


def _relocate_floated_pictures(sections: list[CodexSection]) -> None:
    """Ensure every ``.. picture:: <gid>.svg`` sits inside the leaf item whose ``:g:`` roles reference ``<gid>``."""
    leaf_items: list[CodexItem] = []
    for sec in sections:
        for item in sec.items:
            if item.children:
                leaf_items.extend(item.children)
            else:
                leaf_items.append(item)

    # Map gid -> owning leaf item via :g: / :eq: references
    gid_owner: dict[str, CodexItem] = {}
    for leaf in leaf_items:
        for blk in leaf.blocks:
            if blk.text.lstrip().startswith(".. picture::"):
                continue
            for m in GEOM_GID_RE.finditer(blk.text):
                gid_owner[m.group(1)] = leaf

    # Detach misplaced picture blocks from non-owning containers (including section intro or § 11 intro)
    detached: list[tuple[CodexItem, FolioBlock]] = []
    all_containers: list[tuple[CodexItem | None, list[FolioBlock]]] = []
    for sec in sections:
        all_containers.append((None, sec.intro_blocks))
        for item in sec.items:
            all_containers.append((item, item.blocks))
            for child in item.children:
                all_containers.append((child, child.blocks))

    for holder, blk_list in all_containers:
        kept: list[FolioBlock] = []
        for blk in blk_list:
            pm = PICTURE_RE.match(blk.text.strip())
            if pm:
                pic_file = pm.group(1)
                gid = pic_file.removesuffix(".svg")
                owner = gid_owner.get(gid)
                if owner is not None and owner is not holder:
                    detached.append((owner, blk))
                    continue
            kept.append(blk)
        blk_list[:] = kept

    # Insert each detached picture block right after .. enunciation:: (or at top) in its true owner
    for owner, pic_blk in detached:
        insert_idx = 0
        if owner.blocks and owner.blocks[0].text.lstrip().startswith(".. enunciation::"):
            insert_idx = 1
        owner.blocks.insert(insert_idx, pic_blk)


def decompose_chapter_one(
    folio_entries: list[tuple[str, str, dict[str, str], str]],
) -> list[CodexSection]:
    """Decompose Chapter I (``0020``–``0052``) into 5 ``CodexSection`` containers and leaf items."""
    blocks = extract_depaginated_blocks(folio_entries, strip_chapter_heading=True)

    raw_sections: list[tuple[str, list[FolioBlock]]] = []
    for blk in blocks:
        h = heading_info(blk.text)
        if h is not None and h[1] == "-" and h[0] in CH01_SECTION_META:
            raw_sections.append((h[0], []))
        else:
            if not raw_sections:
                continue
            raw_sections[-1][1].append(blk)

    sections: list[CodexSection] = []
    for sec_order, (sec_heading, sec_blocks) in enumerate(raw_sections, start=1):
        sec_slug, sec_code, sec_title, sec_overview = CH01_SECTION_META[sec_heading]
        section = CodexSection(
            slug=sec_slug,
            code=sec_code,
            title=sec_title,
            anchor=f"ch01-{sec_slug}",
            canonical_id=f"Ch.I.{sec_code}",
            order=sec_order,
            overview=sec_overview,
        )

        last_art_num: int | None = None
        current_item: CodexItem | None = None

        for blk in sec_blocks:
            text = blk.text.strip()
            h = heading_info(text)

            # 1. Subheading item (~ underline): EXERCISES, SUPPLEMENTARY EXERCISES, CONSTRUCTIONS, etc.
            if h is not None and h[1] == "~":
                sub_title = h[0].strip()
                item_order = len(section.items) + 1
                if sec_slug == "review-exercises":
                    rev_map = {
                        "CONSTRUCTIONS": ("01-constructions", "Constructions", "ch01-review-constructions"),
                        "PROPOSITIONS": ("02-propositions", "Propositions", "ch01-review-propositions"),
                        "LOCI": ("03-loci", "Loci", "ch01-review-loci"),
                    }
                    islug, ititle, ianchor = rev_map[sub_title]
                    cid = f"Ch.I.Review.{item_order}"
                elif sub_title == "SUPPLEMENTARY EXERCISES":
                    islug = "022-supplementary-exercises"
                    ititle = "Supplementary Exercises"
                    ianchor = "ch01-supplementary-exercises"
                    cid = "Ch.I.SuppEx"
                else:
                    art_prefix = f"{last_art_num:03d}" if last_art_num else f"{item_order:03d}"
                    islug = f"{art_prefix}-exercises"
                    ititle = f"§ {last_art_num}. Exercises" if last_art_num else "Exercises"
                    ianchor = f"ch01-art-{art_prefix}-exercises"
                    cid = f"Ch.I.{last_art_num}.Ex" if last_art_num else f"Ch.I.{sec_code}.Ex"

                current_item = CodexItem(
                    slug=islug,
                    title=ititle,
                    anchor=ianchor,
                    item_type="item",
                    order=item_order,
                    canonical_id=cid,
                )
                section.items.append(current_item)
                continue

            # 2. Numbered Problem .. enunciation::
            prob_m = PROBLEM_ENUN_RE.search(text) if text.startswith(".. enunciation::") else None
            if prob_m:
                art_num = int(prob_m.group(2))
                last_art_num = art_num
                cleaned = PROBLEM_ENUN_RE.sub(r"\1", text, count=1)
                current_item = CodexItem(
                    slug=f"{art_num:03d}-problem",
                    title=f"§ {art_num}. Problem",
                    anchor=f"ch01-art-{art_num:03d}",
                    item_type="item",
                    order=len(section.items) + 1,
                    canonical_id=f"Ch.I.{art_num}",
                    blocks=[FolioBlock(text=cleaned, folios=list(blk.folios))],
                )
                section.items.append(current_item)
                continue

            # 3. Inline bold numbered article (**1. Notation.**, **4. Analytic Method.**, **11. Important Loci.**, etc.)
            art_m = ARTICLE_INLINE_RE.match(text)
            if art_m:
                art_num = int(art_m.group(1))
                art_label = art_m.group(2).strip()
                remainder = art_m.group(3).strip()
                last_art_num = art_num
                label_slug = re.sub(r"[^a-z0-9]+", "-", art_label.lower()).strip("-")
                current_item = CodexItem(
                    slug=f"{art_num:03d}-{label_slug}",
                    title=f"§ {art_num}. {art_label}",
                    anchor=f"ch01-art-{art_num:03d}",
                    item_type="item",
                    order=len(section.items) + 1,
                    canonical_id=f"Ch.I.{art_num}",
                )
                if remainder:
                    current_item.blocks.append(FolioBlock(text=remainder, folios=list(blk.folios)))
                section.items.append(current_item)
                continue

            # 4. Regular block -> append to current_item or section.intro_blocks
            if current_item is None:
                section.intro_blocks.append(blk)
            else:
                current_item.blocks.append(blk)

        # Finalize exercise range titles & § 11 Locus sub-collection
        for item in section.items:
            if "Exercises" in item.title or section.slug == "review-exercises":
                item.title = item.title + _exercise_range_suffix(item.blocks)
            if item.slug == "011-important-loci":
                _split_important_loci(item)

        sections.append(section)

    _relocate_floated_pictures(sections)
    return sections


def _split_important_loci(item: CodexItem) -> None:
    """Split ``§ 11. Important Loci`` into intro blocks + 12 ``locus-XX`` child items."""
    intro: list[FolioBlock] = []
    current_locus: CodexItem | None = None

    for blk in item.blocks:
        text = blk.text.strip()
        loc_m = LOCUS_ENUN_RE.search(text) if text.startswith(".. enunciation::") else None
        if loc_m:
            loc_num = int(loc_m.group(2))
            cleaned = LOCUS_ENUN_RE.sub(r"\1", text, count=1)
            current_locus = CodexItem(
                slug=f"locus-{loc_num:02d}",
                title=f"Locus {loc_num}",
                anchor=f"ch01-locus-{loc_num:02d}",
                item_type="locus",
                order=loc_num,
                canonical_id=f"Ch.I.11.L{loc_num}",
                blocks=[FolioBlock(text=cleaned, folios=list(blk.folios))],
            )
            item.children.append(current_locus)
        elif current_locus is None:
            intro.append(blk)
        else:
            current_locus.blocks.append(blk)

    item.blocks = intro
    item.child_collection_type = "locus"


FRONTMATTER_UNITS: list[tuple[str, str, str, str, str, str]] = [
    (
        "01-cover",
        "Dover Front Cover",
        "0001",
        "0001",
        "Frontmatter.Cover",
        "Unabridged 2007 Dover republication front cover of Nathan Altshiller-Court's College Geometry.",
    ),
    (
        "02-title-and-dedication",
        "Title, Copyright, and Dedication",
        "0002",
        "0005",
        "Frontmatter.Title",
        "Title page of the Second Edition, Revised and Enlarged (1952 / Dover 2007), bibliographical history, cataloging record, and dedication.",
    ),
    (
        "03-preface",
        "Preface and Acknowledgments",
        "0006",
        "0009",
        "Frontmatter.Preface",
        "Altshiller-Court's 1952 Preface charting the rise of college geometry in American universities and Acknowledgments to J. H. Butchart, L. Wayne Johnson, and Arthur Bernhart.",
    ),
    (
        "04-contents",
        "Table of Contents",
        "0010",
        "0013",
        "Frontmatter.Contents",
        "Analytical Table of Contents spanning Chapters I–X, Historical and Bibliographical Notes, List of Names, and Index (pp. xi–xiv).",
    ),
    (
        "05-to-the-instructor",
        "To the Instructor",
        "0014",
        "0015",
        "Frontmatter.Instructor",
        "Semester course-planning guidance, suggested article selections across Chapters II–X, and pedagogical stratification of exercise sets.",
    ),
    (
        "06-to-the-student",
        "To the Student",
        "0016",
        "0019",
        "Frontmatter.Student",
        "Altshiller-Court's study methodology on active memory, marginal cross-referencing to high-school Euclidean geometry, figure sketching, and problem solving.",
    ),
]


def decompose_frontmatter(
    folio_entries: list[tuple[str, str, dict[str, str], str]],
) -> list[CodexItem]:
    """Decompose Frontmatter (``0001``–``0019``) into 6 leaf ``CodexItem`` units."""
    by_fid = {fid: (fid, pstr, meta, body) for fid, pstr, meta, body in folio_entries}
    items: list[CodexItem] = []

    for order, (slug, title, f_start, f_end, cid, excerpt) in enumerate(FRONTMATTER_UNITS, start=1):
        sub_entries = [
            by_fid[f"{n:04d}"]
            for n in range(int(f_start), int(f_end) + 1)
            if f"{n:04d}" in by_fid
        ]
        # Strip redundant top === heading when single-section frontmatter unit already carries it as page H1
        cleaned_entries: list[tuple[str, str, dict[str, str], str]] = []
        for idx, (fid, pstr, meta, raw_body) in enumerate(sub_entries):
            b = raw_body
            if idx == 0 and slug in {"02-title-and-dedication", "03-preface", "04-contents", "05-to-the-instructor", "06-to-the-student"}:
                b = strip_top_heading(b, "=")
            b = demote_headings(b, {"=": "-", "-": "~"})
            cleaned_entries.append((fid, pstr, meta, b))

        blocks = extract_depaginated_blocks(cleaned_entries, demote_frontmatter=False)
        items.append(
            CodexItem(
                slug=slug,
                title=title,
                anchor=f"frontmatter-{slug}",
                item_type="item",
                order=order,
                canonical_id=cid,
                blocks=blocks,
                excerpt=excerpt,
            )
        )

    return items


def copy_referenced_graphics(
    blocks: list[FolioBlock],
    source_chap_dir: Path,
    dest_item_dir: Path,
) -> tuple[int, int]:
    """Copy ONLY the ``.g*.svg`` and ``.g*.png`` files referenced by ``.. picture::`` in ``blocks``."""
    copied_svgs = 0
    copied_pngs = 0
    seen_stems: set[str] = set()

    for blk in blocks:
        for pm in PICTURE_RE.finditer(blk.text):
            pic_name = pm.group(1).strip()
            stem = pic_name[:-4] if pic_name.endswith((".svg", ".png")) else pic_name
            if stem in seen_stems:
                continue
            seen_stems.add(stem)

            svg_src = source_chap_dir / f"{stem}.svg"
            if svg_src.is_file():
                shutil.copy2(svg_src, dest_item_dir / svg_src.name)
                copied_svgs += 1

            for suffix in (".png", ".inverted.png"):
                png_src = source_chap_dir / f"{stem}{suffix}"
                if png_src.is_file():
                    shutil.copy2(png_src, dest_item_dir / png_src.name)
                    copied_pngs += 1

    return copied_svgs, copied_pngs
