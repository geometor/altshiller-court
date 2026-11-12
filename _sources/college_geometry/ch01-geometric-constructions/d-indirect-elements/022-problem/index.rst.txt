:layout: book
:type: item
:order: 13
:canonical_id: Ch.I.22
:title: § 22. Problem
:folio: 0046
:page: 27
:folios: 0046, 0047
:pages: 27, 28

.. _ch01-art-022:

§ 22. Problem
=============

.. folio:: 0046
   :page: 27

.. enunciation::

   *Construct a* :g:`triangle <0046.g1:< A B C >>` *given the* :g:`base <0046.g1:/ B C />`\ *, the* :g:`opposite angle <0046.g1:< B A C )>`\ *, and the* :g:`difference of the altitudes <0046.g1:/ C G />` *to the other two sides* :math:`(a, A, h_c - h_b)`.

Let :g:`ABC <0046.g1:< A B C >>` (Fig. 22) be the required triangle. Draw the altitudes :g:`BE <0046.g1:/ B E />`, :g:`CF <0046.g1:/ C F />`, and lay off :eq:`FG = BE <0046.g1:/ F G / = 0046.g1:/ B E />`, so that :g:`CG <0046.g1:/ C G />` :math:`= h_c - h_b`. Draw :g:`GH <0046.g1:/ G H />` parallel to :g:`AB <0046.g1:/ A B />`. In the right triangle :g:`CGH <0046.g1:< C G H >>` we know the leg :g:`CG <0046.g1:/ C G />` :math:`= h_c - h_b` and the angle :g:`CHG <0046.g1:< C H G )>` :math:`= A`; hence this triangle may be constructed, and the length :g:`CH <0046.g1:/ C H />` is determined.

.. picture:: 0046.g1.svg
   :alt: Fig. 22 — Right auxiliary triangle CGH with leg CG = h_c - h_b, hypotenuse CH = b - c, and angle bisector BH
   :caption: FIG. 22

We now show that :g:`CH <0046.g1:/ C H />` :math:`= b - c`. Drop the perpendicular :g:`HI <0046.g1:/ H I />` from :g:`H <0046.g1:H>` upon :g:`AB <0046.g1:/ A B />`. We have :eq:`HI = FG <0046.g1:/ H I / = 0046.g1:/ F G />` :math:`=` :g:`BE <0046.g1:/ B E />`, hence the two right triangles :g:`ABE <0046.g1:< A B E >>`, :g:`AHI <0046.g1:< A H I >>` are congruent, having the angle :g:`A <0046.g1:< B A C )>` in common and :eq:`BE = HI <0046.g1:/ B E / = 0046.g1:/ H I />`; therefore :eq:`AH = AB <0046.g1:/ A H / = 0046.g1:/ A B />`, so that:

.. math::

   CH = CA - AH = CA - AB = b - c.

With :math:`b - c` known, the proposed problem is reduced to a known problem (§ 18).

However, the required :g:`triangle <0046.g1:< A B C >>` may be obtained directly from the triangle :g:`CHG <0046.g1:< C G H >>`. The vertex :g:`C <0046.g1:C>` belongs to the required triangle. From the isosceles triangle :g:`ABH <0046.g1:< A B H >>` we have angle :g:`AHB <0046.g1:< A H B )>` :math:`= \tfrac{1}{2}(180^\circ - A)`; but:

.. math::

   \angle AHG = 180^\circ - \angle GHC = 180^\circ - A;

.. folio:: 0047
   :page: 28

hence :g:`BH <0046.g1:[ B H ]>` is the bisector of the angle :g:`AHG <0046.g1:< A H G )>` and thus furnishes a :term:`locus <geometric-locus>` for the vertex :g:`B <0046.g1:B>` of :g:`ABC <0046.g1:< A B C >>`, the other locus being the circle :math:`(C, a)`. The vertex :g:`A <0046.g1:A>` is now obtained as the trace on :g:`CH <0046.g1:[ C H ]>`, produced, of the :term:`mediator` of :g:`BH <0046.g1:/ B H />`.

If the given angle :g:`A <0046.g1:< B A C )>` is obtuse, the triangle :g:`CGH <0046.g1:< C G H >>` will include not :g:`A <0046.g1:< B A C )>`, but its supplement, and the problem may be solved in the same way.

*Note.* The preceding discussion shows that the elements:

.. math::

   b - c, \quad h_c - h_b, \quad A

constitute a :term:`datum`.

----

See :ref:`Commentary on § 22. Problem <ch01-art-022-commentary>`.

.. toctree::
   :hidden:

   commentary
