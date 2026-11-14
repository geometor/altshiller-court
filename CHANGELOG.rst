=========
Changelog
=========

0.3.1 (2026-11-13)
------------------

- **added**: Tracked 334 300 DPI folio raster scans (``0001.png``–``0334.png``) across all 13 structural divisions of *College Geometry* to enable primary-source facsimile resolution via ``photon-platform-publish`` v0.4.0.
- **changed**: Updated ``.gitignore`` to track primary-source folio PNG scans while continuing to exclude source PDFs and built documentation.

0.3.0 (2026-11-12)
------------------

- **fixed**: Eliminated Docutils ``(INFO/1) Enumerated list start value not ordinal-1`` runner file-path messages leaking into ``.. collection::`` card titles and opening paragraphs by formatting lettered section titles as ``Section <Code> — <Title>`` instead of bare ``B.``, ``C.``, ``D.`` prefixes.
- **added**: Implemented ``hero_figures.py`` generating 15 exact symbolic ``geometor.model`` ``.euclid-graphic`` hero SVGs (zero ``sp.Float`` coordinates, deductively verified via ``assert_collinear``, ``assert_concyclic``, ``assert_perpendicular``, and ``cross_ratio``) plus calibrated folio hero SVGs so every Chapter and Section landing page and collection card displays a theme-adaptive hero diagram.
- **added**: Completed multimodal-vision folio transcription, ``.notes.rst`` commentary, and ``100.0%`` Ink-to-Vector SVG calibration (``0072.g1.svg``–``0084.g1.svg``, ``FIG. 39``–``FIG. 47``) for Chapter III (*Properties of the Triangle*, folios ``0072``–``0084``, ``§§ 54–88``: *Section A — Preliminaries*, *Section B — The Circumcircle* including ``§ 84`` *Problem of Pappus*, and *Section C — Medians* centroid concurrency) as 38 one-item-per-page propositions and exercise sets.
- **added**: Replaced scan-allocation stub tables across all remaining sections of Chapters II–X with structured scholarly synopses (``section_synopses.py``), principal theorem roadmaps, Kimberling ``X(n)`` center identifications, and cross-repository GEOMETOR links.

0.2.0 (2026-11-12)
------------------

- **refactored**: Reparsed ``docsrc/college_geometry/`` into a Euclid-style hierarchical **one-item-per-web-page** Book Codex (``Book -> Chapters -> Sections -> Items``) using ``.. collection::`` cards with inline ``.euclid-graphic`` SVG thumbnails and enunciation excerpts at every heading level.
- **added**: Completed multimodal-vision transcription, ``.notes.rst`` commentary, and quantitative Ink-to-Vector SVG calibration across the remainder of Chapter I (folios ``0041``–``0052``, ``§§ 15–22`` *D. Indirect Elements* and *Review Exercises 1–74*, ``FIG. 18``–``FIG. 22`` at ``99.97%``–``100.00%`` scan overlap).
- **added**: Dedicated sub-collection pages for ``§ 11`` (*Important Loci*, ``LOCUS 1``–``LOCUS 12``) and per-item ``commentary.rst`` tracks, updating apparatus back-links across ``205`` compiled HTML pages with zero broken references.

0.1.0 (2026-11-11)
------------------

- Initial repository scaffold for ``geometor-altshiller-court``.
- Complete 334-folio structural breakdown (``structure_map.json``) of Nathan Altshiller-Court's
  *College Geometry* (2nd ed., 1952; Dover 2007), mapping folios ``0001``–``0334`` across
  ``00_frontmatter`` through ``12_index`` and articles ``§§ 1–699``.
- Standardized 300 DPI folio ingestion pipeline (``ingest.py``), calibrated diagram cropper
  with dark-mode inversion (``graphics.py``), and 2-Track Book Codex compiler (``compile_edition.py``).
- Populated scholarly apparatus registries (``persons.json``, ``citations.json``, ``glossary.json``,
  ``folio_reviews.json``) from visually verified *Historical and Bibliographical Notes* and *List of Names*.
- Gold-standard visual transcription, figure calibration, and GEOMETOR commentary for Frontmatter
  (``0001``–``0019``) and Chapter I (*Geometric Constructions*, ``0020``–``0040``).
- Implemented Semantic Ink-to-Vector SVG compiler and quantitative ink-overlap verifier
  (``svg_compiler.py``, ``svg`` and ``verify-svg`` CLI subcommands), vectorizing all 17 Chapter I
  figures (``FIG. 1``–``FIG. 17``, ``0023.g1.svg``–``0040.g1.svg``) with ``99.97%``–``100.00%`` scan
  overlap and zero embedded ``py_file`` scripts.
- Wired Chapter I folios (``0022.rst``–``0040.rst``) interactively with inline ``euclid-graphic``
  SVGs, scoped ``:g:`` geometric element references, ``:eq:`` equality tick/arc assertions, and
  ``.. enunciation::`` / ``.. assertion::`` blocks, plus documented the mandatory
  multimodal-vision-over-OCR workflow in ``SVG_CREATION.md`` and ``docsrc/about/pdf-parsing-guide.rst``.
