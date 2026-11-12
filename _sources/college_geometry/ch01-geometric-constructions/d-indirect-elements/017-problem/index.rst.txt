:layout: book
:type: item
:order: 4
:canonical_id: Ch.I.17
:title: § 17. Problem
:folio: 0041
:page: 22
:folios: 0041, 0042
:pages: 22, 23

.. _ch01-art-017:

§ 17. Problem
=============

.. folio:: 0041
   :page: 22

.. enunciation::

   *Construct a* :g:`triangle <0041.g1:< A B C >>` *given the* :g:`base <0041.g1:/ B C />`\ *, the* :g:`opposite angle <0041.g1:< B A C )>`\ *, and the* :g:`sum of the other two sides <0041.g1:/ B D />` :math:`(a, A, b + c)`.

.. picture:: 0041.g1.svg
   :alt: Fig. 18 — Auxiliary triangle BCD formed by producing BA beyond A to D so that AD = AC and BD = b + c
   :caption: FIG. 18

Let :g:`ABC <0041.g1:< A B C >>` (Fig. 18) be the required triangle. Produce :g:`BA <0041.g1:[ B A ]>` and lay off :eq:`AD = AC <0041.g1:/ A D / = 0041.g1:/ A C />`. In the isosceles triangle :g:`ACD <0041.g1:< A C D >>` we have angle :eq:`D = ACD <0041.g1:< A D C ) = 0041.g1:< A C D )>` :math:`= \tfrac{1}{2}`\ :g:`BAC <0041.g1:< B A C )>`. Thus in the triangle :g:`BCD <0041.g1:< B C D >>` we know the base :g:`BC <0041.g1:/ B C />` :math:`= a`, the side :g:`BD <0041.g1:/ B D />` :math:`= b + c`, and the angle :g:`D <0041.g1:< A D C )>` :math:`= \tfrac{1}{2}\,A`; hence this triangle may be constructed. The vertices :g:`B <0041.g1:B>`, :g:`C <0041.g1:C>` belong also to the required triangle, and the third vertex :g:`A <0041.g1:A>` is the intersection of :g:`BD <0041.g1:/ B D />` with the :term:`mediator` of the segment :g:`CD <0041.g1:/ C D />`.

.. folio:: 0042
   :page: 23

.. assertion:: [Discussion]

   :term:`DISCUSSION. <discussion-step>` The problem is not possible, unless :math:`a < (b + c)`. Assuming that this condition is satisfied, we have given in the auxiliary triangle :g:`BCD <0041.g1:< B C D >>` the :g:`angle <0041.g1:< A D C )>` opposite the smaller side; hence we may have two such triangles, one, or none. From each auxiliary triangle we obtain one and only one required :g:`triangle <0041.g1:< A B C >>`; hence the problem may have two, one, or no solutions.

*Note.* In the auxiliary triangle :g:`BCD <0041.g1:< B C D >>` we have:

.. math::

   \angle D = \tfrac{1}{2}\,\angle A, \qquad B = B,

and:

.. math::

   \begin{aligned}
   \angle BCD &= \angle BCA + \angle ACD = C + \tfrac{1}{2}\,A \\
              &= \tfrac{1}{2}\,C + \tfrac{1}{2}\,C + \tfrac{1}{2}\,A + \tfrac{1}{2}\,B - \tfrac{1}{2}\,B \\
              &= \tfrac{1}{2}(A + B + C) - \tfrac{1}{2}(B - C) = 90^\circ - \tfrac{1}{2}(B - C).
   \end{aligned}

In the triangle :g:`BCD <0041.g1:< B C D >>` the altitude to :g:`BD <0041.g1:/ B D />` is the altitude :math:`h_c` of :g:`ABC <0041.g1:< A B C >>`.

Instead of producing the side :g:`AB <0041.g1:/ B A />`, it is in some cases preferable to produce the side :g:`AC <0041.g1:/ A C />`.

These relations afford a ready solution of the following problems.

Other problems involving the sum of two sides of a triangle will be considered later (§§ 157–173).

----

See :ref:`Commentary on § 17. Problem <ch01-art-017-commentary>`.

.. toctree::
   :hidden:

   commentary
