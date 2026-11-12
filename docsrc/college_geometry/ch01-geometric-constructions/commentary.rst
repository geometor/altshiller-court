:layout: book
:type: commentary
:title: Commentary on Chapter I: Geometric Constructions
:folio: 0020
:page: 1
:folios: 0020–0052
:pages: 1–33

.. _ch01-geometric-constructions-commentary:

Commentary on Chapter I: Geometric Constructions
================================================

Back to :ref:`Chapter I: Geometric Constructions <ch01-geometric-constructions>`.

.. rubric:: Constructive Analysis, Historical Provenance & GEOMETOR Notes (0020–0052, pp. 1–33)

Constructive Architecture & Symbolic Modeling (§§ 1–22)
-------------------------------------------------------

Chapter I lays down the operational grammar of the entire book across 33 verified folios (``0020``–``0052``, pp. ``1``–``33``), 22 interactive ``.euclid-graphic`` diagrams (``Figs. 1–22``), and 167 exercises. Every ruler-and-compass construction is governed by :person:`Pappus' <pappus>` four-stage :term:`analytic method <analytic-method>` (:cite:`Collection, Book VII <pappus:collection:VII>`):

1. :term:`Analysis <analysis-step>` — Assume the required configuration already exists and trace algebraic/synthetic incidences back to known data.
2. :term:`Construction <construction-step>` — Execute elementary straightedge (``line(P, Q)``) and compass (``circle(A, r)``) steps in forward topological order.
3. :term:`Proof <proof-step>` — Verify deductively that the constructed object satisfies every hypothesis.
4. :term:`Discussion <discussion-step>` (*Diorismos*) — Determine exact existence inequalities (``s < 2 OE``, ``a < b + c``, ``a > b - c``), count multiplicity of solutions (``0, 1, 2, 3, 4, 6``, or :math:`\infty`), and identify poristic degeneracies (as in :ref:`§ 9 <ch01-art-009>` when :math:`AC \perp BD` and :math:`AC = BD`).

Mapping Chapter I to ``geometor.model`` & ``geometor.elements``
---------------------------------------------------------------

* **Symbolic DAG Representation**: Altshiller-Court's :ref:`§ 1 <ch01-art-001>` notation—circles :math:`(A, r)` and line intersections :math:`M = (PQ, RS)`—maps one-to-one onto ``geometor.model`` primitives, where every constructed point retains its exact SymPy algebraic coordinates in a quadratic extension tower of :math:`\mathbb{Q}`.
* **The Twelve Fundamental Loci (:ref:`§ 11 <ch01-art-011>`, Folios ``0030``–``0036``)**:
  - *Linear Loci*: Parallel pair (:ref:`Locus 3 <ch01-locus-03>`), :term:`mediator <mediator>` (:ref:`Locus 4 <ch01-locus-04>`, :cite:`Euclid I.10–11 <euclid:elements>`), angle bisectors (:ref:`Locus 5 <ch01-locus-05>`), and constant difference of squares :math:`AM^2 - BM^2 = d^2` (:ref:`Locus 12 <ch01-locus-12>` — point-circle precursor of the :term:`radical axis <radical-axis>` in Chapter VIII, § 422).
  - *Circular Loci*: Circle :math:`(A, r)` (:ref:`Locus 1 <ch01-locus-01>`), concentric tangent-length & subtended-angle circles (:ref:`Loci 2 <ch01-locus-02>`, :ref:`6 <ch01-locus-06>`, :ref:`9 <ch01-locus-09>`), :term:`capable arc <subtended-angle-locus>` & Thales' circle (:ref:`Locus 7 <ch01-locus-07>`, :cite:`Euclid III.21, III.31 <euclid:elements>`), chord-midpoint circle on :math:`OP` (:ref:`Locus 8 <ch01-locus-08>`), Apollonius' median circle :math:`OM^2 = \tfrac{1}{2}s^2 - a^2` (:ref:`Locus 10 <ch01-locus-10>`), and the :term:`Apollonian circle <apollonian-circle>` :math:`AM : MB = p : q` (:ref:`Locus 11 <ch01-locus-11>`, :person:`Apollonius <apollonius>`).
* **Indirect Elements & Auxiliary Triangles (:ref:`Section D <ch01-d-indirect-elements>`, §§ 15–22)**: Unfolding perimeter :math:`2p` into :math:`\triangle AEF` (:ref:`§ 15 <ch01-art-015>`), side sums :math:`b + c` into :math:`\triangle BCD` (:ref:`§ 17 <ch01-art-017>`), side differences :math:`b - c` into :math:`\triangle BCD` and :math:`\triangle BCE` (:ref:`§ 18 <ch01-art-018>`, :ref:`§ 19 <ch01-art-019>`), and altitude sums/differences :math:`h_b \pm h_c` into right triangles :math:`\triangle BGH` and :math:`\triangle CGH` (:ref:`§ 20 <ch01-art-020>`, :ref:`§ 22 <ch01-art-022>`), formalizing two-element :term:`data <datum>` (:ref:`§ 21 <ch01-art-021>`).

Section & Item Commentary Index
-------------------------------

* :ref:`A. Preliminaries <ch01-a-preliminaries>`
  - :ref:`Commentary on § 1. Notation <ch01-art-001-commentary>`
  - :ref:`Commentary on § 2. Basic Constructions <ch01-art-002-commentary>`
  - :ref:`Commentary on § 2. Exercises (1–24) <ch01-art-002-exercises-commentary>`
  - :ref:`Commentary on § 3. Suggestion <ch01-art-003-commentary>`
* :ref:`B. General Method of Solution of Construction Problems <ch01-b-general-method>`
  - :ref:`Commentary on § 4. Analytic Method <ch01-art-004-commentary>`
  - :ref:`Commentary on § 5. Problem <ch01-art-005-commentary>`
  - :ref:`Commentary on § 6. Problem <ch01-art-006-commentary>`
  - :ref:`Commentary on § 7. Problem <ch01-art-007-commentary>`
  - :ref:`Commentary on § 8. Problem <ch01-art-008-commentary>`
  - :ref:`Commentary on § 9. Problem <ch01-art-009-commentary>`
  - :ref:`Commentary on § 10. Suggestions <ch01-art-010-commentary>`
  - :ref:`Commentary on § 10. Exercises (1–14) <ch01-art-010-exercises-commentary>`
* :ref:`C. Geometric Loci <ch01-c-geometric-loci>`
  - :ref:`Commentary on § 11. Important Loci <ch01-art-011-commentary>`
  - :ref:`Commentary on § 11. Exercises (1–4) <ch01-art-011-exercises-commentary>`
  - :ref:`Commentary on § 12. Problem <ch01-art-012-commentary>`
  - :ref:`Commentary on § 13. Problem <ch01-art-013-commentary>`
  - :ref:`Commentary on § 14. Problem <ch01-art-014-commentary>`
  - :ref:`Commentary on § 14. Exercises (1–23) <ch01-art-014-exercises-commentary>`
* :ref:`D. Indirect Elements <ch01-d-indirect-elements>`
  - :ref:`Commentary on § 15. Problem <ch01-art-015-commentary>`
  - :ref:`Commentary on § 16. Remark <ch01-art-016-commentary>`
  - :ref:`Commentary on § 16. Exercises (1–2) <ch01-art-016-exercises-commentary>`
  - :ref:`Commentary on § 17. Problem <ch01-art-017-commentary>`
  - :ref:`Commentary on § 17. Exercises (1–9) <ch01-art-017-exercises-commentary>`
  - :ref:`Commentary on § 18. Problem <ch01-art-018-commentary>`
  - :ref:`Commentary on § 18. Exercises (1–6) <ch01-art-018-exercises-commentary>`
  - :ref:`Commentary on § 19. Problem <ch01-art-019-commentary>`
  - :ref:`Commentary on § 19. Exercises (1–3) <ch01-art-019-exercises-commentary>`
  - :ref:`Commentary on § 20. Problem <ch01-art-020-commentary>`
  - :ref:`Commentary on § 21. Definition <ch01-art-021-commentary>`
  - :ref:`Commentary on § 21. Exercises (1–6) <ch01-art-021-exercises-commentary>`
  - :ref:`Commentary on § 22. Problem <ch01-art-022-commentary>`
  - :ref:`Commentary on § 22. Exercises (1–4) <ch01-art-022-exercises-commentary>`
  - :ref:`Commentary on Supplementary Exercises (1–16) <ch01-supplementary-exercises-commentary>`
* :ref:`Review Exercises <ch01-review-exercises>`
  - :ref:`Commentary on Constructions (1–27) <ch01-review-constructions-commentary>`
  - :ref:`Commentary on Propositions (28–58) <ch01-review-propositions-commentary>`
  - :ref:`Commentary on Loci (59–67) <ch01-review-loci-commentary>`

Cross-Repository GEOMETOR Links
-------------------------------

* ``geometor/elements (I.1–I.47, III.20–III.36, IV.2–IV.5, VI.9–VI.13)``
* ``geometor/fundamentals``
* ``geometor/pappus (Book VII Analysis/Synthesis)``
