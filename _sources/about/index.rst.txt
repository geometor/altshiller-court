:navigation: footer
:nav_title: About
:title: About

.. _about-altshiller-court:

Nathan Altshiller-Court & the Digital Scriptorium
=================================================

.. rubric:: Life, Geometric Pedagogy, and Symbolic Reconstruction in GEOMETOR

Nathan Altshiller-Court (1881–1968)
-----------------------------------

For the complete scholarly biography, academic career at the University of Oklahoma, and bibliography of published treatises for Nathan Altshiller-Court, see his profile in the :ref:`Biographical Register <person-altshiller-court>`.

Digital Scriptorium Methodology
-------------------------------

Following the GEOMETOR Digital Scriptorium architecture established in ``geometor/euclid`` and ``geometor/hoenen`` and powered by ``photon-platform/publish``:

1. **Archival Fidelity (`resources/college_geometry/`)**: Every PDF page (`0001`–`0334`) is rasterized at 300 DPI (`1421 × 2225` px) and organized into 13 structural directories (`00_frontmatter` through `12_index`) governed by ``structure_map.json``.
2. **Atomic Folio Verification (`publish folio`)**: Each folio is transcribed into an atomic ``<NNNN>.rst`` file paired with diplomatic/mathematical notes in ``<NNNN>.notes.rst``, bounding-box figure coordinates in ``<NNNN>.json``, normalized light/dark diagram crops (``<NNNN>.g<k>.png`` and ``.inverted.png``), and verification checklists in ``folio_reviews.json``.
3. **Interactive Semantic SVG Diagrams (`svg_compiler.py`)**: Calibrated 300-DPI crops are reconstructed into exact Euclidean vector models inside ``<NNNN>.json`` (`99.97%`–`100.00%` ink overlap) and compiled into inline ``euclid-graphic`` SVGs wired to ``:g:``, ``:eq:``, ``.. enunciation::``, and ``.. assertion::`` roles and directives.
4. **Hierarchical Item-Per-Page Book Codex (`docsrc/college_geometry/`)**: ``geometor.altshiller_court.compile_edition`` and ``codex_items`` decompose depaginated folios into a multi-level Euclid-style ``.. collection::`` hierarchy (``Book → Chapters → Sections → Items → Loci``), giving every article, problem, locus, and exercise set its own dedicated web page (`index.rst`), co-located ``.euclid-graphic`` SVG(s), marginal ``.. folio::`` milestones, and paired ``Commentary`` track (`commentary.rst`).
5. **Bridge to Symbolic Geometry (`geometor.model`)**: Altshiller-Court's constructive problems (`Analysis`, `Construction`, `Proof`, `Discussion`) translate directly into exact algebraic ruler-and-compass DAGs in ``geometor/model``, harmonic range detectors in ``geometor/divine``, and Kimberling center catalogs in ``geometor/etc``.

.. toctree::
   :maxdepth: 1
   :caption: Methodology Guides

   pdf-parsing-guide
