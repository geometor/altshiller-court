"""Book Codex compiler and scholarly apparatus builder for College Geometry (1952).

Compiles verified diplomatic folio transcriptions (``resources/college_geometry/<dir>/<NNNN>.rst``
and ``<NNNN>.notes.rst``), diagram crops (``<NNNN>.g<k>.png``), ``structure_map.json``, and
apparatus registries (``persons.json``, ``citations.json``, ``glossary.json``, ``folio_reviews.json``)
into a synchronized 2-Track Book Codex (``English`` | ``Commentary``) under ``docsrc/college_geometry/``.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any


def apparatus_slug(key: str) -> str:
    """Deterministic anchor slug matching ``photon_platform.publish.roles.geometry._apparatus_slug``."""
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


CHAPTER_COMMENTARY: dict[str, str] = {
    "ch02-similitude-and-homothecy": """\
Mathematical Architecture & Transformation Theory
-------------------------------------------------

Chapter II introduces the first great transformational pillar of *College Geometry*: **similitude** (§§ 23–30) and :term:`homothecy <homothecy>` (§§ 31–53). Where Chapter I constructs a figure directly at its final position and scale, the :term:`method of similitude <similitude>` temporarily sets aside one linear metric condition, constructs a convenient prototype of the required shape (*species*), and scales it into place from a well-chosen center of homothecy.

* **Homothetic Centers of Two Circles (§§ 39–45)**: Any two unequal circles :math:`(O, R)` and :math:`(O', R')` admit two :term:`centers of similitude <centers-of-similitude>`—external (direct, ratio :math:`+R/R'`) and internal (inverse, ratio :math:`-R/R'`)—which divide the line of centers :math:`OO'` harmonically.
* **Circle of Similitude & Pantograph (§§ 46–53)**: The locus of points from which two given unequal circles subtend equal angles is the :term:`Apollonian circle <apollonian-circle>` having their two centers of similitude as diameter (the *circle of similitude*), coaxal with the two given circles.

GEOMETOR Ecosystem Connections
------------------------------

* **Triangle Centers (`geometor/etc`)**: Applied to the :term:`circumcircle <circumcircle>` and :term:`incircle <incircle>` of :math:`\\triangle ABC`, the internal and external centers of similitude are Kimberling centers :math:`X(55)` (*insimilicenter*) and :math:`X(56)` (*exsimilicenter*), studied by :person:`Euler <euler>`, :person:`Monge <monge>`, and :person:`Poncelet <poncelet>`.
* **Medial & Anticomplementary Homothecy**: At the :term:`centroid <centroid>` :math:`G = X(2)`, the homothecy :math:`\\mathcal{H}(G, -\\tfrac{1}{2})` maps :math:`\\triangle ABC` onto its :term:`complementary (medial) triangle <complementary-triangle>`, driving the synthetic proofs of the :term:`Euler line <euler-line>` and :term:`nine-point circle <nine-point-circle>` in Chapter III.
""",
    "ch03-properties-of-the-triangle": """\
Mathematical Architecture & Classical Triangle Canon
----------------------------------------------------

Spanning 186 articles (§§ 54–239, pp. 53–123), Chapter III is the monumental heart of the first half of *College Geometry*:

1. **Harmonic Preliminaries (§§ 54–67)**: Early introduction of :term:`harmonic division <harmonic-division>` and the :term:`Apollonian circle <apollonian-circle>`, honoring the pedagogical innovation announced in the 1952 :ref:`Preface <frontmatter-en>`.
2. **Circumcircle & Medians (§§ 68–110)**: Antipodal chords, Simson/Johnson precursors, the Problem of :person:`Pappus <pappus>` (§ 84), Apollonius' median formula, the :term:`centroid <centroid>` :math:`G = X(2)`, and the :term:`complementary <complementary-triangle>` and :term:`anticomplementary <anticomplementary-triangle>` triangles.
3. **Tritangent Circles (§§ 111–174)**: The :term:`incircle <incircle>` and three excircles :math:`(I, I_a, I_b, I_c)`, :person:`Carnot's <carnot>` theorem (§ 146), :person:`Chapple <chapple>`–:person:`Euler <euler>` distance formula :math:`OI^2 = R(R - 2r)` (§ 152, :cite:`Euler 1765 <euler:1765>`), and semiperimeter contact identities (:math:`s - a, s - b, s - c`).
4. **Altitudes, Euler Line & Nine-Point Circle (§§ 175–219)**: Concurrency at the :term:`orthocenter <orthocenter>` :math:`H = X(4)`, minimum-perimeter property of the :term:`orthic triangle <orthic-triangle>` (:person:`Fagnano <fagnano>`, § 194), collinearity of :math:`O, G, N, H` on the :term:`Euler line <euler-line>` (§ 202), the :term:`nine-point circle <nine-point-circle>` (§ 206, :person:`Brianchon <brianchon>` & :person:`Poncelet <poncelet>`), and :term:`Feuerbach's theorem <feuerbach-theorem>` (§ 215, :cite:`Feuerbach 1822 <feuerbach:1822>`).
5. **Orthocentric Group (§§ 220–239)**: Symmetric quadruple :math:`\\{A, B, C, H\\}` (:term:`orthocentric quadrilateral <orthocentric-quadrilateral>`) sharing a common nine-point circle.

GEOMETOR Ecosystem Connections
------------------------------

* **`geometor/etc` & :cite:`Kimberling's ETC <kimberling:etc>`**: Establishes exact synthetic constructions for :math:`X(1)` (*incenter*), :math:`X(2)` (*centroid*), :math:`X(3)` (*circumcenter*), :math:`X(4)` (*orthocenter*), :math:`X(5)` (*nine-point center*), and :math:`X(11)` (*Feuerbach point*).
* **`geometor/model`**: Every center and circle in §§ 54–239 is quadratic constructible over :math:`\\mathbb{Q}(A, B, C)` and verifiable symbolically in SymPy without floating-point drift.
""",
    "ch04-the-quadrilateral": """\
Mathematical Architecture (Added in the 1952 Second Edition)
------------------------------------------------------------

Chapter IV (§§ 240–281, pp. 124–139) was newly written for the 1952 Revised and Enlarged Edition (:cite:`2nd ed., 1952 <court:1952>`), organizing quadrilateral geometry into three progressive strata:

* **General Quadrilateral (§§ 240–250)**: Varignon's parallelogram of side midpoints, bimedians, and :person:`Euler's <euler>` theorem relating the sum of squares of the four sides to the squares of the diagonals plus four times the square of the segment joining the diagonal midpoints (§ 246).
* **Cyclic Quadrilateral (§§ 251–267)**: :person:`Ptolemy's <ptolemy>` first and second theorems (§ 255), the :term:`anticenter <anticenter>` (Mathot point, § 260), and :person:`Brahmagupta's <brahmagupta>` area formula and orthodiagonal median-altitude theorem (§§ 261–266).
* **Circumscriptible & Bicentric Quadrilaterals (§§ 268–281)**: Pitot's theorem (:math:`a + c = b + d`), :person:`Newton's <newton>` line of a circumscribed quadrilateral, and :person:`Fuss <euler>` / bicentric relations.
""",
    "ch05-the-simson-line": """\
Mathematical Architecture
-------------------------

Chapter V (§§ 282–305, pp. 140–150) investigates the pedal projections of a point :math:`P` onto the sidelines of :math:`\\triangle ABC`:

* **Wallace–Simson Theorem (§ 283)**: The pedal feet of :math:`P` are collinear on the :term:`Simson line <simson-line>` if and only if :math:`P` lies on the :term:`circumcircle <circumcircle>` (historically discovered by :person:`William Wallace <wallace>` in 1799, :person:`Simson <simson>` having received traditional attribution).
* **Orthocenter Bisection (§ 299)**: The Simson line of :math:`P` bisects the segment :math:`PH` joining :math:`P` to the :term:`orthocenter <orthocenter>` :math:`H`—at a point lying directly on the :term:`nine-point circle <nine-point-circle>`!
* **Angle & Envelope Properties (§§ 290–305)**: Two circumcircle points :math:`P, P'` have Simson lines intersecting at half the central angle of arc :math:`PP'`; diametrically opposite points have perpendicular Simson lines meeting on the nine-point circle (:person:`Steiner's <steiner>` deltoid envelope).
""",
    "ch06-transversals": """\
Mathematical Architecture & Signed Ratios
-----------------------------------------

Chapter VI (§§ 306–344, pp. 151–165) introduces :term:`directed segments <directed-segments>` (:math:`AB = -BA`, :person:`Chasles <chasles>` / :person:`Möbius <mobius>`) to unify collinearity and concurrency:

* **Introductory & Stewart's Theorem (§§ 306–309)**: :person:`Euler's <euler>` four-point identity :math:`AB \\cdot CD + AC \\cdot DB + AD \\cdot BC = 0` (§ 307) and :person:`Stewart's <stewart>` cevian metric identity (§ 308).
* **Menelaus' Theorem (§§ 310–325)**: Signed transversal product :math:`(AF/FB)(BD/DC)(CE/EA) = -1` (:person:`Menelaus of Alexandria <menelaus>`), applied immediately to collinearity of external angle-bisector traces, :person:`Pascal's <pascal>` mystic hexagram, and centers of similitude of three circles (:person:`Monge <monge>`).
* **Ceva's Theorem (§§ 326–344)**: Dual concurrency criterion :math:`(AF/FB)(BD/DC)(CE/EA) = +1` (:cite:`Ceva 1678 <ceva:1678>`), establishing concurrency of medians, altitudes, bisectors, the :term:`Gergonne point <gergonne-point>` :math:`X(7)` (§ 331, :person:`Gergonne <gergonne>`), the :term:`Nagel point <nagel-point>` :math:`X(8)` (§ 333, :person:`Nagel <nagel>`), :term:`isotomic conjugates <isotomic-conjugates>` (§ 334), and :person:`Desargues' <desargues>` Two-Triangle Theorem (§ 343).
""",
    "ch07-harmonic-division": """\
Mathematical Architecture & Projective Core
-------------------------------------------

Chapter VII (§§ 345–357, pp. 166–171) elevates :term:`harmonic division <harmonic-division>` from a metric ratio on a single segment to a projective invariant of pencils and quadrangles:

* **Metric Characterizations (§§ 345–349)**: Equivalent algebraic forms :math:`\\frac{2}{AB} = \\frac{1}{AC} + \\frac{1}{AD}` and :math:`OB^2 = OC \\cdot OD` (where :math:`O` is the midpoint of :math:`AB`), linking harmonic conjugates directly to :term:`inverse points <inverse-points>` in Chapter VIII.
* **Harmonic Pencils (§§ 350–353)**: Projective invariance of :math:`O(ABCD) = -1` under arbitrary transversal sections (:person:`Pappus <pappus>`, :cite:`Collection VII <pappus:collection:VII>`; :person:`Chasles <chasles>`, :cite:`Traité <chl>`).
* **Complete Quadrangle & Complete Quadrilateral (§§ 354–357)**: Straightedge-only construction of the fourth harmonic point via the diagonal triangle of a :term:`complete quadrilateral <complete-quadrilateral>`, including the :person:`Gauss <gauss>`–:person:`Newton <newton>` midpoint line (§ 353).

GEOMETOR Ecosystem Connections
------------------------------

Directly bridges ``geometor/pappus`` (projective cross-ratio invariance) and ``geometor/divine`` (automated detection of golden sections and harmonic ranges in symbolic constructions).
""",
    "ch08-circles": """\
Mathematical Architecture & Circle Systems
------------------------------------------

Spanning 160 articles (§§ 358–517, pp. 172–229), Chapter VIII builds the complete synthetic theory of systems of one, two, and three circles:

1. **Inverse Points & Orthogonal Circles (§§ 358–372)**: :term:`Inverse points <inverse-points>` (:math:`OP \\cdot OP' = R^2`) and :term:`orthogonal circles <orthogonal-circles>` (:math:`r_1^2 + r_2^2 = d^2`), proving that circles through a pair of inverse points cut the reference circle orthogonally.
2. **Poles & Polars (§§ 373–393)**: :person:`La Hire's <hire>` reciprocity theorem (§ 379), self-polar (conjugate) triangles, and harmonic chord division (:term:`pole and polar <pole-and-polar>`).
3. **Centers of Similitude, Power & Radical Axis (§§ 394–439)**: :person:`Monge's <monge>` theorem on the six centers of similitude of three circles (§ 405), :person:`Steiner's <steiner>` :term:`power of a point <power-of-a-point>` (:math:`d^2 - R^2`), and the :term:`radical axis <radical-axis>` of two circles (generalizing Chapter I, § 11, Locus 12).
4. **Coaxal Pencils & Casey's Theorem (§§ 440–490)**: Intersecting, tangent, and non-intersecting :term:`coaxal circles <coaxal-circles>`, :person:`Poncelet's <poncelet>` limiting points :math:`L, L'`, conjugate orthogonal pencils, and :person:`Casey's <casey>` generalized Ptolemy theorem (§ 471, :cite:`Sequel to Euclid <casey:sequel:1892>`).
5. **Three Circles & The Problem of Apollonius (§§ 491–517)**: Radical center, circles of antisimilitude, the ten classical cases (`PPP` through `CCC`) of the :term:`Problem of Apollonius <problem-of-apollonius>`, and :person:`Gergonne's <gergonne>` celebrated master solution (§ 517) constructing complementary pairs of up to eight tangent circles via poles of axes of similitude and the radical center!
""",
    "ch09-inversion": """\
Mathematical Architecture & Conformal Transformation
----------------------------------------------------

Chapter IX (§§ 518–546, pp. 230–243) develops :term:`circular inversion <inversion>` :math:`(O, k)` (:person:`Steiner <steiner>`, :person:`Kelvin <kelvin>`, :person:`Liouville <mobius>`) as an involutory, angle-preserving transformation of the plane:

* **Images of Lines & Circles (§§ 518–531)**: Lines/circles through the center of inversion :math:`O` invert into straight lines; lines/circles not through :math:`O` invert into circles; angles of intersection are preserved in magnitude and reversed in orientation.
* **Peaucellier's Inversor (§ 524)**: Exact mechanical straight-line linkage converting circular motion into rectilinear motion via inversion.
* **Crowning Applications (§§ 532–546)**: Inversion proofs of :person:`Ptolemy's <ptolemy>` theorem and its converse, Steiner's porism on chains of tangent circles, and the breathtakingly short inversion proof of :term:`Feuerbach's theorem <feuerbach-theorem>` (§ 540, :cite:`Feuerbach 1822 <feuerbach:1822>`) by inverting the nine-point circle, incircle, and an excircle from the midpoint of their common tangent segment!
""",
    "ch10-recent-geometry-of-the-triangle": """\
Mathematical Architecture & Late-19th-Century Triangle Renaissance
------------------------------------------------------------------

Spanning 153 articles (§§ 547–699, pp. 244–294), Chapter X synthesizes the explosion of triangle geometry inaugurated in the 1870s–1880s by :person:`Émile Lemoine <lemoine>`, :person:`Henri Brocard <brocard>`, :person:`Joseph Neuberg <neuberg>`, :person:`Maurice d'Ocagne <docagne>`, and :person:`Robert Tucker <tucker>`:

1. **Trilinear Poles & Polars (§§ 547–557)**: Projective duality with respect to a reference triangle :math:`ABC`, harmonically pairing inscribed Ceva configurations with circumscribed Menelaus transversals (e.g., the Lemoine axis as trilinear polar of the Lemoine point).
2. **Symmedians & Lemoine Geometry (§§ 558–596)**: Reflections of medians across angle bisectors (:person:`d'Ocagne <docagne>`), concurrency at the :term:`Lemoine (symmedian) point <lemoine-point>` :math:`K = X(6)` (:cite:`Lemoine 1873 <lemoine:1873>`, :person:`Grebe <grebe>`), least-squares distance property (:math:`\\sum d_i^2` minimum, § 581), and the first and second (cosine) :term:`Lemoine circles <lemoine-circles>` (§§ 588–596).
3. **Apollonian Circles & Isodynamic Points (§§ 597–624)**: The three triangle :term:`Apollonian circles <apollonian-circle>` sharing a common radical axis (the Brocard axis :math:`OK`) and intersecting in the two :term:`isodynamic points <isodynamic-points>` :math:`W, W' = X(15), X(16)` whose pedal triangles are equilateral (§ 606).
4. **Isogonal Conjugates (§§ 625–648)**: :term:`Isogonal conjugation <isogonal-conjugates>` pairing :math:`(O, H)`, :math:`(G, K)`, and circumcircle points with lines at infinity; Miquel/pedal circle theorem.
5. **Brocard Geometry, Tucker Circles & Orthopole (§§ 649–699)**: Direct and retrograde :term:`Brocard points <brocard-points>` :math:`\\Omega, \\Omega'` with Brocard angle :math:`\\cot\\omega = \\cot A + \\cot B + \\cot C` (:cite:`Brocard 1881 <brocard:1881>`, :person:`Crelle <crelle>`), the seven-point :term:`Brocard circle <brocard-circle>` on diameter :math:`OK`, :term:`Steiner and Tarry points <steiner-and-tarry-points>` :math:`X(99), X(98)`, :person:`Tucker <tucker>` & :person:`Taylor <taylor>` circles (§§ 684–689), and :person:`Neuberg's <neuberg>` :term:`orthopole <orthopole>` (§§ 690–699, :cite:`Gallatly 1913 <gy>`).
""",
    "historical-and-bibliographical-notes": """\
Historiographical Value & Scholarly Cross-Referencing
-----------------------------------------------------

Altshiller-Court's *Historical and Bibliographical Notes* (pp. 295–306) and *List of Names* (pp. 307–309) represent one of the richest compact historiographies of synthetic geometry ever compiled in English:

* **Bibliographic Abbreviations (`pp. 295–296`)**: Keys 8 foundational books (`Chl.`, `Cn.`, `Crt.`, `Ech.`, `Gy.`, `LHr.`, `Pt.`, `Rouché-Comberousse`) and 9 problem-and-research periodicals (`Bull.`, `Edinb.`, `ET.`, `GAM.`, `JME.`, `JMS.`, `Mathesis.`, `Monthly.`, `NA.`, `NC.`)—all encoded as structured entries in :ref:`Bibliography <bibliography>`.
* **Article-by-Article Provenance (`§§ 4–697`)**: Traces individual theorems and constructions from :person:`Euclid <euclid>`, :person:`Archimedes <archimedes>`, :person:`Apollonius <apollonius>`, :person:`Heron <heron>`, :person:`Menelaus <menelaus>`, :person:`Ptolemy <ptolemy>`, and :person:`Pappus <pappus>` through :person:`Ceva <ceva>`, :person:`Euler <euler>`, :person:`Carnot <carnot>`, :person:`Poncelet <poncelet>`, :person:`Gergonne <gergonne>`, :person:`Feuerbach <feuerbach>`, :person:`Steiner <steiner>`, :person:`Chasles <chasles>`, :person:`Lemoine <lemoine>`, :person:`Brocard <brocard>`, and :person:`Neuberg <neuberg>`—all cross-linked in :ref:`Index of Persons <persons>`.
""",
    "back-index": """\
Analytical Subject Index & Digital Apparatus Integration
--------------------------------------------------------

Pages 310–313 (folios ``0329``–``0332``) contain Altshiller-Court's alphabetical *Index* keyed to article numbers (`§§ 1–699`), followed by the blank recto leaf ``0333`` (`[314]`) and the 2007 Dover back cover ``0334``.

In this Digital Scriptorium edition, the printed subject index is complemented by three interactive, machine-linked registries:

* :ref:`Technical Glossary <glossary>` — 55 core definitions, loci, transformations, and Kimberling center mappings (`:term:`).
* :ref:`Biographical Register of Persons <persons>` — 67 geometers and scholars with lifespan, biography, works, and article attributions (`:person:`).
* :ref:`Systematic Bibliography <bibliography>` — 31 primary monographs, editions, and 19th/20th-century mathematical journals (`:cite:`).
""",
}


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


def demote_headings_for_frontmatter(body: str) -> str:
    """Demote ``===`` headings in individual frontmatter folios to ``---`` (and ``---`` to ``~~~``)."""
    out_lines = body.splitlines()
    for i in range(1, len(out_lines)):
        prev = out_lines[i - 1]
        cur = out_lines[i].strip()
        if prev.strip() and len(cur) >= len(prev.strip()):
            if set(cur) == {"="}:
                out_lines[i] = "-" * len(prev.strip())
            elif set(cur) == {"-"}:
                out_lines[i] = "~" * len(prev.strip())
    return "\n".join(out_lines)


def strip_top_chapter_heading(body: str) -> str:
    """Remove top ``===`` chapter heading on the first folio of a chapter when chapter wrapper already emits it."""
    lines = body.splitlines()
    if len(lines) >= 2 and lines[0].strip() and set(lines[1].strip()) == {"="} and len(lines[1].strip()) >= 3:
        rest = lines[2:]
        while rest and not rest[0].strip():
            rest.pop(0)
        return "\n".join(rest)
    return body


def _ends_mid_sentence(block: str) -> bool:
    """Return True if a plain paragraph block ends without sentence-closing punctuation."""
    stripped = block.strip()
    if not stripped or stripped.startswith(("..", "|")):
        return False
    lines = stripped.splitlines()
    if len(lines) == 2 and re.match(r"^[=\-~^\"+]{3,}$", lines[1].strip()):
        return False
    last_char = stripped[-1]
    return last_char not in {".", ":", ";", "?", "!", "”", '"', ")", "*"}


def _is_plain_continuation_paragraph(block: str) -> bool:
    """Return True if block is an ordinary prose/math paragraph suitable for joining across a page turn."""
    stripped = block.strip()
    if not stripped or stripped.startswith(("..", "|")):
        return False
    if re.match(r"^(?:\d+\.\s+|\*\*\d+\.|LOCUS\s+\d+|ANALYSIS\.|CONSTRUCTION\.|PROOF\.|DISCUSSION\.|CONVERSELY\.|\*Note\.\*)", stripped):
        return False
    lines = stripped.splitlines()
    return not (len(lines) == 2 and re.match(r"^[=\-~^\"+]{3,}$", lines[1].strip()))


def depaginate_folios(
    folio_entries: list[tuple[str, str, dict[str, str], str]],
    is_frontmatter: bool = False,
) -> str:
    """Assemble consecutive transcribed folios into continuous Book Codex RST with ``.. folio::`` milestones."""
    assembled_blocks: list[str] = []

    for idx, (folio_id, page_str, meta, raw_body) in enumerate(folio_entries):
        status = meta.get("status", "ok")
        if status == "blank":
            continue

        body = demote_headings_for_frontmatter(raw_body) if is_frontmatter else (
            strip_top_chapter_heading(raw_body) if idx == 0 else raw_body
        )

        # Special clean reflow for folio 0038 where side-by-side Figs. 14-15 sit mid-sentence in print
        raw_split = [b.rstrip() for b in re.split(r"\n\s*\n(?=\S)", body.strip()) if b.strip()]
        if folio_id == "0038":
            reordered: list[str] = []
            i = 0
            while i < len(raw_split):
                if (
                    raw_split[i].endswith("given points :math:`A, B`")
                    and i + 3 < len(raw_split)
                    and raw_split[i + 1].startswith(".. picture:: 0038.g1.png")
                    and raw_split[i + 2].startswith(".. picture:: 0038.g2.png")
                ):
                    reordered.append(raw_split[i] + " " + raw_split[i + 3].lstrip())
                    reordered.append(raw_split[i + 1])
                    reordered.append(raw_split[i + 2])
                    i += 4
                else:
                    reordered.append(raw_split[i])
                    i += 1
            blocks = reordered
        else:
            blocks = raw_split

        if not blocks:
            continue

        milestone = f".. folio:: {folio_id}\n   :page: {page_str}"

        if assembled_blocks and _ends_mid_sentence(assembled_blocks[-1]) and _is_plain_continuation_paragraph(blocks[0]):
            # Seamlessly join sentence split across page turn, then emit folio milestone
            assembled_blocks[-1] = assembled_blocks[-1] + " " + blocks[0]
            assembled_blocks.append(milestone)
            assembled_blocks.extend(blocks[1:])
        else:
            assembled_blocks.append(milestone)
            assembled_blocks.extend(blocks)

    return "\n\n".join(assembled_blocks)


def build_section_table_rst(chapter: dict[str, Any]) -> str:
    """Render a clean RST table of chapter sections, folio spans, printed pages, and articles."""
    sections = chapter.get("sections") or []
    if not sections:
        return ""
    lines = [
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 12 48 16 12 12",
        "",
        "   * - Section",
        "     - Title",
        "     - Folios",
        "     - Pages",
        "     - Articles",
    ]
    for sec in sections:
        art = sec.get("articles")
        art_str = f"§§ {art[0]}–{art[1]}" if isinstance(art, list) and len(art) == 2 else "—"
        f_span = (
            f"``{sec['folio_start']}``"
            if sec["folio_start"] == sec["folio_end"]
            else f"``{sec['folio_start']}``–``{sec['folio_end']}``"
        )
        p_span = (
            f"{sec['page_start']}"
            if sec["page_start"] == sec["page_end"]
            else f"{sec['page_start']}–{sec['page_end']}"
        )
        lines.extend([
            f"   * - ``{sec['code']}``",
            f"     - {sec['title']}",
            f"     - {f_span}",
            f"     - {p_span}",
            f"     - {art_str}",
        ])
    return "\n".join(lines)


def build_chapter_unit(
    chapter: dict[str, Any],
    chapter_folios: list[dict[str, Any]],
    volume_dir: Path,
    book_doc_dir: Path,
) -> dict[str, Any]:
    """Build ``<slug>/<slug>-en.rst`` and ``<slug>/<slug>-commentary.rst`` for a single chapter unit."""
    slug = chapter["slug"]
    chap_dir = volume_dir / chapter["dir"]
    unit_dir = book_doc_dir / slug
    unit_dir.mkdir(parents=True, exist_ok=True)

    num = chapter.get("number")
    display_title = f"Chapter {num}: {chapter['title']}" if num else chapter["title"]
    subtitle = chapter.get("subtitle", "")
    art_range = chapter.get("article_range")
    art_str = f"§§ {art_range[0]}–{art_range[1]}" if art_range else "Unnumbered"
    folio_span = f"{chapter['folio_start']}–{chapter['folio_end']}"
    page_span = f"{chapter['page_start']}–{chapter['page_end']}"

    # Copy any calibrated .g*.png and .g*.inverted.png crops into unit_dir for PictureDirective
    copied_graphics = 0
    for g_png in sorted(chap_dir.glob("*.g*.png")):
        shutil.copy2(g_png, unit_dir / g_png.name)
        copied_graphics += 1

    transcribed_entries: list[tuple[str, str, dict[str, str], str]] = []
    notes_entries: list[tuple[str, str, str]] = []
    untranscribed_folios: list[dict[str, Any]] = []

    for f_entry in chapter_folios:
        fid = f_entry["folio"]
        rst_path = chap_dir / f"{fid}.rst"
        notes_path = chap_dir / f"{fid}.notes.rst"
        if rst_path.is_file():
            meta, body = parse_folio_rst(rst_path)
            transcribed_entries.append((fid, str(f_entry["printed_page"]), meta, body))
            if notes_path.is_file():
                notes_entries.append((fid, str(f_entry["printed_page"]), notes_path.read_text(encoding="utf-8").strip()))
        else:
            untranscribed_folios.append(f_entry)

    # ---- Track 1: <slug>-en.rst (English Text / Architectural Blueprint) ----
    en_lines: list[str] = [
        ":layout: book",
        f":title: {display_title}",
        "",
        f".. _{slug}-en:",
        "",
        display_title,
        "=" * len(display_title),
        "",
    ]
    if subtitle:
        en_lines.extend([f".. rubric:: {subtitle}", ""])

    if transcribed_entries:
        depaginated = depaginate_folios(transcribed_entries, is_frontmatter=(chapter["index"] == 0))
        en_lines.append(depaginated)
        en_lines.append("")

        if untranscribed_folios:
            first_rem = untranscribed_folios[0]
            last_rem = untranscribed_folios[-1]
            en_lines.extend([
                "----",
                "",
                ".. note::",
                "",
                f"   **Editorial Continuation (Folios ``{first_rem['folio']}``–``{last_rem['folio']}``, Pages {first_rem['printed_page']}–{last_rem['printed_page']})**",
                "",
                "   Article **§ 15** continues onto Folio ``0041`` (p. 22): *“and therefore the angle* :math:`EAF` *is known. The altitude* :math:`AD` *of the triangle* :math:`ABC` *is also the altitude of* :math:`AEF` *... Since* :math:`BA = BE, CA = CF`, *the vertices* :math:`B, C` *are the traces on* :math:`EF` *of the mediators of* :math:`AE` *and* :math:`AF` *.”*",
                "",
                f"   All 300 DPI archival scans for the remainder of {display_title} (``{first_rem['folio']}.png``–``{last_rem['folio']}.png``, covering **§§ 15–22** and **Review Exercises 1–74**) are ingested in ``resources/college_geometry/{chapter['dir']}/`` and indexed below for Phase 2 transcription.",
                "",
                "Remaining Chapter I Architecture (Folios ``0041``–``0052``)",
                "-----------------------------------------------------------",
                "",
                build_section_table_rst(chapter),
                "",
            ])
    else:
        en_lines.extend([
            ".. admonition:: Digital Scriptorium Architectural Blueprint",
            "",
            f"   * **Archival Span**: Folios ``{folio_span}`` · Printed Pages ``{page_span}`` · Articles **{art_str}**",
            f"   * **300 DPI Raster Scans**: ``{len(chapter_folios)}`` standardized folios ready in ``resources/college_geometry/{chapter['dir']}/``",
            "   * **Companion Track**: Switch to the **Commentary** tab above for mathematical synthesis, triangle-center mappings, and GEOMETOR connections.",
            "",
            "Section & Article Conspectus",
            "----------------------------",
            "",
            build_section_table_rst(chapter),
            "",
            "Folio Scan Allocation",
            "---------------------",
            "",
            ".. list-table::",
            "   :header-rows: 1",
            "   :widths: 14 14 24 28 20",
            "",
            "   * - Folio",
            "     - Page",
            "     - Section",
            "     - Articles",
            "     - Scan Status",
        ])
        for f_entry in chapter_folios:
            arts = f_entry.get("articles") or []
            arts_disp = f"§§ {arts[0]}–{arts[-1]}" if len(arts) > 1 else (f"§ {arts[0]}" if len(arts) == 1 else "—")
            st = "blank verso" if f_entry.get("is_blank") else ("cover (RGB)" if f_entry.get("is_cover") else "300 DPI gray")
            en_lines.extend([
                f"   * - ``{f_entry['folio']}``",
                f"     - ``{f_entry['printed_page']}``",
                f"     - {f_entry.get('section_title', '—')}",
                f"     - {arts_disp}",
                f"     - {st}",
            ])
        en_lines.append("")

    (unit_dir / f"{slug}-en.rst").write_text("\n".join(en_lines), encoding="utf-8")

    # ---- Track 2: <slug>-commentary.rst (Commentary & Diplomatic Notes) ----
    comm_title = f"{display_title} — Commentary"
    comm_lines: list[str] = [
        ":layout: book",
        f":title: {comm_title}",
        "",
        f".. _{slug}-commentary:",
        "",
        comm_title,
        "=" * len(comm_title),
        "",
        f".. rubric:: Constructive Analysis, Historical Provenance & GEOMETOR Notes ({folio_span}, pp. {page_span})",
        "",
    ]

    if slug == "frontmatter":
        comm_lines.extend([
            "Editorial Overview of the Frontmatter (`0001`–`0019`)",
            "-----------------------------------------------------",
            "",
            "The nineteen frontmatter folios of :person:`Nathan Altshiller-Court's <altshiller-court>` :cite:`College Geometry (1952 / Dover 2007) <court:1952>` frame both the historical triumph of synthetic geometry in twentieth-century American higher education and the pedagogical discipline required to master geometric problem solving:",
            "",
            "* **From 1925 to 1952 (`Preface`, pp. vii–viii)**: Between the :cite:`1925 Johnson Publishing first edition <court:1925>` and the :cite:`1952 Barnes & Noble second edition <court:1952>`, college geometry evolved from an experimental elective into a staple course for mathematics majors and prospective teachers. Altshiller-Court rewrote the entire treatise, inserted Chapter IV (*The Quadrilateral*), expanded Chapter X (*Recent Geometry of the Triangle*), and moved :term:`harmonic division <harmonic-division>` forward into Chapter II/III.",
            "* **Pagination Offset Contract**: Folios ``0001``–``0019`` carry cover and Roman numerals ``[iii]``–``[xx]`` (including blank versos ``0005``, ``0009``, ``0015``, ``0019``), establishing the exact body formula ``PDF Folio = Printed Arabic Page + 19`` from Folio ``0020`` (p. ``1``) to Folio ``0332`` (p. ``313``).",
            "* **Problem-Solving Heuristic (`To the Student`, pp. xvii–xix)**: Altshiller-Court's insistence on maintaining bidirectional marginal links to :cite:`Euclid's Elements <euclid:elements>`, memorizing exact definitions and theorems as active deductive tools, restating problems from memory, and sketching diagnostic figures directly parallels George Pólya's *How to Solve It* (1945) and motivates the GEOMETOR Digital Scriptorium.",
            "",
        ])
    elif slug == "ch01-geometric-constructions":
        comm_lines.extend([
            "Constructive Architecture & Symbolic Modeling (`§§ 1–22`)",
            "---------------------------------------------------------",
            "",
            "Chapter I lays down the operational grammar of the entire book. Every ruler-and-compass construction is governed by :person:`Pappus' <pappus>` four-stage :term:`analytic method <analytic-method>` (:cite:`Collection, Book VII <pappus:collection:VII>`):",
            "",
            "1. :term:`Analysis <analysis-step>` — Assume the required configuration already exists and trace algebraic/synthetic incidences back to known data.",
            "2. :term:`Construction <construction-step>` — Execute elementary straightedge (`line(P, Q)`) and compass (`circle(A, r)`) steps in forward topological order.",
            "3. :term:`Proof <proof-step>` — Verify deductively that the constructed object satisfies every hypothesis.",
            "4. :term:`Discussion <discussion-step>` (*Diorismos*) — Determine exact existence inequalities (`s < 2 OE`, `s^2 > 2a^2`), count multiplicity of solutions (`0, 1, 2, 3, 4, 6`, or :math:`\\infty`), and identify poristic degeneracies (as in § 9 when :math:`AC \\perp BD` and :math:`AC = BD`).",
            "",
            "Mapping Chapter I to ``geometor.model`` & ``geometor.elements``",
            "---------------------------------------------------------------",
            "",
            "* **Symbolic DAG Representation**: Altshiller-Court's § 1 notation—circles :math:`(A, r)` and line intersections :math:`M = (PQ, RS)`—maps one-to-one onto ``geometor.model`` primitives, where every constructed point retains its exact SymPy algebraic coordinates in a quadratic extension tower of :math:`\\mathbb{Q}`.",
            "* **The Twelve Fundamental Loci (§ 11, Folios `0030`–`0036`)**:",
            "  - *Linear Loci*: Parallel pair (Locus 3), :term:`mediator <mediator>` (Locus 4, :cite:`Euclid I.10–11 <euclid:elements>`), angle bisectors (Locus 5), and constant difference of squares :math:`AM^2 - BM^2 = d^2` (Locus 12 — the point-circle precursor of the :term:`radical axis <radical-axis>` in Chapter VIII, § 422).",
            "  - *Circular Loci*: Circle :math:`(A, r)` (Locus 1), concentric tangent-length & subtended-angle circles (Loci 2, 6, 9), :term:`capable arc <subtended-angle-locus>` & Thales' circle (Locus 7, :cite:`Euclid III.21, III.31 <euclid:elements>`), chord-midpoint circle on :math:`OP` (Locus 8), Apollonius' median circle :math:`OM^2 = \\tfrac{1}{2}s^2 - a^2` (Locus 10), and the :term:`Apollonian circle <apollonian-circle>` :math:`AM : MB = p : q` (Locus 11, :person:`Apollonius <apollonius>`).",
            "* **Transformational & Unfolding Previews**: § 8 previews parallel translation (:cite:`Petersen <pt>`), § 9 previews :math:`90^\\circ` rotational congruence (:person:`Castillon <castillon>`), and § 15 introduces :term:`indirect elements <indirect-elements>` by unfolding perimeter :math:`2p` into auxiliary triangle :math:`AEF` with vertex angle :math:`90^\\circ + \\tfrac{1}{2}A`.",
            "",
        ])
    else:
        comm_lines.append(CHAPTER_COMMENTARY.get(slug, ""))
        comm_lines.append("")

    geometor_links = chapter.get("geometor_links") or []
    if geometor_links:
        comm_lines.extend([
            "Cross-Repository GEOMETOR Links",
            "-------------------------------",
            "",
        ])
        for gl in geometor_links:
            comm_lines.append(f"* ``geometor/{gl}``")
        comm_lines.append("")

    if notes_entries:
        comm_lines.extend([
            "Folio-by-Folio Diplomatic & Constructive Notes",
            "----------------------------------------------",
            "",
        ])
        for fid, p_str, n_text in notes_entries:
            # Demote headings inside individual folio notes (`===` -> `~~~`, `---` -> `^^^`)
            n_lines = n_text.splitlines()
            demoted: list[str] = []
            for j, ln in enumerate(n_lines):
                s = ln.strip()
                if j > 0 and n_lines[j - 1].strip() and len(s) >= len(n_lines[j - 1].strip()):
                    if set(s) == {"="}:
                        demoted.append("~" * len(n_lines[j - 1].strip()))
                        continue
                    if set(s) == {"-"}:
                        demoted.append("^" * len(n_lines[j - 1].strip()))
                        continue
                demoted.append(ln)
            comm_lines.append("\n".join(demoted))
            comm_lines.append("")

    (unit_dir / f"{slug}-commentary.rst").write_text("\n".join(comm_lines), encoding="utf-8")

    return {
        "slug": slug,
        "display_title": display_title,
        "transcribed_count": len(transcribed_entries),
        "total_folios": len(chapter_folios),
        "copied_graphics": copied_graphics,
    }


def _format_occurrences_line(
    occurrences: list[dict[str, Any]],
    chapter_dir_to_slug: dict[str, str],
) -> str:
    """Format occurrence links to compiled chapter units."""
    if not occurrences:
        return ""
    seen = set()
    parts: list[str] = []
    for occ in occurrences:
        folio = occ.get("folio", "")
        page = occ.get("page", "")
        sec = occ.get("section", "")
        slug = chapter_dir_to_slug.get(sec)
        key = (folio, slug)
        if key in seen:
            continue
        seen.add(key)
        if slug:
            parts.append(f":ref:`f. {folio} (p. {page}) <{slug}-en>`")
        else:
            parts.append(f"f. ``{folio}`` (p. {page})")
    return " · ".join(parts)


def build_apparatus_pages(
    volume_dir: Path,
    book_doc_dir: Path,
    structure: dict[str, Any],
) -> dict[str, int]:
    """Generate ``bibliography.rst``, ``persons.rst``, ``glossary.rst``, and ``scan-inventory.rst``."""
    citations: dict[str, Any] = json.loads((volume_dir / "citations.json").read_text(encoding="utf-8"))
    persons: dict[str, Any] = json.loads((volume_dir / "persons.json").read_text(encoding="utf-8"))
    glossary: dict[str, Any] = json.loads((volume_dir / "glossary.json").read_text(encoding="utf-8"))
    reviews_path = volume_dir / "folio_reviews.json"
    reviews: dict[str, Any] = (
        json.loads(reviews_path.read_text(encoding="utf-8")) if reviews_path.is_file() else {}
    )

    chapter_dir_to_slug = {ch["dir"]: ch["slug"] for ch in structure["chapters"]}

    # 1. bibliography.rst
    bib_lines = [
        ":layout: book",
        ":title: Systematic Bibliography",
        "",
        ".. _bibliography:",
        "",
        "Systematic Bibliography & Abbreviations",
        "=======================================",
        "",
        f".. rubric:: {len(citations)} Editions, Classical Treatises, and Mathematical Periodicals Cited in *College Geometry*",
        "",
        "Every ``:cite:`` reference in the Book Codex resolves to its canonical bibliographic anchor below.",
        "",
    ]
    for ck, entry in sorted(citations.items()):
        c_slug = apparatus_slug(ck)
        occ_str = _format_occurrences_line(entry.get("occurrences", []), chapter_dir_to_slug)
        author_key = entry.get("author_key", "")
        author_disp = entry.get("author", "")
        if author_key and author_key in persons:
            author_ref = f":person:`{author_disp} <{author_key}>`"
        else:
            author_ref = f"**{author_disp}**"
        bib_lines.extend([
            f".. _cite-{c_slug}:",
            "",
            f"``[{ck}]`` — {entry.get('work', '')}",
            "-" * len(f"``[{ck}]`` — {entry.get('work', '')}"),
            "",
            f"* **Author / Editor**: {author_ref}",
            f"* **Locus / Key**: {entry.get('locus', '—')}",
        ])
        if occ_str:
            bib_lines.append(f"* **Referenced At**: {occ_str}")
        bib_lines.append("")

    (book_doc_dir / "bibliography.rst").write_text("\n".join(bib_lines), encoding="utf-8")

    # 2. persons.rst
    pers_lines = [
        ":layout: book",
        ":title: Index of Persons",
        "",
        ".. _persons:",
        "",
        "Biographical Register of Geometers & Scholars",
        "=============================================",
        "",
        f".. rubric:: Prosopographical Apparatus ({len(persons)} Historical Geometers, Editors, and Contemporaries)",
        "",
        "Synthesizes Altshiller-Court's *List of Names* (pp. 307–309), *Historical and Bibliographical Notes* (pp. 295–306), and Frontmatter acknowledgments.",
        "",
    ]
    for pk, entry in sorted(persons.items(), key=lambda kv: kv[1].get("name", kv[0]).lower()):
        p_slug = apparatus_slug(pk)
        heading = f"{entry['name']} ({entry.get('dates', '')})" if entry.get("dates") else entry["name"]
        arts = entry.get("articles") or []
        arts_str = ", ".join(f"§ {a}" for a in arts) if arts else "Frontmatter / Apparatus"
        works = entry.get("works") or []
        occ_str = _format_occurrences_line(entry.get("occurrences", []), chapter_dir_to_slug)

        pers_lines.extend([
            f".. _person-{p_slug}:",
            "",
            heading,
            "-" * len(heading),
            "",
            f"* **Role**: {entry.get('role', '')}",
            f"* **Articles in College Geometry**: {arts_str}",
        ])
        if works:
            pers_lines.append("* **Principal Works**: " + "; ".join(f"*{w}*" for w in works))
        if occ_str:
            pers_lines.append(f"* **Edition Loci**: {occ_str}")
        pers_lines.extend([
            "",
            entry.get("bio", ""),
            "",
        ])

    (book_doc_dir / "persons.rst").write_text("\n".join(pers_lines), encoding="utf-8")

    # 3. glossary.rst
    gloss_lines = [
        ":layout: book",
        ":title: Technical Glossary",
        "",
        ".. _glossary:",
        "",
        "Technical Glossary of Modern Synthetic Geometry",
        "===============================================",
        "",
        f".. rubric:: {len(glossary)} Constructive Methods, Loci, Triangle Centers, Circles, and Projective/Conformal Transformations",
        "",
    ]
    for tk, entry in sorted(glossary.items(), key=lambda kv: kv[1].get("headword", kv[0]).lower()):
        t_slug = apparatus_slug(tk)
        head = entry.get("headword", tk)
        occ_str = _format_occurrences_line(entry.get("occurrences", []), chapter_dir_to_slug)
        gloss_lines.extend([
            f".. _term-{t_slug}:",
            "",
            head,
            "-" * len(head),
            "",
            f"* **Domain & Locus**: {entry.get('language', '')}",
            f"* **Symbolic / Center Identity**: ``{entry.get('translation', '')}``",
        ])
        if occ_str:
            gloss_lines.append(f"* **Edition Loci**: {occ_str}")
        gloss_lines.extend([
            "",
            entry.get("definition", ""),
            "",
        ])

    (book_doc_dir / "glossary.rst").write_text("\n".join(gloss_lines), encoding="utf-8")

    # 4. scan-inventory.rst
    folios = structure["folios"]
    verified_count = sum(1 for v in reviews.values() if v.get("status") == "verified")
    inv_lines = [
        ":layout: book",
        ":title: Archival Scan & Folio Inventory",
        "",
        ".. _scan-inventory:",
        "",
        "334-Folio Archival Scan & Transcription Inventory",
        "=================================================",
        "",
        f".. rubric:: Complete Concordance of PDF Pages, 300 DPI Scans (``1421 × 2225`` px), Articles §§ 1–699, Diagrams, and Review Status ({verified_count} Verified Folios)",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 10 10 26 24 14 16",
        "",
        "   * - Folio",
        "     - Page",
        "     - Chapter Directory",
        "     - Section / Articles",
        "     - Diagrams",
        "     - Status",
    ]
    for f_entry in folios:
        fid = f_entry["folio"]
        cdir = f_entry["chapter_dir"]
        rst_exists = (volume_dir / cdir / f"{fid}.rst").is_file()
        json_path = volume_dir / cdir / f"{fid}.json"
        diag_count = 0
        if json_path.is_file():
            diag_count = len(json.loads(json_path.read_text(encoding="utf-8")).get("graphics", []))
        rev = reviews.get(f"college_geometry:{fid}", {}).get("status")
        if rev == "verified":
            status_disp = "verified (RST + Notes)"
        elif rst_exists:
            status_disp = "transcribed"
        elif f_entry.get("is_blank"):
            status_disp = "blank scan"
        else:
            status_disp = "300 DPI scan ready"

        arts = f_entry.get("articles") or []
        arts_str = f" (🗾 §§ {arts[0]}–{arts[-1]})" if len(arts) > 1 else (f" (§ {arts[0]})" if len(arts) == 1 else "")
        arts_str = arts_str.replace("🗾 ", "")
        sec_disp = f"{f_entry.get('section_code', '')}{arts_str}".strip() or "—"
        diag_disp = f"{diag_count} crop(s)" if diag_count else "—"

        inv_lines.extend([
            f"   * - ``{fid}``",
            f"     - ``{f_entry['printed_page']}``",
            f"     - ``{cdir}``",
            f"     - {sec_disp}",
            f"     - {diag_disp}",
            f"     - {status_disp}",
        ])
    inv_lines.append("")

    (book_doc_dir / "scan-inventory.rst").write_text("\n".join(inv_lines), encoding="utf-8")

    return {
        "citations": len(citations),
        "persons": len(persons),
        "glossary": len(glossary),
        "folios": len(folios),
        "verified": verified_count,
    }


def build_book_index(
    structure: dict[str, Any],
    unit_summaries: list[dict[str, Any]],
    apparatus_counts: dict[str, int],
    book_doc_dir: Path,
) -> None:
    """Write ``docsrc/college_geometry/index.rst`` Book Codex master landing page."""
    work = structure["work"]
    lines = [
        ":navigation: header",
        ":order: 1",
        ":layout: book",
        f":title: {work['title']}",
        f":book_title: {work['title']}",
        f":book_subtitle: {work['subtitle']}",
        f":author: {work['author']}",
        f":series: {work['edition']}",
        f":publisher: {work['original_publisher']} (1952) • {work['reprint_publisher']} (2007)",
        ":location: New York / Mineola",
        f":year: {work['original_year']}",
        "",
        ".. _altshiller-court-index:",
        ".. _college-geometry-index:",
        "",
        "COLLEGE GEOMETRY",
        "================",
        "",
        f".. rubric:: {work['subtitle']} ({work['original_year']} / Dover {work['reprint_year']})",
        "",
        ".. container:: title-page",
        "",
        "   | :person:`NATHAN ALTSHILLER-COURT <altshiller-court>` (1881–1968)",
        "   | *Professor of Mathematics, University of Oklahoma*",
        "   | *Second Edition, Revised and Enlarged* — Barnes & Noble, Inc., New York, 1952",
        "   | *Unabridged Dover Republication* — Dover Publications, Inc., Mineola, N.Y., 2007 (ISBN ``978-0-486-45805-2``)",
        "",
        "----",
        "",
        "Conspectus of the Digital Edition",
        "---------------------------------",
        "",
        "Each division below is published as a synchronized **2-Track Book Codex** (**English** | **Commentary**) with track-preserving navigation, marginal folio milestones, dark-mode normalized geometric figures, and interactive ``:person:``, ``:cite:``, and ``:term:`` apparatus cards.",
        "",
    ]

    for ch, summary in zip(structure["chapters"], unit_summaries):
        slug = ch["slug"]
        heading = summary["display_title"]
        art_range = ch.get("article_range")
        art_badge = f" · Articles **§§ {art_range[0]}–{art_range[1]}**" if art_range else ""
        trans_badge = (
            f" · **{summary['transcribed_count']}/{summary['total_folios']} Folios Verified**"
            if summary["transcribed_count"] > 0
            else f" · **{summary['total_folios']} Archival Scans Indexed**"
        )
        lines.extend([
            heading,
            "~" * len(heading),
            "",
            f"*{ch.get('subtitle', '')}*",
            "",
            f":ref:`English <{slug}-en>` · :ref:`Commentary <{slug}-commentary>` — Folios ``{ch['folio_start']}``–``{ch['folio_end']}`` (pp. ``{ch['page_start']}``–``{ch['page_end']}``){art_badge}{trans_badge}",
            "",
        ])

    lines.extend([
        "Scholarly Apparatus & Concordances",
        "----------------------------------",
        "",
        f"* :ref:`Systematic Bibliography & Periodical Key ({apparatus_counts['citations']} Entries) <bibliography>`",
        f"* :ref:`Biographical Register of Geometers & Scholars ({apparatus_counts['persons']} Persons) <persons>`",
        f"* :ref:`Technical Glossary of Synthetic Geometry ({apparatus_counts['glossary']} Terms) <glossary>`",
        f"* :ref:`334-Folio Archival Scan & Transcription Inventory ({apparatus_counts['verified']} Verified) <scan-inventory>`",
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "   :hidden:",
        "   :caption: English Track",
        "",
    ])
    for ch in structure["chapters"]:
        slug = ch["slug"]
        lines.append(f"   {slug}/{slug}-en")

    lines.extend([
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :hidden:",
        "   :caption: Commentary Track",
        "",
    ])
    for ch in structure["chapters"]:
        slug = ch["slug"]
        lines.append(f"   {slug}/{slug}-commentary")

    lines.extend([
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :hidden:",
        "   :caption: Scholarly Apparatus",
        "",
        "   bibliography",
        "   persons",
        "   glossary",
        "   scan-inventory",
        "",
    ])

    (book_doc_dir / "index.rst").write_text("\n".join(lines), encoding="utf-8")


def compile_edition(repo_root: Path) -> dict[str, Any]:
    """Compile the complete *College Geometry* Book Codex into ``docsrc/college_geometry/``."""
    volume_dir = repo_root / "resources" / "college_geometry"
    book_doc_dir = repo_root / "docsrc" / "college_geometry"
    book_doc_dir.mkdir(parents=True, exist_ok=True)

    structure: dict[str, Any] = json.loads(
        (volume_dir / "structure_map.json").read_text(encoding="utf-8")
    )
    folios_by_dir: dict[str, list[dict[str, Any]]] = {}
    for f_entry in structure["folios"]:
        folios_by_dir.setdefault(f_entry["chapter_dir"], []).append(f_entry)

    unit_summaries: list[dict[str, Any]] = []
    for ch in structure["chapters"]:
        c_folios = folios_by_dir.get(ch["dir"], [])
        summary = build_chapter_unit(ch, c_folios, volume_dir, book_doc_dir)
        unit_summaries.append(summary)

    apparatus_counts = build_apparatus_pages(volume_dir, book_doc_dir, structure)
    build_book_index(structure, unit_summaries, apparatus_counts, book_doc_dir)

    return {
        "units_compiled": len(unit_summaries),
        "transcribed_folios": sum(u["transcribed_count"] for u in unit_summaries),
        "total_folios": apparatus_counts["folios"],
        "verified_folios": apparatus_counts["verified"],
        "graphics_copied": sum(u["copied_graphics"] for u in unit_summaries),
        "apparatus": apparatus_counts,
    }


def get_edition_status(repo_root: Path) -> dict[str, Any]:
    """Return a diagnostic summary of ingested scans, transcriptions, graphics, and reviews."""
    volume_dir = repo_root / "resources" / "college_geometry"
    structure = json.loads((volume_dir / "structure_map.json").read_text(encoding="utf-8"))
    reviews_path = volume_dir / "folio_reviews.json"
    reviews = json.loads(reviews_path.read_text(encoding="utf-8")) if reviews_path.is_file() else {}

    png_count = 0
    rst_count = 0
    notes_count = 0
    json_count = 0
    crop_count = 0

    for f_entry in structure["folios"]:
        cdir = volume_dir / f_entry["chapter_dir"]
        fid = f_entry["folio"]
        if (cdir / f"{fid}.png").is_file():
            png_count += 1
        if (cdir / f"{fid}.rst").is_file():
            rst_count += 1
        if (cdir / f"{fid}.notes.rst").is_file():
            notes_count += 1
        jp = cdir / f"{fid}.json"
        if jp.is_file():
            json_count += 1
            for g in json.loads(jp.read_text(encoding="utf-8")).get("graphics", []):
                if (cdir / g["file"]).is_file():
                    crop_count += 1

    return {
        "total_folios": len(structure["folios"]),
        "scans_present": png_count,
        "rst_transcribed": rst_count,
        "notes_present": notes_count,
        "folios_with_graphics": json_count,
        "diagram_crops": crop_count,
        "verified_reviews": sum(1 for r in reviews.values() if r.get("status") == "verified"),
    }
