"""Exact symbolic ``.euclid-graphic`` hero diagram generator for *College Geometry*.

Constructs canonical synthetic configurations for Chapters I–X, Frontmatter,
Historical Notes, and Section containers using **100% exact SymPy symbolic algebra**
via :class:`geometor.model.Model` (``auto_intersect=False``, zero ``sp.Float``
coordinates), verifies their defining theorems deductively (``assert_collinear``,
``assert_perpendicular``, ``assert_parallel``, ``assert_concyclic``, ``assert_equal``,
and ``cross_ratio``), and projects them onto theme-adaptive ``.euclid-graphic`` SVGs.
"""

from __future__ import annotations

import math
import shutil
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.invariants import cross_ratio, quadrance

from .svg_compiler import compile_graphic_svg


@dataclass
class SymbolicHeroSpec:
    """Declarative visual specification backed by an exact :class:`geometor.model.Model`."""

    key: str
    caption: str
    alt: str
    model: Model
    points: list[tuple[str, spg.Point, str]] = field(default_factory=list)
    elements: list[dict[str, Any]] = field(default_factory=list)
    label_nudges: dict[str, tuple[float, float]] = field(default_factory=dict)


def _assert_zero(expr: sp.Expr, msg: str = "") -> None:
    if sp.simplify(expr) != 0:
        raise AssertionError(f"Symbolic invariant failed ({msg}): {expr}")


def _midpoint(model: Model, p1: spg.Point, p2: spg.Point, pid: str, guide: bool = False) -> spg.Point:
    """Exact rational midpoint registered in ``model`` with causal parents."""
    return model.set_point(
        (p1.x + p2.x) / 2,
        (p1.y + p2.y) / 2,
        parents=[p1, p2],
        ID=pid,
        guide=guide,
    )


def _foot_on_line(
    model: Model, pt: spg.Point, line: spg.Line, pid: str, guide: bool = False
) -> spg.Point:
    """Construct exact orthogonal projection of ``pt`` onto ``line`` via perpendicular line meet."""
    p1, p2 = line.p1, line.p2
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    q_dir = model.set_point(pt.x - dy, pt.y + dx, parents=[pt, line], guide=True)
    perp = model.construct_line(pt, q_dir, guide=True)
    model.assert_perpendicular(perp, line)
    return model.intersect(perp, line, ID=pid, guide=guide)


def _parallel_line(
    model: Model, pt: spg.Point, ref_line: spg.Line, line_id: str = "", guide: bool = False
) -> spg.Line:
    """Construct exact line through ``pt`` parallel to ``ref_line``."""
    p1, p2 = ref_line.p1, ref_line.p2
    q_dir = model.set_point(
        pt.x + (p2.x - p1.x),
        pt.y + (p2.y - p1.y),
        parents=[pt, ref_line],
        guide=True,
    )
    par = model.construct_line(pt, q_dir, ID=line_id, guide=guide)
    model.assert_parallel(par, ref_line)
    return par


def _heronian_base(name: str) -> tuple[Model, dict[str, Any]]:
    """Construct the exact 13–14–15 Heronian scalene acute triangle and its core centers."""
    m = Model(name, logger=False, auto_intersect=False)
    A = m.given_point(sp.Integer(0), sp.Integer(12), ID="A")
    B = m.given_point(sp.Integer(-5), sp.Integer(0), ID="B")
    C = m.given_point(sp.Integer(9), sp.Integer(0), ID="C")

    l_BC = m.construct_line(B, C, guide=True)
    l_CA = m.construct_line(C, A, guide=True)
    l_AB = m.construct_line(A, B, guide=True)

    Ap = _midpoint(m, B, C, "A'")
    Bp = _midpoint(m, C, A, "B'")
    Cp = _midpoint(m, A, B, "C'")

    D = _foot_on_line(m, A, l_BC, "D")
    E = _foot_on_line(m, B, l_CA, "E")
    F = _foot_on_line(m, C, l_AB, "F")

    med_A = m.construct_line(A, Ap, guide=True)
    med_B = m.construct_line(B, Bp, guide=True)
    G = m.intersect(med_A, med_B, ID="G")
    m.assert_collinear(C, Cp, G)

    alt_A = m.construct_line(A, D, guide=True)
    alt_B = m.construct_line(B, E, guide=True)
    H = m.intersect(alt_A, alt_B, ID="H")
    m.assert_collinear(C, F, H)

    # Mediators of BC and CA meet at circumcenter O
    q_mBC = m.set_point(Ap.x, Ap.y + sp.Integer(1), parents=[Ap], guide=True)
    med_perp_BC = m.construct_line(Ap, q_mBC, guide=True)
    q_mCA = m.set_point(Bp.x - (A.y - C.y), Bp.y + (A.x - C.x), parents=[Bp], guide=True)
    med_perp_CA = m.construct_line(Bp, q_mCA, guide=True)
    O = m.intersect(med_perp_BC, med_perp_CA, ID="O")
    m.assert_equal(spg.Segment(O, A), spg.Segment(O, B))
    m.assert_equal(spg.Segment(O, B), spg.Segment(O, C))

    return m, {
        "A": A,
        "B": B,
        "C": C,
        "l_BC": l_BC,
        "l_CA": l_CA,
        "l_AB": l_AB,
        "A'": Ap,
        "B'": Bp,
        "C'": Cp,
        "D": D,
        "E": E,
        "F": F,
        "G": G,
        "H": H,
        "O": O,
    }


def _build_euler_feuerbach() -> SymbolicHeroSpec:
    """Euler line O-G-N-H, Nine-Point Circle, Incircle, and Feuerbach tangency X(11)."""
    m, d = _heronian_base("hero_euler_feuerbach")
    A, B, C = d["A"], d["B"], d["C"]
    Ap, Bp, Cp = d["A'"], d["B'"], d["C'"]
    D, E, F = d["D"], d["E"], d["F"]
    G, H, O = d["G"], d["H"], d["O"]

    N = _midpoint(m, O, H, "N")
    m.assert_collinear(O, G, H)
    m.assert_collinear(O, N, H)
    m.assert_concyclic(D, E, F, Ap)
    m.assert_concyclic(Ap, Bp, Cp, D)

    # Exact incenter I = (aA + bB + cC)/(a+b+c) = (1, 4) for 13-14-15
    I_pt = m.set_point(sp.Integer(1), sp.Integer(4), parents=[A, B, C], ID="I")
    X_in = _foot_on_line(m, I_pt, d["l_BC"], "X", guide=True)
    c_nine = m.construct_circle(N, D)
    c_in = m.construct_circle(I_pt, X_in)
    m.construct_circle(O, A, guide=True)

    # Line IN meets nine-point circle and incircle at exact Feuerbach point Fe = (1, 8)
    l_IN = m.construct_line(I_pt, N, guide=True)
    Fe = m.intersect(l_IN, c_in, side_of=(B, C, 1), near=A, ID="Fe")
    m.assert_incident(Fe, c_nine)
    _assert_zero(
        quadrance(N, I_pt) - (sp.Rational(65, 16) - sp.Integer(4)) ** 2,
        "Feuerbach internal tangency NI = R/2 - r",
    )

    return SymbolicHeroSpec(
        key="euler_feuerbach",
        caption="Euler Line O–G–N–H, Nine-Point Circle (N), Incircle (I), and Feuerbach Point X(11)",
        alt="Exact symbolic diagram of triangle ABC with circumcircle, Euler line OGNH, nine-point circle, incircle, and Feuerbach tangency point Fe",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("O", O, "O"),
            ("G", G, "G"),
            ("N", N, "N"),
            ("H", H, "H"),
            ("I", I_pt, "I"),
            ("D", D, "D"),
            ("A'", Ap, "A'"),
            ("Fe", Fe, "Fe"),
        ],
        elements=[
            {"id": "circum", "type": "circle", "center": "O", "through": "A", "style": "dashed", "ref": "( O A )"},
            {"id": "tri", "type": "polygon", "points": ["A", "B", "C"], "style": "solid", "ref": "< A B C >"},
            {"id": "nine", "type": "circle", "center": "N", "through": "D", "style": "bold", "ref": "( N D )"},
            {"id": "incirc", "type": "circle", "center": "I", "through_pt": X_in, "style": "solid", "ref": "( I Fe )"},
            {"id": "altA", "type": "segment", "p1": "A", "p2": "D", "style": "dashed", "ref": "/ A D /"},
            {"id": "euler", "type": "line", "p1": "O", "p2": "H", "style": "solid", "ref": "[ O H ]"},
        ],
        label_nudges={
            "O": (13, -7),
            "N": (-5, 14),
            "G": (9, 14),
            "I": (-12, -8),
            "H": (-14, 6),
            "Fe": (13, -8),
            "D": (-6, 15),
            "A'": (6, 15),
        },
    )


def _build_apollonian_locus() -> SymbolicHeroSpec:
    """Harmonic division (A, B; C, D) = -1 and Apollonian circle locus MA : MB = 2 : 1."""
    m = Model("hero_apollonian_locus", logger=False, auto_intersect=False)
    A = m.given_point(sp.Integer(-6), sp.Integer(0), ID="A")
    B = m.given_point(sp.Integer(3), sp.Integer(0), ID="B")
    C = m.set_point(sp.Integer(0), sp.Integer(0), parents=[A, B], ID="C")
    D = m.set_point(sp.Integer(12), sp.Integer(0), parents=[A, B], ID="D")
    _assert_zero(cross_ratio(A, B, C, D) + 1, "Harmonic range (A,B;C,D) = -1")

    O = _midpoint(m, C, D, "O")
    c_ap = m.construct_circle(O, C)
    # Exact point M on Apollonian circle (x - 6)^2 + y^2 = 36: x = 18/5, y = 24/5 -> MA^2 = 72^2/25 + 24^2/25 = 5760/25, MB^2 = 9^2/25 + 24^2/25 = 657/25?
    # Check O=(6,0), r=6: take M = (18/5, 24/5): (18/5 - 6)^2 + (24/5)^2 = (-12/5)^2 + (24/5)^2 = 720/25 != 36!
    # Exact Pythagorean point on (x - 6)^2 + y^2 = 36: x = 6 - 18/5 = 12/5, y = 24/5!
    # Check: (12/5 - 6)^2 + (24/5)^2 = (-18/5)^2 + (24/5)^2 = (324 + 576)/25 = 900/25 = 36!
    M = m.set_point(sp.Rational(12, 5), sp.Rational(24, 5), parents=[c_ap], ID="M")
    m.assert_incident(M, c_ap)
    _assert_zero(quadrance(M, A) - 4 * quadrance(M, B), "Apollonian locus MA = 2 MB")

    l_MC = m.construct_line(M, C, guide=True)
    l_MD = m.construct_line(M, D, guide=True)
    m.assert_perpendicular(l_MC, l_MD)

    return SymbolicHeroSpec(
        key="apollonian_locus",
        caption="Harmonic Division (A, B; C, D) = −1 and Apollonian Circle Locus MA : MB = 2 : 1",
        alt="Exact symbolic diagram of segment AB divided harmonically by C and D with Apollonian circle on diameter CD and orthogonal bisectors MC, MD",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("O", O, "O"),
            ("D", D, "D"),
            ("M", M, "M"),
        ],
        elements=[
            {"id": "axis", "type": "line", "p1": "A", "p2": "D", "style": "solid", "ref": "[ A D ]"},
            {"id": "ap_circ", "type": "circle", "center": "O", "through": "C", "style": "bold", "ref": "( O C )"},
            {"id": "s_MA", "type": "segment", "p1": "M", "p2": "A", "style": "solid", "ref": "/ M A /"},
            {"id": "s_MB", "type": "segment", "p1": "M", "p2": "B", "style": "solid", "ref": "/ M B /"},
            {"id": "s_MC", "type": "segment", "p1": "M", "p2": "C", "style": "dashed", "ref": "/ M C /"},
            {"id": "s_MD", "type": "segment", "p1": "M", "p2": "D", "style": "dashed", "ref": "/ M D /"},
            {"id": "ang_CMD", "type": "angle", "vertex": "M", "p1": "C", "p2": "D", "radius": 18, "ref": "< C M D )"},
        ],
        label_nudges={
            "A": (-6, 15),
            "C": (-6, 15),
            "B": (0, 15),
            "O": (0, 15),
            "D": (8, 15),
            "M": (-4, -12),
        },
    )


def _build_homothecy_circles() -> SymbolicHeroSpec:
    """Direct & inverse centers of similitude S, S' and circle of similitude of two circles."""
    m = Model("hero_homothecy_circles", logger=False, auto_intersect=False)
    O1 = m.given_point(sp.Integer(-6), sp.Integer(0), ID="O1")
    O2 = m.given_point(sp.Integer(3), sp.Integer(0), ID="O2")
    R1_pt = m.set_point(sp.Integer(-6), sp.Integer(4), parents=[O1], guide=True)
    R2_pt = m.set_point(sp.Integer(3), sp.Integer(2), parents=[O2], guide=True)

    c1 = m.construct_circle(O1, R1_pt)
    c2 = m.construct_circle(O2, R2_pt)

    # Parallel radii at slope 4/3: on c1 (r=4): (-6 + 12/5, 16/5) = (-18/5, 16/5); on c2 (r=2): (3 + 6/5, 8/5) = (21/5, 8/5)
    P1 = m.set_point(sp.Rational(-18, 5), sp.Rational(16, 5), parents=[c1], ID="P")
    P2 = m.set_point(sp.Rational(21, 5), sp.Rational(8, 5), parents=[c2], ID="P'")
    P2_inv = m.set_point(sp.Rational(9, 5), sp.Rational(-8, 5), parents=[c2], ID="Q'")
    m.assert_incident(P1, c1)
    m.assert_incident(P2, c2)
    m.assert_incident(P2_inv, c2)

    rad1 = m.construct_line(O1, P1, guide=True)
    rad2 = m.construct_line(O2, P2, guide=True)
    m.assert_parallel(rad1, rad2)

    l_centers = m.construct_line(O1, O2)
    l_ext = m.construct_line(P1, P2)
    l_int = m.construct_line(P1, P2_inv, guide=True)
    S = m.intersect(l_centers, l_ext, ID="S")
    Sp = m.intersect(l_centers, l_int, ID="S'")
    _assert_zero(cross_ratio(O1, O2, Sp, S) + 1, "Centers of similitude divide O1 O2 harmonically")

    M_sim = _midpoint(m, S, Sp, "M", guide=True)
    m.construct_circle(M_sim, S, guide=True)

    return SymbolicHeroSpec(
        key="homothecy_circles",
        caption="Direct and Inverse Centers of Similitude S, S' and Circle of Similitude",
        alt="Two unequal circles O, O' with parallel radii, external center of similitude S, internal center S', and dashed circle of similitude",
        model=m,
        points=[
            ("O1", O1, "O"),
            ("O2", O2, "O'"),
            ("P", P1, "P"),
            ("P'", P2, "P'"),
            ("Q'", P2_inv, "Q'"),
            ("S'", Sp, "S'"),
            ("S", S, "S"),
        ],
        elements=[
            {"id": "axis", "type": "line", "p1": "O1", "p2": "S", "style": "solid", "ref": "[ O S ]"},
            {"id": "c1", "type": "circle", "center": "O1", "through": "P", "style": "bold", "ref": "( O P )"},
            {"id": "c2", "type": "circle", "center": "O2", "through": "P'", "style": "bold", "ref": "( O' P' )"},
            {"id": "csim", "type": "circle", "center_pt": M_sim, "through": "S", "style": "dashed", "ref": "( S S' )"},
            {"id": "r1", "type": "segment", "p1": "O1", "p2": "P", "style": "solid", "ref": "/ O P /"},
            {"id": "r2", "type": "segment", "p1": "O2", "p2": "P'", "style": "solid", "ref": "/ O' P' /"},
            {"id": "r2i", "type": "segment", "p1": "O2", "p2": "Q'", "style": "dashed", "ref": "/ O' Q' /"},
            {"id": "ray_ext", "type": "segment", "p1": "P", "p2": "S", "style": "solid", "ref": "/ P S /"},
            {"id": "ray_int", "type": "segment", "p1": "P", "p2": "Q'", "style": "dashed", "ref": "/ P Q' /"},
        ],
        label_nudges={
            "O1": (-6, 15),
            "O2": (4, 15),
            "S'": (-6, -12),
            "S": (8, 15),
            "P": (-6, -10),
            "P'": (4, -10),
            "Q'": (4, 15),
        },
    )


def _build_similitude_inscribed() -> SymbolicHeroSpec:
    """Method of Similitude (§§ 23–30): inscribing a square PQRS in triangle ABC by homothecy from B."""
    m, d = _heronian_base("hero_similitude_inscribed")
    A, B, C = d["A"], d["B"], d["C"]
    l_BC, l_CA, l_AB = d["l_BC"], d["l_CA"], d["l_AB"]

    # Prototype square on AB / BC side from x=-2: P0=(-2, 36/5) on AB (since y = 12/5*(x+5) -> at x=-2, y=36/5)
    S0 = m.set_point(sp.Integer(-2), sp.Integer(0), parents=[l_BC], ID="S0")
    P0 = m.set_point(sp.Integer(-2), sp.Rational(36, 5), parents=[l_AB], ID="P0")
    m.assert_incident(P0, l_AB)
    side0 = P0.y
    Q0 = m.set_point(P0.x + side0, side0, parents=[P0, S0], ID="Q0")
    R0 = m.set_point(S0.x + side0, sp.Integer(0), parents=[Q0, S0], ID="R0")

    ray_BQ0 = m.construct_line(B, Q0)
    Q = m.intersect(ray_BQ0, l_CA, ID="Q")
    R = _foot_on_line(m, Q, l_BC, "R")
    par_Q = _parallel_line(m, Q, l_BC, guide=True)
    P = m.intersect(par_Q, l_AB, ID="P")
    S = _foot_on_line(m, P, l_BC, "S")

    m.assert_equal(spg.Segment(P, Q), spg.Segment(Q, R))
    m.assert_equal(spg.Segment(Q, R), spg.Segment(R, S))
    m.assert_equal(spg.Segment(R, S), spg.Segment(S, P))
    m.assert_perpendicular(spg.Line(P, Q), spg.Line(Q, R))

    return SymbolicHeroSpec(
        key="similitude_inscribed",
        caption="Method of Similitude: Prototype Square Scaled from Homothetic Center B into △ABC",
        alt="Triangle ABC with prototype dashed square P0 Q0 R0 S0 scaled by ray BQ0 into inscribed square PQRS",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("P0", P0, "P'"),
            ("Q0", Q0, "Q'"),
            ("P", P, "P"),
            ("Q", Q, "Q"),
            ("R", R, "R"),
            ("S", S, "S"),
        ],
        elements=[
            {"id": "tri", "type": "polygon", "points": ["A", "B", "C"], "style": "solid", "ref": "< A B C >"},
            {"id": "sq0", "type": "polygon", "points_pt": [P0, Q0, R0, S0], "style": "dashed", "ref": "< P' Q' R' S' >"},
            {"id": "sq_main", "type": "polygon", "points": ["P", "Q", "R", "S"], "style": "bold", "ref": "< P Q R S >"},
            {"id": "ray_B", "type": "segment", "p1": "B", "p2": "Q", "style": "dashed", "ref": "/ B Q /"},
        ],
        label_nudges={
            "P0": (-14, -4),
            "Q0": (6, -8),
            "P": (-14, -4),
            "Q": (10, -4),
            "S": (-4, 15),
            "R": (4, 15),
        },
    )


def _build_medians_centroid() -> SymbolicHeroSpec:
    """Medians AA', BB', CC', centroid G = X(2), and complementary medial triangle A'B'C'."""
    m, d = _heronian_base("hero_medians_centroid")
    A, B, C = d["A"], d["B"], d["C"]
    Ap, Bp, Cp = d["A'"], d["B'"], d["C'"]
    G = d["G"]
    _assert_zero(quadrance(A, G) - 4 * quadrance(G, Ap), "Centroid trisection AG = 2 GA'")

    return SymbolicHeroSpec(
        key="medians_centroid",
        caption="Concurrency of Medians at Centroid G = X(2) and Complementary Triangle △A'B'C'",
        alt="Triangle ABC with medians AA', BB', CC' concurring at centroid G in 2:1 ratio and medial triangle A'B'C'",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("A'", Ap, "A'"),
            ("B'", Bp, "B'"),
            ("C'", Cp, "C'"),
            ("G", G, "G"),
        ],
        elements=[
            {"id": "tri", "type": "polygon", "points": ["A", "B", "C"], "style": "bold", "ref": "< A B C >"},
            {"id": "medial", "type": "polygon", "points": ["A'", "B'", "C'"], "style": "dashed", "ref": "< A' B' C' >"},
            {"id": "mA", "type": "segment", "p1": "A", "p2": "A'", "style": "solid", "ref": "/ A A' /"},
            {"id": "mB", "type": "segment", "p1": "B", "p2": "B'", "style": "solid", "ref": "/ B B' /"},
            {"id": "mC", "type": "segment", "p1": "C", "p2": "C'", "style": "solid", "ref": "/ C C' /"},
        ],
        label_nudges={
            "G": (10, -8),
            "A'": (0, 15),
            "B'": (10, -4),
            "C'": (-16, -4),
        },
    )


def _build_tritangent_incircle() -> SymbolicHeroSpec:
    """Incircle (I, r), angle bisectors, contact points X, Y, Z, and circumcircle (O, R)."""
    m, d = _heronian_base("hero_tritangent_incircle")
    A, B, C, O = d["A"], d["B"], d["C"], d["O"]
    I_pt = m.set_point(sp.Integer(1), sp.Integer(4), parents=[A, B, C], ID="I")
    X = _foot_on_line(m, I_pt, d["l_BC"], "X")
    Y = _foot_on_line(m, I_pt, d["l_CA"], "Y")
    Z = _foot_on_line(m, I_pt, d["l_AB"], "Z")

    m.assert_equal(spg.Segment(I_pt, X), spg.Segment(I_pt, Y))
    m.assert_equal(spg.Segment(I_pt, Y), spg.Segment(I_pt, Z))
    m.assert_equal(spg.Segment(A, Y), spg.Segment(A, Z))
    _assert_zero(
        quadrance(O, I_pt) - (sp.Rational(65, 8) ** 2 - 2 * sp.Rational(65, 8) * sp.Integer(4)),
        "Chapple-Euler identity OI^2 = R(R - 2r)",
    )

    return SymbolicHeroSpec(
        key="tritangent_incircle",
        caption="Incircle (I, r), Angle Bisectors, Contact Points X, Y, Z, and Chapple–Euler Relation",
        alt="Triangle ABC with circumcircle, angle bisectors concurring at incenter I, incircle, and contact radii IX, IY, IZ",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("I", I_pt, "I"),
            ("O", O, "O"),
            ("X", X, "X"),
            ("Y", Y, "Y"),
            ("Z", Z, "Z"),
        ],
        elements=[
            {"id": "circum", "type": "circle", "center": "O", "through": "A", "style": "dashed", "ref": "( O A )"},
            {"id": "tri", "type": "polygon", "points": ["A", "B", "C"], "style": "solid", "ref": "< A B C >"},
            {"id": "incirc", "type": "circle", "center": "I", "through": "X", "style": "bold", "ref": "( I X )"},
            {"id": "bA", "type": "segment", "p1": "A", "p2": "I", "style": "dashed", "ref": "/ A I /"},
            {"id": "bB", "type": "segment", "p1": "B", "p2": "I", "style": "dashed", "ref": "/ B I /"},
            {"id": "bC", "type": "segment", "p1": "C", "p2": "I", "style": "dashed", "ref": "/ C I /"},
            {"id": "rX", "type": "segment", "p1": "I", "p2": "X", "style": "solid", "ref": "/ I X /"},
            {"id": "rY", "type": "segment", "p1": "I", "p2": "Y", "style": "solid", "ref": "/ I Y /"},
            {"id": "rZ", "type": "segment", "p1": "I", "p2": "Z", "style": "solid", "ref": "/ I Z /"},
        ],
        label_nudges={
            "I": (-12, -6),
            "O": (10, -6),
            "X": (0, 15),
            "Y": (10, -4),
            "Z": (-14, -4),
        },
    )


def _build_orthocenter_euler() -> SymbolicHeroSpec:
    """Altitudes AD, BE, CF, orthocenter H = X(4), Euler line OGH, and circumcircle reflection H'."""
    m, d = _heronian_base("hero_orthocenter_euler")
    A, B, C = d["A"], d["B"], d["C"]
    D, E, F = d["D"], d["E"], d["F"]
    G, H, O = d["G"], d["H"], d["O"]

    c_circum = m.construct_circle(O, A)
    alt_A = m.construct_line(A, D, guide=True)
    Hp = m.intersect(alt_A, c_circum, other_than=A, ID="H'")
    m.assert_equal(spg.Segment(H, D), spg.Segment(D, Hp))
    m.assert_collinear(O, G, H)
    _assert_zero(quadrance(G, H) - 4 * quadrance(O, G), "Euler ratio HG = 2 GO")

    return SymbolicHeroSpec(
        key="orthocenter_euler",
        caption="Altitudes, Orthocenter H = X(4), Circumcircle Reflection H', and Euler Line O–G–H",
        alt="Triangle ABC with altitudes AD, BE, CF meeting at orthocenter H, reflection H' on circumcircle, and Euler line OGH",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("D", D, "D"),
            ("E", E, "E"),
            ("F", F, "F"),
            ("H", H, "H"),
            ("G", G, "G"),
            ("O", O, "O"),
            ("H'", Hp, "H'"),
        ],
        elements=[
            {"id": "circum", "type": "circle", "center": "O", "through": "A", "style": "solid", "ref": "( O A )"},
            {"id": "tri", "type": "polygon", "points": ["A", "B", "C"], "style": "bold", "ref": "< A B C >"},
            {"id": "aA", "type": "segment", "p1": "A", "p2": "H'", "style": "dashed", "ref": "/ A H' /"},
            {"id": "aB", "type": "segment", "p1": "B", "p2": "E", "style": "dashed", "ref": "/ B E /"},
            {"id": "aC", "type": "segment", "p1": "C", "p2": "F", "style": "dashed", "ref": "/ C F /"},
            {"id": "euler", "type": "line", "p1": "O", "p2": "H", "style": "solid", "ref": "[ O H ]"},
        ],
        label_nudges={
            "H": (-14, -6),
            "G": (6, 14),
            "O": (10, -8),
            "D": (-10, 14),
            "E": (10, -4),
            "F": (-14, -4),
            "H'": (6, 15),
        },
    )


def _build_orthic_fagnano() -> SymbolicHeroSpec:
    """Orthic triangle DEF (Fagnano minimum-perimeter triangle) with incenter H and nine-point circle."""
    m, d = _heronian_base("hero_orthic_fagnano")
    A, B, C = d["A"], d["B"], d["C"]
    D, E, F = d["D"], d["E"], d["F"]
    H, O = d["H"], d["O"]
    N = _midpoint(m, O, H, "N", guide=True)
    m.assert_concyclic(D, E, F, d["A'"])
    # Altitude AD bisects angle FDE of orthic triangle
    m.assert_spread_equal((F, D, A), (A, D, E))

    return SymbolicHeroSpec(
        key="orthic_fagnano",
        caption="Orthic Triangle △DEF (Fagnano Minimum-Perimeter Triangle) with Incenter H and Nine-Point Circle",
        alt="Acute triangle ABC with altitudes AD, BE, CF meeting at H, highlighted orthic triangle DEF, and circumscribed nine-point circle",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("D", D, "D"),
            ("E", E, "E"),
            ("F", F, "F"),
            ("H", H, "H"),
        ],
        elements=[
            {"id": "tri", "type": "polygon", "points": ["A", "B", "C"], "style": "solid", "ref": "< A B C >"},
            {"id": "orthic", "type": "polygon", "points": ["D", "E", "F"], "style": "bold", "ref": "< D E F >"},
            {"id": "nine", "type": "circle", "center_pt": N, "through": "D", "style": "dashed", "ref": "( D E F )"},
            {"id": "aA", "type": "segment", "p1": "A", "p2": "D", "style": "dashed", "ref": "/ A D /"},
            {"id": "aB", "type": "segment", "p1": "B", "p2": "E", "style": "dashed", "ref": "/ B E /"},
            {"id": "aC", "type": "segment", "p1": "C", "p2": "F", "style": "dashed", "ref": "/ C F /"},
        ],
        label_nudges={
            "H": (8, -6),
            "D": (0, 15),
            "E": (10, -4),
            "F": (-14, -4),
        },
    )


def _build_cyclic_quadrilateral() -> SymbolicHeroSpec:
    """Cyclic quadrilateral ABCD, Ptolemy diagonals, and Varignon parallelogram EFGH."""
    m = Model("hero_cyclic_quadrilateral", logger=False, auto_intersect=False)
    O = m.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    A = m.given_point(sp.Integer(-3), sp.Integer(4), ID="A")
    B = m.given_point(sp.Integer(-5), sp.Integer(0), ID="B")
    C = m.given_point(sp.Integer(3), sp.Integer(-4), ID="C")
    D = m.given_point(sp.Integer(4), sp.Integer(3), ID="D")

    m.construct_circle(O, A)
    m.assert_concyclic(A, B, C, D)

    E = _midpoint(m, A, B, "E")
    F = _midpoint(m, B, C, "F")
    G = _midpoint(m, C, D, "G")
    H = _midpoint(m, D, A, "H")
    m.assert_parallel(spg.Line(E, F), spg.Line(G, H))
    m.assert_parallel(spg.Line(F, G), spg.Line(H, E))

    return SymbolicHeroSpec(
        key="cyclic_quadrilateral",
        caption="Cyclic Quadrilateral ABCD, Ptolemy Diagonals AC, BD, and Varignon Parallelogram EFGH",
        alt="Cyclic quadrilateral ABCD inscribed in circle O with diagonals AC, BD and Varignon midpoint parallelogram EFGH",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("D", D, "D"),
            ("E", E, "E"),
            ("F", F, "F"),
            ("G", G, "G"),
            ("H", H, "H"),
            ("O", O, "O"),
        ],
        elements=[
            {"id": "circ", "type": "circle", "center": "O", "through": "A", "style": "solid", "ref": "( O A )"},
            {"id": "quad", "type": "polygon", "points": ["A", "B", "C", "D"], "style": "bold", "ref": "< A B C D >"},
            {"id": "varignon", "type": "polygon", "points": ["E", "F", "G", "H"], "style": "dashed", "ref": "< E F G H >"},
            {"id": "d1", "type": "segment", "p1": "A", "p2": "C", "style": "solid", "ref": "/ A C /"},
            {"id": "d2", "type": "segment", "p1": "B", "p2": "D", "style": "solid", "ref": "/ B D /"},
        ],
        label_nudges={
            "O": (8, -6),
            "E": (-14, -4),
            "F": (-10, 14),
            "G": (10, 8),
            "H": (4, -10),
        },
    )


def _build_simson_line() -> SymbolicHeroSpec:
    """Wallace–Simson line XYZ of circumcircle point P and bisection of PH at M on the nine-point circle."""
    m, d = _heronian_base("hero_simson_line")
    A, B, C, H, O = d["A"], d["B"], d["C"], d["H"], d["O"]
    c_circum = m.construct_circle(O, A)

    # Exact rational point P = (4, 12) on circumcircle (O, 65/8)
    P = m.set_point(sp.Integer(4), sp.Integer(12), parents=[c_circum], ID="P")
    m.assert_incident(P, c_circum)

    X = _foot_on_line(m, P, d["l_BC"], "X")
    Y = _foot_on_line(m, P, d["l_CA"], "Y")
    Z = _foot_on_line(m, P, d["l_AB"], "Z")
    m.assert_collinear(X, Y, Z)

    M = _midpoint(m, P, H, "M")
    m.assert_collinear(X, Y, M)
    m.assert_concyclic(d["D"], d["E"], d["F"], M)

    return SymbolicHeroSpec(
        key="simson_line",
        caption="Wallace–Simson Line X–Y–Z of Circumcircle Point P Bisecting PH at M",
        alt="Triangle ABC with circumcircle point P, orthogonal projections X, Y, Z collinear on the Wallace-Simson line, and midpoint M of PH",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("P", P, "P"),
            ("X", X, "X"),
            ("Y", Y, "Y"),
            ("Z", Z, "Z"),
            ("H", H, "H"),
            ("M", M, "M"),
        ],
        elements=[
            {"id": "circum", "type": "circle", "center_pt": O, "through": "A", "style": "solid", "ref": "( A B C )"},
            {"id": "tri", "type": "polygon", "points": ["A", "B", "C"], "style": "solid", "ref": "< A B C >"},
            {"id": "ext_AB", "type": "segment", "p1": "A", "p2": "Z", "style": "dashed", "ref": "/ A Z /"},
            {"id": "pX", "type": "segment", "p1": "P", "p2": "X", "style": "dashed", "ref": "/ P X /"},
            {"id": "pY", "type": "segment", "p1": "P", "p2": "Y", "style": "dashed", "ref": "/ P Y /"},
            {"id": "pZ", "type": "segment", "p1": "P", "p2": "Z", "style": "dashed", "ref": "/ P Z /"},
            {"id": "sPH", "type": "segment", "p1": "P", "p2": "H", "style": "dashed", "ref": "/ P H /"},
            {"id": "simson", "type": "line", "p1": "X", "p2": "Z", "style": "bold", "ref": "[ X Z ]"},
        ],
        label_nudges={
            "P": (10, -8),
            "Z": (-14, -8),
            "Y": (10, -4),
            "X": (6, 15),
            "H": (-14, 6),
            "M": (-14, -4),
        },
    )


def _build_menelaus_ceva() -> SymbolicHeroSpec:
    """Ceva concurrency at Gergonne point Ge = X(7) and Menelaus collinear trilinear polar."""
    m, d = _heronian_base("hero_menelaus_ceva")
    A, B, C = d["A"], d["B"], d["C"]
    l_BC, l_CA, l_AB = d["l_BC"], d["l_CA"], d["l_AB"]

    I_pt = m.set_point(sp.Integer(1), sp.Integer(4), parents=[A, B, C], guide=True)
    X = _foot_on_line(m, I_pt, l_BC, "X")
    Y = _foot_on_line(m, I_pt, l_CA, "Y")
    Z = _foot_on_line(m, I_pt, l_AB, "Z")

    l_AX = m.construct_line(A, X, guide=True)
    l_BY = m.construct_line(B, Y, guide=True)
    Ge = m.intersect(l_AX, l_BY, ID="Ge")
    m.assert_collinear(C, Z, Ge)

    # Trilinear polar (Menelaus transversal): Y Z meets BC at U
    l_YZ = m.construct_line(Y, Z, guide=True)
    U = m.intersect(l_YZ, l_BC, ID="U")
    _assert_zero(cross_ratio(B, C, X, U) + 1, "Harmonic conjugate on BC")

    return SymbolicHeroSpec(
        key="menelaus_ceva",
        caption="Ceva Concurrency at Gergonne Point X(7) and Harmonic Menelaus Transversal",
        alt="Triangle ABC with concurrent cevians AX, BY, CZ at Gergonne point Ge and Menelaus transversal UZY",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("X", X, "X"),
            ("Y", Y, "Y"),
            ("Z", Z, "Z"),
            ("Ge", Ge, "Ge"),
            ("U", U, "U"),
        ],
        elements=[
            {"id": "base_line", "type": "segment", "p1": "U", "p2": "C", "style": "solid", "ref": "/ U C /"},
            {"id": "tri", "type": "polygon", "points": ["A", "B", "C"], "style": "bold", "ref": "< A B C >"},
            {"id": "cA", "type": "segment", "p1": "A", "p2": "X", "style": "solid", "ref": "/ A X /"},
            {"id": "cB", "type": "segment", "p1": "B", "p2": "Y", "style": "solid", "ref": "/ B Y /"},
            {"id": "cC", "type": "segment", "p1": "C", "p2": "Z", "style": "solid", "ref": "/ C Z /"},
            {"id": "men", "type": "segment", "p1": "U", "p2": "Y", "style": "dashed", "ref": "/ U Y /"},
        ],
        label_nudges={
            "U": (-6, 15),
            "B": (0, 15),
            "X": (0, 15),
            "C": (6, 15),
            "Y": (10, -4),
            "Z": (-14, -6),
            "Ge": (10, 10),
        },
    )


def _build_harmonic_quadrangle() -> SymbolicHeroSpec:
    """Complete quadrangle KLMN projecting harmonic conjugates (A, B; C, D) = -1."""
    m = Model("hero_harmonic_quadrangle", logger=False, auto_intersect=False)
    A = m.given_point(sp.Integer(-6), sp.Integer(0), ID="A")
    B = m.given_point(sp.Integer(2), sp.Integer(0), ID="B")
    K = m.given_point(sp.Integer(-1), sp.Integer(9), ID="K")
    # Point L on segment AK: A=(-6,0), K=(-1,9) -> L = (-4, 18/5)
    L = m.set_point(sp.Integer(-4), sp.Rational(18, 5), parents=[A, K], ID="L")
    # Point M on segment BK: B=(2,0), K=(-1,9) -> M = (0, 6)
    M = m.set_point(sp.Integer(0), sp.Integer(6), parents=[B, K], ID="M")
    m.assert_collinear(A, L, K)
    m.assert_collinear(B, M, K)

    l_AB = m.construct_line(A, B)
    l_AM = m.construct_line(A, M, guide=True)
    l_BL = m.construct_line(B, L, guide=True)
    N = m.intersect(l_AM, l_BL, ID="N")

    l_KN = m.construct_line(K, N, guide=True)
    l_LM = m.construct_line(L, M, guide=True)
    C = m.intersect(l_KN, l_AB, ID="C")
    D = m.intersect(l_LM, l_AB, ID="D")
    _assert_zero(cross_ratio(A, B, C, D) + 1, "Complete quadrangle harmonic theorem (A,B;C,D) = -1")

    return SymbolicHeroSpec(
        key="harmonic_quadrangle",
        caption="Complete Quadrangle KLMN Generating Harmonic Range (A, B; C, D) = −1 by Straightedge Alone",
        alt="Complete quadrangle KLMN whose sides meet line AB in harmonic conjugates A, C, B, D",
        model=m,
        points=[
            ("A", A, "A"),
            ("C", C, "C"),
            ("B", B, "B"),
            ("D", D, "D"),
            ("K", K, "K"),
            ("L", L, "L"),
            ("M", M, "M"),
            ("N", N, "N"),
        ],
        elements=[
            {"id": "base", "type": "line", "p1": "D", "p2": "B", "style": "bold", "ref": "[ D B ]"},
            {"id": "sAK", "type": "segment", "p1": "A", "p2": "K", "style": "solid", "ref": "/ A K /"},
            {"id": "sBK", "type": "segment", "p1": "B", "p2": "K", "style": "solid", "ref": "/ B K /"},
            {"id": "sAM", "type": "segment", "p1": "A", "p2": "M", "style": "solid", "ref": "/ A M /"},
            {"id": "sBL", "type": "segment", "p1": "B", "p2": "L", "style": "solid", "ref": "/ B L /"},
            {"id": "sKC", "type": "segment", "p1": "K", "p2": "C", "style": "dashed", "ref": "/ K C /"},
            {"id": "sLD", "type": "segment", "p1": "L", "p2": "D", "style": "dashed", "ref": "/ L D /"},
        ],
        label_nudges={
            "D": (-4, 15),
            "A": (-4, 15),
            "C": (-4, 15),
            "B": (4, 15),
            "K": (0, -10),
            "L": (-14, -4),
            "M": (10, -4),
            "N": (12, 12),
        },
    )


def _build_pole_polar_coaxal() -> SymbolicHeroSpec:
    """Inverse points P, P', polar T1 T2, and orthogonal circle (P, PT1) cutting (O, R) at right angles."""
    m = Model("hero_pole_polar_coaxal", logger=False, auto_intersect=False)
    O = m.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    R_pt = m.set_point(sp.Integer(0), sp.Integer(6), parents=[O], guide=True)
    P = m.given_point(sp.Integer(10), sp.Integer(0), ID="P")
    Pp = m.set_point(sp.Rational(18, 5), sp.Integer(0), parents=[O, P], ID="P'")

    c_ref = m.construct_circle(O, R_pt)
    T1 = m.set_point(sp.Rational(18, 5), sp.Rational(24, 5), parents=[c_ref], ID="T1")
    T2 = m.set_point(sp.Rational(18, 5), sp.Rational(-24, 5), parents=[c_ref], ID="T2")
    m.assert_incident(T1, c_ref)
    m.assert_incident(T2, c_ref)

    c_orth = m.construct_circle(P, T1)
    m.assert_incident(T2, c_orth)
    m.assert_perpendicular(spg.Line(O, T1), spg.Line(P, T1))
    _assert_zero(quadrance(O, P) * quadrance(O, Pp) - sp.Integer(36) ** 2, "Inversion OP * OP' = R^2")

    return SymbolicHeroSpec(
        key="pole_polar_coaxal",
        caption="Inverse Points P, P', Polar Line T₁T₂, and Orthogonal Circle (P, PT₁)",
        alt="Reference circle O and orthogonal circle P intersecting perpendicularly at T1, T2 with polar chord T1 T2 through inverse point P'",
        model=m,
        points=[
            ("O", O, "O"),
            ("P'", Pp, "P'"),
            ("P", P, "P"),
            ("T1", T1, "T_1"),
            ("T2", T2, "T_2"),
        ],
        elements=[
            {"id": "axis", "type": "line", "p1": "O", "p2": "P", "style": "solid", "ref": "[ O P ]"},
            {"id": "cref", "type": "circle", "center": "O", "through": "T1", "style": "bold", "ref": "( O T_1 )"},
            {"id": "corth", "type": "circle", "center": "P", "through": "T1", "style": "solid", "ref": "( P T_1 )"},
            {"id": "polar", "type": "line", "p1": "T1", "p2": "T2", "style": "dashed", "ref": "[ T_1 T_2 ]"},
            {"id": "rO", "type": "segment", "p1": "O", "p2": "T1", "style": "solid", "ref": "/ O T_1 /"},
            {"id": "rP", "type": "segment", "p1": "P", "p2": "T1", "style": "solid", "ref": "/ P T_1 /"},
            {"id": "ang_orth", "type": "angle", "vertex": "T1", "p1": "O", "p2": "P", "radius": 16, "ref": "< O T_1 P )"},
        ],
        label_nudges={
            "O": (-12, 15),
            "P'": (-14, 15),
            "P": (8, 15),
            "T1": (-16, -8),
            "T2": (-16, 14),
        },
    )


def _build_circular_inversion() -> SymbolicHeroSpec:
    """Circular inversion (O, k=36): circle not through O -> circle, circle through O -> line."""
    m = Model("hero_circular_inversion", logger=False, auto_intersect=False)
    O = m.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    R_pt = m.set_point(sp.Integer(0), sp.Integer(6), parents=[O], guide=True)
    m.construct_circle(O, R_pt, guide=True)

    # Circle C1 from A=(3,0) to B=(6,0) on diameter AB: center M1=(9/2, 0), r=3/2.
    # Its inverse in (O, k=36) has diameter B'=(6,0) to A'=(12,0): center M2=(9,0), r=3!
    A = m.set_point(sp.Integer(3), sp.Integer(0), parents=[O], ID="A")
    B = m.set_point(sp.Integer(6), sp.Integer(0), parents=[O], ID="B")
    Ap = m.set_point(sp.Integer(12), sp.Integer(0), parents=[O], ID="A'")
    M1 = _midpoint(m, A, B, "M1", guide=True)
    M2 = _midpoint(m, B, Ap, "M2", guide=True)
    c1 = m.construct_circle(M1, B)
    c2 = m.construct_circle(M2, B)

    # Ray at slope 1/2: line y = x/2 meets c1: (x - 9/2)^2 + x^2/4 = 9/4 -> 5/4 x^2 - 9x + 18 = 0 -> x^2 - 36/5 x + 72/5 = 0
    # Use slope 3/4? Try P = (24/5, 6/5) on c1: (24/5 - 9/2)^2 + (6/5)^2 = (3/10)^2 + (12/10)^2 = 153/100 != 9/4.
    # Exact point on c1 ((x - 9/2)^2 + y^2 = 9/4): take x = 9/2 - 9/10 = 18/5, y = 6/5!
    # Check: (-9/10)^2 + (12/10)^2 = (81 + 144)/100 = 225/100 = 9/4! YES!
    # And OP^2 = (18/5)^2 + (6/5)^2 = 360/25 = 72/5, so P' = (36 / (72/5)) * P = (5/2) * P = (9, 3)!
    # Check P'=(9,3) on c2 ((x-9)^2 + y^2 = 9): (9-9)^2 + 3^2 = 9! 100% RATIONAL!
    P = m.set_point(sp.Rational(18, 5), sp.Rational(6, 5), parents=[c1], ID="P")
    Pp = m.set_point(sp.Integer(9), sp.Integer(3), parents=[c2], ID="P'")
    m.assert_incident(P, c1)
    m.assert_incident(Pp, c2)
    m.assert_collinear(O, P, Pp)
    _assert_zero(quadrance(O, P) * quadrance(O, Pp) - sp.Integer(36) ** 2, "Inversion OP * OP' = k^2")

    return SymbolicHeroSpec(
        key="circular_inversion",
        caption="Circular Inversion (O, k): Inverse Circles C₁ ↔ C₂ with Homologous Ray O–P–P'",
        alt="Circle of inversion centered at O mapping inner circle AB onto outer circle BA' with collinear inverse pair P, P'",
        model=m,
        points=[
            ("O", O, "O"),
            ("A", A, "A"),
            ("B", B, "B"),
            ("A'", Ap, "A'"),
            ("P", P, "P"),
            ("P'", Pp, "P'"),
        ],
        elements=[
            {"id": "axis", "type": "line", "p1": "O", "p2": "A'", "style": "solid", "ref": "[ O A' ]"},
            {"id": "cinv", "type": "circle", "center": "O", "through": "B", "style": "dashed", "ref": "( O B )"},
            {"id": "c1", "type": "circle", "center_pt": M1, "through": "B", "style": "bold", "ref": "( A B )"},
            {"id": "c2", "type": "circle", "center_pt": M2, "through": "B", "style": "bold", "ref": "( B A' )"},
            {"id": "rayP", "type": "segment", "p1": "O", "p2": "P'", "style": "dashed", "ref": "/ O P' /"},
        ],
        label_nudges={
            "O": (-12, 15),
            "A": (-6, 15),
            "B": (4, 15),
            "A'": (8, 15),
            "P": (-4, -10),
            "P'": (4, -10),
        },
    )


def _build_lemoine_symmedian() -> SymbolicHeroSpec:
    """Symmedians, Lemoine point K = X(6), Brocard circle, and First Lemoine Circle (§ 588)."""
    m, d = _heronian_base("hero_lemoine_symmedian")
    A, B, C, O = d["A"], d["B"], d["C"], d["O"]
    l_BC, l_CA, l_AB = d["l_BC"], d["l_CA"], d["l_AB"]

    # Exact rational Lemoine point K = (a^2 A + b^2 B + c^2 C) / (a^2 + b^2 + c^2) = (198/295, 1176/295)
    a2, b2, c2 = quadrance(B, C), quadrance(C, A), quadrance(A, B)
    denom = a2 + b2 + c2
    K = m.set_point(
        (a2 * A.x + b2 * B.x + c2 * C.x) / denom,
        (a2 * A.y + b2 * B.y + c2 * C.y) / denom,
        parents=[A, B, C],
        ID="K",
    )

    # Parallels through K to BC, CA, AB cut sides in 6 concyclic points (First Lemoine Circle, § 588)
    par_BC = _parallel_line(m, K, l_BC, guide=True)
    par_CA = _parallel_line(m, K, l_CA, guide=True)
    par_AB = _parallel_line(m, K, l_AB, guide=True)

    P_ab = m.intersect(par_BC, l_AB, ID="P1")
    P_ca = m.intersect(par_BC, l_CA, ID="P2")
    Q_bc = m.intersect(par_CA, l_BC, ID="Q1")
    Q_ab = m.intersect(par_CA, l_AB, ID="Q2")
    R_ca = m.intersect(par_AB, l_CA, ID="R1")
    R_bc = m.intersect(par_AB, l_BC, ID="R2")

    L1 = _midpoint(m, O, K, "L1", guide=True)
    c_lemoine1 = m.construct_circle(L1, P_ab)
    for pt in (P_ca, Q_bc, Q_ab, R_ca, R_bc):
        m.assert_incident(pt, c_lemoine1)

    c_brocard = m.construct_circle(L1, O, guide=True)
    m.assert_incident(K, c_brocard)

    return SymbolicHeroSpec(
        key="lemoine_symmedian",
        caption="Symmedians, Lemoine Point K = X(6), First Lemoine Six-Point Circle, and Brocard Circle",
        alt="Triangle ABC with symmedians meeting at Lemoine point K, parallels through K cutting the sides in six concyclic points on the First Lemoine Circle, and Brocard circle on diameter OK",
        model=m,
        points=[
            ("A", A, "A"),
            ("B", B, "B"),
            ("C", C, "C"),
            ("K", K, "K"),
            ("O", O, "O"),
            ("P1", P_ab, "P_1"),
            ("P2", P_ca, "P_2"),
            ("Q1", Q_bc, "Q_1"),
            ("R2", R_bc, "R_2"),
        ],
        elements=[
            {"id": "tri", "type": "polygon", "points": ["A", "B", "C"], "style": "solid", "ref": "< A B C >"},
            {"id": "lem1", "type": "circle", "center_pt": L1, "through": "P1", "style": "bold", "ref": "( P_1 P_2 Q_1 )"},
            {"id": "broc", "type": "circle", "center_pt": L1, "through": "O", "style": "dashed", "ref": "( O K )"},
            {"id": "symA", "type": "segment", "p1": "A", "p2": "K", "style": "dashed", "ref": "/ A K /"},
            {"id": "symB", "type": "segment", "p1": "B", "p2": "K", "style": "dashed", "ref": "/ B K /"},
            {"id": "symC", "type": "segment", "p1": "C", "p2": "K", "style": "dashed", "ref": "/ C K /"},
            {"id": "pBC", "type": "segment", "p1": "P1", "p2": "P2", "style": "solid", "ref": "/ P_1 P_2 /"},
            {"id": "pCA", "type": "segment", "p1": "Q1", "p2_pt": Q_ab, "style": "solid", "ref": "/ Q_1 Q_2 /"},
            {"id": "pAB", "type": "segment", "p1_pt": R_ca, "p2": "R2", "style": "solid", "ref": "/ R_1 R_2 /"},
        ],
        label_nudges={
            "K": (-14, -4),
            "O": (10, -6),
            "P1": (-16, -4),
            "P2": (8, -4),
            "Q1": (-6, 15),
            "R2": (6, 15),
        },
    )


SYMBOLIC_HERO_BUILDERS: dict[str, Callable[[], SymbolicHeroSpec]] = {
    "euler_feuerbach": _build_euler_feuerbach,
    "apollonian_locus": _build_apollonian_locus,
    "homothecy_circles": _build_homothecy_circles,
    "similitude_inscribed": _build_similitude_inscribed,
    "medians_centroid": _build_medians_centroid,
    "tritangent_incircle": _build_tritangent_incircle,
    "orthocenter_euler": _build_orthocenter_euler,
    "orthic_fagnano": _build_orthic_fagnano,
    "cyclic_quadrilateral": _build_cyclic_quadrilateral,
    "simson_line": _build_simson_line,
    "menelaus_ceva": _build_menelaus_ceva,
    "harmonic_quadrangle": _build_harmonic_quadrangle,
    "pole_polar_coaxal": _build_pole_polar_coaxal,
    "circular_inversion": _build_circular_inversion,
    "lemoine_symmedian": _build_lemoine_symmedian,
}


def render_symbolic_hero_svg(
    spec: SymbolicHeroSpec,
    out_svg_path: Path,
    folio_id: str = "hero",
    vw: float = 420.0,
    vh: float = 280.0,
    pad: float = 34.0,
) -> dict[str, Any]:
    """Project an exact :class:`SymbolicHeroSpec` onto an SVG viewport via ``compile_graphic_svg``."""
    # Verify zero sp.Float coordinates leaked into the symbolic Model
    for geom_key in spec.model:
        if isinstance(geom_key, spg.Point) and (
            geom_key.x.has(sp.Float) or geom_key.y.has(sp.Float)
        ):
            raise ValueError(f"sp.Float detected in symbolic model {spec.key}: {geom_key}")

    pt_lookup: dict[str, spg.Point] = {pk: pt for pk, pt, _ in spec.points}

    # Collect bounding box in Euclidean math coordinates (x right, y up)
    xs: list[float] = []
    ys: list[float] = []
    for _, pt, _ in spec.points:
        xs.append(float(pt.x.evalf()))
        ys.append(float(pt.y.evalf()))

    for el in spec.elements:
        if el["type"] == "circle":
            cpt = el.get("center_pt") or pt_lookup[el["center"]]
            tpt = el.get("through_pt") or pt_lookup[el["through"]]
            cx_m, cy_m = float(cpt.x.evalf()), float(cpt.y.evalf())
            r_m = math.hypot(float(tpt.x.evalf()) - cx_m, float(tpt.y.evalf()) - cy_m)
            xs.extend([cx_m - r_m, cx_m + r_m])
            ys.extend([cy_m - r_m, cy_m + r_m])

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    span_x = max(max_x - min_x, 1e-3)
    span_y = max(max_y - min_y, 1e-3)
    scale = min((vw - 2 * pad) / span_x, (vh - 2 * pad) / span_y)
    mid_x = 0.5 * (min_x + max_x)
    mid_y = 0.5 * (min_y + max_y)

    def to_svg(pt: spg.Point) -> tuple[float, float]:
        sx = 0.5 * vw + (float(pt.x.evalf()) - mid_x) * scale
        sy = 0.5 * vh - (float(pt.y.evalf()) - mid_y) * scale
        return round(sx, 2), round(sy, 2)

    cx_view = 0.5 * vw
    cy_view = 0.5 * vh

    points_json: dict[str, dict[str, Any]] = {}
    for pk, pt, label in spec.points:
        sx, sy = to_svg(pt)
        if pk in spec.label_nudges:
            dx, dy = spec.label_nudges[pk]
            lx, ly = round(sx + dx, 1), round(sy + dy, 1)
        else:
            vx, vy = sx - cx_view, sy - cy_view
            norm = math.hypot(vx, vy) or 1.0
            lx = round(sx + 14.0 * (vx / norm) - 4.0, 1)
            ly = round(sy + 14.0 * (vy / norm) + 5.0, 1)
        points_json[pk] = {
            "x": sx,
            "y": sy,
            "label": label,
            "label_x": max(6.0, min(vw - 18.0, lx)),
            "label_y": max(14.0, min(vh - 6.0, ly)),
        }

    # Register any unnamed helper points needed by elements
    helper_counter = 0

    def ensure_pt_key(pt_obj: spg.Point) -> str:
        nonlocal helper_counter
        for existing_k, existing_pt in pt_lookup.items():
            if existing_pt == pt_obj:
                return existing_k
        helper_counter += 1
        hk = f"HLP{helper_counter}"
        sx, sy = to_svg(pt_obj)
        points_json[hk] = {"x": sx, "y": sy, "hidden": True}
        pt_lookup[hk] = pt_obj
        return hk

    compiled_elements: list[dict[str, Any]] = []
    for el in spec.elements:
        ecopy = dict(el)
        if "center_pt" in ecopy:
            ecopy["center"] = ensure_pt_key(ecopy.pop("center_pt"))
        if "through_pt" in ecopy:
            ecopy["through"] = ensure_pt_key(ecopy.pop("through_pt"))
        if "p1_pt" in ecopy:
            ecopy["p1"] = ensure_pt_key(ecopy.pop("p1_pt"))
        if "p2_pt" in ecopy:
            ecopy["p2"] = ensure_pt_key(ecopy.pop("p2_pt"))
        if "points_pt" in ecopy:
            ecopy["points"] = [ensure_pt_key(p) for p in ecopy.pop("points_pt")]
        if ecopy["type"] == "line" and "p1" in ecopy and "p2" in ecopy:
            p1k, p2k = ecopy.pop("p1"), ecopy.pop("p2")
            ecopy.setdefault("ref", f"[ {p1k} {p2k} ]")
            x1, y1 = points_json[p1k]["x"], points_json[p1k]["y"]
            x2, y2 = points_json[p2k]["x"], points_json[p2k]["y"]
            dx_l, dy_l = x2 - x1, y2 - y1
            len_l = math.hypot(dx_l, dy_l) or 1.0
            overhang = 18.0
            ecopy["x1"] = round(max(8.0, min(vw - 8.0, x1 - overhang * dx_l / len_l)), 2)
            ecopy["y1"] = round(max(8.0, min(vh - 8.0, y1 - overhang * dy_l / len_l)), 2)
            ecopy["x2"] = round(max(8.0, min(vw - 8.0, x2 + overhang * dx_l / len_l)), 2)
            ecopy["y2"] = round(max(8.0, min(vh - 8.0, y2 + overhang * dy_l / len_l)), 2)
        compiled_elements.append(ecopy)

    graphic_dict = {
        "id": spec.key,
        "caption": spec.caption,
        "geometry": {
            "coord_space": "svg",
            "viewBox": f"0 0 {int(vw)} {int(vh)}",
            "points": points_json,
            "elements": compiled_elements,
        },
    }
    return compile_graphic_svg(folio_id, graphic_dict, out_svg_path)


CHAPTER_HERO_KEYS: dict[str, str] = {
    "frontmatter": "euler_feuerbach",
    "ch01-geometric-constructions": "apollonian_locus",
    "ch02-similitude-and-homothecy": "homothecy_circles",
    "ch03-properties-of-the-triangle": "euler_feuerbach",
    "ch04-the-quadrilateral": "cyclic_quadrilateral",
    "ch05-the-simson-line": "simson_line",
    "ch06-transversals": "menelaus_ceva",
    "ch07-harmonic-division": "harmonic_quadrangle",
    "ch08-circles": "pole_polar_coaxal",
    "ch09-inversion": "circular_inversion",
    "ch10-recent-geometry-of-the-triangle": "lemoine_symmedian",
    "historical-and-bibliographical-notes": "orthocenter_euler",
    "back-index": "tritangent_incircle",
}

# Calibrated folio SVGs preferred for specific transcribed sections: (chapter_dir, svg_filename, caption, alt)
CALIBRATED_SECTION_HEROES: dict[tuple[str, str], tuple[str, str, str, str]] = {
    ("ch01-geometric-constructions", "b-general-method"): (
        "01_geometric_constructions",
        "0028.g1.svg",
        "Fig. 6 — Square ABCD circumscribed/inscribed through four given points (§ 9)",
        "Calibrated Fig. 6 diagram illustrating Pappus's four-part analytic construction method",
    ),
    ("ch01-geometric-constructions", "c-geometric-loci"): (
        "01_geometric_constructions",
        "0034.g1.svg",
        "Fig. 11 — The Apollonian Circle locus of constant distance ratio (§ 11, Locus 11)",
        "Calibrated Fig. 11 diagram of the Apollonian circle on harmonic diameter CD",
    ),
    ("ch01-geometric-constructions", "d-indirect-elements"): (
        "01_geometric_constructions",
        "0045.g1.svg",
        "Fig. 21 — Right auxiliary triangle BGH unfolding altitude sum and side sum (§§ 20–21)",
        "Calibrated Fig. 21 diagram of auxiliary right triangle BGH for indirect elements",
    ),
    ("ch01-geometric-constructions", "review-exercises"): (
        "01_geometric_constructions",
        "0039.g1.svg",
        "Fig. 16 — Circular locus and secant ratio construction (§ 14)",
        "Calibrated Fig. 16 diagram of secants from a circle intercepting proportional segments",
    ),
    ("ch03-properties-of-the-triangle", "a-preliminaries"): (
        "03_properties_of_the_triangle",
        "0072.g1.svg",
        "Fig. 39 — Internal and external harmonic division of segment AB (§§ 54–66)",
        "Calibrated Fig. 39 diagram of harmonic division of segment AB via parallel lines",
    ),
    ("ch03-properties-of-the-triangle", "b-the-circumcircle"): (
        "03_properties_of_the_triangle",
        "0079.g1.svg",
        "Fig. 44 — Circumdiameter AK, altitude AD, bisector AU, and median AA' (§§ 73–78, 85)",
        "Calibrated Fig. 44 diagram of triangle ABC in its circumcircle with altitude, bisector, median, and circumdiameter",
    ),
    ("ch03-properties-of-the-triangle", "c-medians"): (
        "03_properties_of_the_triangle",
        "0084.g1.svg",
        "Fig. 47 — Concurrency and 2 : 1 trisection of medians at centroid G (§ 88)",
        "Calibrated Fig. 47 diagram of triangle ABC with medians meeting at centroid G",
    ),
}


def resolve_section_hero_key(chapter_slug: str, sec_code: str) -> str:
    """Select the exact symbolic hero key matching ``(chapter_slug, sec_code)``."""
    if chapter_slug == "ch01-geometric-constructions":
        return "apollonian_locus"
    if chapter_slug == "ch02-similitude-and-homothecy":
        return "similitude_inscribed" if sec_code == "A" else "homothecy_circles"
    if chapter_slug == "ch03-properties-of-the-triangle":
        if sec_code == "A":
            return "apollonian_locus"
        if sec_code == "C":
            return "medians_centroid"
        if sec_code.startswith("D") or sec_code == "Review":
            return "tritangent_incircle"
        if sec_code == "E.b":
            return "orthic_fagnano"
        if sec_code in {"E.a", "E.c", "G"}:
            return "orthocenter_euler"
        if sec_code == "F":
            return "euler_feuerbach"
        return "euler_feuerbach"
    if chapter_slug == "ch04-the-quadrilateral":
        return "cyclic_quadrilateral"
    if chapter_slug == "ch05-the-simson-line":
        return "simson_line"
    if chapter_slug == "ch06-transversals":
        return "menelaus_ceva"
    if chapter_slug == "ch07-harmonic-division":
        return "harmonic_quadrangle"
    if chapter_slug == "ch08-circles":
        if sec_code == "D":
            return "homothecy_circles"
        return "pole_polar_coaxal"
    if chapter_slug == "ch09-inversion":
        return "circular_inversion"
    if chapter_slug == "ch10-recent-geometry-of-the-triangle":
        if sec_code == "C":
            return "apollonian_locus"
        if sec_code == "D":
            return "orthic_fagnano"
        return "lemoine_symmedian"
    if chapter_slug == "historical-and-bibliographical-notes":
        if sec_code == "BibKey":
            return "apollonian_locus"
        if sec_code == "Names":
            return "lemoine_symmedian"
        return "euler_feuerbach"
    if chapter_slug == "back-index":
        return "orthic_fagnano" if sec_code == "Endmatter" else "tritangent_incircle"
    return CHAPTER_HERO_KEYS.get(chapter_slug, "euler_feuerbach")


class HeroFigureRegistry:
    """Lazy-cached builder and emitter of symbolic and calibrated hero ``.euclid-graphic`` SVGs."""

    def __init__(self, volume_dir: Path) -> None:
        self.volume_dir = volume_dir
        self._specs: dict[str, SymbolicHeroSpec] = {}
        self._rendered_bytes: dict[str, str] = {}

    def get_spec(self, key: str) -> SymbolicHeroSpec:
        if key not in self._specs:
            self._specs[key] = SYMBOLIC_HERO_BUILDERS[key]()
        return self._specs[key]

    def write_symbolic_hero(self, key: str, dest_dir: Path, filename: str = "hero.svg") -> tuple[str, str, str]:
        """Write ``<dest_dir>/<filename>`` and return ``(filename, caption, alt)``."""
        spec = self.get_spec(key)
        dest_path = dest_dir / filename
        if key not in self._rendered_bytes:
            render_symbolic_hero_svg(spec, dest_path, folio_id=f"hero-{key}")
            self._rendered_bytes[key] = dest_path.read_text(encoding="utf-8")
        else:
            dest_path.write_text(self._rendered_bytes[key], encoding="utf-8")
        return filename, spec.caption, spec.alt

    def write_section_hero(
        self,
        chapter_slug: str,
        sec_slug: str,
        sec_code: str,
        dest_dir: Path,
        filename: str = "hero.svg",
    ) -> tuple[str, str, str]:
        """Emit calibrated folio SVG if configured for ``(chapter_slug, sec_slug)``, else exact symbolic hero."""
        cal = CALIBRATED_SECTION_HEROES.get((chapter_slug, sec_slug))
        if cal is not None:
            cdir, svg_name, caption, alt = cal
            src_svg = self.volume_dir / cdir / svg_name
            if src_svg.is_file():
                shutil.copy2(src_svg, dest_dir / filename)
                return filename, caption, alt
        key = resolve_section_hero_key(chapter_slug, sec_code)
        return self.write_symbolic_hero(key, dest_dir, filename=filename)
