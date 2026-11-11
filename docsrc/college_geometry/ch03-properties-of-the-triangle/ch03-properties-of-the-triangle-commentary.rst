:layout: book
:title: Chapter III: Properties of the Triangle — Commentary

.. _ch03-properties-of-the-triangle-commentary:

Chapter III: Properties of the Triangle — Commentary
====================================================

.. rubric:: Constructive Analysis, Historical Provenance & GEOMETOR Notes (0072–0142, pp. 53–123)

Mathematical Architecture & Classical Triangle Canon
----------------------------------------------------

Spanning 186 articles (§§ 54–239, pp. 53–123), Chapter III is the monumental heart of the first half of *College Geometry*:

1. **Harmonic Preliminaries (§§ 54–67)**: Early introduction of :term:`harmonic division <harmonic-division>` and the :term:`Apollonian circle <apollonian-circle>`, honoring the pedagogical innovation announced in the 1952 :ref:`Preface <frontmatter-en>`.
2. **Circumcircle & Medians (§§ 68–110)**: Antipodal chords, Simson/Johnson precursors, the Problem of :person:`Pappus <pappus>` (§ 84), Apollonius' median formula, the :term:`centroid <centroid>` :math:`G = X(2)`, and the :term:`complementary <complementary-triangle>` and :term:`anticomplementary <anticomplementary-triangle>` triangles.
3. **Tritangent Circles (§§ 111–174)**: The :term:`incircle <incircle>` and three excircles :math:`(I, I_a, I_b, I_c)`, :person:`Carnot's <carnot>` theorem (§ 146), :person:`Chapple <chapple>`–:person:`Euler <euler>` distance formula :math:`OI^2 = R(R - 2r)` (§ 152, :cite:`Euler 1765 <euler:1765>`), and semiperimeter contact identities (:math:`s - a, s - b, s - c`).
4. **Altitudes, Euler Line & Nine-Point Circle (§§ 175–219)**: Concurrency at the :term:`orthocenter <orthocenter>` :math:`H = X(4)`, minimum-perimeter property of the :term:`orthic triangle <orthic-triangle>` (:person:`Fagnano <fagnano>`, § 194), collinearity of :math:`O, G, N, H` on the :term:`Euler line <euler-line>` (§ 202), the :term:`nine-point circle <nine-point-circle>` (§ 206, :person:`Brianchon <brianchon>` & :person:`Poncelet <poncelet>`), and :term:`Feuerbach's theorem <feuerbach-theorem>` (§ 215, :cite:`Feuerbach 1822 <feuerbach:1822>`).
5. **Orthocentric Group (§§ 220–239)**: Symmetric quadruple :math:`\{A, B, C, H\}` (:term:`orthocentric quadrilateral <orthocentric-quadrilateral>`) sharing a common nine-point circle.

GEOMETOR Ecosystem Connections
------------------------------

* **`geometor/etc` & :cite:`Kimberling's ETC <kimberling:etc>`**: Establishes exact synthetic constructions for :math:`X(1)` (*incenter*), :math:`X(2)` (*centroid*), :math:`X(3)` (*circumcenter*), :math:`X(4)` (*orthocenter*), :math:`X(5)` (*nine-point center*), and :math:`X(11)` (*Feuerbach point*).
* **`geometor/model`**: Every center and circle in §§ 54–239 is quadratic constructible over :math:`\mathbb{Q}(A, B, C)` and verifiable symbolically in SymPy without floating-point drift.


Cross-Repository GEOMETOR Links
-------------------------------

* ``geometor/elements (IV.2–IV.5)``
* ``geometor/pappus (§ 84 Problem of Pappus)``
* ``geometor/etc (X(1) Incenter, X(2) Centroid, X(3) Circumcenter, X(4) Orthocenter, X(5) Nine-Point Center, X(7) Gergonne, X(8) Nagel, X(11) Feuerbach)``
