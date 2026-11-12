=========
Changelog
=========

0.1.0 (Unreleased)
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
