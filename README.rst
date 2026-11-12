==========================
GEOMETOR • altshiller-court
==========================

Digital scriptorium, structural breakdown, and multi-track **Book Codex** edition of
**Nathan Altshiller-Court's** *College Geometry: An Introduction to the Modern Geometry
of the Triangle and the Circle* (Revised & Enlarged 2nd Edition, Barnes & Noble, 1952;
Dover republication, 2007, ISBN ``978-0-486-45805-2``).

Overview
--------

Altshiller-Court's *College Geometry* (699 numbered articles across 10 chapters,
plus extensive *Historical and Bibliographical Notes*) serves within the **GEOMETOR**
ecosystem as the definitive 20th-century synthetic bridge connecting:

- **Euclid's** *Elements* (``geometor/euclid`` & ``geometor/elements``): Direct compass-and-straightedge
  deductions from Books I–VI.
- **Pappus of Alexandria & Harmonic Projectivity** (``geometor/pappus``): The Problem of Pappus
  (§ 84), Menelaus & Ceva transversals (Ch. VI), Harmonic Division (Ch. VII), Poles & Polars,
  and Desargues' Theorem (§ 343).
- **Constructive Methodology** (``geometor/fundamentals``): Chapter I's celebrated four-fold
  pattern for geometric construction problems—**Analysis, Construction, Proof, Discussion**—together
  with the **Method of Geometric Loci**, **Indirect Elements**, and **Similitude & Homothecy**.
- **Clark Kimberling's** *Encyclopedia of Triangle Centers* (``geometor/etc``): Classical synthetic
  foundations for ``X(1)`` Incenter, ``X(2)`` Centroid, ``X(3)`` Circumcenter, ``X(4)`` Orthocenter,
  ``X(5)`` Nine-Point Center, ``X(6)`` Symmedian / Lemoine Point, ``X(7)`` Gergonne Point,
  ``X(8)`` Nagel Point, ``X(10)`` Spieker Center, ``X(11)`` Feuerbach Point, ``X(15), X(16)`` Isodynamic Points,
  ``X(98)`` Tarry Point, ``X(99)`` Steiner Point, Brocard Points ``Ω, Ω'``, Tucker Circles,
  and the Orthopole.

Repository Layout
-----------------

- ``resources/college_geometry/``: Digital Scriptorium workspace discovered natively by
  ``publish folio`` (``photon-platform/publish``).

  - ``pdfs/college_geometry.pdf``: Source 334-page PDF (gitignored; preserved locally).
  - ``structure_map.json``: Complete 334-folio mapping of PDF pages ``0001``–``0334`` to printed
    pages ``[iii]``–``313``, chapters ``00_frontmatter``–``12_index``, sections, and articles ``§§ 1–699``.
  - ``00_frontmatter/`` .. ``12_index/``: Standardized 300 DPI folio PNGs (``<NNNN>.png``),
    verbatim multimodal-vision-verified RST transcriptions (``<NNNN>.rst``, wired with interactive
    ``:g:`` and ``:eq:`` geometric roles—never relying on embedded PDF OCR), scholarly notes
    (``<NNNN>.notes.rst``), and calibrated diagram bounding boxes & declarative Euclidean models
    (``<NNNN>.json`` -> ``<NNNN>.g<k>.png``, ``<NNNN>.g<k>.inverted.png``, and interactive
    ``<NNNN>.g<k>.svg``).
  - ``persons.json`` (67 entries), ``citations.json`` (31 entries), ``glossary.json`` (55 entries),
    ``folio_reviews.json``: Interactive scholarly apparatus registries.

- ``src/geometor/altshiller_court/``: Python ingestion, figure extraction, semantic SVG compiler/verifier,
  and Book Codex compiler.
- ``SVG_CREATION.md`` & ``docsrc/about/pdf-parsing-guide.rst``: Canonical guides for multimodal-vision-over-OCR
  ingestion, exact Euclidean SVG reconstruction, quantitative ink-overlap verification, and interactive text wiring.
- ``docsrc/``: Sphinx documentation source and compiled 2-Track Book Codex (``docsrc/college_geometry/``).

Workflow Commands
-----------------

.. code-block:: bash

   # 1. Extract all 334 standardized 300 DPI folio PNGs into chapter directories
   uv run --no-sync python -m geometor.altshiller_court ingest

   # 2. Extract calibrated light & dark-mode (.inverted.png) figure crops
   uv run --no-sync python -m geometor.altshiller_court graphics

   # 3. Compile declarative Euclidean geometry models into interactive euclid-graphic SVGs
   uv run --no-sync python -m geometor.altshiller_court svg

   # 4. Quantitatively verify SVG ink overlap (>= 95%) against 300 DPI scan crops
   uv run --no-sync python -m geometor.altshiller_court verify-svg

   # 5. Compile de-paginated 2-Track Book Codex and apparatus into docsrc/college_geometry/
   uv run --no-sync python -m geometor.altshiller_court compile

   # 6. Inspect edition transcription, diagram, SVG, and review status
   uv run --no-sync python -m geometor.altshiller_court status

   # 7. Launch interactive Folio Review workbench
   publish folio

   # 8. Build HTML documentation into docs/
   publish build
