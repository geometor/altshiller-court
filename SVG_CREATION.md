# Semantic Ink-to-Vector SVG Creation & Interactive Wiring Guide

This document defines the canonical workflow for extracting, vectorizing, verifying, and interactively wiring historical geometric figures in **GEOMETOR • altshiller-court** (*College Geometry*, 2nd ed., 1952 / Dover 2007).

---

## 1. Mandatory Architectural Rules

### Rule 1 — Multimodal Vision Over OCR (No Embedded OCR Reliance)

> **CRITICAL DIRECTIVE**: For PDFs containing scanned pages—even when an embedded OCR text layer is present—agents **MUST** read the 300-DPI `<NNNN>.png` folio scan images directly using multimodal vision (`view_file`) to ascertain semantic structure, text, formulas, and diagram geometry. **Never rely on `pdftotext` or embedded PDF OCR.**

Embedded OCR layers in historical mathematical treatises systematically corrupt:
- **Displayed & inline formulas**: fractions (`\tfrac{1}{2}`), radicals, ratios (`OT : OC`), squared segments (`AM^2 - BM^2 = d^2`), and multi-line derivations spanning page turns (e.g., `0040.rst` → `0041.rst`).
- **Geometric notation**: angle signs (`\angle EAF`), circle notation `(O, OE)` vs `(E, s)`, parallel/perpendicular symbols, and prime/subscript combinations (`A'`, `T'`, `P_1`, `P_1'`, `C'`).
- **Semantic layout**: italicized problem/locus enunciations, small-caps section leads (`ANALYSIS.`, `CONSTRUCTION.`, `PROOF.`, `DISCUSSION.`, `CONVERSELY.`), numbered exercises in multi-column blocks (e.g., `0039.png`), and sentences split across side-by-side figures (`0038.png`, Figs. 14–15).
- **Figure labels**: serif italic letterpress glyphs adjacent to circles, arcs, and dashed auxiliary lines.

Every `<NNNN>.rst` transcription, `<NNNN>.notes.rst` commentary, and `<NNNN>.json` figure model must be authored and verified optically from `<NNNN>.png` and `<NNNN>.<gid>.png`.

### Rule 2 — Pure Treatise Schema (No `py_file`)

Like `geometor/euclid` (Heath) and `geometor/hoenen`, *College Geometry* is curated as a pure scholarly treatise edition:
- Store the formal declarative `"geometry"` specification and `"svg_file": "<folio>.<gid>.svg"` directly inside `<folio>.json` under `"graphics"`.
- **Never** add `"py_file"` keys or standalone `<folio>.<gid>.py` construction scripts inside `resources/college_geometry/`.

---

## 2. Four-Stage Semantic Ink-to-Vector Pipeline

### Stage 1: Calibrated 300-DPI Figure Cropping (`graphics.py`)
1. Inspect the full-page 300-DPI folio scan (`<NNNN>.png`, `1421 × 2225` px) via `view_file`.
2. Record tight `[x, y, width, height]` pixel bounding boxes in `<NNNN>.json` capturing the geometric ink and letterpress point labels while excluding the printed `FIG. N` caption (which is rendered semantically via `:caption: FIG. N` on `.. picture::`).
3. Run `uv run --no-sync python -m geometor.altshiller_court graphics` to produce background-normalized `<NNNN>.<gid>.png` and `.inverted.png` crops.

### Stage 2: Exact Euclidean Constraint Fitting (`<NNNN>.json` `"geometry"`)
Inspect `<NNNN>.<gid>.png` via `view_file` and fit exact geometric primitives in **300-DPI crop pixel coordinates** (`svg_scale: 0.5` maps 300-DPI pixels cleanly to compact web SVG `viewBox` dimensions):

- **Enforce True Euclidean Invariants**:
  - Points lying on circles (`(O)`, `(O, OE)`, Apollonian circles) satisfy $\|P - O\| = R$ to floating-point precision.
  - Tangents (`CT`, `CT'`, `CD` at `F`, `AG` at `G`) satisfy exact perpendicularity to the radius at the point of contact.
  - Constructed squares (`PQRS` in Fig. 6), right angles (`OTC` in Fig. 13, `ADB` in Fig. 17), parallel chords (`AB \parallel CD` in Figs. 14–15), and isosceles unfolded wings (`BE = BA`, `CF = CA` in Fig. 17) satisfy exact algebraic constraints while matching the historical plate's ink skeleton within `< 1.5` px.
- **Map Letterpress Glyph Centroids**:
  - Each labeled point specifies `"label"`, `"label_x"`, and `"label_y"` at the optical centroid of the printed glyph in `<NNNN>.<gid>.png`, ensuring zero label-stroke collisions.
  - Point IDs use alphanumeric ASCII (`A`, `Aprime`, `P1`, `P1prime`), while `"label"` carries mathematical notation (`"A'"`, `"P_1"`, `"P_1'"`). `svg_compiler.py` formats subscripts before primes (`P₁'`) to match Macmillan typography and automatically registers primed aliases (`A'` ↔ `Aprime`).

#### `<folio>.json` Geometry Entry Schema

```json
{
  "id": "g1",
  "type": "diagram",
  "bbox": [412, 92, 616, 422],
  "caption": "FIG. 13",
  "article": "12",
  "file": "0037.g1.png",
  "inverted_file": "0037.g1.inverted.png",
  "svg_file": "0037.g1.svg",
  "geometry": {
    "svg_scale": 0.5,
    "points": {
      "O": {"x": 204.2, "y": 212.5, "show_dot": false, "label": "O", "label_x": 188.0, "label_y": 223.0},
      "T": {"x": 274.8, "y": 33.4, "show_dot": false, "label": "T", "label_x": 280.0, "label_y": 15.0},
      "Tprime": {"x": 351.6, "y": 362.1, "show_dot": false, "label": "T'", "label_x": 384.0, "label_y": 374.0}
    },
    "elements": [
      {"id": "circO", "type": "circle", "ref": "( O )", "aliases": ["( O T )"], "center": "O", "radius": 192.4},
      {"id": "segCT", "type": "segment", "ref": "/ C T /", "p1": "C", "p2": "T"},
      {"id": "triOTC", "type": "polygon", "ref": "< O T C >", "pts": ["O", "T", "C"], "overlay": true},
      {"id": "angOCT", "type": "angle", "ref": "< O C T )", "p1": "O", "vertex": "C", "p2": "T", "radius": 52.0, "overlay": true}
    ]
  }
}
```

Supported element `"type"` values in `svg_compiler.py`:
- `"segment"` (`class="geom-line"` or `"geom-dashed"`, optional `"ticks": 1|2|3`, optional `"overlay": true`)
- `"circle"` (`class="geom-circle"` or `"geom-dashed"`, optional `"overlay": true`)
- `"arc"` (`center`, `radius`, `start_deg`, `end_deg`, `ccw`, optional `"dashed": true`, optional `"overlay": true`)
- `"polygon"` (`pts`, typically `"overlay": true` for interactive triangle/trapezoid/square highlighting)
- `"angle"` / `"wedge"` (`p1`, `vertex`, `p2`, `radius`, typically `"overlay": true` for `:g:` wedge and `:eq:` green arc highlighting)

### Stage 3: SVG Compilation & Standalone/Inline Compatibility (`svg_compiler.py`)
Run:
```bash
uv run --no-sync python -m geometor.altshiller_court svg
```
`svg_compiler.py` emits `<NNNN>.<gid>.svg` with:
- Root `<svg class="euclid-graphic" data-graphic-id="<NNNN>.<gid>" ...>`
- Pure CSS2 `STANDALONE_STYLE` (`#18181b` strokes, `#c88a1e` hover highlights, `#16a34a` equality assertions) so standalone tools (`inkscape`, `librsvg`, browser file previews) render crisp strokes without choking on CSS3 variables, while `photon_platform.publish.images.directive.prepare_inline_svg` strips `<style>` during `publish build` so site-wide light/dark theme variables (`--geom-fg`, `--geom-bg`) govern inlined HTML graphics.
- `<defs>` tick markers (`#geom-tick-1`, `#geom-tick-2`, `#geom-tick-3`) and hidden `.geom-overlay` wedges, polygons, and angle arcs (`<g class="wedge angle geom-overlay">`) activated dynamically by `geometor_interactive.js`.

### Stage 4: Quantitative Ink-Overlap & Multimodal Visual Verification (`verify-svg`)
Run:
```bash
uv run --no-sync python -m geometor.altshiller_court verify-svg --overlays scratch/overlays
```
1. **Quantitative Gate**: Every vectorized figure must achieve **`overlap_score >= 95.0%`** (percentage of rasterized visible vector pixels landing on the 300-DPI historical scan's ink skeleton within tolerance, excluding hidden `.geom-overlay` elements).
2. **Visual Gate**: Render standalone SVGs via Inkscape alongside the 300-DPI `<NNNN>.<gid>.png` crop and inspect both the RGB diagnostic overlay and side-by-side plate via `view_file` to confirm arc sweep directions, dashed vs. solid strokes, tick marks, point dots, and subscript/prime typography.

---

## 3. Interactive Text Wiring (`0020.rst`–`0040.rst`)

1. **Inlined Vector Diagrams**: Reference `.svg` in `.. picture:: <NNNN>.<gid>.svg` so `publish build` inlines `<svg class="euclid-graphic">` directly into the Book Codex HTML and `publish folio` displays interactive SVG previews.
2. **Scoped `:g:` Element References**:
   - Always include the explicit `<folio>.<gid>:` prefix (e.g., ``:g:`AB <0038.g1:/ A B />```, ``:g:`(O, OE) <0038.g1:( O E )>```) so cross-folio references across page turns and multi-figure chapters resolve unambiguously.
   - Multi-element collective phrases use `;` separators while keeping 100% diplomatic verbatim prose: ``:g:`two solutions <0038.g1:< A B D C >; 0038.g1:< A B D' C' >>```.
   - Subscripts in display text (`P_1`, `P_1'`) are rendered to `<sub>1</sub>` automatically by `g_role`. Keep italic asterisks `*...*` outside `:g:` roles inside italicized enunciations.
3. **Interactive `:eq:` Equality Assertions**:
   - Wrap verbatim equality statements in `:eq:` (avoiding `<` or `>` in the display text):
     - Segment tick marks: ``:eq:`BE = BA <0040.g1:/ B E / = 0040.g1:/ B A />```
     - Equal angles (green arcs): ``:eq:`LQB = AMB <0039.g1:< L Q B ) = 0039.g1:< A M B )>```
4. **Semantic Structural Blocks**:
   - Wrap numbered problem statements (`**1. Problem.**`, `**12. Problem.**`, ...) and `LOCUS 1.`–`LOCUS 12.` statements in `.. enunciation::`.
   - Wrap key deductive conclusions and `PROOF.` steps in `.. assertion::` (with optional bracketed justification header such as `.. assertion:: [§ 11, Locus 7]`).

---

## 4. Chapter I Verification Summary (`FIG. 1`–`FIG. 17`)

| Graphic ID | Caption | Article | Overlap Score | Scan Recall |
| :--- | :--- | :--- | ---: | ---: |
| `0023.g1.svg` | `FIG. 1` | `§ 1` | `100.00%` | `99.95%` |
| `0024.g1.svg` | `FIG. 2` | `§ 3` | `100.00%` | `99.95%` |
| `0025.g1.svg` | `FIG. 3` | `§ 5` | `100.00%` | `99.91%` |
| `0026.g1.svg` | `FIG. 4` | `§ 6` | `100.00%` | `99.95%` |
| `0026.g2.svg` | `FIG. 5` | `§ 7` | `99.98%` | `99.45%` |
| `0027.g1.svg` | `FIG. 6` | `§ 8` | `100.00%` | `99.83%` |
| `0028.g1.svg` | `FIG. 7` | `§ 8` | `99.99%` | `99.32%` |
| `0031.g1.svg` | `FIG. 8` | `§ 11.7` | `100.00%` | `99.93%` |
| `0032.g1.svg` | `FIG. 9` | `§ 11.8` | `100.00%` | `99.86%` |
| `0033.g1.svg` | `FIG. 10` | `§ 11.10` | `100.00%` | `99.89%` |
| `0034.g1.svg` | `FIG. 11` | `§ 11.11` | `100.00%` | `99.88%` |
| `0035.g1.svg` | `FIG. 12` | `§ 11.12` | `100.00%` | `99.92%` |
| `0037.g1.svg` | `FIG. 13` | `§ 12` | `100.00%` | `99.89%` |
| `0038.g1.svg` | `FIG. 14` | `§ 13` | `99.97%` | `99.04%` |
| `0038.g2.svg` | `FIG. 15` | `§ 13` | `100.00%` | `99.13%` |
| `0039.g1.svg` | `FIG. 16` | `§ 14` | `100.00%` | `99.64%` |
| `0040.g1.svg` | `FIG. 17` | `§ 15` | `100.00%` | `99.38%` |
| **Summary (17/17)** | **Ch. I** | **§§ 1–15** | **Min `99.97%` / Mean `100.00%`** | **Mean `99.70%`** |
