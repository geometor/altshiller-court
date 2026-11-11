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
  (``0001``–``0019``) and Chapter I (*Geometric Constructions*, Sections A–C, ``0020``–``0040``).
