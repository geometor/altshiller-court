"""Book Codex compiler and scholarly apparatus builder for *College Geometry* (1952).

Compiles verified diplomatic folio transcriptions (``resources/college_geometry/<dir>/<NNNN>.rst``
and ``<NNNN>.notes.rst``), diagram crops (``<NNNN>.g<k>.png``), interactive SVGs
(``<NNNN>.g<k>.svg``), ``structure_map.json``, and apparatus registries
(``persons.json``, ``citations.json``, ``glossary.json``, ``folio_reviews.json``)
into a multi-level Euclid-style Book Codex (``Book -> Chapters -> Sections -> Items``)
with ``.. collection::`` navigation and ``Commentary`` companion tracks under
``docsrc/college_geometry/``.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from typing import Any

from .codex_items import (
    CHAPTER_SECTION_META_BY_INDEX,
    CodexItem,
    CodexSection,
    FolioBlock,
    copy_referenced_graphics,
    decompose_chapter_folios,
    decompose_frontmatter,
    demote_headings,
    parse_folio_rst,
    render_blocks_with_folios,
)
from .hero_figures import CHAPTER_HERO_KEYS, HeroFigureRegistry
from .section_synopses import (
    CH03_MEDIANS_CONTINUATION,
    SECTION_SYNOPSES,
    SectionSynopsis,
)
from .svg_compiler import compile_all_svgs


def apparatus_slug(key: str) -> str:
    """Deterministic anchor slug matching ``photon_platform.publish.roles.geometry._apparatus_slug``."""
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


CHAPTER_OVERVIEWS: dict[str, str] = {
    "frontmatter": (
        "Nineteen archival frontmatter folios (``0001``–``0019``, pp. ``[cover]``–``[xx]``) framing "
        "Nathan Altshiller-Court's 1952 Second Edition: the Dover cover, title and copyright pages, "
        "dedication, 1952 Preface and Acknowledgments, analytical Table of Contents, *To the Instructor*, "
        "and *To the Student*."
    ),
    "ch01-geometric-constructions": (
        "Foundational treatise on synthetic ruler-and-compass problem solving (**§§ 1–22**, Folios ``0020``–``0052``, "
        "pp. ``1``–``33``): notation and basic constructions, Pappus's four-part analytic method, "
        "twelve fundamental geometric loci, auxiliary-triangle indirect elements, 22 interactive "
        "``.euclid-graphic`` figures, and 167 graded and review exercises."
    ),
    "ch02-similitude-and-homothecy": (
        "Transformational construction and proof via similitude and homothecy (**§§ 23–53**, Folios ``0053``–``0071``, "
        "pp. ``34``–``52``): homothetic figures, direct and inverse centers of similitude of two circles, "
        "the circle of similitude, and the pantograph."
    ),
    "ch03-properties-of-the-triangle": (
        "Classical synthetic geometry of the triangle (**§§ 54–239**, Folios ``0072``–``0142``, pp. ``53``–``123``): "
        "harmonic preliminaries, circumcircle and the Problem of Pappus (**§§ 54–86**), medians and centroid "
        "(**§§ 87–110**), tritangent circles, orthocenter and orthic triangle, Euler line, nine-point circle, "
        "Feuerbach's theorem, and the orthocentric group."
    ),
    "ch04-the-quadrilateral": (
        "Synthetic theory of four-sided figures newly added in the 1952 Second Edition (**§§ 240–281**, "
        "Folios ``0143``–``0158``, pp. ``124``–``139``): Varignon's parallelogram, Euler's diagonal-midpoint "
        "identity, cyclic quadrilaterals, Ptolemy's and Brahmagupta's theorems, the anticenter, and "
        "circumscriptible and bicentric quadrilaterals."
    ),
    "ch05-the-simson-line": (
        "Pedal projections from the circumcircle onto the sidelines of a triangle (**§§ 282–305**, "
        "Folios ``0159``–``0169``, pp. ``140``–``150``): the Wallace–Simson collinearity criterion, "
        "bisection of the orthocenter segment on the nine-point circle, and angular intersection laws."
    ),
    "ch06-transversals": (
        "Directed segments and signed ratio criteria for collinearity and concurrency (**§§ 306–344**, "
        "Folios ``0170``–``0184``, pp. ``151``–``165``): Euler's four-point identity, Stewart's theorem, "
        "Menelaus's transversal theorem, Ceva's concurrency theorem, Gergonne and Nagel points, and "
        "Desargues's two-triangle theorem."
    ),
    "ch07-harmonic-division": (
        "Projective and metric theory of harmonic ranges and pencils (**§§ 345–357**, Folios ``0185``–``0190``, "
        "pp. ``166``–``171``): harmonic conjugates, perspectivity invariance of harmonic pencils, "
        "complete quadrangles and quadrilaterals, and the Gauss–Newton midpoint line."
    ),
    "ch08-circles": (
        "Comprehensive geometry of one, two, and three circles (**§§ 358–517**, Folios ``0191``–``0248``, "
        "pp. ``172``–``229``): inverse points, orthogonal circles, poles and polars, Monge's similitude "
        "axes, power and radical axis, coaxal pencils, Casey's theorem, and Gergonne's solution to the "
        "Problem of Apollonius."
    ),
    "ch09-inversion": (
        "Conformal transformation by reciprocal radii (**§§ 518–546**, Folios ``0249``–``0262``, "
        "pp. ``230``–``243``): images of lines and circles, Peaucellier's straight-line linkage, "
        "and inversion proofs of Ptolemy's theorem, Steiner's porism, and Feuerbach's theorem."
    ),
    "ch10-recent-geometry-of-the-triangle": (
        "Late-nineteenth-century triangle geometry (**§§ 547–699**, Folios ``0263``–``0313``, "
        "pp. ``244``–``294``): trilinear poles and polars, symmedians and the Lemoine point, Lemoine "
        "circles, Apollonian circles and isodynamic points, isogonal conjugates, Brocard points and "
        "circle, Tucker circles, and Neuberg's orthopole."
    ),
    "historical-and-bibliographical-notes": (
        "Altshiller-Court's historiographical apparatus (Folios ``0314``–``0328``, pp. ``295``–``309``): "
        "abbreviations of foundational treatises and periodicals, article-by-article historical "
        "attributions spanning §§ 4–697, and the alphabetical List of Names."
    ),
    "back-index": (
        "Alphabetical analytical subject index keyed to §§ 1–699, terminal blank leaf, and the 2007 "
        "Dover back cover (Folios ``0329``–``0334``, pp. ``310``–``[back cover]``)."
    ),
}


CHAPTER_COMMENTARY: dict[str, str] = {
    "ch02-similitude-and-homothecy": """\
Mathematical Architecture & Transformation Theory
-------------------------------------------------

Chapter II introduces the first great transformational pillar of *College Geometry*: **similitude** (§§ 23–30) and :term:`homothecy <homothecy>` (§§ 31–53). Where Chapter I constructs a figure directly at its final position and scale, the :term:`method of similitude <similitude>` temporarily sets aside one linear metric condition, constructs a convenient prototype of the required shape (*species*), and scales it into place from a well-chosen center of homothecy.

* **Homothetic Centers of Two Circles (§§ 39–45)**: Any two unequal circles :math:`(O, R)` and :math:`(O', R')` admit two :term:`centers of similitude <centers-of-similitude>`—external (direct, ratio :math:`+R/R'`) and internal (inverse, ratio :math:`-R/R'`)—which divide the line of centers :math:`OO'` harmonically.
* **Circle of Similitude & Pantograph (§§ 46–53)**: The locus of points from which two given unequal circles subtend equal angles is the :term:`Apollonian circle <apollonian-circle>` having their two centers of similitude as diameter (the *circle of similitude*), coaxal with the two given circles.

GEOMETOR Ecosystem Connections
------------------------------

* **Triangle Centers (``geometor/etc``)**: Applied to the :term:`circumcircle <circumcircle>` and :term:`incircle <incircle>` of :math:`\\triangle ABC`, the internal and external centers of similitude are Kimberling centers :math:`X(55)` (*insimilicenter*) and :math:`X(56)` (*exsimilicenter*), studied by :person:`Euler <euler>`, :person:`Monge <monge>`, and :person:`Poncelet <poncelet>`.
* **Medial & Anticomplementary Homothecy**: At the :term:`centroid <centroid>` :math:`G = X(2)`, the homothecy :math:`\\mathcal{H}(G, -\\tfrac{1}{2})` maps :math:`\\triangle ABC` onto its :term:`complementary (medial) triangle <complementary-triangle>`, driving the synthetic proofs of the :term:`Euler line <euler-line>` and :term:`nine-point circle <nine-point-circle>` in Chapter III.
""",
    "ch03-properties-of-the-triangle": """\
Mathematical Architecture & Classical Triangle Canon
----------------------------------------------------

Spanning 186 articles (§§ 54–239, pp. 53–123), Chapter III is the monumental heart of the first half of *College Geometry*:

1. **Harmonic Preliminaries (§§ 54–67)**: Early introduction of :term:`harmonic division <harmonic-division>` and the :term:`Apollonian circle <apollonian-circle>`, honoring the pedagogical innovation announced in the 1952 :ref:`Preface <frontmatter-03-preface>`.
2. **Circumcircle & Medians (§§ 68–110)**: Antipodal chords, Simson/Johnson precursors, the Problem of :person:`Pappus <pappus>` (§ 84), Apollonius' median formula, the :term:`centroid <centroid>` :math:`G = X(2)`, and the :term:`complementary <complementary-triangle>` and :term:`anticomplementary <anticomplementary-triangle>` triangles.
3. **Tritangent Circles (§§ 111–174)**: The :term:`incircle <incircle>` and three excircles :math:`(I, I_a, I_b, I_c)`, :person:`Carnot's <carnot>` theorem (§ 146), :person:`Chapple <chapple>`–:person:`Euler <euler>` distance formula :math:`OI^2 = R(R - 2r)` (§ 152, :cite:`Euler 1765 <euler:1765>`), and semiperimeter contact identities (:math:`s - a, s - b, s - c`).
4. **Altitudes, Euler Line & Nine-Point Circle (§§ 175–219)**: Concurrency at the :term:`orthocenter <orthocenter>` :math:`H = X(4)`, minimum-perimeter property of the :term:`orthic triangle <orthic-triangle>` (:person:`Fagnano <fagnano>`, § 194), collinearity of :math:`O, G, N, H` on the :term:`Euler line <euler-line>` (§ 202), the :term:`nine-point circle <nine-point-circle>` (§ 206, :person:`Brianchon <brianchon>` & :person:`Poncelet <poncelet>`), and :term:`Feuerbach's theorem <feuerbach-theorem>` (§ 215, :cite:`Feuerbach 1822 <feuerbach:1822>`).
5. **Orthocentric Group (§§ 220–239)**: Symmetric quadruple :math:`\\{A, B, C, H\\}` (:term:`orthocentric quadrilateral <orthocentric-quadrilateral>`) sharing a common nine-point circle.

GEOMETOR Ecosystem Connections
------------------------------

* **``geometor/etc`` & :cite:`Kimberling's ETC <kimberling:etc>`**: Establishes exact synthetic constructions for :math:`X(1)` (*incenter*), :math:`X(2)` (*centroid*), :math:`X(3)` (*circumcenter*), :math:`X(4)` (*orthocenter*), :math:`X(5)` (*nine-point center*), and :math:`X(11)` (*Feuerbach point*).
* **``geometor/model``**: Every center and circle in §§ 54–239 is quadratic constructible over :math:`\\mathbb{Q}(A, B, C)` and verifiable symbolically in SymPy without floating-point drift.
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
* **Menelaus' Theorem (§§ 310–325)**: Signed transversal product :math:`(AF/FB)(BD/DC)(CE/EA) = -1` (:person:`Menelaus of Alexandria <menelaus>`), applied immediately to collinearity of external angle-bisector traces, Pascal's mystic hexagram (inscribed in a circle), and centers of similitude of three circles (:person:`Monge <monge>`).
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
3. **Centers of Similitude, Power & Radical Axis (§§ 394–439)**: :person:`Monge's <monge>` theorem on the six centers of similitude of three circles (§ 405), :person:`Steiner's <steiner>` :term:`power of a point <power-of-a-point>` (:math:`d^2 - R^2`), and the :term:`radical axis <radical-axis>` of two circles (generalizing Chapter I, :ref:`Locus 12 <ch01-locus-12>`).
4. **Coaxal Pencils & Casey's Theorem (§§ 440–490)**: Intersecting, tangent, and non-intersecting :term:`coaxal circles <coaxal-circles>`, :person:`Poncelet's <poncelet>` limiting points :math:`L, L'`, conjugate orthogonal pencils, and :person:`Casey's <casey>` generalized Ptolemy theorem (§ 471, :cite:`Sequel to Euclid <casey:sequel:1892>`).
5. **Three Circles & The Problem of Apollonius (§§ 491–517)**: Radical center, circles of antisimilitude, the ten classical cases (``PPP`` through ``CCC``) of the :term:`Problem of Apollonius <problem-of-apollonius>`, and :person:`Gergonne's <gergonne>` celebrated master solution (§ 517) constructing complementary pairs of up to eight tangent circles via poles of axes of similitude and the radical center!
""",
    "ch09-inversion": """\
Mathematical Architecture & Conformal Transformation
----------------------------------------------------

Chapter IX (§§ 518–546, pp. 230–243) develops :term:`circular inversion <inversion>` :math:`(O, k)` (:person:`Steiner <steiner>`, :person:`Plücker <plucker>`, :person:`Möbius <mobius>`, Lord Kelvin, and Liouville) as an involutory, angle-preserving transformation of the plane:

* **Images of Lines & Circles (§§ 518–531)**: Lines/circles through the center of inversion :math:`O` invert into straight lines; lines/circles not through :math:`O` invert into circles; angles of intersection are preserved in magnitude and reversed in orientation.
* **Peaucellier's Inversor (§ 533)**: :person:`Peaucellier's <peaucellier>` exact mechanical straight-line linkage converting circular motion into rectilinear motion via inversion.
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

* **Bibliographic Abbreviations (pp. 295–296)**: Keys 8 foundational books (``Chl.``, ``Cn.``, ``Crt.``, ``Ech.``, ``Gy.``, ``LHr.``, ``Pt.``, ``Rouché-Comberousse``) and 9 problem-and-research periodicals (``Bull.``, ``Edinb.``, ``ET.``, ``GAM.``, ``JME.``, ``JMS.``, ``Mathesis.``, ``Monthly.``, ``NA.``, ``NC.``)—all encoded as structured entries in :ref:`Bibliography <bibliography>`.
* **Article-by-Article Provenance (§§ 4–697)**: Traces individual theorems and constructions from :person:`Euclid <euclid>`, :person:`Archimedes <archimedes>`, :person:`Apollonius <apollonius>`, :person:`Heron <heron>`, :person:`Menelaus <menelaus>`, :person:`Ptolemy <ptolemy>`, and :person:`Pappus <pappus>` through :person:`Ceva <ceva>`, :person:`Euler <euler>`, :person:`Carnot <carnot>`, :person:`Poncelet <poncelet>`, :person:`Gergonne <gergonne>`, :person:`Feuerbach <feuerbach>`, :person:`Steiner <steiner>`, :person:`Chasles <chasles>`, :person:`Lemoine <lemoine>`, :person:`Brocard <brocard>`, and :person:`Neuberg <neuberg>`—all cross-linked in :ref:`Index of Persons <persons>`.
""",
    "back-index": """\
Analytical Subject Index & Digital Apparatus Integration
--------------------------------------------------------

Pages 310–313 (folios ``0329``–``0332``) contain Altshiller-Court's alphabetical *Index* keyed to article numbers (§§ 1–699), followed by the blank recto leaf ``0333`` (``[314]``) and the 2007 Dover back cover ``0334``.

In this Digital Scriptorium edition, the printed subject index is complemented by three interactive, machine-linked registries:

* :ref:`Technical Glossary <glossary>` — 56 core definitions, loci, data, transformations, and Kimberling center mappings (``:term:``).
* :ref:`Biographical Register of Persons <persons>` — 67 geometers and scholars with lifespan, biography, works, and article attributions (``:person:``).
* :ref:`Systematic Bibliography <bibliography>` — 31 primary monographs, editions, and 19th/20th-century mathematical journals (``:cite:``).
""",
}


def _section_slug(sec: dict[str, Any]) -> str:
    """Build a deterministic URL slug for a chapter section dictionary."""
    code = apparatus_slug(str(sec.get("code", "")))
    title_clean = re.sub(r"\([^)]*\)", "", str(sec.get("title", ""))).strip()
    title_slug = apparatus_slug(title_clean)
    if title_slug.startswith(code + "-") or title_slug == code:
        return title_slug
    return f"{code}-{title_slug}".strip("-")


def _write_codex_item(
    item: CodexItem,
    parent_dir: Path,
    chap_res_dir: Path,
    notes_by_folio: dict[str, str],
    folio_to_anchor: dict[str, str],
) -> dict[str, int]:
    """Write ``<item.slug>/index.rst``, co-located SVGs/crops, ``commentary.rst``, and children."""
    item_dir = parent_dir / item.slug
    item_dir.mkdir(parents=True, exist_ok=True)

    folios = item.all_folios()
    first_fid = folios[0][0] if folios else ""
    first_page = folios[0][1] if folios else ""
    folios_csv = ", ".join(f for f, _ in folios)
    pages_csv = ", ".join(p for _, p in folios)

    # Register folio -> leaf anchor mapping (prefer deeper leaf items for locus folios)
    for fid, _ in item.blocks[0].folios if item.blocks else folios:
        folio_to_anchor.setdefault(fid, item.anchor)
    for fid, _ in folios:
        if item.item_type == "locus" or fid not in folio_to_anchor:
            folio_to_anchor[fid] = item.anchor

    lines: list[str] = [
        ":layout: book",
        f":type: {item.item_type}",
        f":order: {item.order}",
        f":canonical_id: {item.canonical_id}",
        f":title: {item.title}",
    ]
    if first_fid:
        lines.append(f":folio: {first_fid}")
        lines.append(f":page: {first_page}")
        lines.append(f":folios: {folios_csv}")
        lines.append(f":pages: {pages_csv}")
    if item.excerpt:
        lines.append(f":excerpt: {item.excerpt}")

    lines.extend([
        "",
        f".. _{item.anchor}:",
        "",
        item.title,
        "=" * len(item.title),
        "",
    ])

    # Ensure Table of Contents item has a clean lead paragraph before its list-table
    body_blocks = list(item.blocks)
    if item.slug == "04-contents" and item.excerpt and body_blocks:
        body_blocks = [FolioBlock(text=item.excerpt, folios=list(body_blocks[0].folios))] + body_blocks

    if body_blocks:
        lines.append(render_blocks_with_folios(body_blocks))
        lines.append("")

    if item.children and item.child_collection_type:
        lines.extend([
            ".. collection::",
            f"   :type: {item.child_collection_type}",
            "   :sort: order",
            "",
        ])

    comm_anchor = f"{item.anchor}-commentary"
    lines.extend([
        "----",
        "",
        f"See :ref:`Commentary on {item.title} <{comm_anchor}>`.",
        "",
        ".. toctree::",
        "   :hidden:",
        "",
        "   commentary",
        "",
    ])

    (item_dir / "index.rst").write_text("\n".join(lines), encoding="utf-8")

    svgs_copied, pngs_copied = copy_referenced_graphics(item.blocks, chap_res_dir, item_dir)

    # Companion commentary.rst
    comm_title = f"Commentary on {item.title}"
    comm_lines: list[str] = [
        ":layout: book",
        ":type: commentary",
        f":canonical_id: {item.canonical_id}.commentary",
        f":title: {comm_title}",
    ]
    if first_fid:
        comm_lines.extend([
            f":folio: {first_fid}",
            f":page: {first_page}",
            f":folios: {folios_csv}",
            f":pages: {pages_csv}",
        ])
    comm_lines.extend([
        "",
        f".. _{comm_anchor}:",
        "",
        comm_title,
        "=" * len(comm_title),
        "",
        f"Back to :ref:`{item.title} <{item.anchor}>`.",
        "",
    ])

    own_fids: list[str] = []
    for blk in item.blocks:
        for fid, _ in blk.folios:
            if fid not in own_fids:
                own_fids.append(fid)
    if not own_fids:
        own_fids = [fid for fid, _ in folios]

    for fid in own_fids:
        note_txt = notes_by_folio.get(fid)
        if note_txt:
            comm_lines.append(demote_headings(note_txt, {"=": "-", "-": "~"}))
            comm_lines.append("")

    (item_dir / "commentary.rst").write_text("\n".join(comm_lines), encoding="utf-8")

    items_written = 1
    for child in item.children:
        c_stats = _write_codex_item(child, item_dir, chap_res_dir, notes_by_folio, folio_to_anchor)
        items_written += c_stats["items"]
        svgs_copied += c_stats["svgs"]
        pngs_copied += c_stats["pngs"]

    return {
        "items": items_written,
        "svgs": svgs_copied,
        "pngs": pngs_copied,
    }


NON_LETTERED_SECTION_CODES = {
    "",
    "Main",
    "Review",
    "Supplementary",
    "BibKey",
    "Notes",
    "Names",
    "Index",
    "Endmatter",
    "Cover",
    "Title",
    "Preface",
    "Contents",
    "Instructor",
    "Student",
}


def _format_section_title(sec: dict[str, Any]) -> str:
    """Format section titles without bare ``[A-Z]. `` prefixes that trigger Docutils enumerated lists."""
    code = str(sec.get("code", "")).strip()
    raw_title = str(sec.get("title", "")).strip()
    cleaned_title = re.sub(r"\s+—\s+[a-z]\.\s+", ": ", raw_title)
    if code in NON_LETTERED_SECTION_CODES:
        return cleaned_title
    return f"Section {code} — {cleaned_title}"


def _sanitize_section_label(label: str) -> str:
    """Convert leading ``B. Foo`` or ``D.a. Foo`` labels into ``Section B — Foo`` for RST table cells."""
    s = (label or "").strip()
    s = re.sub(r"\s+—\s+[a-z]\.\s+", ": ", s)
    return re.sub(r"^([A-Z](?:\.[a-z])?)\.\s+", r"Section \1 — ", s)


def _picture_block_lines(filename: str, alt: str, caption: str) -> list[str]:
    """Return a formatted ``.. picture::`` RST directive block."""
    return [
        f".. picture:: {filename}",
        f"   :alt: {alt}",
        f"   :caption: {caption}",
        "",
    ]


def _write_transcribed_sections(
    chapter_slug: str,
    sections: list[CodexSection],
    unit_dir: Path,
    chap_res_dir: Path,
    notes_by_folio: dict[str, str],
    folio_to_anchor: dict[str, str],
    hero_registry: HeroFigureRegistry,
    continuation_synopses: dict[str, SectionSynopsis] | None = None,
) -> dict[str, int]:
    """Write transcribed section ``index.rst`` pages (with hero SVGs) and nested leaf/locus items."""
    total_items = 0
    total_svgs = 0
    total_pngs = 0

    for sec in sections:
        sec_dir = unit_dir / sec.slug
        sec_dir.mkdir(parents=True, exist_ok=True)

        hero_file, hero_caption, hero_alt = hero_registry.write_section_hero(
            chapter_slug, sec.slug, sec.code, sec_dir
        )

        sec_folios: list[tuple[str, str]] = []
        seen_f: set[str] = set()
        for blk in sec.intro_blocks:
            for fp in blk.folios:
                if fp[0] not in seen_f:
                    seen_f.add(fp[0])
                    sec_folios.append(fp)
        for it in sec.items:
            for fp in it.all_folios():
                if fp[0] not in seen_f:
                    seen_f.add(fp[0])
                    sec_folios.append(fp)

        first_fid = sec_folios[0][0] if sec_folios else ""
        first_page = sec_folios[0][1] if sec_folios else ""
        folios_csv = ", ".join(f for f, _ in sec_folios)
        pages_csv = ", ".join(p for _, p in sec_folios)

        sec_lines = [
            ":layout: book",
            ":type: section",
            f":order: {sec.order}",
            f":canonical_id: {sec.canonical_id}",
            f":title: {sec.title}",
            f":folio: {first_fid}",
            f":page: {first_page}",
            f":folios: {folios_csv}",
            f":pages: {pages_csv}",
            f":excerpt: {sec.overview}",
            "",
            f".. _{sec.anchor}:",
            "",
            sec.title,
            "=" * len(sec.title),
            "",
            *_picture_block_lines(hero_file, hero_alt, hero_caption),
        ]
        if sec.intro_blocks:
            sec_lines.append(render_blocks_with_folios(sec.intro_blocks))
            sec_lines.append("")
        else:
            sec_lines.append(sec.overview)
            sec_lines.append("")

        sec_lines.extend([
            ".. collection::",
            "   :type: item",
            "   :sort: order",
            "",
        ])

        cont = (continuation_synopses or {}).get(sec.slug)
        if cont is not None:
            sec_lines.extend([
                "----",
                "",
                "Subsequent Articles Roadmap (§§ 89–110)",
                "---------------------------------------",
                "",
                cont.summary,
                "",
            ])
            for hl in cont.highlights:
                sec_lines.append(f"* {hl}")
            sec_lines.extend([
                "",
                cont.geometor_note,
                "",
            ])

        (sec_dir / "index.rst").write_text("\n".join(sec_lines), encoding="utf-8")

        for item in sec.items:
            stats = _write_codex_item(item, sec_dir, chap_res_dir, notes_by_folio, folio_to_anchor)
            total_items += stats["items"]
            total_svgs += stats["svgs"]
            total_pngs += stats["pngs"]

    return {
        "sections": len(sections),
        "items": total_items,
        "svgs": total_svgs,
        "pngs": total_pngs,
    }


def _write_synopsis_section(
    sec: dict[str, Any],
    order: int,
    chapter: dict[str, Any],
    folios_by_id: dict[str, dict[str, Any]],
    unit_dir: Path,
    folio_to_anchor: dict[str, str],
    hero_registry: HeroFigureRegistry,
) -> None:
    """Write a rich scholarly synopsis, hero ``.euclid-graphic`` SVG, and theorem roadmap for a section."""
    slug = chapter["slug"]
    num = chapter.get("number")
    chap_label = f"Chapter {num}: {chapter['title']}" if num else chapter["title"]
    sec_slug = _section_slug(sec)
    sec_dir = unit_dir / sec_slug
    sec_dir.mkdir(parents=True, exist_ok=True)
    sec_anchor = f"{slug}-{sec_slug}"

    code = str(sec.get("code", "")).strip()
    sec_title = _format_section_title(sec)
    hero_file, hero_caption, hero_alt = hero_registry.write_section_hero(slug, sec_slug, code, sec_dir)

    art = sec.get("articles")
    art_rubric = f"Articles §§ {art[0]}–{art[1]}" if isinstance(art, list) and len(art) == 2 else "Archival Apparatus"
    f_start, f_end = sec["folio_start"], sec["folio_end"]
    p_start, p_end = sec["page_start"], sec["page_end"]
    f_span_raw = f_start if f_start == f_end else f"{f_start}–{f_end}"
    p_span_raw = p_start if p_start == p_end else f"{p_start}–{p_end}"

    for n in range(int(f_start), int(f_end) + 1):
        fid = f"{n:04d}"
        if fid in folios_by_id:
            folio_to_anchor.setdefault(fid, sec_anchor)

    syn = SECTION_SYNOPSES[(slug, code)]
    plain_excerpt = re.sub(r":[a-z]+:`([^`<]+)(?:\s*<[^>]+>)?`", r"\1", syn.summary)
    plain_excerpt = re.sub(r"[*`\\]", "", plain_excerpt).strip()

    sec_lines = [
        ":layout: book",
        ":type: section",
        f":order: {order}",
        f":title: {sec_title}",
        f":folio: {f_start}",
        f":page: {p_start}",
        f":folios: {f_span_raw}",
        f":pages: {p_span_raw}",
        f":excerpt: {plain_excerpt}",
        "",
        f".. _{sec_anchor}:",
        "",
        sec_title,
        "=" * len(sec_title),
        "",
        f".. rubric:: {chap_label} • {art_rubric} (Folios {f_span_raw}, pp. {p_span_raw})",
        "",
        *_picture_block_lines(hero_file, hero_alt, hero_caption),
        syn.summary,
        "",
        "Principal Theorems, Constructions & Identities",
        "----------------------------------------------",
        "",
    ]
    for hl in syn.highlights:
        sec_lines.append(f"* {hl}")

    sec_lines.extend([
        "",
        "Constructive & Symbolic Connections",
        "-----------------------------------",
        "",
        syn.geometor_note,
        "",
        "----",
        "",
        f"See :ref:`Commentary on {chap_label} <{slug}-commentary>` and :ref:`334-Folio Archival Scan Inventory <scan-inventory>`.",
        "",
    ])
    (sec_dir / "index.rst").write_text("\n".join(sec_lines), encoding="utf-8")


def build_chapter_unit(
    chapter: dict[str, Any],
    chapter_folios: list[dict[str, Any]],
    volume_dir: Path,
    book_doc_dir: Path,
    folio_to_anchor: dict[str, str],
    hero_registry: HeroFigureRegistry,
) -> dict[str, Any]:
    """Build ``<slug>/index.rst``, ``<slug>/commentary.rst``, and nested section/item collections."""
    slug = chapter["slug"]
    chap_dir = volume_dir / chapter["dir"]
    unit_dir = book_doc_dir / slug
    unit_dir.mkdir(parents=True, exist_ok=True)

    num = chapter.get("number")
    display_title = f"Chapter {num}: {chapter['title']}" if num else chapter["title"]
    subtitle = chapter.get("subtitle", "")
    folio_span = f"{chapter['folio_start']}–{chapter['folio_end']}"
    page_span = f"{chapter['page_start']}–{chapter['page_end']}"

    hero_key = CHAPTER_HERO_KEYS.get(slug, "euler_feuerbach")
    chap_hero_file, chap_hero_caption, chap_hero_alt = hero_registry.write_symbolic_hero(hero_key, unit_dir)

    transcribed_entries: list[tuple[str, str, dict[str, str], str]] = []
    notes_by_folio: dict[str, str] = {}

    for f_entry in chapter_folios:
        fid = f_entry["folio"]
        rst_path = chap_dir / f"{fid}.rst"
        notes_path = chap_dir / f"{fid}.notes.rst"
        if rst_path.is_file():
            meta, body = parse_folio_rst(rst_path)
            transcribed_entries.append((fid, str(f_entry["printed_page"]), meta, body))
        if notes_path.is_file():
            notes_by_folio[fid] = notes_path.read_text(encoding="utf-8").strip()

    collection_child_type = "item" if chapter["index"] == 0 else "section"
    overview_para = CHAPTER_OVERVIEWS.get(slug, subtitle)

    idx_lines: list[str] = [
        ":layout: book",
        ":type: chapter",
        f":order: {chapter['index']}",
        f":title: {display_title}",
        f":folio: {chapter['folio_start']}",
        f":page: {chapter['page_start']}",
        f":folios: {folio_span}",
        f":pages: {page_span}",
        "",
        f".. _{slug}:",
        f".. _{slug}-en:",
        "",
        display_title,
        "=" * len(display_title),
        "",
    ]
    if subtitle:
        idx_lines.extend([f".. rubric:: {subtitle}", ""])

    idx_lines.extend([
        *_picture_block_lines(chap_hero_file, chap_hero_alt, chap_hero_caption),
        overview_para,
        "",
        ".. collection::",
        f"   :type: {collection_child_type}",
        "   :sort: order",
        "",
        "----",
        "",
        f"See :ref:`Commentary on {display_title} <{slug}-commentary>`.",
        "",
        ".. toctree::",
        "   :hidden:",
        "",
        "   commentary",
        "",
    ])
    (unit_dir / "index.rst").write_text("\n".join(idx_lines), encoding="utf-8")

    sections_compiled = 0
    items_compiled = 0
    copied_svgs = 0
    copied_graphics = 0
    frontmatter_items: list[CodexItem] = []
    decomposed_sections: list[CodexSection] = []
    folios_by_id = {f["folio"]: f for f in chapter_folios}

    if chapter["index"] == 0:
        frontmatter_items = decompose_frontmatter(transcribed_entries)
        for item in frontmatter_items:
            st = _write_codex_item(item, unit_dir, chap_dir, notes_by_folio, folio_to_anchor)
            items_compiled += st["items"]
            copied_svgs += st["svgs"]
            copied_graphics += st["pngs"]
    elif chapter["index"] in CHAPTER_SECTION_META_BY_INDEX and transcribed_entries:
        chap_prefix, chap_roman, sec_meta_map = CHAPTER_SECTION_META_BY_INDEX[chapter["index"]]
        decomposed_sections = decompose_chapter_folios(
            transcribed_entries, chap_prefix, chap_roman, sec_meta_map
        )
        cont_map = {"c-medians": CH03_MEDIANS_CONTINUATION} if chapter["index"] == 3 else None
        st = _write_transcribed_sections(
            slug,
            decomposed_sections,
            unit_dir,
            chap_dir,
            notes_by_folio,
            folio_to_anchor,
            hero_registry,
            continuation_synopses=cont_map,
        )
        sections_compiled += st["sections"]
        items_compiled += st["items"]
        copied_svgs += st["svgs"]
        copied_graphics += st["pngs"]

        compiled_codes = {s.code for s in decomposed_sections}
        for order, sec in enumerate(chapter.get("sections") or [], start=1):
            if str(sec.get("code", "")).strip() not in compiled_codes:
                _write_synopsis_section(
                    sec, order, chapter, folios_by_id, unit_dir, folio_to_anchor, hero_registry
                )
                sections_compiled += 1
    else:
        for order, sec in enumerate(chapter.get("sections") or [], start=1):
            _write_synopsis_section(
                sec, order, chapter, folios_by_id, unit_dir, folio_to_anchor, hero_registry
            )
            sections_compiled += 1

    for f_entry in chapter_folios:
        folio_to_anchor.setdefault(f_entry["folio"], slug)

    # Chapter-level commentary.rst
    comm_title = f"Commentary on {display_title}"
    comm_lines: list[str] = [
        ":layout: book",
        ":type: commentary",
        f":title: {comm_title}",
        f":folio: {chapter['folio_start']}",
        f":page: {chapter['page_start']}",
        f":folios: {folio_span}",
        f":pages: {page_span}",
        "",
        f".. _{slug}-commentary:",
        "",
        comm_title,
        "=" * len(comm_title),
        "",
        f"Back to :ref:`{display_title} <{slug}>`.",
        "",
        f".. rubric:: Constructive Analysis, Historical Provenance & GEOMETOR Notes ({folio_span}, pp. {page_span})",
        "",
    ]

    if slug == "frontmatter":
        comm_lines.extend([
            "Editorial Overview of the Frontmatter (``0001``–``0019``)",
            "---------------------------------------------------------",
            "",
            "The nineteen frontmatter folios of :person:`Nathan Altshiller-Court's <altshiller-court>` :cite:`College Geometry (1952 / Dover 2007) <court:1952>` frame both the historical triumph of synthetic geometry in twentieth-century American higher education and the pedagogical discipline required to master geometric problem solving:",
            "",
            "* **From 1925 to 1952 (Preface, pp. vii–viii)**: Between the :cite:`1925 Johnson Publishing first edition <court:1925>` and the :cite:`1952 Barnes & Noble second edition <court:1952>`, college geometry evolved from an experimental elective into a staple course for mathematics majors and prospective teachers. Altshiller-Court rewrote the entire treatise, inserted Chapter IV (*The Quadrilateral*), expanded Chapter X (*Recent Geometry of the Triangle*), and moved :term:`harmonic division <harmonic-division>` forward into Chapter III.",
            "* **Pagination Offset Contract**: Folios ``0001``–``0019`` carry cover and Roman numerals ``[iii]``–``[xx]`` (including blank versos ``0005``, ``0009``, ``0015``, ``0019``), establishing the exact body formula ``PDF Folio = Printed Arabic Page + 19`` from Folio ``0020`` (p. ``1``) to Folio ``0332`` (p. ``313``).",
            "* **Problem-Solving Heuristic (To the Student, pp. xvii–xix)**: Altshiller-Court's insistence on maintaining bidirectional marginal links to :cite:`Euclid's Elements <euclid:elements>`, memorizing exact definitions and theorems as active deductive tools, restating problems from memory, and sketching diagnostic figures directly motivates the GEOMETOR Digital Scriptorium.",
            "",
            "Item-by-Item Diplomatic Notes",
            "-----------------------------",
            "",
        ])
        for item in frontmatter_items:
            comm_lines.append(f"* :ref:`Commentary on {item.title} <{item.anchor}-commentary>`")
        comm_lines.append("")
    elif slug == "ch01-geometric-constructions":
        comm_lines.extend([
            "Constructive Architecture & Symbolic Modeling (§§ 1–22)",
            "-------------------------------------------------------",
            "",
            "Chapter I lays down the operational grammar of the entire book across 33 verified folios (``0020``–``0052``, pp. ``1``–``33``), 22 interactive ``.euclid-graphic`` diagrams (``Figs. 1–22``), and 167 exercises. Every ruler-and-compass construction is governed by :person:`Pappus' <pappus>` four-stage :term:`analytic method <analytic-method>` (:cite:`Collection, Book VII <pappus:collection:VII>`):",
            "",
            "1. :term:`Analysis <analysis-step>` — Assume the required configuration already exists and trace algebraic/synthetic incidences back to known data.",
            "2. :term:`Construction <construction-step>` — Execute elementary straightedge (``line(P, Q)``) and compass (``circle(A, r)``) steps in forward topological order.",
            "3. :term:`Proof <proof-step>` — Verify deductively that the constructed object satisfies every hypothesis.",
            "4. :term:`Discussion <discussion-step>` (*Diorismos*) — Determine exact existence inequalities (``s < 2 OE``, ``a < b + c``, ``a > b - c``), count multiplicity of solutions (``0, 1, 2, 3, 4, 6``, or :math:`\\infty`), and identify poristic degeneracies (as in :ref:`§ 9 <ch01-art-009>` when :math:`AC \\perp BD` and :math:`AC = BD`).",
            "",
            "Mapping Chapter I to ``geometor.model`` & ``geometor.elements``",
            "---------------------------------------------------------------",
            "",
            "* **Symbolic DAG Representation**: Altshiller-Court's :ref:`§ 1 <ch01-art-001>` notation—circles :math:`(A, r)` and line intersections :math:`M = (PQ, RS)`—maps one-to-one onto ``geometor.model`` primitives, where every constructed point retains its exact SymPy algebraic coordinates in a quadratic extension tower of :math:`\\mathbb{Q}`.",
            "* **The Twelve Fundamental Loci (:ref:`§ 11 <ch01-art-011>`, Folios ``0030``–``0036``)**:",
            "  - *Linear Loci*: Parallel pair (:ref:`Locus 3 <ch01-locus-03>`), :term:`mediator <mediator>` (:ref:`Locus 4 <ch01-locus-04>`, :cite:`Euclid I.10–11 <euclid:elements>`), angle bisectors (:ref:`Locus 5 <ch01-locus-05>`), and constant difference of squares :math:`AM^2 - BM^2 = d^2` (:ref:`Locus 12 <ch01-locus-12>` — point-circle precursor of the :term:`radical axis <radical-axis>` in Chapter VIII, § 422).",
            "  - *Circular Loci*: Circle :math:`(A, r)` (:ref:`Locus 1 <ch01-locus-01>`), concentric tangent-length & subtended-angle circles (:ref:`Loci 2 <ch01-locus-02>`, :ref:`6 <ch01-locus-06>`, :ref:`9 <ch01-locus-09>`), :term:`capable arc <subtended-angle-locus>` & Thales' circle (:ref:`Locus 7 <ch01-locus-07>`, :cite:`Euclid III.21, III.31 <euclid:elements>`), chord-midpoint circle on :math:`OP` (:ref:`Locus 8 <ch01-locus-08>`), Apollonius' median circle :math:`OM^2 = \\tfrac{1}{2}s^2 - a^2` (:ref:`Locus 10 <ch01-locus-10>`), and the :term:`Apollonian circle <apollonian-circle>` :math:`AM : MB = p : q` (:ref:`Locus 11 <ch01-locus-11>`, :person:`Apollonius <apollonius>`).",
            "* **Indirect Elements & Auxiliary Triangles (:ref:`Section D <ch01-d-indirect-elements>`, §§ 15–22)**: Unfolding perimeter :math:`2p` into :math:`\\triangle AEF` (:ref:`§ 15 <ch01-art-015>`), side sums :math:`b + c` into :math:`\\triangle BCD` (:ref:`§ 17 <ch01-art-017>`), side differences :math:`b - c` into :math:`\\triangle BCD` and :math:`\\triangle BCE` (:ref:`§ 18 <ch01-art-018>`, :ref:`§ 19 <ch01-art-019>`), and altitude sums/differences :math:`h_b \\pm h_c` into right triangles :math:`\\triangle BGH` and :math:`\\triangle CGH` (:ref:`§ 20 <ch01-art-020>`, :ref:`§ 22 <ch01-art-022>`), formalizing two-element :term:`data <datum>` (:ref:`§ 21 <ch01-art-021>`).",
            "",
            "Section & Item Commentary Index",
            "-------------------------------",
            "",
        ])
        for sec in decomposed_sections:
            comm_lines.append(f"* :ref:`{sec.title} <{sec.anchor}>`")
            for item in sec.items:
                comm_lines.append(f"  - :ref:`Commentary on {item.title} <{item.anchor}-commentary>`")
        comm_lines.append("")
    else:
        comm_lines.append(CHAPTER_COMMENTARY.get(slug, ""))
        comm_lines.append("")
        if decomposed_sections:
            comm_lines.extend([
                "Transcribed Section & Item Commentary Index",
                "-------------------------------------------",
                "",
            ])
            for sec in decomposed_sections:
                comm_lines.append(f"* :ref:`{sec.title} <{sec.anchor}>`")
                for item in sec.items:
                    comm_lines.append(f"  - :ref:`Commentary on {item.title} <{item.anchor}-commentary>`")
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

    (unit_dir / "commentary.rst").write_text("\n".join(comm_lines), encoding="utf-8")

    return {
        "slug": slug,
        "display_title": display_title,
        "transcribed_count": len(transcribed_entries),
        "total_folios": len(chapter_folios),
        "sections_compiled": sections_compiled,
        "items_compiled": items_compiled,
        "copied_graphics": copied_graphics,
        "copied_svgs": copied_svgs,
    }


def _format_occurrences_line(
    occurrences: list[dict[str, Any]],
    folio_to_anchor: dict[str, str],
    chapter_dir_to_slug: dict[str, str],
) -> str:
    """Format occurrence back-links to exact leaf item or section pages."""
    if not occurrences:
        return ""
    seen: set[tuple[str, str]] = set()
    parts: list[str] = []
    for occ in occurrences:
        folio = occ.get("folio", "")
        page = occ.get("page", "")
        sec = occ.get("section", "")
        target = folio_to_anchor.get(folio) or chapter_dir_to_slug.get(sec)
        key = (folio, target or "")
        if key in seen:
            continue
        seen.add(key)
        if target:
            parts.append(f":ref:`f. {folio} (p. {page}) <{target}>`")
        else:
            parts.append(f"f. ``{folio}`` (p. {page})")
    return " · ".join(parts)


def build_apparatus_pages(
    volume_dir: Path,
    book_doc_dir: Path,
    structure: dict[str, Any],
    folio_to_anchor: dict[str, str],
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
        ":navigation: header",
        ":order: 6",
        ":nav_title: Bibliography",
        ":layout: book",
        ":title: Systematic Bibliography",
        "",
        ".. _bibliography:",
        "",
        "Bibliography",
        "============",
        "",
        f".. rubric:: {len(citations)} Editions, Classical Treatises, and Mathematical Periodicals Cited in *College Geometry*",
        "",
        "Every ``:cite:`` reference in the Book Codex resolves to its canonical bibliographic anchor below.",
        "",
    ]
    for ck, entry in sorted(citations.items()):
        c_slug = apparatus_slug(ck)
        occ_str = _format_occurrences_line(
            entry.get("occurrences", []), folio_to_anchor, chapter_dir_to_slug
        )
        author_key = entry.get("author_key", "")
        author_disp = entry.get("author", "")
        if author_key and author_key in persons:
            author_ref = f":person:`{author_disp} <{author_key}>`"
        else:
            author_ref = f"**{author_disp}**"
        heading = f"``[{ck}]`` — {entry.get('work', '')}"
        bib_lines.extend([
            f".. _cite-{c_slug}:",
            "",
            heading,
            "-" * len(heading),
            "",
            f"* **Author / Editor**: {author_ref}",
            f"* **Locus / Key**: {entry.get('locus', '—')}",
        ])
        if occ_str:
            bib_lines.append(f"* **Referenced At**: {occ_str}")
        bib_lines.append("")

    (book_doc_dir / "bibliography.rst").write_text("\n".join(bib_lines), encoding="utf-8")

    # 2. people/index.rst + people/<slug>.rst
    people_dir = book_doc_dir / "people"
    people_dir.mkdir(parents=True, exist_ok=True)
    stale_persons = book_doc_dir / "persons.rst"
    if stale_persons.exists():
        stale_persons.unlink()

    people_index_lines = [
        ":navigation: header",
        ":order: 5",
        ":nav_title: People",
        ":layout: book",
        ":title: People",
        "",
        ".. _persons:",
        "",
        "People",
        "======",
        "",
        f".. rubric:: Biographical Register of Geometers, Translators, and Scholars ({len(persons)} Historical Figures)",
        "",
        "Synthesizes Altshiller-Court's *List of Names* (pp. 307–309), *Historical and Bibliographical Notes* (pp. 295–306), and Frontmatter acknowledgments.",
        "",
        ".. people-directory::",
        "   :sort: death_year",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :hidden:",
        "   :glob:",
        "",
        "   *",
        "",
    ]
    (people_dir / "index.rst").write_text("\n".join(people_index_lines), encoding="utf-8")

    for pk, entry in sorted(persons.items(), key=lambda kv: kv[1].get("name", kv[0]).lower()):
        p_slug = apparatus_slug(pk)
        name = entry.get("name", pk)
        dates = entry.get("dates", "")
        arts = entry.get("articles") or []
        arts_str = ", ".join(f"§ {a}" for a in arts) if arts else "Frontmatter / Apparatus"
        works = entry.get("works") or []
        occ_str = _format_occurrences_line(
            entry.get("occurrences", []), folio_to_anchor, chapter_dir_to_slug
        )
        rec_lines = [
            ":type: person",
            ":layout: book",
            f":title: {name}",
        ]
        if dates:
            rec_lines.append(f":lifespan: {dates}")
        rec_lines.extend([
            "",
            f".. _person-{p_slug}:",
            "",
            name,
            "=" * len(name),
            "",
        ])
        if dates:
            rec_lines.append(f"*{dates}*")
            rec_lines.append("")
        rec_lines.extend([
            f"* **Role**: {entry.get('role', '')}",
            f"* **Articles in College Geometry**: {arts_str}",
        ])
        if works:
            rec_lines.append("* **Principal Works**: " + "; ".join(f"*{w}*" for w in works))
        if occ_str:
            rec_lines.append(f"* **Edition Loci**: {occ_str}")
        rec_lines.extend([
            "",
            entry.get("bio", ""),
            "",
        ])
        (people_dir / f"{p_slug}.rst").write_text("\n".join(rec_lines), encoding="utf-8")

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
        f".. rubric:: {len(glossary)} Constructive Methods, Loci, Data, Triangle Centers, Circles, and Projective/Conformal Transformations",
        "",
    ]
    for tk, entry in sorted(glossary.items(), key=lambda kv: kv[1].get("headword", kv[0]).lower()):
        t_slug = apparatus_slug(tk)
        head = entry.get("headword", tk)
        occ_str = _format_occurrences_line(
            entry.get("occurrences", []), folio_to_anchor, chapter_dir_to_slug
        )
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
        "   :widths: 10 10 24 26 14 16",
        "",
        "   * - Folio",
        "     - Page",
        "     - Codex Locus",
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
        svg_count = 0
        if json_path.is_file():
            g_list = json.loads(json_path.read_text(encoding="utf-8")).get("graphics", [])
            diag_count = len(g_list)
            svg_count = sum(
                1 for g in g_list if g.get("svg_file") and (volume_dir / cdir / g["svg_file"]).is_file()
            )
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
        arts_str = f" (§§ {arts[0]}–{arts[-1]})" if len(arts) > 1 else (f" (§ {arts[0]})" if len(arts) == 1 else "")
        sec_label = f_entry.get("section") or f_entry.get("section_code") or ""
        sec_disp = f"{sec_label}{arts_str}".strip() or "—"
        if svg_count:
            diag_disp = f"{svg_count} SVG + crop(s)"
        elif diag_count:
            diag_disp = f"{diag_count} crop(s)"
        else:
            diag_disp = "—"

        anchor = folio_to_anchor.get(fid)
        locus_disp = f":ref:`{fid} <{anchor}>`" if anchor else f"``{fid}``"

        inv_lines.extend([
            f"   * - {locus_disp}",
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
    apparatus_counts: dict[str, int],
    book_doc_dir: Path,
) -> None:
    """Write ``docsrc/college_geometry/index.rst`` Book Codex master landing page."""
    work = structure["work"]
    lines = [
        ":navigation: header",
        ":order: 1",
        ":nav_title: College Geometry",
        ":layout: book",
        ":type: book",
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
        "College Geometry",
        "================",
        "",
        f".. rubric:: {work['subtitle']} ({work['original_year']} / Dover {work['reprint_year']})",
        "",
        ".. container:: title-page",
        "",
        "   | :person:`Nathan Altshiller-Court <altshiller-court>` (1881–1968)",
        "   | *Professor of Mathematics, University of Oklahoma*",
        "   | *Second Edition, Revised and Enlarged* — Barnes & Noble, Inc., New York, 1952",
        "   | *Unabridged Dover Republication* — Dover Publications, Inc., Mineola, N.Y., 2007 (ISBN ``978-0-486-45805-2``)",
        "",
        "----",
        "",
        "Table of Contents",
        "-----------------",
        "",
        (
            "Published as a hierarchical **Book Codex** (``Book → Chapters → Sections → Items``) with "
            "one article, problem, locus, or exercise set per page, inline ``.euclid-graphic`` interactive "
            "diagrams, marginal ``.. folio::`` milestones, and companion **Commentary** tracks."
        ),
        "",
        ".. collection::",
        "   :type: chapter",
        "   :sort: order",
        "",
        "Scholarly Apparatus",
        "-------------------",
        "",
        f"* :ref:`Systematic Bibliography & Periodical Key ({apparatus_counts['citations']} Entries) <bibliography>`",
        f"* :ref:`Biographical Register of Geometers & Scholars ({apparatus_counts['persons']} Persons) <persons>`",
        f"* :ref:`Technical Glossary of Synthetic Geometry ({apparatus_counts['glossary']} Terms) <glossary>`",
        f"* :ref:`334-Folio Archival Scan & Transcription Inventory ({apparatus_counts['verified']} Verified) <scan-inventory>`",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :hidden:",
        "   :caption: Scholarly Apparatus",
        "",
        "   bibliography",
        "   people/index",
        "   glossary",
        "   scan-inventory",
        "",
    ]

    (book_doc_dir / "index.rst").write_text("\n".join(lines), encoding="utf-8")


def compile_edition(repo_root: Path) -> dict[str, Any]:
    """Compile the complete *College Geometry* Book Codex into ``docsrc/college_geometry/``."""
    volume_dir = repo_root / "resources" / "college_geometry"
    book_doc_dir = repo_root / "docsrc" / "college_geometry"
    book_doc_dir.mkdir(parents=True, exist_ok=True)

    # Remove stale subdirectories or legacy monolithic files before regenerating
    for existing in list(book_doc_dir.iterdir()):
        if existing.is_dir():
            shutil.rmtree(existing)
        elif existing.is_file() and existing.suffix == ".rst":
            existing.unlink()

    svg_info = compile_all_svgs(volume_dir)

    structure: dict[str, Any] = json.loads(
        (volume_dir / "structure_map.json").read_text(encoding="utf-8")
    )
    folios_by_dir: dict[str, list[dict[str, Any]]] = {}
    for f_entry in structure["folios"]:
        folios_by_dir.setdefault(f_entry["chapter_dir"], []).append(f_entry)

    hero_registry = HeroFigureRegistry(volume_dir)
    folio_to_anchor: dict[str, str] = {}
    unit_summaries: list[dict[str, Any]] = []
    for ch in structure["chapters"]:
        c_folios = folios_by_dir.get(ch["dir"], [])
        summary = build_chapter_unit(
            ch, c_folios, volume_dir, book_doc_dir, folio_to_anchor, hero_registry
        )
        unit_summaries.append(summary)

    apparatus_counts = build_apparatus_pages(volume_dir, book_doc_dir, structure, folio_to_anchor)
    build_book_index(structure, apparatus_counts, book_doc_dir)

    return {
        "units_compiled": len(unit_summaries),
        "sections_compiled": sum(u["sections_compiled"] for u in unit_summaries),
        "items_compiled": sum(u["items_compiled"] for u in unit_summaries),
        "transcribed_folios": sum(u["transcribed_count"] for u in unit_summaries),
        "total_folios": apparatus_counts["folios"],
        "verified_folios": apparatus_counts["verified"],
        "svgs_compiled": svg_info["svgs_compiled"],
        "svgs_copied": sum(u["copied_svgs"] for u in unit_summaries),
        "graphics_copied": sum(u["copied_graphics"] for u in unit_summaries),
        "apparatus": apparatus_counts,
    }


def get_edition_status(repo_root: Path) -> dict[str, Any]:
    """Return a diagnostic summary of ingested scans, transcriptions, graphics, SVGs, and reviews."""
    volume_dir = repo_root / "resources" / "college_geometry"
    structure = json.loads((volume_dir / "structure_map.json").read_text(encoding="utf-8"))
    reviews_path = volume_dir / "folio_reviews.json"
    reviews = json.loads(reviews_path.read_text(encoding="utf-8")) if reviews_path.is_file() else {}

    png_count = 0
    rst_count = 0
    notes_count = 0
    json_count = 0
    crop_count = 0
    svg_count = 0

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
                if g.get("svg_file") and (cdir / g["svg_file"]).is_file():
                    svg_count += 1

    return {
        "total_folios": len(structure["folios"]),
        "scans_present": png_count,
        "rst_transcribed": rst_count,
        "notes_present": notes_count,
        "folios_with_graphics": json_count,
        "diagram_crops": crop_count,
        "svg_diagrams": svg_count,
        "verified_reviews": sum(1 for r in reviews.values() if r.get("status") == "verified"),
    }
