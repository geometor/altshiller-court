# GEOMETOR • altshiller-court

Digital Scriptorium and 2-Track **Book Codex** edition of **Nathan Altshiller-Court's**
*College Geometry: An Introduction to the Modern Geometry of the Triangle and the Circle*
(Revised & Enlarged 2nd Edition, 1952; Dover republication, 2007, ISBN `978-0-486-45805-2`, 334 PDF pages).

## Architectural Rules

1. **Mandatory Multimodal Vision Over OCR**: For scanned PDFs—even when an embedded OCR text layer is
   present—agents **MUST** read the 300-DPI `<NNNN>.png` folio scan images directly via multimodal vision
   (`view_file`) to ascertain semantic structure, prose, mathematical formulas (`\tfrac`, `\angle`, ratios,
   exponents), primes/subscripts (`A'`, `P_1`, `P_1'`), and diagram geometry. **Never rely on `pdftotext`
   or embedded PDF OCR.** Every transcribed folio (`.rst`), scholarly note (`.notes.rst`), figure bounding
   box, and vector SVG model (`.json`) must be optically verified against `<NNNN>.png` and `<NNNN>.<gid>.png`.
   See `SVG_CREATION.md` and `docsrc/about/pdf-parsing-guide.rst`.
2. **Pure Scholarly Treatise (No Embedded Python Construction Scripts)**: Like `geometor/hoenen`
   and `geometor/euclid`, this repository preserves the faithful treatise text, calibrated interactive
   vector diagrams (`.. picture:: <NNNN>.<gid>.svg`), folio provenance anchors (`.. folio::`), semantic
   roles (`:g:`, `:eq:`, `:math:`, `:term:`, `:person:`, `:cite:`), structural directives
   (`.. enunciation::`, `.. assertion::`), and Track 2 commentary cross-referencing Euclid's *Elements*
   (`I.1`–`VI.*`), `geometor/pappus`, `geometor/fundamentals`, and Clark Kimberling's *Encyclopedia
   of Triangle Centers* (`X(1)`–`X(n)` in `geometor/etc`).
   Do **not** embed `py_file` construction scripts inside the treatise edition; store declarative
   `"geometry"` models directly inside `<NNNN>.json`.
3. **Native `photon-platform/publish` Integration**: Do not create custom Flask apps. `resources/college_geometry/`
   plugs directly into `publish folio` (`FolioScanner` + `ReviewManager`), and `docsrc/college_geometry/`
   uses `:layout: book` with `English` (`<stem>-en.rst`) and `Commentary` (`<stem>-commentary.rst`)
   companion tracks and inline `euclid-graphic` SVGs powered by `geometor_interactive.js`.

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
- `svg_compiler.py`: Compiles declarative `"geometry"` models in `<NNNN>.json` into interactive
  `euclid-graphic` SVGs (`<NNNN>.g<k>.svg`), verifies sub-pixel ink overlap (`>= 95%`) against
  `<NNNN>.g<k>.png`, and indexes Geometor reference keysets (`build_svg_ref_keyset`).
- `compile_edition.py`: Compiles SVGs, copies `.svg`/`.png` assets, and assembles folio `.rst` and
  `.notes.rst` files into the de-paginated 2-Track Book Codex (`docsrc/college_geometry/`) plus
  `bibliography.rst`, `persons.rst`, `glossary.rst`, and `scan-inventory.rst`.
- `__main__.py`: Unified CLI (`ingest`, `graphics`, `svg`, `verify-svg`, `compile`, `status`).
