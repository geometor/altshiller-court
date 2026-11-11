"""Semantic Ink-to-Vector SVG compiler and overlap verifier for Altshiller-Court's College Geometry.

Compiles formal ``"geometry"`` models stored in ``<folio>.json`` into interactive
``euclid-graphic`` SVGs compatible with ``photon_platform.publish`` (``geometor_interactive.js``),
and quantitatively verifies sub-pixel alignment against the 300-DPI ``<folio>.<gid>.png`` crops.
"""

from __future__ import annotations

import html
import json
import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFilter

STANDALONE_STYLE = """    .euclid-graphic {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-style: normal;
      font-weight: 700;
      background-color: #ffffff;
    }
    .geom-line {
      stroke: #18181b;
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-bold {
      stroke: #18181b;
      stroke-width: 2.3;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-circle, .geom-curve, .geom-ellipse {
      stroke: #18181b;
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-arc {
      stroke: #18181b;
      stroke-width: 1.6;
      stroke-linecap: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-dashed, .geom-line-dashed, .geom-arc-dashed, .geom-aux, .geom-Auxiliary, .geom-construction {
      stroke: #18181b;
      stroke-width: 1.5;
      stroke-dasharray: 4, 3;
      stroke-linecap: round;
      stroke-linejoin: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-arc-dotted {
      stroke: #18181b;
      stroke-width: 1.5;
      stroke-dasharray: 2.5, 2.5;
      stroke-linecap: round;
      fill: none;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-ray {
      stroke: #18181b;
      stroke-width: 1.25;
      stroke-linecap: round;
      fill: none;
      opacity: 0.85;
      transition: stroke 0.15s, stroke-width 0.15s;
    }
    .geom-tick {
      stroke: #18181b;
      stroke-width: 1.5;
      stroke-linecap: round;
      fill: none;
    }
    .geom-tick-mark {
      stroke: #16a34a;
      stroke-width: 2;
      stroke-linecap: round;
      fill: none;
    }
    .geom-ang-arc {
      fill: none;
      stroke: #16a34a;
      stroke-width: 2.2;
      stroke-linecap: round;
    }
    .geom-polygon {
      fill: #000000;
      fill-opacity: 0.04;
      stroke: none;
      transition: fill-opacity 0.15s, stroke 0.15s;
    }
    .geom-polygon-bordered, .geom-polygon-stroked, .geom-space {
      fill: #000000;
      fill-opacity: 0.04;
      stroke: #18181b;
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      transition: fill-opacity 0.15s, stroke 0.15s, stroke-width 0.15s;
    }
    .wedge, .angle {
      fill: #c88a1e;
      fill-opacity: 0.24;
      stroke: #c88a1e;
      stroke-width: 2;
      stroke-linejoin: round;
      transition: opacity 0.12s ease, fill-opacity 0.12s ease;
    }
    .geom-point {
      fill: #18181b;
      stroke: #ffffff;
      stroke-width: 1;
      transition: fill 0.15s, r 0.15s;
    }
    .geom-dot {
      fill: #18181b;
      stroke: none;
      transition: fill 0.15s, r 0.15s;
    }
    .geom-label {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 14.5px;
      font-weight: 700;
      font-style: normal;
      fill: #18181b;
      user-select: none;
    }
    .geom-label-sm {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 11px;
      font-weight: 700;
      font-style: normal;
      fill: #18181b;
      user-select: none;
    }
    .geom-label-sub {
      font-family: 'Fira Sans Condensed', 'Fira Sans', sans-serif;
      font-size: 11px;
      font-style: normal;
      font-weight: 700;
      fill: #18181b;
    }
    .geom-overlay {
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.12s ease;
    }
    [data-ref]:hover, .highlight, .geom-highlight-active {
      opacity: 1 !important;
      stroke: #c88a1e !important;
      cursor: pointer;
    }
    text[data-ref]:hover, text.highlight, text.geom-highlight-active, text.geom-highlight-secondary, text.geom-highlight-active *, text.geom-highlight-secondary * {
      opacity: 1 !important;
      fill: #c88a1e !important;
      stroke: none !important;
    }
    .geom-polygon:hover, .geom-polygon.highlight, .geom-polygon-bordered:hover, .geom-polygon-bordered.highlight, polygon.geom-highlight-active, path.geom-polygon.geom-highlight-active, .wedge:hover, .wedge.highlight, .wedge.angle:hover, .wedge.angle.highlight, .wedge.angle.geom-highlight-active, path.wedge.geom-highlight-active, path.angle.geom-highlight-active {
      opacity: 1 !important;
      fill-opacity: 0.24 !important;
      fill: #c88a1e !important;
      stroke: #c88a1e !important;
    }
    .geom-point:hover, .geom-point.highlight, circle.geom-point.geom-highlight-active, .geom-dot:hover, .geom-dot.highlight, circle.geom-highlight-active {
      opacity: 1 !important;
      fill: #c88a1e !important;
      stroke: none !important;
    }
    .geom-assert-active {
      opacity: 1 !important;
      stroke: #16a34a !important;
    }
    text.geom-assert-active, text.geom-assert-secondary, text.geom-assert-active *, text.geom-assert-secondary * {
      opacity: 1 !important;
      fill: #16a34a !important;
      stroke: none !important;
    }
    polygon.geom-assert-active, path.geom-polygon.geom-assert-active, .wedge.angle.geom-assert-active, path.wedge.geom-assert-active, path.angle.geom-assert-active {
      opacity: 1 !important;
      fill-opacity: 0.22 !important;
      fill: #16a34a !important;
      stroke: #16a34a !important;
    }
    path.geom-ang-arc.geom-assert-active {
      opacity: 1 !important;
      fill: none !important;
      stroke: #16a34a !important;
    }
    circle.geom-point.geom-assert-active, circle.geom-assert-active {
      opacity: 1 !important;
      fill: #16a34a !important;
      stroke: none !important;
    }
    path.geom-assert-active.geom-tick-1 {
      marker-mid: url(#geom-tick-1);
    }
    path.geom-assert-active.geom-tick-2 {
      marker-mid: url(#geom-tick-2);
    }
    path.geom-assert-active.geom-tick-3 {
      marker-mid: url(#geom-tick-3);
    }"""

DEFS_BLOCK = """  <defs>
    <marker id="geom-tick-1" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" class="geom-tick-mark" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="-1.8" y1="-4.5" x2="-1.8" y2="4.5" class="geom-tick-mark" />
      <line x1="1.8" y1="-4.5" x2="1.8" y2="4.5" class="geom-tick-mark" />
    </marker>
    <marker id="geom-tick-3" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" markerUnits="userSpaceOnUse" orient="auto">
      <line x1="-3.2" y1="-4.5" x2="-3.2" y2="4.5" class="geom-tick-mark" />
      <line x1="0" y1="-4.5" x2="0" y2="4.5" class="geom-tick-mark" />
      <line x1="3.2" y1="-4.5" x2="3.2" y2="4.5" class="geom-tick-mark" />
    </marker>
  </defs>"""


def fmt_num(val: float) -> str:
    """Format floating-point SVG coordinates cleanly."""
    if abs(val - round(val)) < 1e-5:
        return str(round(val))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def esc_attr(val: str) -> str:
    """Escape XML attribute value including ``<`` and ``>``."""
    return (
        val.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def safe_dom_id(raw: str) -> str:
    """Convert a point or element key like ``P_1'`` into a clean DOM id token ``P1prime``."""
    out = raw.replace("''", "dprime").replace("'", "prime").replace("_", "")
    return re.sub(r"[^A-Za-z0-9-]+", "-", out).strip("-")


def canonical_point_ref(pt_key: str) -> str:
    """Return collision-safe point ``data-ref`` compatible with ``geometor_interactive.js``.

    In ``geometor_interactive.js``, bare point references strip non-alphanumeric characters
    (``str.replace(/[^A-Za-z0-9]/g, '')``). Mapping primed points ``A'`` -> ``Aprime`` and
    ``P_1'`` -> ``P1prime`` prevents ``A'`` from colliding with unprimed ``A``, while ``P_1``
    naturally normalizes to ``P1``.
    """
    if "'" in pt_key:
        return pt_key.replace("''", "dprime").replace("'", "prime").replace("_", "")
    return pt_key


def format_label_svg_inner(label_text: str) -> str:
    """Render primed and subscripted mathematical labels with SVG ``<tspan>`` children."""
    m_both = re.match(r"^([A-Za-z]+)_(\d+)('+)$", label_text)
    if m_both:
        base, sub, primes = m_both.groups()
        return (
            f"{html.escape(base)}"
            f'<tspan dy="3" class="geom-label-sub">{html.escape(sub)}</tspan>'
            f'<tspan dy="-3">{html.escape(primes)}</tspan>'
        )
    m_sub = re.match(r"^([A-Za-z]+)_(\d+)$", label_text)
    if m_sub:
        base, sub = m_sub.groups()
        return f'{html.escape(base)}<tspan dy="3" class="geom-label-sub">{html.escape(sub)}</tspan>'
    return html.escape(label_text)


def midpoint_line_d(x1: float, y1: float, x2: float, y2: float) -> str:
    """Build a 3-vertex SVG straight path so ``marker-mid`` renders equality ticks at midpoint."""
    mx = 0.5 * (x1 + x2)
    my = 0.5 * (y1 + y2)
    return f"M {fmt_num(x1)} {fmt_num(y1)} L {fmt_num(mx)} {fmt_num(my)} L {fmt_num(x2)} {fmt_num(y2)}"


def arc_svg_d(cx: float, cy: float, r: float, start_deg: float, end_deg: float, ccw: bool = False) -> str:
    """Build an SVG circular arc path from ``start_deg`` to ``end_deg`` (standard screen degrees: 0=right, 90=down)."""
    t1 = math.radians(start_deg)
    t2 = math.radians(end_deg)
    x1 = cx + r * math.cos(t1)
    y1 = cy + r * math.sin(t1)
    x2 = cx + r * math.cos(t2)
    y2 = cy + r * math.sin(t2)

    if not ccw:
        sweep_deg = (end_deg - start_deg) % 360.0
        sf = 1
    else:
        sweep_deg = (start_deg - end_deg) % 360.0
        sf = 0
    laf = 1 if sweep_deg > 180.0 else 0
    return f"M {fmt_num(x1)} {fmt_num(y1)} A {fmt_num(r)} {fmt_num(r)} 0 {laf} {sf} {fmt_num(x2)} {fmt_num(y2)}"


def wedge_and_mid_arc_d(
    vx: float,
    vy: float,
    p1x: float,
    p1y: float,
    p2x: float,
    p2y: float,
    radius: float,
) -> tuple[str, str]:
    """Compute minor interior angle wedge path and 3-vertex ``.geom-ang-arc`` path."""
    t1 = math.atan2(p1y - vy, p1x - vx)
    t2 = math.atan2(p2y - vy, p2x - vx)
    diff = (t2 - t1) % (2.0 * math.pi)
    if diff <= math.pi:
        sf = 1
        t_mid = t1 + 0.5 * diff
    else:
        sf = 0
        t_mid = t1 - 0.5 * (2.0 * math.pi - diff)

    x1 = vx + radius * math.cos(t1)
    y1 = vy + radius * math.sin(t1)
    xm = vx + radius * math.cos(t_mid)
    ym = vy + radius * math.sin(t_mid)
    x2 = vx + radius * math.cos(t2)
    y2 = vy + radius * math.sin(t2)
    r_str = fmt_num(radius)
    wedge_d = (
        f"M {fmt_num(vx)} {fmt_num(vy)} L {fmt_num(x1)} {fmt_num(y1)} "
        f"A {r_str} {r_str} 0 0 {sf} {fmt_num(x2)} {fmt_num(y2)} Z"
    )
    arc_d = (
        f"M {fmt_num(x1)} {fmt_num(y1)} A {r_str} {r_str} 0 0 {sf} {fmt_num(xm)} {fmt_num(ym)} "
        f"A {r_str} {r_str} 0 0 {sf} {fmt_num(x2)} {fmt_num(y2)}"
    )
    return wedge_d, arc_d


def expand_prime_aliases(ref: str, extra_aliases: list[str] | None = None) -> tuple[str, str]:
    """Normalize ``data-ref`` and expand prime/subscript aliases automatically."""
    all_refs: list[str] = [ref]
    if extra_aliases:
        all_refs.extend(extra_aliases)

    expanded: list[str] = []
    for item in all_refs:
        if item not in expanded:
            expanded.append(item)
        if "'" in item or "_" in item:
            # Replace primed/subscripted tokens inside delimiters with canonical point tokens
            def _tok_repl(m: re.Match[str]) -> str:
                return canonical_point_ref(m.group(0))

            alt = re.sub(r"[A-Za-z]+(?:_\d+)?'+|[A-Za-z]+_\d+", _tok_repl, item)
            if alt not in expanded:
                expanded.append(alt)

    primary = expanded[0]
    aliases = " | ".join(expanded[1:])
    return primary, aliases


def tick_paths_for_segment(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    count: int,
    half_len: float = 4.5,
    tick_pos: float = 0.5,
) -> list[str]:
    """Generate perpendicular static tick mark SVG paths along a segment."""
    dx = x2 - x1
    dy = y2 - y1
    length = math.hypot(dx, dy)
    if length < 1e-6 or count <= 0:
        return []
    ux, uy = dx / length, dy / length
    nx, ny = -uy, ux
    mx, my = x1 + tick_pos * dx, y1 + tick_pos * dy

    offsets = {1: [0.0], 2: [-1.8, 1.8], 3: [-3.2, 0.0, 3.2]}.get(count, [0.0])
    paths: list[str] = []
    for off in offsets:
        cx = mx + off * ux
        cy = my + off * uy
        tx1, ty1 = cx - half_len * nx, cy - half_len * ny
        tx2, ty2 = cx + half_len * nx, cy + half_len * ny
        paths.append(midpoint_line_d(tx1, ty1, tx2, ty2))
    return paths


def compile_graphic_svg(
    folio: str,
    graphic: dict[str, Any],
    out_svg_path: Path,
    png_size: tuple[int, int] | None = None,
) -> dict[str, Any]:
    """Compile a single graphic's ``geometry`` schema into ``<folio>.<gid>.svg``."""
    gid = graphic.get("id", "g1")
    geom = graphic.get("geometry")
    if not geom:
        raise ValueError(f"Graphic {folio}.{gid} has no 'geometry' definition.")

    scale = float(geom.get("svg_scale", 0.5))
    bbox = graphic.get("bbox", [0, 0, 600, 400])
    raw_w = png_size[0] if png_size else int(bbox[2])
    raw_h = png_size[1] if png_size else int(bbox[3])

    if "viewBox" in geom and geom.get("coord_space") == "svg":
        vb_parts = [float(v) for v in str(geom["viewBox"]).split()]
        vw, vh = vb_parts[2], vb_parts[3]
        scale = 1.0
    else:
        vw = round(raw_w * scale, 2)
        vh = round(raw_h * scale, 2)

    points_cfg: dict[str, dict[str, Any]] = geom.get("points", {})
    pts_svg: dict[str, tuple[float, float]] = {}
    for pk, pdata in points_cfg.items():
        pts_svg[pk] = (float(pdata["x"]) * scale, float(pdata["y"]) * scale)

    elements_group: list[str] = []
    graphics_group: list[str] = []
    highlights_group: list[str] = []
    points_group: list[str] = []
    labels_group: list[str] = []

    for idx, el in enumerate(geom.get("elements", [])):
        etype = el["type"]
        eid = safe_dom_id(el.get("id", f"{etype}_{idx}"))
        style = el.get("style", "solid")
        raw_ref = el.get("ref", "")
        raw_aliases = list(el.get("aliases", []))

        if etype == "circle":
            if "center" in el:
                cx, cy = pts_svg[el["center"]]
            else:
                cx, cy = float(el["cx"]) * scale, float(el["cy"]) * scale
            if "through" in el:
                tx, ty = pts_svg[el["through"]]
                r = math.hypot(tx - cx, ty - cy)
            else:
                r = float(el["r"]) * scale

            if not raw_ref and "center" in el and "through" in el:
                raw_ref = f"( {el['center']} {el['through']} )"
            pref, paliases = expand_prime_aliases(raw_ref, raw_aliases)
            alias_attr = f' data-aliases="{esc_attr(paliases)}"' if paliases else ""
            ref_attr = f' data-ref="{esc_attr(pref)}"' if pref else ""

            cls = {
                "solid": "geom-circle",
                "bold": "geom-bold",
                "dashed": "geom-arc-dashed",
                "dotted": "geom-arc-dotted",
                "overlay": "geom-circle geom-overlay",
            }.get(style, "geom-circle")

            elements_group.append(
                f'    <circle id="el-circle-{eid}"{ref_attr}{alias_attr} data-type="circle" '
                f'cx="{fmt_num(cx)}" cy="{fmt_num(cy)}" r="{fmt_num(r)}" class="{cls}" />'
            )
            if pref and style != "overlay":
                highlights_group.append(
                    f'    <circle id="hl-circle-{eid}"{ref_attr}{alias_attr} '
                    f'cx="{fmt_num(cx)}" cy="{fmt_num(cy)}" r="{fmt_num(r)}" class="geom-circle geom-overlay" />'
                )

        elif etype == "arc":
            if "center" in el:
                cx, cy = pts_svg[el["center"]]
            else:
                cx, cy = float(el["cx"]) * scale, float(el["cy"]) * scale
            if "through" in el:
                tx, ty = pts_svg[el["through"]]
                r = math.hypot(tx - cx, ty - cy)
            else:
                r = float(el["r"]) * scale

            start_deg = float(el["start_deg"])
            end_deg = float(el["end_deg"])
            ccw = bool(el.get("ccw", False))
            d_str = arc_svg_d(cx, cy, r, start_deg, end_deg, ccw=ccw)

            pref, paliases = expand_prime_aliases(raw_ref, raw_aliases)
            alias_attr = f' data-aliases="{esc_attr(paliases)}"' if paliases else ""
            ref_attr = f' data-ref="{esc_attr(pref)}"' if pref else ""

            cls = {
                "solid": "geom-arc",
                "bold": "geom-bold",
                "dashed": "geom-arc-dashed",
                "dotted": "geom-arc-dotted",
                "overlay": "geom-arc geom-overlay",
            }.get(style, "geom-arc")

            elements_group.append(
                f'    <path id="el-arc-{eid}"{ref_attr}{alias_attr} data-type="arc" '
                f'd="{d_str}" class="{cls}" />'
            )
            if pref and style != "overlay":
                highlights_group.append(
                    f'    <path id="hl-arc-{eid}"{ref_attr}{alias_attr} '
                    f'd="{d_str}" class="geom-arc geom-overlay" />'
                )

        elif etype in ("line", "segment"):
            if "p1" in el and "p2" in el:
                x1, y1 = pts_svg[el["p1"]]
                x2, y2 = pts_svg[el["p2"]]
                if not raw_ref:
                    raw_ref = f"[ {el['p1']} {el['p2']} ]" if etype == "line" else f"/ {el['p1']} {el['p2']} /"
            else:
                x1, y1 = float(el["x1"]) * scale, float(el["y1"]) * scale
                x2, y2 = float(el["x2"]) * scale, float(el["y2"]) * scale

            d_str = midpoint_line_d(x1, y1, x2, y2)
            pref, paliases = expand_prime_aliases(raw_ref, raw_aliases)
            alias_attr = f' data-aliases="{esc_attr(paliases)}"' if paliases else ""
            ref_attr = f' data-ref="{esc_attr(pref)}"' if pref else ""

            cls = {
                "solid": "geom-line",
                "bold": "geom-bold",
                "dashed": "geom-dashed",
                "dotted": "geom-arc-dotted",
                "thin": "geom-ray",
                "tick": "geom-tick",
                "overlay": "geom-line geom-overlay",
            }.get(style, "geom-line")

            prefix = "line" if etype == "line" else "seg"
            target_group = elements_group if etype == "line" else graphics_group
            target_group.append(
                f'    <path id="el-{prefix}-{eid}"{ref_attr}{alias_attr} data-type="{etype}" '
                f'class="{cls}" d="{d_str}" />'
            )
            if pref and style != "overlay":
                highlights_group.append(
                    f'    <path id="hl-{prefix}-{eid}"{ref_attr}{alias_attr} '
                    f'class="geom-line geom-overlay" d="{d_str}" />'
                )

            ticks = int(el.get("ticks", 0))
            if ticks > 0:
                t_pos = float(el.get("tick_pos", 0.5))
                for t_idx, td in enumerate(tick_paths_for_segment(x1, y1, x2, y2, ticks, tick_pos=t_pos)):
                    graphics_group.append(
                        f'    <path id="el-tick-{eid}-{t_idx + 1}" class="geom-tick" d="{td}" />'
                    )

        elif etype == "polygon":
            poly_pts = el["points"]
            coords_str = " ".join(f"{fmt_num(pts_svg[p][0])},{fmt_num(pts_svg[p][1])}" for p in poly_pts)
            if not raw_ref:
                raw_ref = f"< {' '.join(poly_pts)} >"
            pref, paliases = expand_prime_aliases(raw_ref, raw_aliases)
            alias_attr = f' data-aliases="{esc_attr(paliases)}"' if paliases else ""
            ref_attr = f' data-ref="{esc_attr(pref)}"' if pref else ""

            cls = {
                "region": "geom-polygon",
                "solid": "geom-polygon",
                "bordered": "geom-polygon-bordered",
                "overlay": "geom-polygon geom-overlay",
            }.get(style, "geom-polygon")

            graphics_group.append(
                f'    <polygon id="el-poly-{eid}"{ref_attr}{alias_attr} data-type="polygon" '
                f'points="{coords_str}" class="{cls}" />'
            )
            if pref and style != "overlay":
                highlights_group.append(
                    f'    <polygon id="hl-poly-{eid}"{ref_attr}{alias_attr} '
                    f'points="{coords_str}" class="geom-polygon geom-overlay" />'
                )

        elif etype == "angle":
            v_key = el["vertex"]
            p1_key = el["p1"]
            p2_key = el["p2"]
            vx, vy = pts_svg[v_key]
            p1x, p1y = pts_svg[p1_key]
            p2x, p2y = pts_svg[p2_key]
            ang_r = float(el.get("radius", 36.0)) * scale
            wedge_d, arc_d = wedge_and_mid_arc_d(vx, vy, p1x, p1y, p2x, p2y, ang_r)

            if not raw_ref:
                raw_ref = f"< {p1_key} {v_key} {p2_key} )"
            if f"< {p2_key} {v_key} {p1_key} )" not in raw_aliases:
                raw_aliases.append(f"< {p2_key} {v_key} {p1_key} )")
            pref, paliases = expand_prime_aliases(raw_ref, raw_aliases)
            alias_attr = f' data-aliases="{esc_attr(paliases)}"' if paliases else ""
            ref_attr = f' data-ref="{esc_attr(pref)}"'

            graphics_group.append(
                f'    <path id="el-ang-{eid}"{ref_attr}{alias_attr} data-type="wedge" '
                f'd="{wedge_d}" class="wedge angle geom-overlay" />'
            )
            highlights_group.append(
                f'    <path id="hl-ang-{eid}"{ref_attr}{alias_attr} '
                f'd="{wedge_d}" class="wedge angle geom-overlay" />'
            )
            highlights_group.append(
                f'    <path id="hl-arc-{eid}"{ref_attr}{alias_attr} '
                f'd="{arc_d}" class="geom-ang-arc geom-overlay" />'
            )

    # Emit points & labels
    for pk, pdata in points_cfg.items():
        px, py = pts_svg[pk]
        pid = safe_dom_id(pk)
        pt_ref = canonical_point_ref(pdata.get("ref", pk))
        pt_aliases_list = list(pdata.get("aliases", []))
        alias_attr = f' data-aliases="{esc_attr(" | ".join(pt_aliases_list))}"' if pt_aliases_list else ""

        is_label_only = bool(pdata.get("label_only", False))
        hidden_point = bool(pdata.get("hidden", False))
        explicit_dot = bool(pdata.get("dot", False))

        if not is_label_only and not hidden_point:
            r_val = float(pdata.get("r", 3.1 if explicit_dot else 2.6))
            pt_cls = "geom-point" if not pdata.get("point_overlay", False) else "geom-point geom-overlay"
            points_group.append(
                f'    <circle id="el-pt-{pid}" data-ref="{esc_attr(pt_ref)}"{alias_attr} '
                f'data-type="point" cx="{fmt_num(px)}" cy="{fmt_num(py)}" r="{fmt_num(r_val)}" class="{pt_cls}" />'
            )

        label_str = pdata.get("label")
        if label_str:
            lx = float(pdata.get("label_x", pdata["x"])) * scale
            ly = float(pdata.get("label_y", pdata["y"])) * scale
            anchor = pdata.get("anchor", "middle")
            lbl_cls = pdata.get("label_class", "geom-label")
            inner_lbl = format_label_svg_inner(str(label_str))
            labels_group.append(
                f'    <text id="lbl-{pid}" data-ref="{esc_attr(pt_ref)}"{alias_attr} '
                f'x="{fmt_num(lx)}" y="{fmt_num(ly)}" text-anchor="{anchor}" '
                f'dominant-baseline="central" class="{lbl_cls}">{inner_lbl}</text>'
            )

    article_attr = (
        f' data-article="{esc_attr(str(graphic["article"]))}"' if graphic.get("article") else ""
    )
    svg_lines = [
        (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {fmt_num(vw)} {fmt_num(vh)}" '
            f'width="{fmt_num(vw)}" height="{fmt_num(vh)}" class="euclid-graphic" '
            f'data-graphic-id="{folio}.{gid}" data-folio="{folio}" data-graphic="{gid}"{article_attr}>'
        ),
        "  <style>",
        STANDALONE_STYLE,
        "  </style>",
        DEFS_BLOCK,
        '  <g id="elements">',
        *elements_group,
        "  </g>",
        '  <g id="graphics">',
        *graphics_group,
        "  </g>",
        '  <g id="highlights" style="pointer-events: none;">',
        *highlights_group,
        "  </g>",
        '  <g id="points">',
        *points_group,
        "  </g>",
        '  <g id="labels">',
        *labels_group,
        "  </g>",
        "</svg>",
        "",
    ]

    svg_content = "\n".join(svg_lines)
    # Validate well-formed XML before writing
    ET.fromstring(svg_content)
    out_svg_path.write_text(svg_content, encoding="utf-8")

    return {
        "graphic_id": f"{folio}.{gid}",
        "svg_file": out_svg_path.name,
        "viewBox": f"0 0 {fmt_num(vw)} {fmt_num(vh)}",
        "elements_count": len(elements_group) + len(graphics_group),
        "points_count": len(points_group),
        "labels_count": len(labels_group),
    }


def compile_all_svgs(volume_dir: Path) -> dict[str, Any]:
    """Compile SVGs for all ``<NNNN>.json`` graphics with ``geometry`` schemas."""
    json_files = sorted(
        p for p in volume_dir.glob("*/*.json") if p.stem.isdigit() and len(p.stem) == 4
    )
    compiled: list[dict[str, Any]] = []
    for jp in json_files:
        data = json.loads(jp.read_text(encoding="utf-8"))
        folio = str(data.get("folio") or jp.stem)
        updated = False
        for g in data.get("graphics", []):
            if "geometry" not in g:
                continue
            gid = g.get("id", "g1")
            svg_name = f"{folio}.{gid}.svg"
            if g.get("svg_file") != svg_name:
                g["svg_file"] = svg_name
                updated = True
            png_path = jp.parent / g.get("file", f"{folio}.{gid}.png")
            png_size = Image.open(png_path).size if png_path.is_file() else None
            info = compile_graphic_svg(folio, g, jp.parent / svg_name, png_size=png_size)
            compiled.append(info)
        if updated:
            jp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return {
        "svgs_compiled": len(compiled),
        "graphics": compiled,
    }


def _draw_dashed_segment(
    draw: ImageDraw.ImageDraw,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    dash_px: float = 9.0,
    gap_px: float = 7.0,
    width: int = 3,
) -> None:
    length = math.hypot(x2 - x1, y2 - y1)
    if length < 1e-3:
        return
    ux, uy = (x2 - x1) / length, (y2 - y1) / length
    pos = 0.0
    while pos < length:
        end = min(pos + dash_px, length)
        draw.line(
            [(x1 + ux * pos, y1 + uy * pos), (x1 + ux * end, y1 + uy * end)],
            fill=255,
            width=width,
        )
        pos += dash_px + gap_px


def _draw_arc_polyline(
    draw: ImageDraw.ImageDraw,
    cx: float,
    cy: float,
    r: float,
    start_deg: float,
    end_deg: float,
    ccw: bool = False,
    dashed: bool = False,
    width: int = 3,
) -> None:
    if not ccw:
        sweep = (end_deg - start_deg) % 360.0
        step_sign = 1.0
    else:
        sweep = (start_deg - end_deg) % 360.0
        step_sign = -1.0

    steps = max(24, math.ceil((math.radians(sweep) * r) / 2.0))
    pts = []
    for i in range(steps + 1):
        ang = math.radians(start_deg + step_sign * sweep * (i / steps))
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))

    if not dashed:
        draw.line(pts, fill=255, width=width)
    else:
        acc = 0.0
        draw_on = True
        for i in range(len(pts) - 1):
            seg_len = math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1])
            if draw_on:
                draw.line([pts[i], pts[i + 1]], fill=255, width=width)
            acc += seg_len
            limit = 9.0 if draw_on else 7.0
            if acc >= limit:
                acc = 0.0
                draw_on = not draw_on


def verify_svg_against_scan(
    svg_path: Path,
    png_path: Path,
    graphic: dict[str, Any],
    tolerance_px: int = 4,
    overlay_out_path: Path | None = None,
) -> dict[str, Any]:
    """Rasterize visible geometric primitives and measure pixel overlap against ``<folio>.<gid>.png``.

    Computes:

    - ``overlap_score``: percentage of rasterized SVG stroke pixels falling within
      ``tolerance_px`` of actual scan ink pixels (target >= 95.0%).
    - ``scan_recall``: percentage of non-label scan ink pixels covered within ``tolerance_px``
      by the rasterized SVG strokes.
    """
    scan_gray = Image.open(png_path).convert("L")
    w, h = scan_gray.size
    scan_ink = scan_gray.point(lambda p: 255 if p < 210 else 0)
    filter_size = 2 * tolerance_px + 1
    scan_dilated = scan_ink.filter(ImageFilter.MaxFilter(filter_size))

    geom = graphic["geometry"]
    pts_scan: dict[str, tuple[float, float]] = {
        k: (float(v["x"]), float(v["y"])) for k, v in geom.get("points", {}).items()
    }

    vec_mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(vec_mask)

    for el in geom.get("elements", []):
        etype = el["type"]
        style = el.get("style", "solid")
        if style == "overlay" or etype == "angle":
            continue

        if etype == "circle":
            cx, cy = pts_scan[el["center"]] if "center" in el else (float(el["cx"]), float(el["cy"]))
            if "through" in el:
                tx, ty = pts_scan[el["through"]]
                r = math.hypot(tx - cx, ty - cy)
            else:
                r = float(el["r"])
            _draw_arc_polyline(
                draw, cx, cy, r, 0.0, 359.99, ccw=False, dashed=(style in ("dashed", "dotted")), width=3
            )
        elif etype == "arc":
            cx, cy = pts_scan[el["center"]] if "center" in el else (float(el["cx"]), float(el["cy"]))
            if "through" in el:
                tx, ty = pts_scan[el["through"]]
                r = math.hypot(tx - cx, ty - cy)
            else:
                r = float(el["r"])
            _draw_arc_polyline(
                draw,
                cx,
                cy,
                r,
                float(el["start_deg"]),
                float(el["end_deg"]),
                ccw=bool(el.get("ccw", False)),
                dashed=(style in ("dashed", "dotted")),
                width=3,
            )
        elif etype in ("line", "segment"):
            if "p1" in el and "p2" in el:
                x1, y1 = pts_scan[el["p1"]]
                x2, y2 = pts_scan[el["p2"]]
            else:
                x1, y1 = float(el["x1"]), float(el["y1"])
                x2, y2 = float(el["x2"]), float(el["y2"])
            stroke_w = 4 if style == "bold" else (2 if style == "thin" else 3)
            if style in ("dashed", "dotted"):
                _draw_dashed_segment(draw, x1, y1, x2, y2, width=stroke_w)
            else:
                draw.line([(x1, y1), (x2, y2)], fill=255, width=stroke_w)
            ticks = int(el.get("ticks", 0))
            if ticks > 0:
                dx, dy = x2 - x1, y2 - y1
                seg_l = math.hypot(dx, dy)
                if seg_l > 1e-3:
                    t_pos = float(el.get("tick_pos", 0.5))
                    ux, uy = dx / seg_l, dy / seg_l
                    nx, ny = -uy, ux
                    mx, my = x1 + t_pos * dx, y1 + t_pos * dy
                    for off in ({1: [0.0], 2: [-3.6, 3.6], 3: [-6.4, 0.0, 6.4]}[ticks]):
                        cx_t, cy_t = mx + off * ux, my + off * uy
                        draw.line(
                            [(cx_t - 9.0 * nx, cy_t - 9.0 * ny), (cx_t + 9.0 * nx, cy_t + 9.0 * ny)],
                            fill=255,
                            width=3,
                        )
        elif etype == "polygon" and style == "bordered":
            p_list = [pts_scan[p] for p in el["points"]]
            draw.line([*p_list, p_list[0]], fill=255, width=3)

    for pdata in geom.get("points", {}).values():
        if pdata.get("dot"):
            px, py = float(pdata["x"]), float(pdata["y"])
            draw.ellipse([(px - 4, py - 4), (px + 4, py + 4)], fill=255)

    # Mask out glyph bounding boxes around declared label centers when measuring scan_recall
    scan_geom_only = scan_ink.copy()
    mask_draw = ImageDraw.Draw(scan_geom_only)
    for pdata in geom.get("points", {}).values():
        if pdata.get("label"):
            lx = float(pdata.get("label_x", pdata["x"]))
            ly = float(pdata.get("label_y", pdata["y"]))
            rx = 24 if ("_" in str(pdata["label"]) or "'" in str(pdata["label"])) else 18
            ry = 18
            mask_draw.rectangle([(lx - rx, ly - ry), (lx + rx, ly + ry)], fill=0)

    vec_dilated = vec_mask.filter(ImageFilter.MaxFilter(filter_size))

    vec_bytes = vec_mask.tobytes()
    scan_dil_bytes = scan_dilated.tobytes()
    scan_geom_bytes = scan_geom_only.tobytes()
    vec_dil_bytes = vec_dilated.tobytes()

    vec_total = sum(1 for b in vec_bytes if b > 0)
    vec_hit = sum(1 for vb, sb in zip(vec_bytes, scan_dil_bytes) if vb > 0 and sb > 0)
    overlap_score = (100.0 * vec_hit / vec_total) if vec_total > 0 else 0.0

    scan_geom_total = sum(1 for b in scan_geom_bytes if b > 0)
    scan_geom_hit = sum(1 for sb, vb in zip(scan_geom_bytes, vec_dil_bytes) if sb > 0 and vb > 0)
    scan_recall = (100.0 * scan_geom_hit / scan_geom_total) if scan_geom_total > 0 else 100.0

    if overlay_out_path is not None:
        overlay_out_path.parent.mkdir(parents=True, exist_ok=True)
        rgb = Image.new("RGB", (w, h), (255, 255, 255))
        scan_raw_bytes = scan_ink.tobytes()
        out_pixels = []
        for sb, vb, sdb in zip(scan_raw_bytes, vec_bytes, scan_dil_bytes):
            if vb > 0 and sdb > 0:
                out_pixels.append((20, 140, 60))  # Exact hit: crisp green
            elif vb > 0:
                out_pixels.append((220, 30, 30))  # Vector outside tolerance: bright red
            elif sb > 0:
                out_pixels.append((170, 185, 205))  # Uncovered scan ink (mostly labels): slate
            else:
                out_pixels.append((255, 255, 255))
        rgb.putdata(out_pixels)
        rgb.save(overlay_out_path)

    return {
        "svg_file": svg_path.name,
        "overlap_score": round(overlap_score, 2),
        "scan_recall": round(scan_recall, 2),
        "vector_pixels": vec_total,
    }


def verify_all_svgs(volume_dir: Path, overlay_dir: Path | None = None) -> dict[str, Any]:
    """Run quantitative ink-overlap verification across all vectorized SVGs."""
    json_files = sorted(
        p for p in volume_dir.glob("*/*.json") if p.stem.isdigit() and len(p.stem) == 4
    )
    results: list[dict[str, Any]] = []
    for jp in json_files:
        data = json.loads(jp.read_text(encoding="utf-8"))
        folio = str(data.get("folio") or jp.stem)
        for g in data.get("graphics", []):
            if "geometry" not in g:
                continue
            gid = g.get("id", "g1")
            svg_path = jp.parent / g.get("svg_file", f"{folio}.{gid}.svg")
            png_path = jp.parent / g.get("file", f"{folio}.{gid}.png")
            ov_path = (overlay_dir / f"{folio}.{gid}.overlay.png") if overlay_dir else None
            res = verify_svg_against_scan(svg_path, png_path, g, overlay_out_path=ov_path)
            results.append(res)

    min_overlap = min((r["overlap_score"] for r in results), default=0.0)
    avg_overlap = sum(r["overlap_score"] for r in results) / len(results) if results else 0.0
    avg_recall = sum(r["scan_recall"] for r in results) / len(results) if results else 0.0
    return {
        "verified_count": len(results),
        "min_overlap_score": round(min_overlap, 2),
        "mean_overlap_score": round(avg_overlap, 2),
        "mean_scan_recall": round(avg_recall, 2),
        "results": results,
    }


def parse_geometor_ref_keys(raw_str: str, default_graphic_id: str) -> list[str]:
    """Python mirror of ``EuclidInteractive.parseGeometorRef`` in ``geometor_interactive.js``."""
    s = (raw_str or "").strip()
    if not s:
        return []

    graphic_id = default_graphic_id
    if ":" in s:
        prefix, rest = s.split(":", 1)
        prefix = prefix.strip()
        s = rest.strip()
        if prefix:
            graphic_id = prefix if "." in prefix else f"{default_graphic_id.split('.')[0]}.{prefix}"
    if not s:
        return []

    def extract_pts(inner: str) -> list[str]:
        tokens = [t for t in re.split(r"[\s,]+", inner.strip()) if t]
        if len(tokens) == 1 and re.match(r"^[A-Z]{2,}$", tokens[0]):
            return list(tokens[0])
        return tokens

    def scoped(expr: str) -> str:
        return f"{graphic_id}:{expr}"

    keys: list[str] = []

    def add(k: str) -> None:
        if k not in keys:
            keys.append(k)

    full_wedge = re.match(r"^\(([^)]+)\)\s*<([^>]+)>$", s)
    short_wedge = (not full_wedge) and re.match(r"^<([^)]+)\)$", s)
    line_m = re.match(r"^\[([^\]]+)\]$", s)
    seg_m = re.match(r"^/([^/]+)/$", s) or re.match(r"^\}([^{]+)\{$", s)
    circle_m = (not full_wedge) and re.match(r"^\(([^)]+)\)$", s)
    poly_m = (not full_wedge) and (not short_wedge) and re.match(r"^<([^>]+)>$", s)

    if full_wedge:
        c_pts = extract_pts(full_wedge.group(1))
        a_pts = extract_pts(full_wedge.group(2))
        c_part = f"( {' '.join(c_pts)} )"
        add(scoped(f"{c_part}< {' '.join(a_pts)} >"))
        add(scoped(f"< {' '.join(a_pts)} )"))
        if len(a_pts) == 3:
            rev = [a_pts[2], a_pts[1], a_pts[0]]
            add(scoped(f"{c_part}< {' '.join(rev)} >"))
            add(scoped(f"< {' '.join(rev)} )"))
    elif short_wedge:
        pts = extract_pts(short_wedge.group(1))
        add(scoped(f"< {' '.join(pts)} )"))
        if len(pts) == 3:
            rev = [pts[2], pts[1], pts[0]]
            add(scoped(f"< {' '.join(rev)} )"))
        elif len(pts) == 2:
            add(scoped(f"< {pts[1]} {pts[0]} )"))
    elif line_m:
        pts = extract_pts(line_m.group(1))
        add(scoped(f"[ {' '.join(pts)} ]"))
        add(scoped(f"[ {' '.join(reversed(pts))} ]"))
    elif seg_m:
        pts = extract_pts(seg_m.group(1))
        add(scoped(f"/ {' '.join(pts)} /"))
        add(scoped(f"/ {' '.join(reversed(pts))} /"))
    elif circle_m:
        pts = extract_pts(circle_m.group(1))
        if len(pts) == 2:
            add(scoped(f"( {' '.join(pts)} )"))
        elif len(pts) == 3:
            a, b, c = pts
            for p in ([a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]):
                add(scoped(f"( {' '.join(p)} )"))
        else:
            add(scoped(f"( {' '.join(pts)} )"))
            add(scoped(f"( {' '.join(reversed(pts))} )"))
    elif poly_m:
        pts = extract_pts(poly_m.group(1))
        if len(pts) == 3:
            a, b, c = pts
            for p in ([a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]):
                add(scoped(f"< {' '.join(p)} >"))
        elif len(pts) > 3:
            n = len(pts)
            for i in range(n):
                rot = pts[i:] + pts[:i]
                add(scoped(f"< {' '.join(rot)} >"))
                add(scoped(f"< {' '.join(reversed(rot))} >"))
        else:
            add(scoped(f"< {' '.join(pts)} >"))
            add(scoped(f"< {' '.join(reversed(pts))} >"))
    else:
        clean = re.sub(r"[^A-Za-z0-9]", "", s).strip()
        if not clean:
            return []
        if len(clean) == 1 or re.match(r"^[A-Z]\d+$", clean):
            add(scoped(clean))
        elif len(clean) == 2:
            add(scoped(clean))
            add(scoped(clean[1] + clean[0]))
            add(scoped(f"/ {clean[0]} {clean[1]} /"))
            add(scoped(f"/ {clean[1]} {clean[0]} /"))
        elif len(clean) == 3:
            a, b, c = clean[0], clean[1], clean[2]
            for p in (a + b + c, a + c + b, b + a + c, b + c + a, c + a + b, c + b + a):
                add(scoped(p))
        else:
            add(scoped(clean))

    return keys


def build_svg_ref_keyset(svg_path: Path) -> set[str]:
    """Parse an SVG file and build the exact set of scoped Geometor keys indexed by ``geometor_interactive.js``."""
    root = ET.fromstring(svg_path.read_text(encoding="utf-8"))
    full_gid = root.attrib.get("data-graphic-id", svg_path.stem)
    indexed: set[str] = set()

    skip_ids = {
        "elements",
        "graphics",
        "highlights",
        "points",
        "labels",
        "construction",
        "geometry",
    }

    for elem in root.iter():
        local_tag = elem.tag.split("}")[-1].lower()
        if local_tag in ("defs", "marker", "style", "svg", "tspan"):
            continue
        if local_tag == "g" and "data-ref" not in elem.attrib:
            continue

        raw_ref = (elem.attrib.get("data-ref") or elem.attrib.get("id") or "").strip()
        if not raw_ref or raw_ref in skip_ids:
            continue

        refs_to_index = [raw_ref]
        aliases = elem.attrib.get("data-aliases", "").strip()
        if aliases:
            for part in re.split(r"[|;]", aliases):
                if part.strip():
                    refs_to_index.append(part.strip())

        for r in refs_to_index:
            for key in parse_geometor_ref_keys(r, full_gid):
                indexed.add(key)

    return indexed


def parse_geom_role_text(raw_content: str) -> tuple[str, str]:
    """Parse ``:g:`` role content ``display <target>`` or bare ``target`` into ``(display, target)``."""
    text = (raw_content or "").strip()
    if not text:
        return "", ""

    match = re.match(r"^(.+?)\s+<(.+)>$", text)
    if match:
        display = match.group(1).strip()
        if len(display) >= 2 and display.startswith("$") and display.endswith("$"):
            display = display[1:-1].strip()
        target = match.group(2).strip()
        return display, target

    target = text
    expr = target.split(":", 1)[-1].strip() if ":" in target else target
    letters = "".join(re.findall(r"[A-Za-z0-9]+", expr))
    display = letters if letters else target
    return display, target


def parse_eq_role_text(raw_content: str) -> tuple[str, str]:
    """Parse ``:eq:`` role content ``display <spec>`` into ``(display, spec)``."""
    text = (raw_content or "").strip()
    if not text:
        return "", ""

    match = re.match(r"^([^<>]+?)\s+<(.+)>$", text)
    if match:
        return match.group(1).strip(), match.group(2).strip()
    return "", text
