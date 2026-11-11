:layout: book
:title: Chapter I: Geometric Constructions

.. _ch01-geometric-constructions-en:

Chapter I: Geometric Constructions
==================================

.. rubric:: Preliminaries, Analytic Method (Analysis, Construction, Proof, Discussion), Geometric Loci, and Indirect Elements

.. folio:: 0020
   :page: 1

A. PRELIMINARIES
----------------

**1. Notation.** We shall frequently denote by:

:math:`A, B, C, \dots` the vertices or the corresponding angles of a polygon;

:math:`a, b, c, \dots` the sides of the polygon (in the case of a triangle, the small letter will denote the side opposite the vertex indicated by the same capital letter);

:math:`2p` the perimeter of a triangle;

:math:`h_a, h_b, h_c` the altitudes and :math:`m_a, m_b, m_c` the medians of a triangle :math:`ABC` corresponding to the sides :math:`a, b, c`;

:math:`t_a, t_b, t_c` the internal, and :math:`t_a', t_b', t_c'` the external, bisectors of the angles :math:`A, B, C`;

:math:`R, r` the radii of the circumscribed and inscribed circles (for the sake of brevity, we shall use the terms *circumcircle*, *circumradius*, :term:`circumcenter <circumcircle>`, and *incircle*, *inradius*, :term:`incenter <incircle>`);

:math:`(A, r)` the circle having the point :math:`A` for center and the segment :math:`r` for radius;

:math:`M = (PQ, RS)` the point of intersection :math:`M` of the two lines :math:`PQ` and :math:`RS`.

**2. Basic Constructions.** Frequent use will be made of the following constructions:

To divide a given segment into a given number of equal parts.

To divide a given segment in a given ratio (i) internally; (ii) externally (§ 54).

To construct the :term:`fourth proportional <fourth-proportional>` to three given segments.

.. folio:: 0021
   :page: 2

To construct the :term:`mean proportional <fourth-proportional>` to two given segments.

To construct a square equivalent to a given (i) rectangle; (ii) triangle.

To construct a square equivalent to the sum of two, three, or more given squares.

To construct two segments given their sum and their difference.

To construct the tangents from a given point to a given circle.

To construct the internal and the external common tangents of two given circles.

EXERCISES
~~~~~~~~~

Construct a triangle, given:

1. :math:`a, b, c`.
2. :math:`a, b, C`.
3. :math:`a, B, C`.
4. :math:`a, h_a, B`.
5. :math:`a, b, m_a`.
6. :math:`a, B, t_b`.
7. :math:`A, h_a, t_a`.

Construct a right triangle, with its right angle at :math:`A`, given:

8. :math:`a, B`.
9. :math:`b, C`.
10. :math:`a, b`.
11. :math:`b, c`.

Construct a parallelogram :math:`ABCD`, given:

12. :math:`AB, BC, AC`.
13. :math:`AB, AC, B`.
14. :math:`AB, BD, \angle ABD`.

Construct a quadrilateral :math:`ABCD`, given:

15. :math:`A, B, C, AB, AD`.
16. :math:`AB, BC, CD, B, C`.
17. :math:`A, B, C, AD, CD`.

18. With a given radius to draw a circle tangent at a given point to a given (i) line; (ii) circle.
19. Through two given points to draw a circle (i) having a given radius; (ii) having its center on a given line.
20. To a given circle to draw a tangent having a given direction.
21. To divide a given segment internally and externally in the ratio of the squares of two given segments :math:`p, q`. (*Hint.* If :math:`AD` is the perpendicular to the hypotenuse :math:`BC` of the right triangle :math:`ABC`, :math:`AB^2 : AC^2 = BD : DC`.)
22. Construct a right triangle, given the hypotenuse and the ratio of the squares of the legs.
23. Given the segments :math:`a, p, q`, construct the segment :math:`x` so that :math:`x^2 : a^2 = p : q`.
24. Construct an equilateral triangle equivalent to a given triangle.

**3. Suggestion.** Most of the preceding problems are stated in conventional symbols. It is instructive to state them in words. For instance, Exercise 4 may be stated as follows: Construct a triangle given the base, the corresponding altitude, and one of the base angles.

.. folio:: 0022
   :page: 3

B. GENERAL METHOD OF SOLUTION OF CONSTRUCTION PROBLEMS
------------------------------------------------------

**4. Analytic Method.** Some construction problems are direct applications of known propositions and their solutions are almost immediately apparent. Example: Construct an equilateral triangle.

If the solution of a problem is more involved, but the solution is known, it may be presented by starting with an operation which we know how to perform, followed by a series of operations of this kind, until the goal is reached.

This procedure is called the :term:`synthetic method <synthetic-method>` of solution of problems. It is used to present the solutions of problems in textbooks.

However, this method cannot be followed when one is confronted with a problem the solution of which is not apparent, for it offers no clue as to what the first step shall be, and the possible first steps are far too numerous to be tried at random.

On the other hand, we do know definitely what the problem is — we know what figure we want to obtain in the end. It is therefore helpful to start with this very figure, provisionally taken for granted. By a careful and attentive study of this figure a way may be discovered leading to the desired solution. The procedure, which is called the :term:`analytic method <analytic-method>` of solving problems, consists, in outline, of the following steps:

:term:`ANALYSIS <analysis-step>`. Assuming the problem solved, draw a figure approximately satisfying the conditions of the problem and investigate how the given parts and the unknown parts of the figure are related to one another, until you discover a relation that may be used for the construction of the required figure.

:term:`CONSTRUCTION <construction-step>`. Utilizing the information obtained in the analysis, carry out the actual construction.

:term:`PROOF <proof-step>`. Show that the figure thus constructed satisfies all the requirements of the problem.

:term:`DISCUSSION <discussion-step>`. Discuss the problem as to the conditions of its possibility, the number of solutions, etc.

The following examples illustrate the method.

**5. Problem.** *Two points* :math:`A, B` *are marked on two given parallel lines* :math:`x, y`. *Through a given point* :math:`C`, *not on either of these lines, to draw a secant* :math:`CA'B'` *meeting* :math:`x, y` *in* :math:`A', B'` *so that the segments* :math:`AA', BB'` *shall be proportional to two given segments* :math:`p, q`.

.. folio:: 0023
   :page: 4

.. picture:: 0023.g1.png
   :alt: Fig. 1 — Secant CA'B' meeting parallel lines x, y so that AA' : BB' = p : q
   :caption: FIG. 1

ANALYSIS. Let :math:`CA'B'` be the required line, so that (Fig. 1):

.. math::

   AA' : BB' = p : q,

and let :math:`O = (AB, A'B')`. The two triangles :math:`OAA', OBB'` are similar; hence:

.. math::

   AO : BO = AA' : BB'.

But the latter ratio is known; hence the point :math:`O` divides the given segment :math:`AB` in the given ratio :math:`p : q`. Thus we may construct :math:`O`, and :math:`OC` is the required line.

CONSTRUCTION. Construct the point :math:`O` such that:

.. math::

   AO : BO = p : q.

The points :math:`O` and :math:`C` determine the required line.

PROOF. Left to the student.

DISCUSSION. There are two points, :math:`O` and :math:`O'`, which divide the given segment :math:`AB` in the given ratio :math:`p : q`, one externally and the other internally, and we can always construct these two points; hence the problem has two solutions if neither of the lines :math:`CO, CO'` is parallel to the lines :math:`x, y`.

Consider the case when :math:`p = q`.

**6. Problem.** *Through a given point, outside a given circle, to draw a secant so that the chord intercepted on it by the circle shall subtend at the center an angle equal to the acute angle between the required secant and the diameter, produced, passing through the given point.*

.. folio:: 0024
   :page: 5

ANALYSIS. Let the required secant :math:`MBA` (Fig. 2) through the given point :math:`M` cut the given circle, center :math:`O`, in :math:`A` and :math:`B`. The two triangles :math:`AOB, AOM` have the angle :math:`A` in common and, by assumption, angle :math:`AOB =` angle :math:`M`; hence the two triangles are equiangular. But the triangle :math:`AOB` is isosceles; hence the triangle :math:`AOM` is also isosceles, and :math:`MA = MO`. Now the length :math:`MO` is known; hence the distance :math:`MA` of the point :math:`A` from :math:`M` is known, so that the point :math:`A` may be constructed, and the secant :math:`MA` may be drawn.

CONSTRUCTION. Draw the circle :math:`(M, MO)`. If :math:`A` is a point common to the two circles, the line :math:`MA` satisfies the conditions of the problem.

PROOF. Let the line :math:`MA` meet the given circle again in :math:`B`. The triangles :math:`AOB, AOM` are isosceles, for :math:`OA = OB`, :math:`MA = MO`, as radii of the same circle, and the angle :math:`A` is a common base angle in the two triangles; hence the angles :math:`AOB` and :math:`M` opposite the respective bases :math:`AB` and :math:`AO` in the two triangles are equal. Thus :math:`MA` is the required line.

.. picture:: 0024.g1.png
   :alt: Fig. 2 — Secant MBA from exterior point M to circle (O) with MA = MO
   :caption: FIG. 2

DISCUSSION. We can always draw the circle :math:`(M, MO)` which will cut the given circle in two points :math:`A` and :math:`A'`; hence the problem always has two solutions, symmetrical with respect to the line :math:`MO`.

Could the line :math:`MBA` be drawn so that the angle :math:`AOB` would be equal to the *obtuse* angle between :math:`MBA` and :math:`MO`? If that were possible, we would have:

.. math::

   \angle AOB + \angle OMA = 180^\circ;

hence:

.. math::

   \angle OMA = \angle OAB + \angle OBA.

.. folio:: 0025
   :page: 6

But in the triangle :math:`OBM` we have:

.. math::

   \angle M < \angle OBA.

We are thus led to a contradiction; hence a line satisfying the imposed condition cannot be drawn.

Consider the problem when the point :math:`M` is given inside the given circle, or on the given circle.

.. picture:: 0025.g1.png
   :alt: Fig. 3 — Equal three-segment chain AD = DE = EC on triangle ABC via auxiliary circles (B, BA) and (K, BA)
   :caption: FIG. 3

**7. Problem.** *On the sides* :math:`AB, AC`, *produced if necessary, of the triangle* :math:`ABC` *to find two points* :math:`D, E` *such that the segments* :math:`AD, DE`, *and* :math:`EC` *shall be equal* (Fig. 3).

ANALYSIS. Suppose that the points :math:`D, E` satisfy the conditions of the problem, and let the parallels through :math:`B` to the lines :math:`DE, DC` meet :math:`AC` in :math:`K, L`. The two triangles :math:`ADE, ABK` are similar, and since :math:`AD = DE`, by assumption, we have :math:`AB = BK`, and the point :math:`K` is readily constructed.

Again, the triangles :math:`DEC, BKL` are similar, and since :math:`DE = EC`, by assumption, we have :math:`BK = KL`; hence :math:`L` is known.

CONSTRUCTION. Draw the circle :math:`(B, BA)` cutting :math:`AC` again in :math:`K`. Draw the circle :math:`(K, BA)` cutting :math:`AC` in :math:`L`. The parallel through :math:`C` to :math:`BL` meets the line :math:`AB` in the first required point :math:`D`, and the parallel through :math:`D` to :math:`BK` meets :math:`AC` in the second required point :math:`E`.

PROOF. The steps in the proof are the same as those in the analysis, but taken in reverse order.

DISCUSSION. The point :math:`K` always has one and only one position. When :math:`K` is constructed we find two positions for :math:`L`, and we have two solutions, :math:`DE` and :math:`D'E'`, for the problem.

If :math:`A` is a right angle the problem becomes trivial.

.. folio:: 0026
   :page: 7

**8. Problem.** *On two given circles find two points a given distance apart and such that the line joining them shall have a given direction.*

ANALYSIS. Let :math:`P, Q` be the required points on the two given circles :math:`(A), (B)`. Through the center :math:`A` of :math:`(A)` (Fig. 4) draw a parallel to :math:`PQ` and lay off :math:`AR = PQ`. In the parallelogram :math:`APQR` we have :math:`RQ = AP`. But :math:`AP` is a radius of a given circle; hence the length :math:`RQ` is known. On the other hand the point :math:`R` is known, for both the direction and the length of :math:`AR` are given; hence the point :math:`Q` may be constructed. The point :math:`P` is then readily found.

CONSTRUCTION. Through the center :math:`A` of one of the two given circles, :math:`(A)`, draw a line having the given direction and lay off :math:`AR` equal to the given length, :math:`m`. With :math:`R` as center and radius equal to the radius of :math:`(A)` draw a circle :math:`(A')`, meeting the second given circle in a point :math:`Q`. Through :math:`Q` draw a parallel to :math:`AR` and lay off :math:`QP = AR`, so as to form a parallelogram in which :math:`AR` is a side (and not a diagonal). The points :math:`P, Q` satisfy the conditions of the problem.

PROOF. The segment :math:`PQ` has the given length and the given direction, by construction. The point :math:`Q` was taken on the circle :math:`(B)`. In order to show that :math:`P` lies on the circle :math:`(A)` it is enough to point out that in the parallelogram :math:`ARQP` we have :math:`AP = RQ`, and :math:`RQ` is equal to the radius of :math:`(A)`, by construction.

.. picture:: 0026.g1.png
   :alt: Fig. 4 — Translation of circle (A) by vector AR of length m to intersect circle (B) at Q
   :caption: FIG. 4

.. picture:: 0026.g2.png
   :alt: Fig. 5 — Four-solution configuration of § 8 via symmetric translated centers R and R'
   :caption: FIG. 5

DISCUSSION. It is always possible to draw through :math:`A` a line having the given direction. The point :math:`R` may then be marked on either side of :math:`A`, so that we always have for :math:`R` two positions, :math:`R` and :math:`R'`. The circle with either of these points as center and radius equal to the radius of :math:`(A)` may cut :math:`(B)` in two points, or may be tangent to :math:`(B)`, or may not cut :math:`(B)` at all. Consequently the problem may have four, three, two, one, or no solutions.

Figure 5 illustrates the case when there are four solutions.

.. folio:: 0027
   :page: 8

**9. Problem.** *Construct a square so that each side, or the side produced, shall pass through a given point.*

ANALYSIS. Let :math:`PQRS` be a square whose sides :math:`PQ, QR, RS, SP` pass, respectively, through the given points :math:`A, B, C, D` (Fig. 6).

If the perpendicular from :math:`D` upon :math:`AC` meets the line :math:`QR` in :math:`F`, then :math:`DF = AC`. Indeed, if we leave the line :math:`DF` fixed while we revolve the square, and the line :math:`AC` with it, around its center by an angle of :math:`90^\circ` so that the sides :math:`PQ, QR, RS, SP` shall occupy the present positions of :math:`QR, RS, SP, PQ`, respectively, the line :math:`AC` will become parallel to :math:`DF`; hence :math:`AC = DF`.

.. picture:: 0027.g1.png
   :alt: Fig. 6 — Square PQRS circumscribed about four given points A, B, C, D with DF perpendicular and equal to AC
   :caption: FIG. 6

That :math:`DF = AC` may also be seen in another way. Let the parallels through :math:`Q` to the lines :math:`AC, DF` meet :math:`RS, SP` in the points :math:`K, L`. In the right triangles :math:`PQL, QRK` we have:

.. math::

   \angle PQL = \angle LQR - \angle PQR = \angle LQR - \angle LQK = \angle KQR.

Thus the two triangles are equiangular, and since :math:`PQ = QR`, by assumption, they are congruent; hence :math:`QL = QK`. But :math:`QL = DF`, :math:`QK = AC`; hence :math:`AC = DF`.

The equality of these two segments suggests the following

CONSTRUCTION. From the given point :math:`D` drop a perpendicular :math:`DF` upon the given line :math:`AC` and lay off :math:`DF = AC`. Join :math:`F` to the fourth given point :math:`B`, and through :math:`D` draw a parallel to :math:`BF`. These two parallel lines and the perpendiculars to them through :math:`A` and :math:`C` form the required square :math:`PQRS`.

.. folio:: 0028
   :page: 9

.. picture:: 0028.g1.png
   :alt: Fig. 7 — Six-solution configuration of squares passing through four given points A, B, C, D
   :caption: FIG. 7

PROOF. From the construction it follows immediately that :math:`PQRS` is a rectangle whose sides pass respectively through the given points :math:`A, B, C, D`.

To show that this rectangle is a square we consider again the triangles :math:`PQL, QRK`, and, as in the analysis, we show that they are equiangular. Now :math:`DF = AC`, by construction; hence :math:`QL = QK`; therefore the triangles are congruent, and :math:`QP = QR`.

DISCUSSION. We obtain a second solution if we make the symmetric :math:`F'` of :math:`F` with respect to :math:`D` play the role of the point :math:`F`.

Moreover, the perpendicular from :math:`D` may also be dropped upon either of the other two sides :math:`AB, BC` of the triangle :math:`ABC`, and we will obtain two more pairs of solutions. The problem thus has, in general, six different solutions. It is, of course, immaterial to which of the four given points we assign the role of the point :math:`D`.

Should the point :math:`F` happen to coincide with :math:`B`, the direction of the line :math:`BF` becomes indeterminate, that is, any line through :math:`B` may be taken as a side of the required square, and the figure completed accordingly. Thus if the segment joining two of the four given points is equal to and perpendicular to the segment joining the remaining two points, the problem has an infinite number of solutions.

Figure 7 presents the case when the problem has six solutions.

**10. Suggestions.** The figure for the analysis may be drawn freehand and the given elements arranged as conveniently as possible to give a correct idea of the problem and to exhibit the existing interrelations between the elements involved.

.. folio:: 0029
   :page: 10

The construction should be carried out with ruler and compasses. The given magnitudes, like segments and angles, should be set down before any construction is attempted, and used in the actual construction. If the problem involves points and lines given in position, these data should be marked in the figure before any constructional operations are begun.

In the discussion each step of the construction should be examined for the number of ways it may be carried out and for the number of lines or points of intersection the considered step will yield.

The different aspects which the problem may assume, as indicated by the discussion, should be illustrated by suitable figures. As a general rule a problem or a figure has many more possibilities than is at first apparent. A careful study of a problem will often reveal vistas which in a more casual treatment may readily escape notice.

EXERCISES
~~~~~~~~~

1. Through a given point to draw a line making equal angles with the sides of a given angle.
2. Through a given point to draw a line so that two given parallel lines shall intercept on it a segment of given length.
3. Through one of the two points of intersection of two equal circles to draw two equal chords, one in each circle, forming a given angle.
4. Through a given point of a circle to draw a chord which shall be twice as long as the distance of this chord from the center of the circle.
5. On a produced diameter of a given circle to find a point such that the tangents drawn from it to this circle shall be equal to the radius of the circle.
6. With a given point as center to describe a circle which shall bisect a given circle, that is, the common chord shall be a diameter of the given circle.
7. Through two given points to draw a circle so that its common chord with a given circle shall be parallel to a given line.
8. Construct a parallelogram so that three of its sides shall have for midpoints three given points.
9. On a given leg of a right triangle to find a point equidistant from the hypotenuse and from the vertex of the right angle.
10. With two given points as centers to draw equal circles so that one of their common tangents shall (i) pass through a (third) given point; (ii) be tangent to a given circle.
11. Through a given point to draw a line so that the two chords intercepted on it by two given equal circles shall be equal.
12. To a given circle, located between two parallel lines, to draw a tangent so that the segment intercepted on it by the given parallels shall have a given length.
13. Construct a right triangle given the hypotenuse and the distance from the middle point of the hypotenuse to one leg.

.. folio:: 0030
   :page: 11

14. Construct a triangle given an altitude and the circumradii (i.e., the radii of the circumscribed circles) of the two triangles into which this altitude divides the required triangle.

C. GEOMETRIC LOCI
-----------------

**11. Important Loci.** In a great many cases the solution of a geometric problem depends upon the finding of a point which satisfies certain conditions. For instance, in order to draw a circle passing through three given points, it is necessary to find a point, the center of the circle, equidistant from the three given points.

The problem of drawing a tangent from a given point to a given circle is solved when we find the point of contact, i.e., the point on the circle at which a right angle is subtended by the segment limited by the given point and the center of the given circle.

If one of the conditions which the required point must satisfy be set aside, the problem may have many solutions. However, the point will not become arbitrary, but will move along a certain path, the :term:`geometric locus <geometric-locus>` of the point. Now by taking into consideration the discarded condition and setting aside another, we make the required point describe another geometric locus. A point common to the two loci is the point sought.

The problem of drawing a circle passing through three given points may again serve as an illustration. In order to find a point equidistant from three given points, :math:`A, B, C`, we disregard one of the given points, say :math:`C`, and try to find a point equidistant from :math:`A` and :math:`B`. Thus stated, the problem has many solutions, the required point being any point of the perpendicular bisector of the segment :math:`AB`. Now considering the point :math:`C` and leaving out the point :math:`A`, the required point describes the perpendicular bisector of the segment :math:`BC`. The required point lies at the intersection of the two perpendicular bisectors.

The nature of the loci obtained depends upon the condition omitted. In elementary geometry these conditions must be such that the loci shall consist of straight lines and circles. The neatness and simplicity of a solution depend very largely upon the judicious choice of the geometric loci.

Knowledge about a considerable number of geometric loci may often enable one to discover immediately where the required point is to be located.

.. folio:: 0031
   :page: 12

.. picture:: 0031.g1.png
   :alt: Fig. 8 — Capable arc AMB on chord AB with tangent AT making angle BAT = angle AMB
   :caption: FIG. 8

The following are the most important and the most frequently useful geometric loci:

LOCUS 1. *The locus of a point in a plane at a given distance from a given point is a circle having the given point for center and the given distance for radius.*

LOCUS 2. *The locus of a point from which tangents of given length can be drawn to a given circle is a circle concentric with the given circle.*

LOCUS 3. *The locus of a point at a given distance from a given line consists of two lines parallel to the given line.*

LOCUS 4. *The locus of a point equidistant from two given points is the perpendicular bisector of the segment determined by the two points.*

For the sake of brevity the expression *perpendicular bisector* may be replaced conveniently by the term :term:`mediator <mediator>`.

LOCUS 5. *The locus of a point equidistant from two intersecting lines indefinitely produced consists of the two bisectors of the angles formed by the two given lines.*

LOCUS 6. *The locus of a point such that the tangents from it to a given circle form a given angle, or, more briefly, at which the circle subtends a given angle, is a circle concentric with the given circle.*

LOCUS 7. *The* :term:`locus of a point <subtended-angle-locus>`\ *, on one side of a given segment, at which this segment subtends a given angle is an arc of a circle passing through the ends of the segment.*

Let :math:`M` (Fig. 8) be a point of the locus so that the angle :math:`AMB` is equal to the given angle. Pass a circle through the three points :math:`A, B, M`. At any point :math:`M'` of the arc :math:`AMB` the segment :math:`AB` subtends the same angle as at :math:`M`; hence every point of the arc :math:`AMB` belongs to the required locus. On the other hand, any point :math:`N` not on the arc :math:`AMB` will lie either inside or outside this arc. In the first case the angle :math:`ANB` will be larger, and in the second case smaller, than the angle :math:`AMB`. Hence :math:`N` does not belong to the locus.

.. folio:: 0032
   :page: 13

The tangent :math:`AT` to the circle :math:`AMB` at the point :math:`A` makes an angle with :math:`AB` equal to the angle :math:`AMB`. Hence :math:`AT` may be drawn. The construction of the circle :math:`AMB` is therefore reduced to the problem of drawing a circle tangent to a given line :math:`AT` at a given point :math:`A`, and passing through another given point :math:`B`.

If the condition that the point :math:`M` is to lie on a given side of the line :math:`AB` is disregarded, the required locus consists of two arcs of circles congruent to each other and located on opposite sides of :math:`AB`.

If the given angle is a right angle, the two arcs will be two semicircles of the same radius, and we have: *The locus of a point at which a given segment subtends a right angle is the circle having this segment for diameter.*

LOCUS 8. *The locus of the midpoints of the chords of a given circle which pass through a fixed point is a circle when the point lies inside of or on the circle.*

Let :math:`P` (Fig. 9) be the given point, and :math:`M` the midpoint of a chord :math:`AB` of the given circle :math:`(O)`, the chord passing through the given point :math:`P`.

.. picture:: 0032.g1.png
   :alt: Fig. 9 — Circle on diameter OP as locus of midpoints M of chords AB of circle (O) through P
   :caption: FIG. 9

The segment :math:`OP` subtends a right angle at :math:`M`; hence :math:`M` lies on the circle having :math:`OP` for diameter (locus 7). On the other hand, any point :math:`M` of this circle joined to :math:`P` determines a chord of the circle :math:`(O)` which is perpendicular to :math:`OM` at :math:`M`. Hence :math:`M` is the midpoint of this chord and therefore belongs to the required locus.

.. folio:: 0033
   :page: 14

If the point :math:`P` lies outside of :math:`(O)`, any point :math:`M` of the locus must lie on the circle having :math:`OP` for diameter, but not every point of this circle belongs to the locus. The locus consists of the part of the circle :math:`(OP)` which lies within the given circle :math:`(O)`.

LOCUS 9. *The locus of the midpoints of all the chords of given length drawn in a given circle is a circle concentric with the given circle.*

.. picture:: 0033.g1.png
   :alt: Fig. 10 — Triangle ABM with median MO and altitude MD for Locus 10 (sum of squares of distances)
   :caption: FIG. 10

The chords are all tangent to this circle at their respective midpoints.

LOCUS 10. *The locus of a point the sum of the squares of whose distances from two given points is equal to a given constant is a circle having for center the midpoint of the given segment.*

Let :math:`M` (Fig. 10) be a point on the locus. Join :math:`M` to the midpoint :math:`O` of the segment :math:`AB` determined by the two given points :math:`A, B` and drop the perpendicular :math:`MD` from :math:`M` upon :math:`AB`. From the triangles :math:`AOM` and :math:`BOM` we have:

.. math::

   AM^2 = OM^2 + OA^2 - 2\,OA \cdot OD, \qquad BM^2 = OM^2 + OB^2 + 2\,OB \cdot OD.

But:

.. math::

   OA = OB = \tfrac{1}{2}\,AB;

hence, adding, we have:

.. math::

   AM^2 + BM^2 = 2\,OM^2 + 2\,OA^2.

Now :math:`AM^2 + BM^2` is, by assumption, equal to a given constant, say :math:`s^2`, and :math:`OA^2 = a^2`, where :math:`2a` represents the length of the known segment :math:`AB`. Hence:

.. math::

   (1) \qquad OM^2 = \tfrac{1}{2}\,s^2 - a^2.

Thus the point :math:`M` lies at a fixed distance :math:`OM` from the fixed point :math:`O`, and therefore the locus of :math:`M` is a circle with :math:`O` as center.

The radius :math:`OM` may be constructed from the formula (1) as follows. :math:`OM` is one leg of a right triangle which has for its other leg half the length of the given segment :math:`AB`, and for hypotenuse the side of a square whose diagonal is equal to :math:`s`.

.. folio:: 0034
   :page: 15

LOCUS 11. *The locus of a point the ratio of whose distances from two fixed points is constant, is a circle, called the circle of* :person:`Apollonius <apollonius>`, *or the* :term:`Apollonian circle <apollonian-circle>`.

Let :math:`A, B` be the two given points (Fig. 11) and :math:`p : q` the given ratio. Let the points :math:`C, D` divide the segment :math:`AB` internally and externally in the given ratio, and let :math:`M` be any point of the locus. We have thus:

.. math::

   AC : CB = AD : DB = AM : MB = p : q.

The lines :math:`MC, MD` divide the side :math:`AB` of the triangle :math:`ABM` internally and externally in the ratio of the sides :math:`MA, MB`; hence :math:`MC, MD` are the internal and external bisectors of the angle :math:`AMB`, and therefore are perpendicular to each other. Thus at any point :math:`M` of the required locus the known segment :math:`CD` subtends a right angle; hence :math:`M` lies on the circle having :math:`CD` for diameter (§ 11, locus 7).

.. picture:: 0034.g1.png
   :alt: Fig. 11 — Apollonian circle on diameter CD dividing AB internally and externally in ratio p : q
   :caption: FIG. 11

CONVERSELY. Let us take any point :math:`M` on this circle and show that this point belongs to the required locus. Through the point :math:`B` draw the parallels :math:`BE, BF` to the lines :math:`MC, MD` meeting :math:`AM` in :math:`E, F`, respectively. We thus have:

.. math::

   (1) \qquad AM : ME = AC : CB, \qquad AM : FM = AD : BD.

But the second ratios in these proportions are equal, by construction, hence:

.. math::

   AM : ME = AM : FM;

therefore:

.. math::

   ME = MF.

.. folio:: 0035
   :page: 16

Thus :math:`M` is the midpoint of the segment :math:`EF`. But :math:`EBF` is a right angle, for its sides are parallel to the sides of the right angle :math:`CMD`, and in the right triangle :math:`EBF` the line :math:`MB` is equal to half the hypotenuse :math:`EF`; hence, replacing in the first proportion of (1) the segment :math:`ME` by the equal segment :math:`MB`, we obtain:

.. math::

   AM : MB = AC : CB = p : q,

which shows that :math:`M` belongs to the locus.

Where, in this converse proof, has the fact been used that :math:`M` is a point of the circle?

*Note.* The point :math:`C` divides the segment :math:`AB` internally so that :math:`AC : CB = p : q`. But we may also construct the point :math:`C'` such that :math:`BC' : C'A = p : q`. Similarly for the external point of division. Thus the locus actually consists of two :term:`Apollonian circles <apollonian-circle>`, unless the order in which the two given points are to be taken is specified in the statement of the locus. In actual applications the nature of the problem often indicates the order in which the points are to be considered.

.. picture:: 0035.g1.png
   :alt: Fig. 12 — Perpendicular MC to line AB for Locus 12 (constant difference of squares AM^2 - BM^2 = d^2)
   :caption: FIG. 12

LOCUS 12. *The locus of a point the difference of the squares of whose distances from two given points is constant, is a straight line perpendicular to the line joining the given points.*

Let :math:`A, B` (Fig. 12) be the two given points, and let :math:`M` be a point such that:

.. math::

   AM^2 - BM^2 = d^2,

where :math:`d` is given.

If :math:`MC` is the perpendicular from :math:`M` to :math:`AB`, we have from right triangles:

.. math::

   AM^2 - AC^2 = MC^2 = MB^2 - BC^2;

hence:

.. math::

   AM^2 - MB^2 = AC^2 - BC^2 = d^2,

or:

.. math::

   (AC - BC)(AC + BC) = d^2,

.. folio:: 0036
   :page: 17

and therefore, denoting :math:`AC + BC = AB` by :math:`a`:

.. math::

   AC - BC = d^2 \div a.

This equality gives the difference of the segments :math:`AC` and :math:`BC`, while the sum of these segments is equal to :math:`a`. Thus these segments may be constructed, and the point :math:`C` located on the line :math:`AB`. Hence the foot :math:`C` of the perpendicular dropped upon :math:`AB` from any point :math:`M` of the locus is a fixed point of :math:`AB`. Consequently the point :math:`M` lies on the perpendicular to the line :math:`AB` at the point :math:`C`. It is readily shown that, conversely, every point of this perpendicular belongs to the locus.

*Note.* We will obtain a different line for the locus of :math:`M` if we consider that :math:`BM^2 - AM^2 = d^2`. In fact, the locus actually consists of two straight lines, unless the order in which the two given points are to be considered is specified in the statement of the locus.

EXERCISES
~~~~~~~~~

1. A variable parallel to the base :math:`BC` of a triangle :math:`ABC` meets :math:`AB, AC` in :math:`D, E`. Show that the locus of the point :math:`M = (BE, CD)` is a straight line.
2. On the sides :math:`AB, AC` of a triangle :math:`ABC` are laid off two equal segments :math:`AB', AC'` of variable length. The perpendiculars to :math:`AB, AC` at :math:`B', C'` meet in :math:`D`. Show that the locus of the point :math:`D` is a straight line. Find the locus of the projection of :math:`D` upon the line :math:`B'C'`.
3. Find the locus of a point at which two consecutive segments :math:`AB, BC` of the same straight line subtend equal angles.
4. The base :math:`BC` of a variable triangle :math:`ABC` is fixed, and the sum :math:`AB + AC` is constant. The line :math:`DP` drawn through the midpoint :math:`D` of :math:`BC` parallel to :math:`AB` meets the parallel :math:`CP` through :math:`C` to the internal bisector of the angle :math:`A`, in :math:`P`. Show that the locus of :math:`P` is a circle having :math:`D` for center.

The following are examples of the use of loci in the solution of problems.

**12. Problem.** *Draw a circle passing through two given points and subtending a given angle at a third given point.*

ANALYSIS. Let :math:`(O)` be the required circle passing through the two given points :math:`A, B` (Fig. 13). The angle formed by the tangents :math:`CT, CT'` from the given point :math:`C` to :math:`(O)` is given; hence in the right triangle :math:`OTC` we know the acute angle :math:`OCT`, i.e., we know the shape of this triangle. Thus the ratio :math:`OT : OC` is known, therefore also the ratios:

.. math::

   OA : OC = OB : OC.

Consequently we have two loci for the point :math:`O` (two :term:`Apollonian circles <apollonian-circle>`), and the point may be found.

.. folio:: 0037
   :page: 18

.. picture:: 0037.g1.png
   :alt: Fig. 13 — Circle (O) through A and B subtending given angle at C via intersection of two Apollonian circles
   :caption: FIG. 13

CONSTRUCTION. On the internal bisector :math:`PQ` of the given angle :math:`P` take an arbitrary point :math:`Q` and drop the perpendicular :math:`QR` upon one of the sides. Divide each of the two given segments :math:`AC, BC` internally and externally in the ratio :math:`QR : QP` in the points :math:`E, F` and :math:`G, H`, respectively. A point :math:`O` common to the two circles having :math:`EF` and :math:`GH` for diameters is the center of the required circle.

The proof and the discussion are left to the student.

**13. Problem.** *Through two given points of a circle to draw two parallel chords whose sum shall have a given length.*

ANALYSIS. Let :math:`A, B` be the two given points of the circle, center :math:`O`, and let :math:`AC, BD` be the two required chords. In the isosceles trapezoid :math:`ABDC` (Fig. 14) :math:`CD = AB`, and the length :math:`AB` is known; hence :math:`CD` is tangent to a known circle having :math:`O` for center and touching :math:`CD` at its midpoint :math:`F` (§ 11, locus 9).

If :math:`E` is the midpoint of :math:`AB` we have:

.. math::

   2\,EF = AC + BD.

Now the point :math:`E` and the length :math:`AC + BD` are known; hence we have a second locus for the point :math:`F`.

CONSTRUCTION. Draw the circle :math:`(O, OE)`. If :math:`2s` is the given length, draw the circle :math:`(E, s)` meeting :math:`(O, OE)` in :math:`F`. The tangent to :math:`(O, OE)` at :math:`F` meets the given circle :math:`(O)` in :math:`C` and :math:`D`. The lines :math:`AC, BD` are the required chords.

PROOF. The two chords :math:`AB, CD` are equal, for they are equidistant from the center :math:`O` of the given circle :math:`(O)`. Hence :math:`ABDC` is an isosceles trapezoid, and therefore:

.. math::

   AC + BD = 2\,EF.

Now :math:`EF = s`, by construction; hence :math:`AC + BD` has the required length.

.. folio:: 0038
   :page: 19

DISCUSSION. The circle :math:`(E, s)` will not cut the circle :math:`(O, OE)`, if :math:`s` is greater than :math:`2\,OE`. If :math:`s < 2\,OE`, we obtain two points of intersection :math:`F` and :math:`F'`, and therefore two solutions.

The tangent to the circle :math:`(O, OE)` at :math:`F` determines the two points :math:`C, D` on the circle :math:`(O)`. These two points and the given points :math:`A, B` determine four lines, namely two sides and the two diagonals of the isosceles trapezoid. The figure will show which two of these four lines are those required.

.. picture:: 0038.g1.png
   :alt: Fig. 14 — Isosceles trapezoid ABDC inscribed in circle (O) with midline EF = s tangent to (O, OE)
   :caption: FIG. 14

.. picture:: 0038.g2.png
   :alt: Fig. 15 — Crossed-trapezoid regime when s < EG so tangent at F crosses chord AB
   :caption: FIG. 15

Let :math:`G` (Fig. 15) be the point of contact of the second tangent issued from :math:`A` to the circle :math:`(O, OE)`. If :math:`s < EG`, the tangent to :math:`(O, OE)` at :math:`F` will cross the chord :math:`AB`, and in the resulting trapezoid the line :math:`AB` will be a diagonal. The line :math:`EF` is equal to one-half the difference of the two bases.

Consider the case when the two chords are required to have a given difference.

**14. Problem.** *On a given circle to find a point such that the lines joining it to two given points on this circle shall meet a given line in two points the ratio of whose distances from a given point on this line shall have a given value.*

Let the lines :math:`AM, BM` joining the given points :math:`A, B` on the circle to the required point :math:`M` meet the given line :math:`FPQ` in the points :math:`P, Q` (Fig. 16). If :math:`F` is the given fixed point and the parallel :math:`QL` to :math:`MA` through :math:`Q` meets the line :math:`FA` in :math:`L`, we have angle :math:`LQB = AMB`, and the latter angle is known, for the chord :math:`AB` is given.

.. folio:: 0039
   :page: 20

.. picture:: 0039.g1.png
   :alt: Fig. 16 — Point M on circle projecting A, B onto line FPQ with given ratio FQ : FP via capable arc on LB
   :caption: FIG. 16

On the other hand we have:

.. math::

   FL : FA = FQ : FP,

and the second ratio is given; hence the point :math:`L` is known. Thus the known segment :math:`LB` subtends a given angle at the point :math:`Q`, which gives a locus for this point (§ 11, locus 7). The point :math:`Q` lies at the intersection of this locus with the given line :math:`FPQ`. The line :math:`BQ` meets the circle in the required point :math:`M`.

The proof and discussion are left to the reader.

EXERCISES
~~~~~~~~~

Construct a triangle, given:

1. :math:`a, b, A`.
2. :math:`a, c, h_b`.
3. :math:`a, h_a, m_a`.
4. :math:`a, h_a, b : c`.
5. :math:`a, m_a, b : c`.
6. :math:`a, t_a, b : c`.

Construct a parallelogram, given:

7. An altitude and the two diagonals.
8. The two altitudes and an angle.
9. The two altitudes and a diagonal.
10. A side, an angle, and a diagonal.
11. A side, the corresponding altitude, and the angle between the diagonals.

Construct a quadrilateral :math:`ABCD`, given:

12. The diagonal :math:`AC` and the angles :math:`ABC, ADC, BAC, DAC`.
13. The sides :math:`AB, BC`, the diagonal :math:`CA`, and the angles :math:`ADB, BDC`.
14. The sides :math:`AB, AD`, the angle :math:`DAB`, and the radius of the inscribed circle.
15. Construct a quadrilateral given three sides and the radius of the circumscribed circle. Give a discussion.
16. Given three points, to find a fourth point, in the same plane, such that its distances to the given points may have given ratios.

.. folio:: 0040
   :page: 21

17. With a given radius to draw a circle so that it shall touch a given circle and have its center on a given line.
18. With a given radius to draw a circle so that it shall pass through a given point and the tangents drawn to this circle from another given point shall be of given length.
19. In a given circle to inscribe a right triangle so that each leg shall pass through a given point.
20. Construct a triangle given the base, the opposite angle, and the point in which the bisector of this angle meets the base.
21. Construct a triangle given the base and the angles which the median to the base makes with the other two sides.
22. About a given circle to circumscribe a triangle given a side and one of its adjacent angles, so that the vertex of this angle shall lie on a given line.
23. Construct a triangle given the base, an adjacent angle, and the angle which the median issued from the vertex of this angle makes with the side opposite the vertex of this angle.

D. INDIRECT ELEMENTS
--------------------

Among the conditions which a figure to be constructed may be required to satisfy, elements may be given which do not occur directly in the figure in question. For instance, it may be required that the sum of two sides of a triangle shall have a given length, or that the difference of the base angles shall have a given magnitude, etc. In order to arrive at a method of solution of such a problem, it is necessary to introduce this “:term:`indirect element <indirect-elements>`” in the analysis of the problem.

**15. Problem.** *Construct a triangle given the perimeter, the angle opposite the base, and the altitude to the base* :math:`(2p, A, h_a)`.

.. picture:: 0040.g1.png
   :alt: Fig. 17 — Auxiliary triangle AEF of base EF = 2p unfolded from triangle ABC by laying off BE = BA and CF = CA
   :caption: FIG. 17

Let :math:`ABC` (Fig. 17) be the required triangle. Produce :math:`BC` on both sides and lay off :math:`BE = BA`, :math:`CF = CA`. Thus :math:`EF = 2p`.

The triangles :math:`EAB, FCA` are isosceles, hence:

.. math::

   \angle E = \angle EAB = \tfrac{1}{2}\,\angle ABC, \qquad \angle F = \angle FAC = \tfrac{1}{2}\,\angle ACB;

hence:

.. math::

   \angle EAF = \tfrac{1}{2}\,B + A + \tfrac{1}{2}\,C = \tfrac{1}{2}(A + B + C) + \tfrac{1}{2}\,A = 90^\circ + \tfrac{1}{2}\,A,

----

.. note::

   **Editorial Continuation (Folios ``0041``–``0052``, Pages 22–33)**

   Article **§ 15** continues onto Folio ``0041`` (p. 22): *“and therefore the angle* :math:`EAF` *is known. The altitude* :math:`AD` *of the triangle* :math:`ABC` *is also the altitude of* :math:`AEF` *... Since* :math:`BA = BE, CA = CF`, *the vertices* :math:`B, C` *are the traces on* :math:`EF` *of the mediators of* :math:`AE` *and* :math:`AF` *.”*

   All 300 DPI archival scans for the remainder of Chapter I: Geometric Constructions (``0041.png``–``0052.png``, covering **§§ 15–22** and **Review Exercises 1–74**) are ingested in ``resources/college_geometry/01_geometric_constructions/`` and indexed below for Phase 2 transcription.

Remaining Chapter I Architecture (Folios ``0041``–``0052``)
-----------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 12 48 16 12 12

   * - Section
     - Title
     - Folios
     - Pages
     - Articles
   * - ``A``
     - Preliminaries
     - ``0020``–``0021``
     - 1–2
     - §§ 1–3
   * - ``B``
     - General Method of Solution of Construction Problems
     - ``0022``–``0030``
     - 3–11
     - §§ 4–10
   * - ``C``
     - Geometric Loci
     - ``0030``–``0040``
     - 11–21
     - §§ 11–14
   * - ``D``
     - Indirect Elements
     - ``0040``–``0048``
     - 21–29
     - §§ 15–22
   * - ``Review``
     - Review Exercises (1–74)
     - ``0048``–``0052``
     - 29–33
     - —
