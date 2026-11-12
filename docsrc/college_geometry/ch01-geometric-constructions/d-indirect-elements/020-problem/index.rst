:layout: book
:type: item
:order: 10
:canonical_id: Ch.I.20
:title: § 20. Problem
:folio: 0044
:page: 25
:folios: 0044, 0045
:pages: 25, 26

.. _ch01-art-020:

§ 20. Problem
=============

.. folio:: 0044
   :page: 25

.. enunciation::

   *Construct a* :g:`triangle <0045.g1:< A B C >>` *given the* :g:`base <0045.g1:/ B C />`\ *, the* :g:`opposite angle <0045.g1:< B A C )>`\ *, and the* :g:`sum of the altitudes <0045.g1:/ B G />` *to the other two sides* :math:`(a, A, h_b + h_c)`.

Let :g:`ABC <0045.g1:< A B C >>` be the required triangle (Fig. 21). Produce the altitude :g:`BE <0045.g1:/ B E />` and lay off :eq:`EG <0045.g1:/ E G / = 0045.g1:/ C F />` equal to the altitude :g:`CF <0045.g1:/ C F />`. Through :g:`G <0045.g1:G>` draw the line :g:`GH <0045.g1:[ G H ]>` parallel to :g:`AC <0045.g1:/ A C />` meeting :g:`BA <0045.g1:[ B A ]>`, produced, in :g:`H <0045.g1:H>`. Hence:

.. math::

   \angle BHG = \angle BAC = A, \qquad \angle BGH = \angle BEA = 90^\circ.

Thus in the right triangle :g:`BGH <0045.g1:< B G H >>` we know the leg :g:`BG <0045.g1:/ B G />` :math:`= h_b + h_c` and the acute angle :g:`BHG <0045.g1:< B H G )>` :math:`= A`; hence this triangle may be constructed and the length :g:`BH <0045.g1:/ B H />` determined.

It is readily shown that :g:`BH <0045.g1:/ B H />` :math:`= b + c`. Draw the line :g:`AI <0045.g1:/ A I />` parallel to :g:`BG <0045.g1:/ B G />` meeting :g:`HG <0045.g1:[ H G ]>` in the point :g:`I <0045.g1:I>`. :g:`AIGE <0045.g1:< A I G E >>` is a rectangle and therefore :eq:`AI = EG <0045.g1:/ A I / = 0045.g1:/ E G />` :math:`= h_c`. Now in the right triangles :g:`ACF <0045.g1:< A C F >>`, :g:`AHI <0045.g1:< A H I >>`, we have:

.. folio:: 0045
   :page: 26

.. picture:: 0045.g1.svg
   :alt: Fig. 21 — Right auxiliary triangle BGH with leg BG = h_b + h_c, hypotenuse BH = b + c, and angle bisector HC
   :caption: FIG. 21

.. math::

   AI = CF = h_c, \qquad \angle AHI = \angle CAF = A;

hence the two triangles are congruent, and :eq:`AH = AC <0045.g1:/ A H / = 0045.g1:/ A C />` :math:`= b`; therefore:

.. math::

   BH = BA + AH = b + c.

Thus, of the required triangle :g:`ABC <0045.g1:< A B C >>` we know now: :math:`a, A, b + c`, and the problem is reduced to a known problem (§ 17).

.. assertion:: [Direct Locus Recovery]

   However, the passage from the auxiliary triangle :g:`BGH <0045.g1:< B G H >>` to the required triangle :g:`ABC <0045.g1:< A B C >>` may be made directly in the figure. The vertex :g:`B <0045.g1:B>` of :g:`BGH <0045.g1:< B G H >>` belongs to :g:`ABC <0045.g1:< A B C >>`. In order to find :g:`C <0045.g1:C>` we observe that in the isosceles triangle :g:`AHC <0045.g1:< A H C >>` we have:

   .. math::

      \angle AHC = \angle ACH = \tfrac{1}{2}\,A,

   and since angle :g:`AHG <0045.g1:< A H G )>` :math:`= A`, the line :g:`HC <0045.g1:[ H C ]>` is the bisector of the angle :g:`H <0045.g1:< B H G )>`, and this line constitutes a :term:`locus <geometric-locus>` for the point :g:`C <0045.g1:C>`. The circle :math:`(B, a)` is a second locus for :g:`C <0045.g1:C>`. The vertex :g:`A <0045.g1:A>` is then determined on the side :g:`BH <0045.g1:/ B H />` of :g:`BGH <0045.g1:< B G H >>` by the :term:`mediator` of :g:`CH <0045.g1:/ C H />`.

If the given angle :g:`A <0045.g1:< B A C )>` is obtuse, the triangle :g:`BGH <0045.g1:< B G H >>` will include not :g:`A <0045.g1:< B A C )>` but its supplement, and the problem may be solved in the same way.

----

See :ref:`Commentary on § 20. Problem <ch01-art-020-commentary>`.

.. toctree::
   :hidden:

   commentary
