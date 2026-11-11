:navigation: header
:order: 20
:title: About

.. _about-altshiller-court:

Nathan Altshiller-Court & the Digital Scriptorium
=================================================

.. rubric:: Life, Geometric Pedagogy, and Symbolic Reconstruction in GEOMETOR

Biography of Nathan Altshiller-Court (1881–1968)
------------------------------------------------

Born in Warsaw on January 22, 1881, **Nathan Altshiller-Court** pursued his mathematical studies in Belgium at the **University of Ghent**, earning his *Doctor of Science* in 1911 within the vibrant Franco-Belgian synthetic geometry tradition shaped by **Paul Mansion** and **Joseph Neuberg** (*Mathesis*). Emigrating to the United States, he studied at Columbia University and taught briefly at the University of Washington and the University of Colorado before joining the **University of Oklahoma** in Norman in 1916, where he served as Professor of Mathematics until his retirement in 1951.

Across half a century of scholarship, Altshiller-Court authored three enduring works:

1. *College Geometry: A Second Course in Plane Geometry for Colleges and Normal Schools* (Richmond: Johnson Publishing Co., 1925), thoroughly rewritten and expanded as *College Geometry: An Introduction to the Modern Geometry of the Triangle and the Circle* (New York: Barnes & Noble, 1952; Dover republication, 2007).
2. *Modern Pure Solid Geometry* (New York: Macmillan, 1935; 2nd ed. Chelsea, 1964), extending synthetic methods to the tetrahedron and sphere.
3. *Mathematics in Fun and in Earnest* (New York: Dial Press, 1958), philosophical and historical essays on mathematical invention and intuition.

Digital Scriptorium Methodology
-------------------------------

Following the GEOMETOR Digital Scriptorium architecture established in ``geometor/euclid`` and ``geometor/hoenen`` and powered by ``photon-platform/publish``:

1. **Archival Fidelity (`resources/college_geometry/`)**: Every PDF page (`0001`–`0334`) is rasterized at 300 DPI (`1421 × 2225` px) and organized into 13 structural directories (`00_frontmatter` through `12_index`) governed by ``structure_map.json``.
2. **Atomic Folio Verification (`publish folio`)**: Each folio is transcribed into an atomic ``<NNNN>.rst`` file paired with diplomatic/mathematical notes in ``<NNNN>.notes.rst``, bounding-box figure coordinates in ``<NNNN>.json``, normalized light/dark diagram crops (``<NNNN>.g<k>.png`` and ``.inverted.png``), and verification checklists in ``folio_reviews.json``.
3. **Interactive Semantic SVG Diagrams (`svg_compiler.py`)**: Calibrated 300-DPI crops are reconstructed into exact Euclidean vector models inside ``<NNNN>.json`` (`99.97%`–`100.00%` ink overlap) and compiled into inline ``euclid-graphic`` SVGs wired to ``:g:``, ``:eq:``, ``.. enunciation::``, and ``.. assertion::`` roles and directives.
4. **2-Track Book Codex (`docsrc/college_geometry/`)**: ``geometor.altshiller_court.compile_edition`` de-paginates consecutive folios into continuous reading chapters with marginal ``.. folio::`` milestones (`English` track) paired side-by-side with constructive and ecosystem commentary (`Commentary` track).
5. **Bridge to Symbolic Geometry (`geometor.model`)**: Altshiller-Court's constructive problems (`Analysis`, `Construction`, `Proof`, `Discussion`) translate directly into exact algebraic ruler-and-compass DAGs in ``geometor/model``, harmonic range detectors in ``geometor/divine``, and Kimberling center catalogs in ``geometor/etc``.

.. toctree::
   :maxdepth: 1
   :caption: Methodology Guides

   pdf-parsing-guide
