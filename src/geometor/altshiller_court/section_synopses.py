"""Scholarly section synopses and theorem roadmaps for *College Geometry* (1952).

Provides mathematically substantive section introductions, article-keyed theorem
and construction roadmaps, LaTeX identities, prosopographical/bibliographic links,
and GEOMETOR cross-references for sections across Chapters II–X, Historical Notes,
and the Subject Index.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SectionSynopsis:
    """Structured scholarly synopsis and theorem roadmap for a Book Codex section."""

    summary: str
    highlights: tuple[str, ...]
    geometor_note: str


# Continuation roadmap appended beneath transcribed §§ 87–88 on Chapter III Section C (Medians)
CH03_MEDIANS_CONTINUATION = SectionSynopsis(
    summary=(
        "Following the midline theorem (:ref:`§ 87 <ch03-art-087>`) and concurrency of the three medians "
        "at the :term:`centroid <centroid>` :math:`G = X(2)` (:ref:`§ 88 <ch03-art-088>`), Section C "
        "continues across Folios ``0085``–``0090`` (pp. ``66``–``71``, **§§ 89–110**) to develop the "
        "homothetic pair of the :term:`complementary <complementary-triangle>` and "
        ":term:`anticomplementary <anticomplementary-triangle>` triangles and the metric laws of medians."
    ),
    highlights=(
        ("**§§ 89–95 — Complementary & Anticomplementary Triangles**: The midpoint triangle :math:`A'B'C'` "
        "(:term:`complementary triangle <complementary-triangle>`) and parallel-through-vertices triangle "
        "(:term:`anticomplementary triangle <anticomplementary-triangle>`) correspond to :math:`\\triangle ABC` "
        "under :term:`homothecies <homothecy>` :math:`\\mathcal{H}(G, -\\tfrac{1}{2})` and :math:`\\mathcal{H}(G, -2)`."),
        ("**§§ 96–102 — Triangle of Medians & Area Ratio**: Segments parallel and equal to the three medians "
        ":math:`m_a, m_b, m_c` form a triangle whose area is :math:`\\tfrac{3}{4}` the area of :math:`\\triangle ABC`, "
        "yielding immediate ruler-and-compass constructions from :math:`(m_a, m_b, m_c)`."),
        ("**§§ 103–110 — Apollonius' Median Theorem & Leibniz Sum**: Establishes :person:`Apollonius' <apollonius>` "
        "identity :math:`b^2 + c^2 = 2m_a^2 + \\tfrac{1}{2}a^2`, the sum of squares :math:`m_a^2 + m_b^2 + m_c^2 = "
        "\\tfrac{3}{4}(a^2 + b^2 + c^2)`, and :math:`PA^2 + PB^2 + PC^2 = GA^2 + GB^2 + GC^2 + 3PG^2`."),
    ),
    geometor_note=(
        "In ``geometor/etc`` and ``geometor/model``, the centroid :math:`G = X(2) = \\tfrac{1}{3}(A + B + C)` "
        "has exact rational coordinates over :math:`\\mathbb{Q}(A, B, C)` and anchors the :math:`-2 : 1` "
        "homothecy driving the :term:`Euler line <euler-line>` and :term:`nine-point circle <nine-point-circle>`."
    ),
)


SECTION_SYNOPSES: dict[tuple[str, str], SectionSynopsis] = {
    # ------------------------------------------------------------------
    # Chapter II — Similitude and Homothecy (§§ 23–53)
    # ------------------------------------------------------------------
    ("ch02-similitude-and-homothecy", "A"): SectionSynopsis(
        summary=(
            "Introduces the constructive :term:`method of similitude <similitude>` (**§§ 23–30**): when all "
            "conditions save one linear dimension determine the shape (*species*) of a figure, a convenient "
            "similar prototype is constructed first and then scaled to satisfy the remaining boundary or "
            "metric condition (:cite:`Euclid VI <euclid:elements>`)."
        ),
        highlights=(
            ("**§§ 23–25 — Principle of Auxiliary Similar Prototypes**: Suppressing one linear datum converts "
            "a rigid placement problem into a one-parameter family of similar figures sharing fixed angular "
            "and ratio invariants."),
            ("**§§ 26–28 — Inscribed Squares & Given-Shape Triangles**: Classic constructions inscribing a "
            "square in a given triangle :math:`ABC` and inscribing a triangle of given angles or side ratios "
            "inside another triangle or circle."),
            ("**§§ 29–30 — Ratio-of-Distances Loci & Exercises**: Reduces linear combinations of distances from "
            "two intersecting lines to straight-line loci passing through their vertex."),
        ),
        geometor_note=(
            "Models scaling transformations in ``geometor/fundamentals`` and ``geometor/elements`` Book VI, "
            "where rational scale factors preserve exact algebraic field membership."
        ),
    ),
    ("ch02-similitude-and-homothecy", "B"): SectionSynopsis(
        summary=(
            "Develops central dilation or :term:`homothecy <homothecy>` :math:`\\mathcal{H}(S, k)` (**§§ 31–53**) "
            "as a point-to-point geometric transformation preserving parallelism, angles, and ratio of lengths, "
            "culminating in the :term:`centers of similitude <centers-of-similitude>` and circle of similitude "
            "of two circles."
        ),
        highlights=(
            ("**§§ 31–38 — Homothetic Figures & Homothetic Center**: Homologous segments are parallel and "
            "proportional (:math:`S P' / S P = k`); any two unequal parallel segments or circles are both "
            "directly (:math:`k > 0`) and inversely (:math:`k < 0`) homothetic."),
            ("**§§ 39–45 — Direct & Inverse Centers of Similitude of Two Circles**: Two unequal circles "
            ":math:`(O, R)` and :math:`(O', R')` possess external and internal centers of similitude :math:`S, S'` "
            "dividing :math:`OO'` :term:`harmonically <harmonic-division>` in ratio :math:`R : R'`, through which "
            "common tangents and antihomologous secants pass."),
            ("**§§ 46–53 — Circle of Similitude & The Pantograph**: Proves that the locus of points from which "
            "two unequal circles subtend equal angles is the :term:`Apollonian circle <apollonian-circle>` on "
            "diameter :math:`SS'`, and analyzes Scheiner's mechanical pantograph linkage."),
        ),
        geometor_note=(
            "Applied to a triangle's circumcircle and incircle in ``geometor/etc``, the internal and external "
            "similicenters yield Kimberling centers :math:`X(55)` and :math:`X(56)`."
        ),
    ),
    # ------------------------------------------------------------------
    # Chapter III — Properties of the Triangle (§§ 111–239)
    # ------------------------------------------------------------------
    ("ch03-properties-of-the-triangle", "D.a"): SectionSynopsis(
        summary=(
            "Opens the theory of the four :term:`tritangent circles <tritangent-circles>` (**§§ 111–116**) by "
            "establishing the harmonic, metric, and circumcircle-midpoint properties of the internal and "
            "external angle bisectors of :math:`\\triangle ABC`."
        ),
        highlights=(
            ("**§§ 111–113 — Harmonic Bisector Traces**: The internal and external bisectors of :math:`\\angle A` "
            "are perpendicular and divide the opposite side :math:`BC` :term:`harmonically <harmonic-division>` "
            "in the ratio :math:`c : b` (:cite:`Euclid VI.3 <euclid:elements>`)."),
            ("**§§ 114–115 — Circumcircle Arc Midpoints**: The internal and external bisectors of :math:`\\angle A` "
            "pass through the diametrically opposite midpoints of the arcs :math:`BC` on the "
            ":term:`circumcircle <circumcircle>`."),
            ("**§ 116 — Bisector Length Formula**: Expresses the internal bisector length via :math:`t_a^2 = "
            "bc - DB \\cdot DC = bc\\bigl(1 - \\frac{a^2}{(b+c)^2}\\bigr)`."),
        ),
        geometor_note=(
            "Connects angle-bisector harmonic ranges directly to the :term:`Apollonian circles <apollonian-circle>` "
            "of the triangle studied in Chapter X (§§ 597–624)."
        ),
    ),
    ("ch03-properties-of-the-triangle", "D.b"): SectionSynopsis(
        summary=(
            "Establishes the concurrency of the internal and external angle bisectors at the :term:`incenter <incircle>` "
            ":math:`I = X(1)` and the three excenters :math:`I_a, I_b, I_c` (**§§ 117–130**), revealing their "
            "orthocentric duality with :math:`\\triangle ABC`."
        ),
        highlights=(
            ("**§§ 117–121 — Existence of the Four Tritangent Centers**: Three internal bisectors concur at "
            ":math:`I`, while each internal bisector concurs with two external bisectors at :math:`I_a, I_b, I_c`, "
            "forming an :term:`orthocentric group <orthocentric-quadrilateral>` for which :math:`\\triangle ABC` is "
            "the :term:`orthic triangle <orthic-triangle>`!"),
            ("**§§ 122–126 — Trident (Incenter–Excenter) Lemma**: If the bisector :math:`AII_a` meets the "
            "circumcircle at :math:`M`, then :math:`M` is the midpoint of :math:`II_a` and :math:`MB = MC = MI = MI_a`."),
            ("**§§ 127–130 — Circumcircle of the Excentral Triangle**: Shows that the circumcircle of "
            ":math:`\\triangle I_a I_b I_c` has radius :math:`2R` and is centered at the reflection of :math:`I` "
            "across the circumcenter :math:`O` (:math:`X(40)`, the Bevan point)."),
        ),
        geometor_note=(
            "Demonstrates in ``geometor/etc`` how the map :math:`\\triangle I_a I_b I_c \\mapsto \\triangle ABC` "
            "interchanges excentral/orthic invariants, sending orthocenter to incenter :math:`X(1)` and "
            "nine-point circle to circumcircle."
        ),
    ),
    ("ch03-properties-of-the-triangle", "D.c"): SectionSynopsis(
        summary=(
            "Derives the classic metric relations linking the inradius :math:`r`, exradii :math:`r_a, r_b, r_c`, "
            "circumradius :math:`R`, semiperimeter :math:`s`, and area :math:`S` (**§§ 131–155**), highlighted by "
            ":person:`Carnot's <carnot>` and :person:`Euler's <euler>` theorems."
        ),
        highlights=(
            ("**§§ 131–145 — Area & Reciprocal Radius Identities**: Proves :math:`S = rs = r_a(s - a) = "
            "\\sqrt{r\\,r_a r_b r_c}`, :math:`\\frac{1}{r} = \\frac{1}{r_a} + \\frac{1}{r_b} + \\frac{1}{r_c} = "
            "\\frac{1}{h_a} + \\frac{1}{h_b} + \\frac{1}{h_c}`, and :math:`r_a + r_b + r_c - r = 4R`."),
            ("**§§ 146–149 — Carnot's Theorem**: The signed sum of distances from the circumcenter :math:`O` to "
            "the three sides of :math:`\\triangle ABC` satisfies :math:`d_a + d_b + d_c = R + r` (:person:`Carnot <carnot>`)."),
            ("**§§ 150–155 — Chapple–Euler Distance Theorem**: Proves :math:`OI^2 = R(R - 2r)` and "
            ":math:`OI_a^2 = R(R + 2r_a)` (:person:`Chapple <chapple>` 1746; :cite:`Euler 1765 <euler:1765>`), "
            "yielding Euler's inequality :math:`R \\ge 2r`."),
        ),
        geometor_note=(
            "In ``geometor/wildberger`` and ``geometor/model``, :math:`OI^2 = R(R - 2r)` provides an exact "
            "quadrance certificate and triggers Poncelet's porism for bicentric triangles."
        ),
    ),
    ("ch03-properties-of-the-triangle", "D.d"): SectionSynopsis(
        summary=(
            "Analyzes the twelve contact points where the :term:`incircle <incircle>` and three excircles touch "
            "the sidelines :math:`BC, CA, AB` (**§§ 156–174**), expressing every tangent segment cleanly in "
            "terms of :math:`s, s - a, s - b, s - c`."
        ),
        highlights=(
            ("**§§ 156–163 — Semiperimeter Tangent Segments**: Incircle contacts cut off segments :math:`s - a, "
            "s - b, s - c` from vertices :math:`A, B, C`, whereas the :math:`A`-excircle touches :math:`AB, AC` "
            "produced at distance :math:`s` from :math:`A` and touches :math:`BC` at the :term:`isotomic <isotomic-conjugates>` "
            "reflection of the incircle contact!"),
            ("**§§ 164–170 — Antipodal Incircle–Excircle Property**: If :math:`X` is the contact of :math:`(I)` "
            "with :math:`BC` and :math:`X'` its diametrically opposite point on :math:`(I)`, then :math:`A, X', X_a` "
            "are collinear—anticipating the :term:`Nagel point <nagel-point>` :math:`X(8)`."),
            ("**§§ 171–174 — Contact Constructions & Heron's Formula**: Applies tangent-segment differences "
            ":math:`b - c` and semiperimeter :math:`s` to auxiliary-triangle constructions and :person:`Heron's <heron>` "
            "area formula :math:`S = \\sqrt{s(s-a)(s-b)(s-c)}`."),
        ),
        geometor_note=(
            "Contact Ceva configurations directly generate Kimberling's :term:`Gergonne point <gergonne-point>` "
            ":math:`X(7)` and :term:`Nagel point <nagel-point>` :math:`X(8)` in ``geometor/etc``."
        ),
    ),
    ("ch03-properties-of-the-triangle", "E.a"): SectionSynopsis(
        summary=(
            "Proves the concurrency of the three altitudes of :math:`\\triangle ABC` at the :term:`orthocenter <orthocenter>` "
            ":math:`H = X(4)` (**§§ 175–182**) by embedding :math:`\\triangle ABC` as the complementary triangle of "
            "its :term:`anticomplementary triangle <anticomplementary-triangle>`."
        ),
        highlights=(
            ("**§ 175 — Concurrency via Anticomplementary Mediators**: Parallels through :math:`A, B, C` to the "
            "opposite sides form a triangle whose perpendicular bisectors (:term:`mediators <mediator>`) are "
            "precisely the altitudes of :math:`\\triangle ABC`, proving concurrency in one synthetic step."),
            ("**§§ 176–179 — Circumcircle Reflections of the Orthocenter**: The reflection of :math:`H` across "
            "any side :math:`BC`—and across the midpoint :math:`A'` of :math:`BC`—lies directly on the "
            ":term:`circumcircle <circumcircle>` :math:`(O)`!"),
            ("**§§ 180–182 — Equal-Chord & Power Identities**: Establishes :math:`HA \\cdot HD = HB \\cdot HE = "
            "HC \\cdot HF` and shows that the circumcircles of :math:`\\triangle HBC, \\triangle HCA, \\triangle HAB` "
            "all have radius :math:`R` equal to that of :math:`(ABC)`."),
        ),
        geometor_note=(
            "In ``geometor/model``, :math:`H = X(4)` is constructed over :math:`\\mathbb{Q}(A, B, C)` by pure "
            "linear intersection of two perpendiculars without any square-root extension."
        ),
    ),
    ("ch03-properties-of-the-triangle", "E.b"): SectionSynopsis(
        summary=(
            "Investigates the :term:`orthic (pedal) triangle <orthic-triangle>` :math:`\\triangle DEF` formed by "
            "the feet of the three altitudes (**§§ 183–200**), uncovering its antiparallel sides, optical "
            "reflection law, and :person:`Fagnano's <fagnano>` minimum-perimeter theorem."
        ),
        highlights=(
            ("**§§ 183–189 — Antiparallel Sides & Altitudes as Bisectors**: Cyclic quadrilaterals :math:`BCEF, "
            "CAFD, ABDE` render :math:`EF, FD, DE` antiparallel to :math:`BC, CA, AB`; the altitudes of an acute "
            ":math:`\\triangle ABC` bisect the interior angles of :math:`\\triangle DEF`, making :math:`H` the "
            "incenter of :math:`\\triangle DEF`!"),
            ("**§§ 190–193 — Circumradius perpendicularity**: Each circumradius :math:`OA, OB, OC` is "
            "perpendicular to the corresponding orthic side :math:`EF, FD, DE` (:person:`Nagel's <nagel>` theorem)."),
            ("**§§ 194–200 — Fagnano's Problem (1775)**: Among all triangles inscribed in an acute triangle "
            ":math:`ABC`, the :term:`orthic triangle <orthic-triangle>` :math:`\\triangle DEF` uniquely minimizes "
            "the perimeter, equal to :math:`2S / R` (:person:`Fagnano <fagnano>`)."),
        ),
        geometor_note=(
            "Illustrated symbolically in the ``orthic_fagnano`` hero model via exact Rational Trigonometry "
            "spread equality :math:`s(FD, DA) = s(DA, DE)`."
        ),
    ),
    ("ch03-properties-of-the-triangle", "E.c"): SectionSynopsis(
        summary=(
            "Establishes :person:`Leonhard Euler's <euler>` 1765 discovery (**§§ 201–205**, :cite:`Euler 1765 <euler:1765>`) "
            "that the :term:`circumcenter <circumcircle>` :math:`O`, :term:`centroid <centroid>` :math:`G`, and "
            ":term:`orthocenter <orthocenter>` :math:`H` of any non-equilateral triangle are collinear on the "
            ":term:`Euler line <euler-line>`."
        ),
        highlights=(
            ("**§§ 201–202 — Homothetic Proof of the Euler Line**: Because :math:`O` is the orthocenter of the "
            "complementary triangle :math:`\\triangle A'B'C'` and :math:`\\mathcal{H}(G, -2)` maps :math:`\\triangle A'B'C'` "
            "onto :math:`\\triangle ABC`, we obtain immediately :math:`AH = 2\\,OA'` and :math:`GH = -2\\,GO`."),
            ("**§§ 203–205 — Orthocenter–Circumcenter Distance & Reconstruction**: Derives :math:`OH^2 = "
            "9R^2 - (a^2 + b^2 + c^2)` and solves reconstruction problems given subsets of :math:`(O, G, H, A)`."),
        ),
        geometor_note=(
            "Forms the central spine of Kimberling's ETC (`geometor/etc`): :math:`X(2), X(3), X(4), X(5), X(20), X(30)` "
            "all lie on the Euler line with exact integer/rational barycentric combinations."
        ),
    ),
    ("ch03-properties-of-the-triangle", "F"): SectionSynopsis(
        summary=(
            "Presents two jewels of nineteenth-century synthetic geometry (**§§ 206–219**): the "
            ":term:`nine-point circle <nine-point-circle>` (:person:`Euler <euler>`, :person:`Brianchon <brianchon>`, "
            ":person:`Poncelet <poncelet>`) and :term:`Feuerbach's theorem <feuerbach-theorem>` (**§ 215**, "
            ":cite:`Feuerbach 1822 <feuerbach:1822>`)."
        ),
        highlights=(
            ("**§§ 206–210 — The Nine-Point Circle**: The three side midpoints :math:`A', B', C'`, the three "
            "altitude feet :math:`D, E, F`, and the three Euler points (midpoints of :math:`HA, HB, HC`) lie on "
            "a single circle of radius :math:`R/2` centered at :math:`N = X(5)`, the midpoint of :math:`OH`."),
            ("**§§ 211–214 — Homothecy from H and G**: The nine-point circle is homothetic to the circumcircle "
            "from :math:`H` with ratio :math:`+\\tfrac{1}{2}` (bisecting every segment from :math:`H` to :math:`(O)`) "
            "and from :math:`G` with ratio :math:`-\\tfrac{1}{2}`."),
            ("**§§ 215–219 — Feuerbach's Theorem (1822)**: The nine-point circle of a triangle is internally "
            "tangent to the :term:`incircle <incircle>` at the Feuerbach point :math:`Fe = X(11)` (:math:`NI = "
            "\\tfrac{1}{2}R - r`) and externally tangent to each of the three excircles (:math:`NI_a = \\tfrac{1}{2}R + r_a`)."),
        ),
        geometor_note=(
            "Rendered with 100% exact coordinates in the ``euler_feuerbach`` codex hero model on the Heronian "
            ":math:`13\\text{–}14\\text{–}15` triangle, where :math:`Fe = (1, 8)`, :math:`I = (1, 4)`, and :math:`N = (15/16, 49/16)`."
        ),
    ),
    ("ch03-properties-of-the-triangle", "G"): SectionSynopsis(
        summary=(
            "Reveals the symmetric structure of the :term:`orthocentric quadrilateral <orthocentric-quadrilateral>` "
            "(or *orthocentric group*) :math:`\\{A, B, C, H\\}` (**§§ 220–239**), in which each point is the "
            "orthocenter of the triangle formed by the other three."
        ),
        highlights=(
            ("**§§ 220–226 — Symmetric Four-Point Role**: The four triangles :math:`ABC, HBC, HCA, HAB` share "
            "the *same* orthic triangle :math:`\\triangle DEF` and the *same* :term:`nine-point circle <nine-point-circle>`!"),
            ("**§§ 227–233 — Equal Circumradii & Circumcenter Group**: Their four circumcircles all have equal "
            "radius :math:`R`, and their four circumcenters form a second orthocentric group congruent and "
            "centrally symmetric to :math:`\\{A, B, C, H\\}` across :math:`N`."),
            ("**§§ 234–239 — Centroids & Four Euler Lines**: Their four centroids also form an orthocentric "
            "quadruple homothetic to :math:`\\{A, B, C, H\\}`, while their four Euler lines concur at :math:`N`."),
        ),
        geometor_note=(
            "Provides a finite :math:`S_4` symmetry action on triangle configurations in ``geometor/model`` and "
            "connects directly to :person:`Johnson's <johnson>` three-equal-circles theorem."
        ),
    ),
    ("ch03-properties-of-the-triangle", "Review"): SectionSynopsis(
        summary=(
            "Concludes Chapter III across Folios ``0134``–``0142`` (pp. ``115``–``123``) with a comprehensive "
            "corpus of synthesis constructions, deductive propositions, and locus problems uniting circumcircle, "
            "centroid, tritangent, orthocentric, Euler-line, and nine-point geometry."
        ),
        highlights=(
            ("**Triangle Reconstruction Challenges**: Multi-constraint problems reconstructing :math:`\\triangle ABC` "
            "from combinations of :math:`(O, G, H, N, I, I_a)` and pedal/midpoint traces."),
            ("**Metric & Area Inequalities**: Deductive exercises linking :math:`R, r, r_a, r_b, r_c, s, h_a, m_a, t_a` "
            "and orthogonal projections of vertices onto bisectors and altitudes."),
            ("**Locus Synthesis**: Variable-vertex loci on a fixed circumcircle or fixed base where centers "
            ":math:`H, G, I, N` trace circles and straight lines."),
        ),
        geometor_note=(
            "Serves as an ideal benchmark suite for automated geometric theorem proving and locus discovery "
            "in ``geometor/model`` and ``geometor/divine``."
        ),
    ),
    # ------------------------------------------------------------------
    # Chapter IV — The Quadrilateral (§§ 240–281)
    # ------------------------------------------------------------------
    ("ch04-the-quadrilateral", "A"): SectionSynopsis(
        summary=(
            "Opens the 1952 Second Edition's new Chapter IV (**§§ 240–250**) by developing affine and metric "
            "properties valid for *any* planar quadrilateral :math:`ABCD`—convex, re-entrant, or crossed."
        ),
        highlights=(
            ("**§§ 240–244 — Varignon's Parallelogram & Bimedians**: The midpoints :math:`E, F, G, H` of the four "
            "sides form :person:`Varignon's <varignon>` parallelogram whose sides are parallel to and half the "
            "diagonals :math:`AC, BD`, and whose area equals half the area of :math:`ABCD`; the two bimedians "
            "and the segment joining the diagonal midpoints bisect one another at the vertex centroid."),
            ("**§§ 245–247 — Euler's Quadrilateral Identity**: The sum of the squares of the four sides equals "
            "the sum of the squares of the two diagonals plus four times the square of the segment joining "
            "the midpoints of the diagonals (:person:`Euler <euler>` 1748)."),
            ("**§§ 248–250 — Area & Orthodiagonal Characterization**: Area via :math:`\\tfrac{1}{2} AC \\cdot BD \\sin\\theta`, "
            "and proof that :math:`AB^2 + CD^2 = BC^2 + DA^2` holds if and only if :math:`AC \\perp BD`."),
        ),
        geometor_note=(
            "Modeled with exact integer coordinates in the ``cyclic_quadrilateral`` hero diagram, verifying "
            "parallelism of opposite Varignon sides symbolically."
        ),
    ),
    ("ch04-the-quadrilateral", "B"): SectionSynopsis(
        summary=(
            "Studies quadrilaterals inscribed in a circle (**§§ 251–267**), uniting :person:`Ptolemy's <ptolemy>` "
            "diagonal theorems, :person:`Brahmagupta's <brahmagupta>` area and orthodiagonal theorems, and "
            "Mathot's :term:`anticenter <anticenter>`."
        ),
        highlights=(
            ("**§§ 251–257 — Ptolemy's First & Second Theorems**: In a cyclic quadrilateral :math:`ABCD`, "
            ":math:`AC \\cdot BD = AB \\cdot CD + BC \\cdot DA` (**§ 255**, :person:`Ptolemy <ptolemy>`) and "
            ":math:`AC / BD = (AB \\cdot DA + BC \\cdot CD) / (AB \\cdot BC + CD \\cdot DA)`, determining individual "
            "diagonal lengths directly from the four sides."),
            ("**§§ 258–260 — The Anticenter (Mathot Point)**: Lines drawn through the midpoint of each side "
            "perpendicular to the *opposite* side concur at the :term:`anticenter <anticenter>`, symmetric of "
            "the circumcenter across the vertex centroid!"),
            ("**§§ 261–267 — Brahmagupta's Theorems**: Establishes :math:`S = \\sqrt{(s-a)(s-b)(s-c)(s-d)}` and "
            "proves that if the diagonals of a cyclic quadrilateral are perpendicular at :math:`P`, the line "
            "through :math:`P` bisecting one side is perpendicular to the opposite side (:person:`Brahmagupta <brahmagupta>`)."),
        ),
        geometor_note=(
            "Ptolemy's relation reappears under conformal :term:`inversion <inversion>` in Chapter IX (§ 535) "
            "and generalizes to four tangent circles in :person:`Casey's <casey>` theorem (§ 471)."
        ),
    ),
    ("ch04-the-quadrilateral", "C"): SectionSynopsis(
        summary=(
            "Examines quadrilaterals circumscribed about an incircle (*circumscriptible*) and quadrilaterals "
            "simultaneously inscribed and circumscribed (*bicentric*, **§§ 268–281**)."
        ),
        highlights=(
            ("**§§ 268–273 — Pitot's Theorem**: A convex quadrilateral admits an inscribed circle if and only if "
            "sums of opposite sides are equal (:math:`AB + CD = BC + DA`)."),
            ("**§§ 274–277 — Newton's Line**: In any circumscribed quadrilateral, the incenter lies on the "
            "straight line joining the midpoints of the two diagonals (:person:`Newton <newton>`)."),
            ("**§§ 278–281 — Bicentric Quadrilaterals**: Combines cyclic and tangential conditions (:math:`S = "
            "\\sqrt{abcd}`), perpendicularity of opposite-contact chords, and Fuss's relation between :math:`R, r`, "
            "and center distance."),
        ),
        geometor_note=(
            "Bridges Euclidean circle tangency (``geometor/elements`` Book IV) with projective Brianchon "
            "degeneracies in ``geometor/pappus``."
        ),
    ),
    # ------------------------------------------------------------------
    # Chapter V — The Simson Line (§§ 282–305)
    # ------------------------------------------------------------------
    ("ch05-the-simson-line", "Main"): SectionSynopsis(
        summary=(
            "Develops the complete synthetic theory of the :term:`Wallace–Simson line <simson-line>` (**§§ 282–305**, "
            "Folios ``0159``–``0169``, pp. ``140``–``150``), discovered by :person:`William Wallace <wallace>` "
            "in 1799 and traditionally named after :person:`Robert Simson <simson>`."
        ),
        highlights=(
            ("**§§ 282–287 — Wallace–Simson Collinearity Criterion**: The feet :math:`X, Y, Z` of the perpendiculars "
            "dropped from a point :math:`P` onto the sidelines :math:`BC, CA, AB` of :math:`\\triangle ABC` are "
            "collinear if and only if :math:`P` lies on the :term:`circumcircle <circumcircle>` of :math:`\\triangle ABC`."),
            ("**§§ 288–297 — Angular Rotation & Perpendicular Simson Lines**: As :math:`P` traverses the "
            "circumcircle, its Simson line rotates at half the angular rate in the *opposite* sense; the "
            "Simson lines of two diametrically opposite points :math:`P, P'` are mutually perpendicular."),
            ("**§§ 298–305 — Bisection of PH on the Nine-Point Circle**: The Simson line of :math:`P` bisects "
            "the segment :math:`PH` joining :math:`P` to the :term:`orthocenter <orthocenter>` :math:`H` at a "
            "point :math:`M` on the :term:`nine-point circle <nine-point-circle>`, and two diametral Simson "
            "lines intersect right on the nine-point circle (:person:`Steiner's <steiner>` three-cusped hypocycloid envelope)."),
        ),
        geometor_note=(
            "Verified symbolically in the ``simson_line`` codex hero model (:math:`P = (4, 12)` on the "
            ":math:`13\\text{–}14\\text{–}15` circumcircle), proving collinearity of :math:`X, Y, Z, M` and concyclicity "
            "of :math:`M` with the nine-point circle."
        ),
    ),
    # ------------------------------------------------------------------
    # Chapter VI — Transversals (§§ 306–344)
    # ------------------------------------------------------------------
    ("ch06-transversals", "A"): SectionSynopsis(
        summary=(
            "Introduces signed :term:`directed segments <directed-segments>` on an oriented line (**§§ 306–307**, "
            ":person:`Möbius <mobius>`, :person:`Chasles <chasles>`), eliminating case-splitting between internal "
            "and external points of division."
        ),
        highlights=(
            ("**§ 306 — Chasles's Relation**: For any three collinear points :math:`A, B, C` in any order, "
            ":math:`AB + BC + CA = 0` and :math:`AB = -BA`, uniquely encoding a point on :math:`AB` by its "
            "signed ratio :math:`AC / CB`."),
            ("**§ 307 — Euler's Four-Point Collinear Identity**: For any four collinear points :math:`A, B, C, D`, "
            "signed segments satisfy :math:`AB \\cdot CD + AC \\cdot DB + AD \\cdot BC = 0` (:person:`Euler <euler>`)."),
        ),
        geometor_note=(
            "Corresponds to affine 1D coordinate differences in ``geometor/model`` and underpins signed "
            "cross-ratios in ``geometor/pappus``."
        ),
    ),
    ("ch06-transversals", "B"): SectionSynopsis(
        summary=(
            "Establishes :person:`Matthew Stewart's <stewart>` 1746 cevian theorem (**§§ 308–309**, "
            ":cite:`Stewart 1746 <stewart:1746>`), expressing the length of *any* segment from vertex :math:`A` "
            "to line :math:`BC` in terms of the side lengths and base segments."
        ),
        highlights=(
            ("**§ 308 — Stewart's Theorem**: For any three collinear points :math:`B, C, D` on the base and "
            "arbitrary apex :math:`A`, signed segments obey :math:`AB^2 \\cdot CD + AC^2 \\cdot DB + AD^2 \\cdot BC + "
            "BC \\cdot CD \\cdot DB = 0`."),
            ("**§ 309 — Unified Cevian Corollaries**: Specializing :math:`D` to the midpoint or bisector trace "
            "recovering Apollonius' median formula and the angle-bisector length formula in a single stroke."),
        ),
        geometor_note=(
            "In ``geometor/wildberger``, Stewart's identity is a pure polynomial relation among quadrances "
            "requiring zero trigonometric functions or square roots."
        ),
    ),
    ("ch06-transversals", "C"): SectionSynopsis(
        summary=(
            "Proves :person:`Menelaus of Alexandria's <menelaus>` *Sphaerica* transversal theorem and its "
            "converse (**§§ 310–325**), turning collinearity proofs across synthetic geometry into concise "
            "products of three signed ratios."
        ),
        highlights=(
            ("**§§ 310–313 — Menelaus' Theorem & Converse**: Points :math:`L, M, N` on sidelines :math:`BC, CA, AB` "
            "are collinear if and only if :math:`\\frac{BL}{LC} \\cdot \\frac{CM}{MA} \\cdot \\frac{AN}{NB} = -1`."),
            ("**§§ 314–320 — Bisector Traces & Tangential Axis**: Immediate proofs that the three external "
            "angle-bisector feet (and two internal with one external) are collinear, and that tangents to "
            "the circumcircle at :math:`A, B, C` meet the opposite sides in three collinear points (the Lemoine axis)."),
            ("**§§ 321–325 — Similitude Axes & Pascal's Hexagon**: Proves :person:`Monge's <monge>` theorem on "
            "the collinearity of external centers of similitude of three circles and Pascal's theorem for a "
            "hexagon inscribed in a circle."),
        ),
        geometor_note=(
            "Directly powers projective collinearity verification in ``geometor/pappus`` (Pappus's and Pascal's "
            "hexagon theorems)."
        ),
    ),
    ("ch06-transversals", "D"): SectionSynopsis(
        summary=(
            "Presents :person:`Giovanni Ceva's <ceva>` 1678 concurrency theorem (**§§ 326–344**, "
            ":cite:`Ceva 1678 <ceva:1678>`), pairing Menelaus collinearity with cevian concurrency and "
            "culminating in :person:`Desargues' <desargues>` two-triangle theorem."
        ),
        highlights=(
            ("**§§ 326–330 — Ceva's Theorem & Trigonometric Form**: Cevians :math:`AX, BY, CZ` concur if and "
            "only if :math:`\\frac{BX}{XC} \\cdot \\frac{CY}{YA} \\cdot \\frac{AZ}{ZB} = +1` (and equivalent sine-ratio form), "
            "instantly proving concurrency of medians, altitudes, and angle bisectors."),
            ("**§§ 331–336 — Gergonne Point, Nagel Point & Isotomic Conjugates**: Proves concurrency of "
            "incircle-contact cevians at the :term:`Gergonne point <gergonne-point>` :math:`Ge = X(7)` (**§ 331**, "
            ":person:`Gergonne <gergonne>`), excircle-contact cevians at the :term:`Nagel point <nagel-point>` "
            ":math:`Na = X(8)` (**§ 333**, :person:`Nagel <nagel>`), and general :term:`isotomic conjugation <isotomic-conjugates>`."),
            ("**§§ 337–344 — Harmonic Cevian–Transversal Duality & Desargues' Theorem**: Shows that if :math:`AX, BY, CZ` "
            "concur, line :math:`YZ` meets :math:`BC` at the harmonic conjugate of :math:`X`, and proves "
            ":person:`Desargues' <desargues>` perspective-triangles theorem (**§ 343**)."),
        ),
        geometor_note=(
            "Visualized in the ``menelaus_ceva`` hero construction showing exact concurrency at :math:`Ge = X(7)` "
            "paired with its harmonic trilinear polar transversal."
        ),
    ),
    # ------------------------------------------------------------------
    # Chapter VII — Harmonic Division (§§ 345–357)
    # ------------------------------------------------------------------
    ("ch07-harmonic-division", "Main"): SectionSynopsis(
        summary=(
            "Elevates :term:`harmonic division <harmonic-division>` (**§§ 345–357**, Folios ``0185``–``0190``, "
            "pp. ``166``–``171``) from a metric segment ratio to the fundamental projective invariant of "
            "harmonic pencils, complete quadrangles, and complete quadrilaterals (:cite:`Pappus VII <pappus:collection:VII>`, "
            ":cite:`Chasles <chl>`)."
        ),
        highlights=(
            ("**§§ 345–349 — Algebraic & Midpoint Characterizations**: Proves the equivalence of :math:`(A,B;C,D) = -1` "
            "with the harmonic mean :math:`\\frac{2}{AB} = \\frac{1}{AC} + \\frac{1}{AD}` and :person:`Newton's <newton>` "
            "midpoint relation :math:`MA^2 = MB^2 = MC \\cdot MD`."),
            ("**§§ 350–353 — Harmonic Pencils & Gauss–Newton Line**: Any transversal cuts a harmonic pencil "
            ":math:`O(ABCD)` in four harmonic points; a transversal parallel to one ray is bisected by the "
            "other three; midpoints of the three diagonals of a :term:`complete quadrilateral <complete-quadrilateral>` "
            "are collinear (:person:`Gauss <gauss>`–:person:`Newton <newton>` line)."),
            ("**§§ 354–357 — Complete Quadrangle & Straightedge Harmonic Construction**: Opposite sides of a "
            "complete quadrangle meet a diagonal line in harmonic conjugates, constructing the fourth harmonic "
            "point with the straightedge alone!"),
        ),
        geometor_note=(
            "Directly unites ``geometor/pappus`` (projective cross-ratio invariance) and ``geometor/divine`` "
            "(automated detection of harmonic and golden ranges), illustrated in the ``harmonic_quadrangle`` hero figure."
        ),
    ),
    # ------------------------------------------------------------------
    # Chapter VIII — Circles (§§ 358–517)
    # ------------------------------------------------------------------
    ("ch08-circles", "A"): SectionSynopsis(
        summary=(
            "Defines :term:`inverse points <inverse-points>` :math:`P, P'` with respect to a reference circle "
            ":math:`(O, R)` (**§§ 358–362**) via collinearity on a ray from :math:`O` and :math:`OP \\cdot OP' = R^2`."
        ),
        highlights=(
            ("**§§ 358–360 — Harmonic Diameter Separation**: Two points :math:`P, P'` on a diameter line are "
            "inverse with respect to :math:`(O, R)` if and only if they divide the endpoints of that diameter "
            ":term:`harmonically <harmonic-division>` (§ 63)."),
            ("**§§ 361–362 — Ruler-and-Compass Construction & Ratio Property**: Constructs :math:`P'` via right-triangle "
            "chords or tangent secants, and shows that :math:`(O, R)` is an :term:`Apollonian circle <apollonian-circle>` "
            "for every pair of inverse points :math:`MP / MP' = OP / R`."),
        ),
        geometor_note=(
            "Establishes the point-pair foundation for poles/polars (§ 373) and conformal :term:`inversion <inversion>` "
            "(Chapter IX)."
        ),
    ),
    ("ch08-circles", "B"): SectionSynopsis(
        summary=(
            "Develops the geometry of :term:`orthogonal circles <orthogonal-circles>` (**§§ 363–372**)—pairs of "
            "circles whose tangents (and radii) at their points of intersection meet at right angles."
        ),
        highlights=(
            ("**§§ 363–367 — Metric & Tangent Criteria**: Circles :math:`(O, R)` and :math:`(O', R')` are "
            "orthogonal if and only if :math:`OO'^2 = R^2 + R'^2`, or equivalently the radius of one to an "
            "intersection point is tangent to the other."),
            ("**§§ 368–372 — Fundamental Inversion-Orthogonality Theorem**: A circle cuts :math:`(O, R)` "
            "orthogonally if and only if every diameter of :math:`(O, R)` meeting it is divided harmonically—"
            "i.e., if and only if it passes through the inverse :math:`P'` of every point :math:`P` it contains!"),
        ),
        geometor_note=(
            "Verified symbolically in the ``pole_polar_coaxal`` hero figure with exact Pythagorean radii "
            ":math:`6, 8` on center distance :math:`10`."
        ),
    ),
    ("ch08-circles", "C"): SectionSynopsis(
        summary=(
            "Presents the projective-metric duality of :term:`poles and polars <pole-and-polar>` with respect "
            "to a circle :math:`(O, R)` (**§§ 373–393**, :person:`Apollonius <apollonius>`, :person:`Desargues <desargues>`, "
            ":person:`La Hire <hire>`, :person:`Poncelet <poncelet>`)."
        ),
        highlights=(
            ("**§§ 373–378 — Polar Definition & Chord of Contact**: Defines the polar of :math:`P` as the "
            "perpendicular to :math:`OP` through its inverse point :math:`P'`; for external :math:`P`, it "
            "coincides with the chord of contact :math:`T_1 T_2`, and divides every secant chord through :math:`P` "
            "harmonically."),
            ("**§§ 379–385 — La Hire's Reciprocity Theorem**: Point :math:`Q` lies on the polar of :math:`P` if "
            "and only if :math:`P` lies on the polar of :math:`Q` (:person:`La Hire <hire>`, :cite:`Sectiones Conicae <lhr>`), "
            "translating collinear ranges into concurrent pencils."),
            ("**§§ 386–393 — Conjugate (Self-Polar) Triangles & Salmon's Theorem**: Shows that the orthocenter "
            "of an obtuse self-polar triangle is the circle's center :math:`O`, and relates pole distances to "
            "polar distances (Salmon's proportional identity)."),
        ),
        geometor_note=(
            "Bridges Euclidean circle polarity in ``geometor/model`` with general conic polarity in ``geometor/pappus``."
        ),
    ),
    ("ch08-circles", "D"): SectionSynopsis(
        summary=(
            "Extends Chapter II's :term:`centers of similitude <centers-of-similitude>` to systems of two and "
            "three circles (**§§ 394–409**), culminating in :person:`Gaspard Monge's <monge>` theorem on axes "
            "of similitude."
        ),
        highlights=(
            ("**§§ 394–404 — Homologous & Antihomologous Points**: Pairs of antihomologous points on two circles "
            "are concyclic and yield constant secant products from each center of similitude, governing common "
            "tangent constructions."),
            ("**§§ 405–409 — Monge's Circle Theorem (§ 405)**: Given three unequal circles, their six centers "
            "of similitude lie by threes on **four straight lines** (*axes of similitude*): one external axis "
            "containing all three external centers, and three mixed axes containing one external and two "
            "internal centers (:person:`Monge <monge>`)."),
        ),
        geometor_note=(
            "The four axes of similitude constructed here form the essential first step of :person:`Gergonne's <gergonne>` "
            "master solution to the :term:`Problem of Apollonius <problem-of-apollonius>` (§ 517)."
        ),
    ),
    ("ch08-circles", "E"): SectionSynopsis(
        summary=(
            "Formalizes :person:`Jakob Steiner's <steiner>` algebraic-geometric invariant (**§§ 410–420**): "
            "the :term:`power of a point <power-of-a-point>` :math:`P` with respect to circle :math:`(O, R)`."
        ),
        highlights=(
            ("**§§ 410–415 — Signed Secant Product**: For any line through :math:`P` meeting :math:`(O, R)` in "
            ":math:`A, B`, the signed product :math:`PA \\cdot PB = PO^2 - R^2` depends solely on :math:`P` "
            "(:cite:`Euclid III.35–36 <euclid:elements>`): positive outside (equal to :math:`PT^2`), zero on, "
            "and negative inside (:math:`-\\text{half-min-chord}^2`)."),
            ("**§§ 416–420 — Orthogonal Circle Power Criterion**: The power of the center of one circle with "
            "respect to a second circle equals the square of its own radius if and only if the two circles "
            "are :term:`orthogonal <orthogonal-circles>`."),
        ),
        geometor_note=(
            "Represented in ``geometor/model`` and ``geometor/wildberger`` as the exact rational polynomial "
            ":math:`Q(P, O) - R^2`."
        ),
    ),
    ("ch08-circles", "F"): SectionSynopsis(
        summary=(
            "Constructs and characterizes the :term:`radical axis <radical-axis>` of two non-concentric circles "
            "(**§§ 421–439**, Gaultier 1813, :person:`Steiner <steiner>`): the straight-line locus of "
            "points having equal :term:`powers <power-of-a-point>` with respect to both circles."
        ),
        highlights=(
            ("**§§ 421–428 — Linear Locus & Common Secant/Tangent**: Generalizes Chapter I :ref:`Locus 12 <ch01-locus-12>` "
            "(:math:`PO^2 - PO'^2 = R^2 - R'^2`): perpendicular to the line of centers :math:`OO'`, coinciding "
            "with the common chord when circles intersect, common internal tangent when tangent, and bisecting "
            "all four common tangents."),
            ("**§§ 429–439 — Construction for Non-Intersecting Circles**: Introduces an auxiliary circle cutting "
            "both given circles, intersecting their two common chords at a point on the required radical axis, "
            "and proves that orthogonal circles have centers on the radical axis."),
        ),
        geometor_note=(
            "Subtracting two circle equations :math:`(x - x_i)^2 + (y - y_i)^2 - R_i^2 = 0` in ``geometor/model`` "
            "cancels :math:`x^2 + y^2`, producing the exact linear radical axis over :math:`\\mathbb{Q}`."
        ),
    ),
    ("ch08-circles", "G"): SectionSynopsis(
        summary=(
            "Develops the theory of :term:`coaxal pencils of circles <coaxal-circles>` (**§§ 440–490**), "
            ":person:`Poncelet's <poncelet>` limiting points, conjugate orthogonal pencils, and :person:`John Casey's <casey>` "
            "generalized Ptolemy theorem (**§ 471**)."
        ),
        highlights=(
            ("**§§ 440–458 — Intersecting, Tangent & Non-Intersecting Pencils**: Classifies coaxal systems "
            "sharing a common :term:`radical axis <radical-axis>`, identifies :person:`Poncelet's <poncelet>` "
            "point-circles (*limiting points* :math:`L, L'`), and proves that two conjugate orthogonal coaxal "
            "pencils swap base points and limiting points!"),
            ("**§§ 459–470 — Poncelet's Triangle-Pencil Theorems**: Studies variable triangles inscribed in one "
            "circle whose sides touch circles of a coaxal pencil."),
            ("**§§ 471–490 — Casey's Theorem (§ 471)**: Four circles tangent to a fifth circle (or line) satisfy "
            ":math:`t_{12} t_{34} \\pm t_{13} t_{24} \\pm t_{14} t_{23} = 0` among their common tangent lengths "
            "(:cite:`Casey, Sequel to Euclid <casey:sequel:1892>`), providing an algebraic proof of Feuerbach's theorem!"),
        ),
        geometor_note=(
            "Connects projective pencils of conics in ``geometor/pappus`` with Feuerbach tangency verification "
            "in ``geometor/etc``."
        ),
    ),
    ("ch08-circles", "H"): SectionSynopsis(
        summary=(
            "Analyzes systems of three circles (**§§ 491–505**): the concurrency of their three pairwise "
            ":term:`radical axes <radical-axis>` at the *radical center* and their orthogonal circle."
        ),
        highlights=(
            ("**§§ 491–497 — The Radical Center & Orthogonal Circle**: The three radical axes of three "
            "non-coaxal circles concur at the unique radical center :math:`R_c`; when :math:`R_c` lies outside "
            "the three circles, the circle centered at :math:`R_c` with radius equal to the common tangent length "
            "cuts all three given circles :term:`orthogonally <orthogonal-circles>`!"),
            ("**§§ 498–505 — Radical Circle & Circles of Antisimilitude**: Studies circles coaxal with pairs "
            "of given circles and loci where ratios of powers remain constant."),
        ),
        geometor_note=(
            "Applied to three point-circles at :math:`A, B, C`, the radical center recovers the circumcenter "
            ":math:`O = X(3)`; applied to the excircles, it yields the Spieker radical center!"
        ),
    ),
    ("ch08-circles", "I"): SectionSynopsis(
        summary=(
            "Crowns Chapter VIII with the :term:`Problem of Apollonius <problem-of-apollonius>` (**§§ 506–517**): "
            "to construct a circle tangent to three given circles (or any combination of points ``P``, lines ``L``, "
            "and circles ``C``)."
        ),
        highlights=(
            ("**§§ 506–515 — Viète's Systematic Reduction of the Ten Cases**: Resolves ``PPP``, ``PPL``, ``PLL``, "
            "``LLL``, ``PPC``, ``PLC``, ``LLC``, ``PCC``, and ``LCC`` step-by-step via radical-axis intersections "
            "and radius-contraction to earlier cases (:person:`Viète <viete>`, *Apollonius Gallus* 1600)."),
            ("**§§ 516–517 — Gergonne's Master Solution to CCC (§ 517)**: Without shrinking radii, constructs "
            "all four pairs of complementary Apollonius circles directly using the radical center of the three "
            "circles, the four :person:`Monge <monge>` axes of similitude (§ 405), and their poles with respect "
            "to the three given circles (:person:`Gergonne <gergonne>` 1816)!"),
        ),
        geometor_note=(
            "One of the supreme constructive milestones linking ``geometor/pappus`` (Apollonius *Tangencies* "
            "reported in Pappus Book VII) and ``geometor/model``."
        ),
    ),
    # ------------------------------------------------------------------
    # Chapter IX — Inversion (§§ 518–546)
    # ------------------------------------------------------------------
    ("ch09-inversion", "Main"): SectionSynopsis(
        summary=(
            "Develops conformal transformation by reciprocal radii—:term:`circular inversion <inversion>` "
            ":math:`\\mathcal{I}(O, k)` (**§§ 518–546**, Folios ``0249``–``0262``, pp. ``230``–``243``)—converting "
            "intractable circle-tangency configurations into elementary rectilinear geometry."
        ),
        highlights=(
            ("**§§ 518–531 — Images of Lines, Circles & Conformal Angle Preservation**: Lines and circles through "
            ":math:`O` invert into lines; lines and circles not through :math:`O` invert into circles; angles "
            "between intersecting curves are preserved in magnitude; metric law :math:`A'B' = |k| \\cdot AB / (OA \\cdot OB)`."),
            ("**§§ 532–534 — Peaucellier's Inversor Linkage (§ 533)**: Proves that :person:`Peaucellier's <peaucellier>` "
            "1864 seven-bar rhombic cell realizes exact mathematical inversion and converts circular arc motion "
            "into a rigorous straight line without any reference straightedge!"),
            ("**§§ 535–546 — Ptolemy, Steiner Porism & Feuerbach by Inversion (§ 540)**: Proves Ptolemy's "
            "theorem and inequality by inverting from a vertex, resolves Steiner's porismatic ring of tangent "
            "circles via concentric inversion, and proves :term:`Feuerbach's theorem <feuerbach-theorem>` in "
            "a single paragraph by inverting from the midpoint of the interior common tangent to :math:`(I)` "
            "and :math:`(I_a)`!"),
        ),
        geometor_note=(
            "Modeled symbolically in the ``circular_inversion`` hero diagram (:math:`OP \\cdot OP' = 36` over "
            ":math:`\\mathbb{Q}`) and reproducible algebraically in ``geometor/model``."
        ),
    ),
    # ------------------------------------------------------------------
    # Chapter X — Recent Geometry of the Triangle (§§ 547–699)
    # ------------------------------------------------------------------
    ("ch10-recent-geometry-of-the-triangle", "A"): SectionSynopsis(
        summary=(
            "Introduces projective duality relative to a reference triangle (**§§ 547–557**): the "
            ":term:`trilinear polar <trilinear-polar>` of a point and the *trilinear pole* of a transversal line."
        ),
        highlights=(
            ("**§§ 547–552 — Harmonic Ceva–Menelaus Pairing**: Given point :math:`P` with cevian traces "
            ":math:`X, Y, Z` on :math:`BC, CA, AB`, the harmonic conjugates :math:`X', Y', Z'` of :math:`X, Y, Z` "
            "are collinear on a Menelaus transversal—the :term:`trilinear polar <trilinear-polar>` of :math:`P`!"),
            ("**§§ 553–557 — Notable Trilinear Polars**: Identifies the line at infinity as the trilinear polar "
            "of the :term:`centroid <centroid>` :math:`G`, the orthic axis as the trilinear polar of the "
            ":term:`orthocenter <orthocenter>` :math:`H`, and the Lemoine axis of circumcircle tangents as "
            "the trilinear polar of the :term:`Lemoine point <lemoine-point>` :math:`K`."),
        ),
        geometor_note=(
            "In ``geometor/etc``, trilinear polarity sends point :math:`(u : v : w)` directly to the line "
            ":math:`x/u + y/v + z/w = 0` in homogeneous trilinear coordinates."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "B.a"): SectionSynopsis(
        summary=(
            "Develops the theory of :term:`symmedians <symmedian>` (**§§ 558–571**, :person:`Maurice d'Ocagne <docagne>`, "
            ":person:`Émile Lemoine <lemoine>`): the reflections of the medians of a triangle across the "
            "corresponding internal angle bisectors."
        ),
        highlights=(
            ("**§§ 558–564 — Antiparallel Bisection & Harmonic Tangents**: A symmedian from :math:`A` bisects "
            "every antiparallel to :math:`BC`, passes through the pole of :math:`BC` with respect to the "
            ":term:`circumcircle <circumcircle>` (intersection of tangents at :math:`B` and :math:`C`), and "
            "divides :math:`BC` in the squared side ratio :math:`c^2 : b^2`!"),
            ("**§§ 565–571 — Distances Proportional to Sides**: Points on the :math:`A`-symmedian have "
            "perpendicular distances to sides :math:`AB, AC` proportional to the side lengths :math:`c : b`."),
        ),
        geometor_note=(
            "Because symmedians divide opposite sides in squared ratios :math:`c^2 : b^2` (*quadrances*!), "
            "symmedian geometry is 100% rational over :math:`\\mathbb{Q}(A, B, C)` in ``geometor/wildberger``."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "B.b"): SectionSynopsis(
        summary=(
            "Establishes the concurrency of the three symmedians at the :term:`Lemoine (symmedian) point <lemoine-point>` "
            ":math:`K = X(6)` (**§§ 572–587**, :person:`Grebe <grebe>` 1847; :cite:`Lemoine 1873 <lemoine:1873>`), "
            "the crown jewel of late-nineteenth-century triangle geometry."
        ),
        highlights=(
            ("**§§ 572–578 — Concurrency & Gergonne Identification**: Ceva's theorem on :math:`(c^2/b^2)(a^2/c^2)(b^2/a^2) = 1` "
            "proves concurrency at :math:`K`, whose distances to :math:`BC, CA, AB` are proportional to :math:`a, b, c`; "
            ":math:`K` is the :term:`Gergonne point <gergonne-point>` of the tangential triangle!"),
            ("**§§ 579–587 — Gauss–Lemoine Least-Squares Minimum & Centroid Pedal Property**: Among all points "
            "in the plane, :math:`K = X(6)` uniquely minimizes the sum of squares of distances :math:`d_a^2 + d_b^2 + d_c^2` "
            "to the three sides (**§ 581**), and :math:`K` is the unique point that is the centroid of its own "
            "pedal triangle!"),
        ),
        geometor_note=(
            "Constructed with exact rational coordinates :math:`K = (a^2 A + b^2 B + c^2 C)/(a^2 + b^2 + c^2)` "
            "in ``geometor/etc`` (:math:`X(6)`) and the ``lemoine_symmedian`` hero figure."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "B.c"): SectionSynopsis(
        summary=(
            "Constructs the two remarkable six-point circles discovered by :person:`Émile Lemoine <lemoine>` "
            "in 1873 (**§§ 588–596**, :cite:`Lemoine 1873 <lemoine:1873>`): the first and second (cosine) "
            ":term:`Lemoine circles <lemoine-circles>`."
        ),
        highlights=(
            ("**§§ 588–592 — The First Lemoine Circle**: Straight lines drawn through the :term:`Lemoine point <lemoine-point>` "
            ":math:`K` parallel to the three sides :math:`BC, CA, AB` intersect the sidelines in **six concyclic "
            "points** whose circle is centered at the midpoint :math:`X(182)` of segment :math:`OK`!"),
            ("**§§ 593–596 — The Second Lemoine (Cosine) Circle**: Antiparallels to the three sides drawn through "
            ":math:`K` are bisected at :math:`K` and all have equal length, so their six endpoints lie on a "
            "circle centered at :math:`K` itself whose chord intercepts are proportional to :math:`\\cos A, \\cos B, \\cos C`."),
        ),
        geometor_note=(
            "Both the First Lemoine Circle and Brocard Circle appear in exact symbolic precision in the "
            "``lemoine_symmedian`` hero diagram; both belong to the Tucker circle family (§ 684)."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "C"): SectionSynopsis(
        summary=(
            "Studies the coaxal triad of :term:`Apollonian circles <apollonian-circle>` of a triangle "
            "(**§§ 597–624**), their two common :term:`isodynamic points <isodynamic-points>` :math:`W, W' = X(15), X(16)`, "
            "and their orthogonality to the circumcircle."
        ),
        highlights=(
            ("**§§ 597–605 — Coaxal Triad Orthogonal to Circumcircle**: Each circle of locus :math:`MB : MC = c : b` "
            "passes through a vertex and cuts :math:`(O)` orthogonally; all three belong to a single coaxal "
            "pencil whose common radical axis is the Brocard axis :math:`OK` and whose conjugate line of centers "
            "is the Lemoine axis!"),
            ("**§§ 606–624 — The Isodynamic Points W, W' (§ 606)**: The three Apollonian circles intersect in "
            "two real points :math:`W, W'` inverse with respect to :math:`(O)`, whose pedal triangles are "
            "**equilateral** (:person:`Neuberg <neuberg>`), and which invert :math:`\\triangle ABC` into an "
            "equilateral triangle!"),
        ),
        geometor_note=(
            "Links ``geometor/etc`` (:math:`X(15), X(16)`, isogonal conjugates of the Fermat points :math:`X(13), X(14)`) "
            "with conformal inversion symmetry."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "D"): SectionSynopsis(
        summary=(
            "Develops the quadratic Cremona transformation of :term:`isogonal conjugation <isogonal-conjugates>` "
            "with respect to :math:`\\triangle ABC` (**§§ 625–648**), pairing every interior/exterior point "
            ":math:`P` with its reflection-in-bisectors conjugate :math:`P'`."
        ),
        highlights=(
            ("**§§ 625–634 — Existence & Classical Conjugate Pairs**: Reflections of concurrent cevians :math:`AP, BP, CP` "
            "across the internal angle bisectors concur at :math:`P'`; incenter/excenters are self-conjugate, "
            ":math:`(O, H)` are isogonal conjugates, and :math:`(G, K)` are isogonal conjugates!"),
            ("**§§ 635–643 — Shared Pedal Circle Theorem**: The six pedal projections of an isogonal pair "
            ":math:`P, P'` onto the three sides lie on a single **pedal circle** centered at the midpoint of "
            ":math:`PP'` (specializing for :math:`(O, H)` right back to the :term:`nine-point circle <nine-point-circle>`!)."),
            ("**§§ 644–648 — Circumcircle Degeneracy**: Points on the circumcircle have isogonal conjugates at "
            "infinity in the direction perpendicular to their :term:`Simson lines <simson-line>`."),
        ),
        geometor_note=(
            "Corresponds to reciprocal trilinear coordinates :math:`(u : v : w) \\mapsto (1/u : 1/v : 1/w)` "
            "across ``geometor/etc``."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "E.a"): SectionSynopsis(
        summary=(
            "Introduces the asymmetric rotational jewel of triangle geometry (**§§ 649–665**): the direct and "
            "retrograde :term:`Brocard points <brocard-points>` :math:`\\Omega, \\Omega'` and the Brocard angle "
            ":math:`\\omega` (:person:`Crelle <crelle>` 1816, :person:`Jacobi <jacobi>` 1828, :cite:`Brocard 1881 <brocard:1881>`)."
        ),
        highlights=(
            ("**§§ 649–655 — Construction via Tangent Adjunct Circles**: Three circles tangent to :math:`BC, CA, AB` "
            "at :math:`B, C, A` and passing through :math:`C, A, B` concur at the first Brocard point :math:`\\Omega` "
            "where :math:`\\angle\\Omega BC = \\angle\\Omega CA = \\angle\\Omega AB = \\omega`; cyclic reversal yields "
            ":math:`\\Omega'`, the :term:`isogonal conjugate <isogonal-conjugates>` of :math:`\\Omega`!"),
            ("**§§ 656–665 — Brocard Angle Formula & Inequality**: Proves :math:`\\cot\\omega = \\cot A + \\cot B + \\cot C = "
            "(a^2 + b^2 + c^2) / 4S`, :math:`\\csc^2\\omega = \\csc^2 A + \\csc^2 B + \\csc^2 C`, and :math:`\\omega \\le 30^\\circ` "
            "(equality iff :math:`\\triangle ABC` is equilateral)."),
        ),
        geometor_note=(
            "Notice :math:`\\cot\\omega = (Q_a + Q_b + Q_c) / 4S` is rational in the side quadrances and area, "
            "connecting Brocard geometry to ``geometor/etc`` (:math:`X(39)` Brocard midpoint) and ``geometor/wildberger``."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "E.b"): SectionSynopsis(
        summary=(
            "Unites :math:`O, K, \\Omega, \\Omega'` on the seven-point :term:`Brocard circle <brocard-circle>` "
            "(**§§ 666–683**), introducing Brocard's first and second triangles and the :term:`Steiner and Tarry points <steiner-and-tarry-points>`."
        ),
        highlights=(
            ("**§§ 666–675 — The Brocard Circle & Brocard Triangles**: The circle on diameter :math:`OK` passes "
            "through :math:`O, K, \\Omega, \\Omega'` (with :math:`O\\Omega = O\\Omega'`, :math:`\\angle\\Omega O\\Omega' = 2\\omega`), "
            "as well as the three vertices of Brocard's first and second triangles!"),
            ("**§§ 676–683 — Steiner Point X(99) & Tarry Point X(98)**: Parallels through :math:`A, B, C` to "
            "the sides of Brocard's first triangle concur on the circumcircle at the :person:`Steiner <steiner>` "
            "point :math:`X(99)`, diametrically opposite the :person:`Tarry <tarry>` point :math:`X(98)` where "
            "the corresponding perpendiculars concur."),
        ),
        geometor_note=(
            "Maps directly to Kimberling centers :math:`X(39)`, :math:`X(98)`, :math:`X(99)`, and :math:`X(182)` "
            "in ``geometor/etc``."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "F"): SectionSynopsis(
        summary=(
            "Generalizes the circumcircle, first and second Lemoine circles, and three-point pedal circles "
            "into the one-parameter family of :term:`Tucker circles <tucker-circles>` (**§§ 684–689**, "
            ":person:`Robert Tucker <tucker>` 1883), highlighted by the :person:`Taylor <taylor>` circle (**§ 689**)."
        ),
        highlights=(
            ("**§§ 684–688 — Six-Point Antiparallel-Parallel Hexagon**: If a triangle homothetic to :math:`\\triangle ABC` "
            "from the :term:`Lemoine point <lemoine-point>` :math:`K` has its sides extended to meet :math:`BC, CA, AB`, "
            "the six resulting intercepts have alternating parallel and equal antiparallel chords and lie on a "
            "**Tucker circle** whose center lies on segment :math:`OK`!"),
            ("**§ 689 — The Taylor Circle**: The six orthogonal projections of the altitude feet :math:`D, E, F` "
            "onto the other two sides of :math:`\\triangle ABC` lie on a distinguished Tucker circle discovered "
            "by :person:`H. M. Taylor <taylor>` (centered at :math:`X(389)`)."),
        ),
        geometor_note=(
            "Provides a continuous affine family parameterized along the Brocard axis :math:`OK` in ``geometor/etc``."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "G"): SectionSynopsis(
        summary=(
            "Culminates the entire 699-article treatise with :person:`Joseph Neuberg's <neuberg>` theory of the "
            ":term:`orthopole <orthopole>` :math:`M` of a line :math:`m` with respect to :math:`\\triangle ABC` "
            "(**§§ 690–699**, :cite:`Gallatly 1913 <gy>`)."
        ),
        highlights=(
            ("**§§ 690–694 — Existence & Concurrency**: Drop perpendiculars :math:`AA_1, BB_1, CC_1` from the "
            "vertices of :math:`\\triangle ABC` onto any line :math:`m`; the perpendiculars from :math:`A_1, B_1, C_1` "
            "onto the opposite sides :math:`BC, CA, AB` concur at the :term:`orthopole <orthopole>` :math:`M` of :math:`m`!"),
            ("**§§ 695–699 — Circumdiameter, Simson & Pedal-Circle Laws**: If :math:`m` passes through the "
            "circumcenter :math:`O`, its orthopole lies on the :term:`nine-point circle <nine-point-circle>` "
            "(and equals the Simson-line intersection of the diameter endpoints!); if :math:`m` cuts :math:`(O)` "
            "in :math:`P, Q`, then :math:`M` is the intersection of the :term:`Simson lines <simson-line>` of :math:`P` "
            "and :math:`Q` (Soons, :person:`Neuberg <neuberg>`, Lemoyne)!"),
        ),
        geometor_note=(
            "Synthesizes orthocenter, nine-point, Simson-line, and pedal-circle geometry into one unified "
            "incidence theorem verifiable in ``geometor/model``."
        ),
    ),
    ("ch10-recent-geometry-of-the-triangle", "Supplementary"): SectionSynopsis(
        summary=(
            "Concludes Chapter X across Folios ``0310``–``0313`` (pp. ``291``–``[294]``) with advanced "
            "supplementary problems spanning trilinear polarity, Lemoine–Brocard geometry, Tucker circles, "
            "and orthopoles, followed by the blank verso leaf ``[294]``."
        ),
        highlights=(
            ("**Lemoine & Symmedian Synthesis**: Problems linking symmedian chords, tangential triangles, and "
            "cosine/Tucker circle radii."),
            ("**Isodynamic & Brocard Configurations**: Metric relations among :math:`\\omega`, :math:`OK`, "
            "Brocard triangles, and isogonal pedal circles."),
            ("**Orthopole & Simson Loci**: Locus problems as a line rotates about a fixed point or remains "
            "tangent to an inscribed circle (Lemoyne's circle theorem)."),
        ),
        geometor_note=(
            "Provides deep research-grade synthetic challenges for symbolic exploration in ``geometor/etc`` "
            "and ``geometor/model``."
        ),
    ),
    # ------------------------------------------------------------------
    # Historical and Bibliographical Notes & Index
    # ------------------------------------------------------------------
    ("historical-and-bibliographical-notes", "BibKey"): SectionSynopsis(
        summary=(
            "Keys the bibliographic abbreviations on Folios ``0314``–``0315`` (pp. ``295``–``296``) to the "
            "eight classical treatises and ten nineteenth/twentieth-century mathematical journals cited "
            "throughout Altshiller-Court's historical notes."
        ),
        highlights=(
            ("**Foundational Treatises**: :cite:`Chasles (Chl.) <chl>`, :cite:`Coolidge (Cn.) <cn>`, "
            ":cite:`Altshiller-Court Modern Pure Solid Geometry (Crt.) <crt>`, :cite:`Catalan (Ech.) <ech>`, "
            ":cite:`Gallatly (Gy.) <gy>`, :cite:`Lachlan (LHr.) <lhr>`, :cite:`Petersen (Pt.) <pt>`, and "
            ":cite:`Rouché & de Comberousse <rouche>`."),
            ("**Problem & Research Periodicals**: *Bulletin des sciences mathématiques* (:cite:`Bull. <per:bull>`), "
            "*Proceedings of the Edinburgh Mathematical Society* (:cite:`Edinb. <per:edinb>`), *Educational Times* "
            "(:cite:`ET. <per:et>`), *Giornale di Matematiche* (:cite:`GAM. <per:gam>`), *Journal de mathématiques "
            "élémentaires* (:cite:`JME. <per:jme>`), *Mathesis* (:cite:`Mathesis <per:mathesis>`), *American "
            "Mathematical Monthly* (:cite:`Monthly <per:monthly>`), and *Nouvelles Annales* (:cite:`NA. <per:na>`)."),
        ),
        geometor_note=(
            "Every bibliographic key is fully resolved as a clickable anchor in :ref:`Systematic Bibliography <bibliography>`."
        ),
    ),
    ("historical-and-bibliographical-notes", "Notes"): SectionSynopsis(
        summary=(
            "Presents Altshiller-Court's article-by-article historical and bibliographic commentary spanning "
            "**§§ 4–697** across Folios ``0315``–``0325`` (pp. ``296``–``306``), documenting priority, "
            "independent rediscoveries, and journal problem origins."
        ),
        highlights=(
            ("**Antiquity to Early Modern (§§ 4–344)**: Attributions to :person:`Plato <plato>`, :person:`Euclid <euclid>`, "
            ":person:`Archimedes <archimedes>`, :person:`Apollonius <apollonius>`, :person:`Heron <heron>`, "
            ":person:`Menelaus <menelaus>`, :person:`Ptolemy <ptolemy>`, :person:`Pappus <pappus>`, :person:`Viète <viete>`, "
            ":person:`Desargues <desargues>`, :person:`Ceva <ceva>`, :person:`Newton <newton>`, :person:`Stewart <stewart>`, "
            "and :person:`Euler <euler>`."),
            ("**Projective & Circle Renaissance (§§ 345–546)**: Priority histories of :person:`Carnot <carnot>`, "
            ":person:`Brianchon <brianchon>`, :person:`Poncelet <poncelet>`, :person:`Gergonne <gergonne>`, "
            ":person:`Feuerbach <feuerbach>`, :person:`Steiner <steiner>`, :person:`Chasles <chasles>`, "
            ":person:`Peaucellier <peaucellier>`, and :person:`Casey <casey>`."),
            ("**Modern Triangle Geometry (§§ 547–697)**: Detailed journal citations for :person:`Lemoine <lemoine>`, "
            ":person:`Brocard <brocard>`, :person:`Neuberg <neuberg>`, :person:`d'Ocagne <docagne>`, "
            ":person:`Tucker <tucker>`, :person:`Taylor <taylor>`, :person:`Tarry <tarry>`, and :person:`Thébault <thebault>`."),
        ),
        geometor_note=(
            "Cross-linked prosopographically throughout this edition via :ref:`Index of Persons <persons>` "
            "and :ref:`Systematic Bibliography <bibliography>`."
        ),
    ),
    ("historical-and-bibliographical-notes", "Names"): SectionSynopsis(
        summary=(
            "Alphabetical prosopographical index across Folios ``0326``–``0328`` (pp. ``307``–``309``) mapping "
            "every geometer named in *College Geometry* to page numbers in the text and historical notes."
        ),
        highlights=(
            ("**Interactive Prosopographical Expansion**: Expanded in this Digital Scriptorium into the "
            "67-entry :ref:`Biographical Register of Geometers & Scholars <persons>` with dates, institutional "
            "roles, principal treatises, and direct article links."),
        ),
        geometor_note=(
            "Consult :ref:`Index of Persons <persons>` for live biographical entries and back-links into "
            "transcribed folios."
        ),
    ),
    ("back-index", "Index"): SectionSynopsis(
        summary=(
            "Altshiller-Court's four-page analytical *Subject Index* across Folios ``0329``–``0332`` "
            "(pp. ``310``–``313``), indexing definitions, loci, triangle centers, notable circles, "
            "named theorems, and transformations by article number (**§§ 1–699**)."
        ),
        highlights=(
            ("**Digital Apparatus Concordance**: Paired interactively with the :ref:`Technical Glossary <glossary>` "
            "(``:term:``), :ref:`Index of Persons <persons>` (``:person:``), :ref:`Systematic Bibliography <bibliography>` "
            "(``:cite:``), and :ref:`334-Folio Archival Scan Inventory <scan-inventory>`."),
        ),
        geometor_note=(
            "Every core headword is mapped to its Kimberling ``X(n)`` center identifier and symbolic locus "
            "definition in :ref:`Technical Glossary <glossary>`."
        ),
    ),
    ("back-index", "Endmatter"): SectionSynopsis(
        summary=(
            "Terminal archival leaves of the 334-page Dover witness (Folios ``0333``–``0334``): the blank "
            "recto leaf ``[314]`` and the unabridged 2007 Dover Publications back cover (ISBN ``978-0-486-45805-2``)."
        ),
        highlights=(
            ("**Witness Completeness**: Preserves the unbroken 334-folio archival sequence from front cover "
            "(:ref:`Folio 0001 <frontmatter-01-cover>`) to back cover (``Folio 0334``)."),
        ),
        geometor_note=(
            "Recorded in :ref:`334-Folio Archival Scan & Transcription Inventory <scan-inventory>`."
        ),
    ),
}
