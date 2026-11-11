# GEOMETOR • altshiller-court

Digital Scriptorium and 2-Track **Book Codex** edition of **Nathan Altshiller-Court's**
*College Geometry: An Introduction to the Modern Geometry of the Triangle and the Circle*
(Revised & Enlarged 2nd Edition, 1952; Dover republication, 2007, ISBN `978-0-486-45805-2`, 334 PDF pages).

## Architectural Rules

1. **Strict Visual Verification**: Never commit unverified OCR. Every transcribed folio (`.rst`),
   scholarly note (`.notes.rst`), and figure bounding box (`.json`) must be visually verified
   against the 300 DPI folio scan (`<NNNN>.png`).
2. **Pure Scholarly Treatise (No Embedded Python Construction Scripts)**: Like `geometor/hoenen`
   and `geometor/euclid`, this repository preserves the faithful treatise text, calibrated historical
   diagrams, semantic roles (`:g:`, `:term:`, `:person:`, `:cite:`, `:just:`), and Track 2 commentary
   cross-referencing Euclid's *Elements* (`I.1`–`VI.*`), `geometor/pappus`, `geometor/fundamentals`,
   and Clark Kimberling's *Encyclopedia of Triangle Centers* (`X(1)`–`X(n)` in `geometor/etc`).
   Do **not** embed `py_file` construction scripts inside the treatise edition.
3. **Native `photon-platform/publish` Integration**: Do not create custom Flask apps. `resources/college_geometry/`
   plugs directly into `publish folio` (`FolioScanner` + `ReviewManager`), and `docsrc/college_geometry/`
   uses `:layout: book` with `English` (`<stem>-en.rst`) and `Commentary` (`<stem>-commentary.rst`)
   companion tracks.

## Pagination Formula (334 Folios)

- **Frontmatter (`0001`–`0019`)**: `0001` = Dover Front Cover; `0002`–`0019` = Roman pages `[iii]`–`[xx]`
  (`Folio + 1 = Roman Page`), with blank versos at `0005` (`[vi]`), `0009` (`[x]`), `0015` (`[xvi]`), `0019` (`[xx]`).
- **Body & Backmatter (`0020`–`0334`)**: Unbroken **`PDF Folio = Printed Page + 19`** from page `1` (`0020`)
  through page `313` (`0332`), plus blank `0313` (`[294]`), blank `0333` (`[314]`), and Dover Back Cover `0334`.

## Key Modules (`src/geometor/altshiller_court/`)

- `ingest.py`: Extracts all 334 pages from `resources/college_geometry/pdfs/college_geometry.pdf` at
  300 DPI via `pdftoppm` and routes `<NNNN>.png` into `00_frontmatter`..`12_index` per `structure_map.json`.
- `graphics.py`: Crops calibrated diagram regions from `<NNNN>.json` (`[x, y, w, h]`), normalizes paper
  background, and writes `<NNNN>.g<k>.png` + dark-mode `<NNNN>.g<k>.inverted.png`.
- `compile_edition.py`: Compiles folio `.rst` and `.notes.rst` files into the de-paginated 2-Track
  Book Codex (`docsrc/college_geometry/`) and generates `bibliography.rst`, `persons.rst`,
  `glossary.rst`, and `scan-inventory.rst`.
- `__main__.py`: Unified CLI (`ingest`, `graphics`, `compile`, `all`).
