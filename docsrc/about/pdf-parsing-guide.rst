:title: PDF Parsing & SVG Guide

.. _pdf-parsing-guide:

Scanned PDF Optical Ingestion & Interactive SVG Vectorization
=============================================================

.. rubric:: Multimodal Vision Transcription, Semantic Structure Recovery, and Exact Vector Reconstruction

Historical mathematical treatises such as Nathan Altshiller-Court's *College Geometry* (1925 / 1952) combine dense synthetic reasoning, displayed algebraic proportions, italic and primed geometric notation, and compass-and-straightedge plates. This guide documents the canonical **GEOMETOR Digital Scriptorium** methodology for transforming archival PDF scans into an interactive, verifiable **2-Track Book Codex**.

.. important::

   **Mandatory Rule — Multimodal Vision Over OCR**

   For PDFs with scanned pages—even when an embedded OCR text stream exists inside the PDF—agents **must read the 300-DPI scan images directly** (`<NNNN>.png` and `<NNNN>.<gid>.png`) using multimodal vision to ascertain semantic structure, prose, mathematical formulas, and diagram geometry. **Never rely on embedded PDF OCR (`pdftotext`) for transcription or structural parsing.**

Why Multimodal Vision Supersedes OCR on Mathematical Scans
----------------------------------------------------------

Embedded OCR layers in scanned 19th- and 20th-century geometry books fail systematically on the exact constructs that carry mathematical meaning:

1. **Formulas, Ratios, and Fractions**: Displayed proportions such as ``FL : FA = FQ : FP``, stacked fractions like :math:`\tfrac{1}{2}\,\angle ABC`, radicals, and difference-of-squares identities (:math:`AM^2 - BM^2 = d^2`) are routinely flattened, dropped, or misread by character-level OCR.
2. **Primes, Subscripts, and Compound Labels**: Constructive geometry relies heavily on homologous point families—such as ``A, A'``, ``T, T'``, ``P_1, P_2``, and compound subscript-prime labels ``P_1', P_2'`` (e.g., Figure 5 on folio ``0026``)—as well as distinguishing circle center ``O`` from ``0`` and angle ``\angle E`` from ``L E``.
3. **Typographic Semantic Hierarchy**: Altshiller-Court encodes logical structure through typography: bold article headers (``13. Problem.``), italicized enunciations, small-caps dialectical stages (``ANALYSIS.``, ``CONSTRUCTION.``, ``PROOF.``, ``DISCUSSION.``, ``CONVERSELY.``), multi-column exercise blocks (folio ``0039``), and sentences flowing across side-by-side figures (folio ``0038``, Figures 14 and 15). Reading the scan image directly preserves every structural boundary and mid-sentence page/figure continuation.
4. **Diagram Callouts & Visual Invariants**: Optical inspection of ``<NNNN>.png`` reveals dashed auxiliary lines, tick marks on equal segments (Figure 17 on folio ``0040``), center dots, and tangency contacts that cannot be inferred from text alone.

End-to-End Pipeline
-------------------

1. Standardized 300-DPI Rasterization (``ingest.py``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``geometor.altshiller_court.ingest`` rasterizes all 334 PDF pages at 300 DPI via ``pdftoppm -png -r 300`` and routes each ``<NNNN>.png`` scan into its structural chapter directory (``00_frontmatter`` through ``12_index``) governed by ``resources/college_geometry/structure_map.json``. Body and backmatter folios obey the unbroken pagination invariant:

.. math::

   \text{PDF Folio} = \text{Printed Page} + 19 \qquad (\text{folios } 0020\text{–}0332 \leftrightarrow \text{pp. } 1\text{–}313).

2. Optical Transcription & Diplomatic Verification (``<NNNN>.rst``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each folio scan ``<NNNN>.png`` is inspected directly via multimodal vision and transcribed verbatim into ``<NNNN>.rst`` with:

- YAML/field-list provenance metadata (``:folio:``, ``:page:``, ``:book:``, ``:section:``, ``:title:``, ``:status:``).
- Exact LaTeX math (``:math:`` and ``.. math::``) verified glyph-by-glyph against the scan.
- Scholarly apparatus links (``:person:``, ``:cite:``, ``:term:``) and companion constructive commentary in ``<NNNN>.notes.rst``.

3. Calibrated Figure Cropping & Semantic SVG Compilation (``graphics.py`` & ``svg_compiler.py``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For every folio containing geometric plates:

1. **Crop Extraction**: ``<NNNN>.json`` records tight 300-DPI ``[x, y, w, h]`` bounding boxes; ``graphics.py`` normalizes paper tone to pure white ``#ffffff`` and outputs ``<NNNN>.<gid>.png`` and ``.inverted.png``.
2. **Declarative Euclidean Model (No Embedded Python Scripts)**: Inside ``<NNNN>.json``, each graphic entry stores a declarative ``"geometry"`` dictionary (``svg_scale: 0.5``, exact point coordinates, letterpress glyph centroids ``label_x``/``label_y``, and typed ``segment``, ``circle``, ``arc``, ``polygon``, and ``angle`` elements) plus ``"svg_file": "<NNNN>.<gid>.svg"``. No ``py_file`` scripts are embedded in the treatise workspace.
3. **Interactive SVG Compilation**: ``svg_compiler.py`` compiles each ``"geometry"`` model into an interactive ``<svg class="euclid-graphic" data-graphic-id="<NNNN>.<gid>">`` diagram compatible with ``photon-platform/publish`` and ``geometor_interactive.js``.
4. **Quantitative & Visual Verification**: ``verify_svg_against_scan`` rasterizes visible vector strokes back onto the 300-DPI crop grid, requiring **at least 95% pixel ink overlap** (Chapter I achieves ``99.97%``–``100.00%`` across all 22 figures), followed by direct visual inspection of RGB overlays and standalone renders.

4. Interactive Text-to-Diagram Wiring & Book Codex Compilation (``compile_edition.py``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Folio transcriptions switch ``.. picture:: <NNNN>.<gid>.svg`` and wire:

- ``:g:`` scoped geometric references (e.g., ``:g:`(O, OE) <0038.g1:( O E )>```) highlighting points, lines, circles, arcs, polygons, and angle wedges on hover or click—self-contained on each item's dedicated page.
- ``:eq:`` equality assertions (e.g., ``:eq:`BE = BA <0040.g1:/ B E / = 0040.g1:/ B A />```) activating dynamic green tick marks and angle arcs.
- ``.. enunciation::`` and ``.. assertion::`` blocks structuring problem statements, geometric loci, and deductive conclusions.

Finally, ``compile_edition.py`` and ``codex_items.py`` de-paginate consecutive folios (reflowing mid-sentence page breaks and floated figures), decompose each chapter into ``.. collection::`` sections, leaf items, and loci, and co-locate only each item's referenced ``.svg`` assets inside ``<item-slug>/`` so ``publish build`` renders inline interactive SVG thumbnails on collection cards and full interactive diagrams on item pages.
