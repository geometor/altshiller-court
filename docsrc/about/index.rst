:navigation: header
:order: 10
:nav_title: About

.. _about:
.. _about-index:
.. _about-altshiller-court:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

This critical digital edition reconstructs Nathan Altshiller-Court's landmark treatise, *College Geometry: An Introduction to the Modern Geometry of the Triangle and the Circle* (Second Edition, Revised and Enlarged, Barnes & Noble, 1952; Dover unabridged republication, 2007). Spanning 334 archival folios and 699 numbered articles, Altshiller-Court's work represents the pinnacle of 20th-century synthetic geometry, bridging classical Euclidean constructions with modern triangle and circle geometry, including similitude, homothecy, the Euler line, the nine-point circle, Feuerbach's theorem, the Wallace–Simson line, Menelaus' and Ceva's theorems, harmonic division, inversion, and the Brocard–Lemoine configuration.

Through the GEOMETOR Digital Scriptorium methodology, this edition moves beyond flat facsimile scans into an addressable, computable semantic codex. Every article, definition, theorem, problem, locus, and exercise set is extracted into dedicated semantic entities paired with atomic folio verification (``publish folio``), diplomatic transcription notes, and synchronized commentary tracks. Archival line drawings are reconstructed as calibrated, resolution-independent ``.euclid-graphic`` diagrams, enabling readers to interact directly with the underlying geometric constructions.

Within the broader GEOMETOR canon, this codex serves as the vital synthetic bridge between classical Euclidean foundations (``geometor.elements`` and ``geometor.euclid``), projective and harmonic ranges (``geometor.pappus`` and ``geometor.divine``), and the modern Kimberling triangle center taxonomy explored in ``geometor.etc``.

The GEOMETOR Mission
--------------------

The GEOMETOR project, directed by **phi ARCHITECT**, is dedicated to the systematic recovery, exact formalization, and dynamic re-expression of foundational geometric and philosophical knowledge. The mission unfolds across three essential pillars:

* **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises—elevating prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.
* **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (using ``SymPy``) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic fields rather than floating-point approximations.
* **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (via ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across ``geometor.com``.

Sources, Provenance & Methodology
---------------------------------

Archival Source & Biographical Provenance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Source Edition**: Nathan Altshiller-Court, *College Geometry: An Introduction to the Modern Geometry of the Triangle and the Circle*, Second Edition, Revised and Enlarged. New York: Barnes & Noble, Inc., 1952. Unabridged republication, Mineola, NY: Dover Publications, Inc., 2007 (ISBN ``978-0-486-45805-2``, 334 folios, 699 numbered articles).
* **Author Biography**: For the complete scholarly biography, academic career at the University of Oklahoma, and bibliography of published treatises for Nathan Altshiller-Court, see his profile in the :ref:`Biographical Register <person-altshiller-court>`.

Digital Scriptorium Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Following the GEOMETOR Digital Scriptorium architecture established in ``geometor/euclid`` and ``geometor/hoenen`` and powered by ``photon-platform/publish``:

1. **Archival Fidelity (``resources/college_geometry/``)**: Every PDF page (``0001``–``0334``) is rasterized at 300 DPI (``1421 × 2225`` px) and organized into 13 structural directories (``00_frontmatter`` through ``12_index``) governed by ``structure_map.json``.
2. **Atomic Folio Verification (``publish folio``)**: Each folio is transcribed into an atomic ``<NNNN>.rst`` file paired with diplomatic/mathematical notes in ``<NNNN>.notes.rst``, bounding-box figure coordinates in ``<NNNN>.json``, normalized light/dark diagram crops (``<NNNN>.g<k>.png`` and ``.inverted.png``), and verification checklists in ``folio_reviews.json``.
3. **Interactive Semantic SVG Diagrams (``svg_compiler.py``)**: Calibrated 300-DPI crops are reconstructed into exact Euclidean vector models inside ``<NNNN>.json`` (``99.97%``–``100.00%`` ink overlap) and compiled into inline ``euclid-graphic`` SVGs wired to ``:g:``, ``:eq:``, ``.. enunciation::``, and ``.. assertion::`` roles and directives.
4. **Hierarchical Item-Per-Page Book Codex (``docsrc/college_geometry/``)**: ``geometor.altshiller_court.compile_edition`` and ``codex_items`` decompose depaginated folios into a multi-level Euclid-style ``.. collection::`` hierarchy (``Book → Chapters → Sections → Items → Loci``), giving every article, problem, locus, and exercise set its own dedicated web page (``index.rst``), co-located ``.euclid-graphic`` SVG(s), marginal ``.. folio::`` milestones, and paired ``Commentary`` track (``commentary.rst``).
5. **Bridge to Symbolic Geometry (``geometor.model``)**: Altshiller-Court's constructive problems (*Analysis*, *Construction*, *Proof*, *Discussion*) translate directly into exact algebraic ruler-and-compass DAGs in ``geometor/model``, harmonic range detectors in ``geometor/divine``, and Kimberling center catalogs in ``geometor/etc``.

Methodology Guides & Essays
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :ref:`Scanned PDF Optical Ingestion & Interactive SVG Vectorization Guide <pdf-parsing-guide>`

.. toctree::
   :maxdepth: 1
   :hidden:

   pdf-parsing-guide
