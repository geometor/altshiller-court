:layout: book
:title: Chapter I: Geometric Constructions — Commentary

.. _ch01-geometric-constructions-commentary:

Chapter I: Geometric Constructions — Commentary
===============================================

.. rubric:: Constructive Analysis, Historical Provenance & GEOMETOR Notes (0020–0052, pp. 1–33)

Constructive Architecture & Symbolic Modeling (`§§ 1–22`)
---------------------------------------------------------

Chapter I lays down the operational grammar of the entire book. Every ruler-and-compass construction is governed by :person:`Pappus' <pappus>` four-stage :term:`analytic method <analytic-method>` (:cite:`Collection, Book VII <pappus:collection:VII>`):

1. :term:`Analysis <analysis-step>` — Assume the required configuration already exists and trace algebraic/synthetic incidences back to known data.
2. :term:`Construction <construction-step>` — Execute elementary straightedge (`line(P, Q)`) and compass (`circle(A, r)`) steps in forward topological order.
3. :term:`Proof <proof-step>` — Verify deductively that the constructed object satisfies every hypothesis.
4. :term:`Discussion <discussion-step>` (*Diorismos*) — Determine exact existence inequalities (`s < 2 OE`, `s^2 > 2a^2`), count multiplicity of solutions (`0, 1, 2, 3, 4, 6`, or :math:`\infty`), and identify poristic degeneracies (as in § 9 when :math:`AC \perp BD` and :math:`AC = BD`).

Mapping Chapter I to ``geometor.model`` & ``geometor.elements``
---------------------------------------------------------------

* **Symbolic DAG Representation**: Altshiller-Court's § 1 notation—circles :math:`(A, r)` and line intersections :math:`M = (PQ, RS)`—maps one-to-one onto ``geometor.model`` primitives, where every constructed point retains its exact SymPy algebraic coordinates in a quadratic extension tower of :math:`\mathbb{Q}`.
* **The Twelve Fundamental Loci (§ 11, Folios `0030`–`0036`)**:
  - *Linear Loci*: Parallel pair (Locus 3), :term:`mediator <mediator>` (Locus 4, :cite:`Euclid I.10–11 <euclid:elements>`), angle bisectors (Locus 5), and constant difference of squares :math:`AM^2 - BM^2 = d^2` (Locus 12 — the point-circle precursor of the :term:`radical axis <radical-axis>` in Chapter VIII, § 422).
  - *Circular Loci*: Circle :math:`(A, r)` (Locus 1), concentric tangent-length & subtended-angle circles (Loci 2, 6, 9), :term:`capable arc <subtended-angle-locus>` & Thales' circle (Locus 7, :cite:`Euclid III.21, III.31 <euclid:elements>`), chord-midpoint circle on :math:`OP` (Locus 8), Apollonius' median circle :math:`OM^2 = \tfrac{1}{2}s^2 - a^2` (Locus 10), and the :term:`Apollonian circle <apollonian-circle>` :math:`AM : MB = p : q` (Locus 11, :person:`Apollonius <apollonius>`).
* **Transformational & Unfolding Previews**: § 8 previews parallel translation (:cite:`Petersen <pt>`), § 9 previews :math:`90^\circ` rotational congruence (:person:`Castillon <castillon>`), and § 15 introduces :term:`indirect elements <indirect-elements>` by unfolding perimeter :math:`2p` into auxiliary triangle :math:`AEF` with vertex angle :math:`90^\circ + \tfrac{1}{2}A`.

Cross-Repository GEOMETOR Links
-------------------------------

* ``geometor/elements (I.1–I.47, III.20–III.36, IV.2–IV.5, VI.9–VI.13)``
* ``geometor/fundamentals``
* ``geometor/pappus (Book VII Analysis/Synthesis)``

Folio-by-Folio Diplomatic & Constructive Notes
----------------------------------------------

Folio 0020 (Page 1) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0019 (Page [xx], Blank Verso)
- **Current Folio** (``0020.rst``): Page ``1``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0021 (Page 2, § 2 concluded, Exercises 1–24, and § 3)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Opening recto of Chapter 1 (printed page ``1``; tall chapter numeral ``1`` above ``GEOMETRIC CONSTRUCTIONS``, section ``A. PRELIMINARIES``), defining Altshiller-Court's global symbolic conventions (§ 1) and beginning the catalog of Euclidean elementary constructions (§ 2).
- **Document Headings on Folio**: ``1 GEOMETRIC CONSTRUCTIONS``, ``A. PRELIMINARIES``, ``1. Notation.``, ``2. Basic Constructions.``
- **Line-Break Hyphenations Resolved**: ``circum-center``, ``ex-ternally``

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note two signature conventions of Altshiller-Court (§ 1): (1) :math:`2p` denotes the perimeter so that :math:`p` is the semiperimeter (where many British texts write :math:`2s` and :math:`s`); (2) :math:`(A, r)` and :math:`M = (PQ, RS)` correspond directly to ``model.construct_circle_by_center_and_point`` and line-line intersection nodes in ``geometor.model``. The three § 2 items on this page invoke :cite:`Euclid VI.9, VI.10, and VI.12 <euclid:elements>`.

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0020.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0021 (Page 2) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0020 (Page 1, §§ 1–2)
- **Current Folio** (``0021.rst``): Page ``2``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0022 (Page 3, Section B, §§ 4–5)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``2`` (running header ``2 / GEOMETRIC CONSTRUCTIONS / [Ch. I, §§ 2, 3``), completing § 2 (*Basic Constructions*), presenting the 24 Preliminary ``EXERCISES``, and adding § 3 (*Suggestion*).
- **Document Headings on Folio**: ``EXERCISES``, ``3. Suggestion.``
- **Line-Break Hyphenations Resolved**: ``tri-angle``, ``hypote-nuse``, ``con-ventional``

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raw OCR omitted Exercise 7 (:math:`A, h_a, t_a`) and garbled Exercise 5 (:math:`m_a`), Exercise 14 (:math:`\angle ABD`), Exercise 21 (:math:`AB^2 : AC^2 = BD : DC`), and Exercise 23 (:math:`x^2 : a^2 = p : q`); all verified against ``0021.png``. The § 2 constructions correspond to :cite:`Euclid VI.13, II.14, I.47, and III.17 <euclid:elements>`.

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0021.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0022 (Page 3) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0021 (Page 2, §§ 2–3)
- **Current Folio** (``0022.rst``): Page ``3``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0023 (Page 4, Fig. 1, solution of § 5, and statement of § 6)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``3`` (running header ``Ch. I, §§ 4, 5] / GENERAL METHOD OF SOLUTION / 3``), opening Section B with § 4 (*Analytic Method* — defining Analysis, Construction, Proof, Discussion) and stating § 5 (*Problem*).
- **Document Headings on Folio**: ``B. GENERAL METHOD OF SOLUTION OF CONSTRUCTION PROBLEMS``, ``4. Analytic Method.``, ``5. Problem.``
- **Line-Break Hyphenations Resolved**: ``applica-tions``, ``follow-ing``, ``approxi-mately``, ``con-struction``, ``re-quirements``, ``possi-bility``

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Altshiller-Court's four-part schema in § 4 restates for modern collegiate instruction the classical Greek method of *analysis* and *synthesis* preserved by :person:`Pappus of Alexandria <pappus>` in :cite:`Collection, Book VII <pappus:collection:VII>` (with *Discussion* corresponding to Greek *diorismos*, and the opening example invoking :cite:`Euclid I.1 <euclid:elements>`).

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0022.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0023 (Page 4) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0022 (Page 3, §§ 4–5)
- **Current Folio** (``0023.rst``): Page ``4``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0024 (Page 5, Fig. 2 and solution of § 6)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``4`` (running header ``4 / GEOMETRIC CONSTRUCTIONS / [Ch. I, §§ 5, 6``), presenting ``FIG. 1`` (``0023.g1.png``), the four-part solution of § 5, and the italicized enunciation of § 6 (*Problem*).
- **Document Headings on Folio**: ``6. Problem.``
- **Line-Break Hyphenations Resolved**: None

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0023.g1.png`` (bbox ``[383, 162, 664, 611]``, white-point ``238``): Fig. 1. Secant CA'B' through C meeting parallel lines x, y so that AA' : BB' = p : q (§ 5).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In § 5, :math:`O` and :math:`O'` are harmonic conjugates with respect to :math:`A` and :math:`B` (anticipating Chapter II, § 59). When :math:`p = q`, the internal division point :math:`O'` is the midpoint of :math:`AB`, while the external division point :math:`O` recedes to infinity along :math:`AB`, so the second solution becomes the line through :math:`C` parallel to :math:`AB`!

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0023.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0024 (Page 5) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0023 (Page 4, §§ 5–6)
- **Current Folio** (``0024.rst``): Page ``5``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0025 (Page 6, conclusion of § 6 Discussion, Fig. 3, and § 7)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``5`` (running header ``Ch. I, § 6] / GENERAL METHOD OF SOLUTION / 5``), presenting the Analysis, Construction, Proof, ``FIG. 2`` (``0024.g1.png``), and Discussion of § 6.
- **Document Headings on Folio**: None
- **Line-Break Hyphenations Resolved**: None

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0024.g1.png`` (bbox ``[407, 1018, 608, 488]``, white-point ``238``): Fig. 2. Secant MBA from external point M cutting circle (O) so that central angle AOB equals angle M (§ 6).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Remarkable economy of construction in ``geometor.model``: given circle :math:`(O, R)` and exterior point :math:`M`, a single compass operation ``circle(M, O)`` immediately constructs both solution secants :math:`MA` and :math:`MA'` in two steps!

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0024.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0025 (Page 6) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0024 (Page 5, § 6)
- **Current Folio** (``0025.rst``): Page ``6``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0026 (Page 7, § 8, Figs. 4–5)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``6`` (running header ``6 / GEOMETRIC CONSTRUCTIONS / [Ch. I, §§ 6, 7``), concluding the Discussion of § 6 and presenting ``FIG. 3`` (``0025.g1.png``) and the complete four-part solution of § 7.
- **Document Headings on Folio**: ``7. Problem.``
- **Line-Break Hyphenations Resolved**: ``tri-angle``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0025.g1.png`` (bbox ``[380, 530, 663, 513]``, white-point ``238``): Fig. 3. Points D, E on sides AB, AC of triangle ABC such that AD = DE = EC (§ 7).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Problem 7 is a classic gem of synthetic analysis (also solvable by homothecy in Chapter II): by projecting the unknown broken equal chain :math:`AD = DE = EC` from :math:`A` onto :math:`B`, the scale ambiguity vanishes and :math:`K, L` are constructed by two compass transfers of :math:`BA`. When :math:`\angle A = 90^\circ`, :math:`K` coincides with :math:`A`.

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0025.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0026 (Page 7) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0025 (Page 6, §§ 6–7)
- **Current Folio** (``0026.rst``): Page ``7``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0027 (Page 8, § 9, Fig. 6)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``7`` (running header ``Ch. I, § 8] / GENERAL METHOD OF SOLUTION / 7``), presenting the complete solution of § 8 together with side-by-side diagrams ``FIG. 4`` (``0026.g1.png``) and ``FIG. 5`` (``0026.g2.png``).
- **Document Headings on Folio**: ``8. Problem.``
- **Line-Break Hyphenations Resolved**: ``direc-tion``, ``con-structed``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0026.g1.png`` (bbox ``[95, 1248, 585, 424]``, white-point ``238``): Fig. 4. Points P, Q on circles (A), (B) at given distance m and given direction — Analysis (§ 8).
- ``0026.g2.png`` (bbox ``[720, 1225, 606, 439]``, white-point ``238``): Fig. 5. Four solutions for points on circles (A), (B) at given distance and direction (§ 8).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Problem 8 exemplifies Julius :person:`Petersen's <petersen>` *Method of Parallel Translation* (:cite:`Methods and Theories <pt>`): translating circle :math:`(A)` by :math:`\pm\vec{m}` yields two circles centered at :math:`R, R'` whose intersections with :math:`(B)` give up to four solutions :math:`P_1Q_1, P_2Q_2, P_1'Q_1', P_2'Q_2'` (Fig. 5).

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0026.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0027 (Page 8) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0026 (Page 7, § 8)
- **Current Folio** (``0027.rst``): Page ``8``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0028 (Page 9, Fig. 7, Proof & Discussion of § 9, and § 10)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``8`` (running header ``8 / GEOMETRIC CONSTRUCTIONS / [Ch. I, § 9``), stating § 9 (circumscribing a square through four given points), giving two distinct proofs in the Analysis (one by :math:`90^\circ` rotation, one by congruent right triangles), ``FIG. 6`` (``0027.g1.png``), and the Construction.
- **Document Headings on Folio**: ``9. Problem.``
- **Line-Break Hyphenations Resolved**: ``as-sumption``, ``paral-lel``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0027.g1.png`` (bbox ``[313, 668, 801, 722]``, white-point ``238``): Fig. 6. Construction of a square PQRS whose sides pass through four given points A, B, C, D (§ 9).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Notice how Altshiller-Court pairs a transformational argument (:math:`90^\circ` rotation around the center of the square) with a pure Euclidean congruence argument (:math:`\triangle PQL \cong \triangle QRK`). Compare :person:`Castillon's <castillon>` and :cite:`Catalan's <cn>` classical incidence problems.

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0027.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0028 (Page 9) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0027 (Page 8, § 9)
- **Current Folio** (``0028.rst``): Page ``9``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0029 (Page 10, conclusion of § 10 and Exercises 1–13)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``9`` (running header ``Ch. I, §§ 9, 10] / GENERAL METHOD OF SOLUTION / 9``), displaying ``FIG. 7`` (``0028.g1.png``), the Proof and full combinatoric/poristic Discussion of § 9, and the opening paragraph of § 10 (*Suggestions*).
- **Document Headings on Folio**: ``10. Suggestions.``
- **Line-Break Hyphenations Resolved**: ``tri-angles``, ``equi-angular``, ``sym-metric``, ``ac-cordingly``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0028.g1.png`` (bbox ``[327, 160, 774, 596]``, white-point ``238``): Fig. 7. General configuration of six squares whose sides pass through four given points A, B, C, D (§ 9).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The poristic case in the Discussion (:math:`F = B`, when :math:`AC \perp BD` and :math:`AC = BD`, an *orthodiagonal equidiagonal* quadruple) yields a 1-parameter infinity of circumscribed squares—a striking preview of Chapter IV (*Other Quadrilaterals*, §§ 271–282).

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0028.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0029 (Page 10) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0028 (Page 9, §§ 9–10)
- **Current Folio** (``0029.rst``): Page ``10``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0030 (Page 11, Exercise 14 and Section C: Geometric Loci, § 11)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``10`` (running header ``10 / GEOMETRIC CONSTRUCTIONS / [Ch. I, § 10``), completing § 10 (*Suggestions* on exact ruler-and-compass execution and exhaustive *Discussion* branching) and listing Exercises 1–13.
- **Document Headings on Folio**: ``EXERCISES``
- **Line-Break Hyphenations Resolved**: ``construc-tion``, ``opera-tions``, ``inter-cept``, ``com-mon``

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Notice how Exercises 6 and 7 quietly anticipate Chapter VIII (*Circles*): Exercise 6 constructs a circle bisecting a given circle (:math:`R_1^2 = d^2 + R^2`), while Exercise 7 constructs a circle whose :term:`radical axis <radical-axis>` with a given circle has a prescribed direction.

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0029.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0030 (Page 11) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0029 (Page 10, § 10, Exercises 1–13)
- **Current Folio** (``0030.rst``): Page ``11``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0031 (Page 12, Fig. 8 and Loci 1–7)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``11`` (running header ``Ch. I, §§ 10, 11] / GEOMETRIC LOCI / 11``), concluding Section B with Exercise 14 and opening Section C (*Geometric Loci*) with the theoretical introduction to § 11 (*Important Loci*).
- **Document Headings on Folio**: ``C. GEOMETRIC LOCI``, ``11. Important Loci.``
- **Line-Break Hyphenations Resolved**: ``geo-metric``, ``dis-carded``, ``equidis-tant``, ``bi-sectors``

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Altshiller-Court's exposition of the *Method of Loci* (relaxing one constraint at a time to intersect two 1-dimensional straightedge-and-compass loci) directly follows :person:`Plato's <pappus>` school, :cite:`Simon L'Huilier (1809) <lhr>`, and :cite:`Julius Petersen (1866/1879) <pt>`. In Exercise 14, the hypotenuse of each right subtriangle is a side (:math:`b = 2R_1, c = 2R_2`)!

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0030.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0031 (Page 12) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0030 (Page 11, § 11 introduction)
- **Current Folio** (``0031.rst``): Page ``12``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0032 (Page 13, proof of Locus 7, Fig. 9, and Locus 8)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``12`` (running header ``12 / GEOMETRIC CONSTRUCTIONS / [Ch. I, § 11``), displaying ``FIG. 8`` (``0031.g1.png``) at top and enunciating ``LOCUS 1`` through ``LOCUS 7`` (introducing the term *mediator* in ``LOCUS 4``). Ends mid-sentence across the page turn.
- **Document Headings on Folio**: None
- **Line-Break Hyphenations Resolved**: ``dis-tance``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0031.g1.png`` (bbox ``[433, 162, 553, 673]``, white-point ``238``): Fig. 8. Arc of circle AMB as the locus of points on one side of AB subtending a given angle, with tangent AT (§ 11, Locus 7).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The term *mediator* (French *médiatrice*, coined by Joseph :person:`Neuberg <neuberg>`) introduced here in Locus 4 is used systematically throughout *College Geometry* (e.g., § 15, § 68).

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0031.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0032 (Page 13) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0031 (Page 12, Loci 1–7: '...Pass a circle through the three points')
- **Current Folio** (``0032.rst``): Page ``13``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0033 (Page 14, exterior case of Locus 8, Locus 9, Fig. 10, and Locus 10)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``13`` (running header ``Ch. I, § 11] / GEOMETRIC LOCI / 13``), completing the double-inclusion proof and tangent construction of ``LOCUS 7`` (including Thales' right-angle corollary), and presenting ``LOCUS 8`` with ``FIG. 9`` (``0032.g1.png``).
- **Document Headings on Folio**: None
- **Line-Break Hyphenations Resolved**: ``semi-circles``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0032.g1.png`` (bbox ``[451, 1291, 518, 514]``, white-point ``238``): Fig. 9. Circular locus of the midpoints M of chords AB of circle (O) passing through a fixed point P (§ 11, Locus 8).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Notice Altshiller-Court's rigor on every locus proof: he establishes both *inclusiveness* (every point on the path satisfies the condition) and *exclusiveness* (no point off the path satisfies it, or conversely every point on the path belongs to the locus). Locus 7 rests on :cite:`Euclid III.21, III.31, III.32, and III.33 <euclid:elements>`.

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0032.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0033 (Page 14) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0032 (Page 13, Loci 7–8)
- **Current Folio** (``0033.rst``): Page ``14``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0034 (Page 15, conclusion of Locus 10, Fig. 11, and Locus 11: Apollonian circle)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``14`` (running header ``14 / GEOMETRIC CONSTRUCTIONS / [Ch. I, § 11``), treating the exterior-point restriction of ``LOCUS 8``, stating ``LOCUS 9``, displaying ``FIG. 10`` (``0033.g1.png``), and deriving ``LOCUS 10`` via Apollonius' median theorem. Ends mid-sentence.
- **Document Headings on Folio**: None
- **Line-Break Hyphenations Resolved**: ``dis-tances``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0033.g1.png`` (bbox ``[406, 488, 612, 386]``, white-point ``238``): Fig. 10. Locus of a point M the sum of the squares of whose distances from A and B is constant (§ 11, Locus 10).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raw OCR dropped both :math:`\frac{1}{2}` fractions in :math:`OA = OB = \frac{1}{2} AB` and :math:`OM^2 = \frac{1}{2} s^2 - a^2`; restored from ``0033.png``. Note the implicit *diorismos* of equation (1): the locus is a real circle iff :math:`s^2 > 2a^2 = \frac{1}{2} AB^2`, degenerates to the midpoint :math:`O` when :math:`s^2 = 2a^2`, and is empty when :math:`s^2 < 2a^2`.

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0033.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0034 (Page 15) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0033 (Page 14, Loci 8–10: '...for its other leg half the')
- **Current Folio** (``0034.rst``): Page ``15``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0035 (Page 16, conclusion of Locus 11, Note, Fig. 12, and Locus 12)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``15`` (running header ``Ch. I, § 11] / GEOMETRIC LOCI / 15``), finishing the compass-and-straightedge radius construction of ``LOCUS 10`` and introducing ``LOCUS 11`` (*circle of Apollonius* / *Apollonian circle*) with ``FIG. 11`` (``0034.g1.png``) and the first half of its ``CONVERSELY`` proof.
- **Document Headings on Folio**: None
- **Line-Break Hyphenations Resolved**: ``there-fore``, ``re-quired``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0034.g1.png`` (bbox ``[318, 1005, 790, 485]``, white-point ``238``): Fig. 11. Circle of Apollonius: locus of a point M whose distances from fixed points A, B have a constant ratio p : q (§ 11, Locus 11).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Locus 11 (:person:`Apollonius of Perga <apollonius>`, *Plane Loci* II) is one of the pillars of *College Geometry*: :math:`(A, B; C, D) = -1` is a :term:`harmonic range <harmonic-division>`, reappearing in Chapter II (§ 61), Chapter VIII (coaxal limiting points, § 448), and Chapter X (the three Apollonian circles of a triangle meeting in the :term:`isodynamic points <isodynamic-points>` :math:`X(15), X(16)`, §§ 597–606).

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0034.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0035 (Page 16) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0034 (Page 15, Locus 11: 'therefore: ME = MF.')
- **Current Folio** (``0035.rst``): Page ``16``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0036 (Page 17, conclusion of Locus 12, Exercises 1–4, and § 12)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``16`` (running header ``16 / GEOMETRIC CONSTRUCTIONS / [Ch. I, § 11``), completing the converse proof and Socratic query of ``LOCUS 11`` (plus ``Note`` on the twin Apollonian circles), displaying ``FIG. 12`` (``0035.g1.png``), and beginning ``LOCUS 12``.
- **Document Headings on Folio**: None
- **Line-Break Hyphenations Resolved**: ``seg-ment``, ``state-ment``, ``tri-angles``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0035.g1.png`` (bbox ``[419, 1020, 585, 368]``, white-point ``238``): Fig. 12. Perpendicular line locus of a point M where AM² - BM² = d² is constant (§ 11, Locus 12).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Answer to Altshiller-Court's Socratic question on ``LOCUS 11``: the hypothesis that :math:`M` lies on the circle with diameter :math:`CD` is used strictly in asserting that :math:`\angle CMD` is a right angle (by Thales' locus, Locus 7)! And ``LOCUS 12`` (:math:`AM^2 - BM^2 = d^2`) is precisely the point-circle case of the :term:`radical axis <radical-axis>` of two circles (Chapter VIII, § 422).

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0035.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0036 (Page 17) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0035 (Page 16, Locus 12: '(AC - BC)(AC + BC) = d^2,')
- **Current Folio** (``0036.rst``): Page ``17``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0037 (Page 18, Fig. 13, Construction of § 12, and § 13)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``17`` (running header ``Ch. I, §§ 11, 12] / GEOMETRIC LOCI / 17``), concluding ``LOCUS 12`` (constructing :math:`AC - BC = d^2 \div a` via fourth proportional and sum-and-difference of segments, § 2), listing Locus Exercises 1–4, and presenting the enunciation and Analysis of § 12 (*Problem*).
- **Document Headings on Folio**: ``EXERCISES``, ``12. Problem.``
- **Line-Break Hyphenations Resolved**: ``con-sider``, ``con-stant``

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raw OCR corrupted :math:`AC - BC = d^2 \div a` to ``dl-, a``; verified against ``0036.png``. Note Exercise 1 (the median through :math:`A` is the locus of :math:`M = (BE, CD)` by harmonic properties of trapezoids, Ch. VII) and Exercise 3 (an Apollonian circle on :math:`AC` passing through :math:`B`, since :math:`MB` bisects :math:`\angle AMC` iff :math:`MA : MC = AB : BC`!).

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0036.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0037 (Page 18) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0036 (Page 17, §§ 11–12)
- **Current Folio** (``0037.rst``): Page ``18``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0038 (Page 19, Figs. 14–15, Discussion of § 13, and § 14)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``18`` (running header ``18 / GEOMETRIC CONSTRUCTIONS / [Ch. I, §§ 12, 13``), displaying ``FIG. 13`` (``0037.g1.png``), the Construction of § 12, and the Analysis, Construction, and Proof of § 13 (*Problem*).
- **Document Headings on Folio**: ``13. Problem.``
- **Line-Break Hyphenations Resolved**: ``re-spectively``, ``trape-zoid``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0037.g1.png`` (bbox ``[403, 162, 618, 466]``, white-point ``238``): Fig. 13. Circle (O) passing through A and B and subtending a given angle at external point C (§ 12).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In § 12, notice that :math:`O` also lies on the :term:`mediator <mediator>` of :math:`AB`, which is simultaneously the radical axis of the two Apollonian circles :math:`(EF)` and :math:`(GH)`—giving at most two centers :math:`O, O'`! In § 13, Locus 9 and Locus 1 intersect cleanly at :math:`F`.

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0037.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0038 (Page 19) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0037 (Page 18, §§ 12–13)
- **Current Folio** (``0038.rst``): Page ``19``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0039 (Page 20, Fig. 16, conclusion of § 14, and Exercises 1–16)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``19`` (running header ``Ch. I, §§ 13, 14] / GEOMETRIC LOCI / 19``), presenting the Discussion of § 13 with side-by-side ``FIG. 14`` (``0038.g1.png``) and ``FIG. 15`` (``0038.g2.png``), and starting § 14 (*Problem*).
- **Document Headings on Folio**: ``14. Problem.``
- **Line-Break Hyphenations Resolved**: ``intersec-tion``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0038.g1.png`` (bbox ``[107, 458, 607, 619]``, white-point ``238``): Fig. 14. Parallel chords AC, BD through A, B in circle (O) having a given sum 2s (§ 13).
- ``0038.g2.png`` (bbox ``[732, 543, 593, 530]``, white-point ``238``): Fig. 15. Case where tangent crosses chord AB, yielding difference of bases 2EF (§ 13).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Raw OCR misread ``2 OE`` as ``2 OR`` and ``FIG. 15`` as ``FIG. 16``; verified against ``0038.png``. Note the topological transition at :math:`s = EG` in § 13: when :math:`s < EG`, the parallel chords cross inside the circle so that :math:`2\,EF = |AC - BD|` instead of :math:`AC + BD`, immediately solving the companion difference problem!

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0038.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0039 (Page 20) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0038 (Page 19, §§ 13–14)
- **Current Folio** (``0039.rst``): Page ``20``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0040 (Page 21, Exercises 17–23 and Section D: Indirect Elements, § 15, Fig. 17)

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``20`` (running header ``20 / GEOMETRIC CONSTRUCTIONS / [Ch. I, § 14``), displaying ``FIG. 16`` (``0039.g1.png``), completing § 14 via Locus 7, and listing Locus Exercises 1–16.
- **Document Headings on Folio**: ``EXERCISES``
- **Line-Break Hyphenations Resolved**: ``dis-tances``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0039.g1.png`` (bbox ``[409, 162, 608, 553]``, white-point ``238``): Fig. 16. Point M on circle (A, B) whose joins AM, BM cut line FPQ in given ratio FP : FQ from F (§ 14).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Look at Exercises 4–6 (:math:`a, h_a, b:c`; :math:`a, m_a, b:c`; :math:`a, t_a, b:c`): each intersects the :term:`Apollonian circle <apollonian-circle>` for :math:`b:c` on base :math:`BC` with a second locus (parallel line at height :math:`h_a` in Ex. 4, circle :math:`(M_a, m_a)` in Ex. 5, and a neat circle locus in Ex. 6). Exercise 16 intersects two Apollonian circles—foreshadowing the :term:`isodynamic points <isodynamic-points>` :math:`X(15), X(16)` in Chapter X (§ 606)!

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0039.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)

Folio 0040 (Page 21) — Diplomatic & Mathematical Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Summary & Folio Continuity
^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Preceding Folio**: Folio 0039 (Page 20, § 14, Exercises 1–16)
- **Current Folio** (``0040.rst``): Page ``21``, Chapter I [``01_geometric_constructions``] — Status: ``ok``
- **Following Folio**: Folio 0041 (Page 22, conclusion of § 15: 'and therefore the angle EAF is known. The altitude AD of the triangle ABC is also the altitude of AEF...')

Structural & Diplomatic Observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Overview**: Page ``21`` (running header ``Ch. I, §§ 14, 15] / INDIRECT ELEMENTS / 21``), completing Locus Exercises 17–23, introducing Section D (*Indirect Elements*), and presenting § 15 (*Problem*: constructing :math:`\triangle ABC` from :math:`(2p, A, h_a)`) with ``FIG. 17`` (``0040.g1.png``). Ends with a comma at the bottom of page ``21``, continuing onto folio ``0041`` (page ``22``).
- **Document Headings on Folio**: ``D. INDIRECT ELEMENTS``, ``15. Problem.``
- **Line-Break Hyphenations Resolved**: ``adja-cent``, ``dif-ference``, ``neces-sary``, ``op-posite``

Calibrated Diagrams on Folio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0040.g1.png`` (bbox ``[247, 1400, 923, 330]``, white-point ``238``): Fig. 17. Construction of triangle ABC given perimeter 2p, vertical angle A, and altitude h_a via indirect triangle AEF (§ 15).

Mathematical & Constructive Commentary
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In § 15, unfolding :math:`BA` and :math:`CA` onto line :math:`BC` turns the indirect perimeter :math:`2p` into the single segment :math:`EF = 2p` of auxiliary triangle :math:`AEF`, which is constructed from base :math:`EF = 2p`, capable arc for :math:`\angle EAF = 90^\circ + \frac{1}{2}A` (Locus 7), and parallel line at height :math:`h_a` (Locus 3); on folio ``0041`` (p. 22), vertices :math:`B, C` are recovered as the traces on :math:`EF` of the :term:`mediators <mediator>` of :math:`AE` and :math:`AF`!

Scan Quality & Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **Archival Scan**: ``01_geometric_constructions/0040.png`` (300 DPI, ``1421 × 2225`` px)
- **Verification Status**: ``ok`` (visually verified against raster scan)
