:layout: book
:type: item
:order: 6
:canonical_id: Ch.I.18
:title: § 18. Problem
:folio: 0042
:page: 23
:folios: 0042, 0043
:pages: 23, 24

.. _ch01-art-018:

§ 18. Problem
=============

.. folio:: 0042
   :page: 23

.. enunciation::

   *Construct a* :g:`triangle <0043.g1:< A B C >>` *given the* :g:`base <0043.g1:/ B C />`\ *, the* :g:`opposite angle <0043.g1:< B A C )>`\ *, and the* :g:`difference of the other two sides <0043.g1:/ D C />` :math:`(a, A, b - c)`.

Let :g:`ABC <0043.g1:< A B C >>` (Fig. 19) be the required triangle. On :g:`AC <0043.g1:/ A C />` lay off :eq:`AD = AB <0043.g1:/ A D / = 0043.g1:/ A B />`, so that :g:`CD <0043.g1:/ C D />` :math:`= b - c`. In the isosceles triangle :g:`ADB <0043.g1:< A B D >>`

.. math::

   \angle ADB = \angle ABD = \tfrac{1}{2}(180^\circ - A) = 90^\circ - \tfrac{1}{2}\,A;

.. folio:: 0043
   :page: 24

hence angle :g:`BDC <0043.g1:< B D C )>` :math:`= 90^\circ + \tfrac{1}{2}\,A`. Thus in the triangle :g:`BCD <0043.g1:< B C D >>` we know the base :g:`BC <0043.g1:/ B C />` :math:`= a`, the opposite angle :g:`BDC <0043.g1:< B D C )>` :math:`= 90^\circ + \tfrac{1}{2}\,A`, and the side :g:`CD <0043.g1:/ C D />` :math:`= b - c`; hence this triangle may be constructed. The vertices :g:`B <0043.g1:B>`, :g:`C <0043.g1:C>` belong to the required triangle :g:`ABC <0043.g1:< A B C >>`, whose third vertex :g:`A <0043.g1:A>` lies on :g:`CD <0043.g1:[ C D ]>` produced and on the :term:`mediator` of :g:`BD <0043.g1:/ B D />`.

.. picture:: 0043.g1.svg
   :alt: Fig. 19 — Auxiliary triangle BCD formed on AC by laying off AD = AB so that CD = b - c with altitude h_b
   :caption: FIG. 19

.. assertion:: [Discussion]

   The problem is impossible, unless :math:`a > (b - c)`. When this condition is satisfied, the :g:`given angle <0043.g1:< B D C )>` in the triangle :g:`BCD <0043.g1:< B C D >>` lies opposite the larger side :g:`BC <0043.g1:/ B C />`, and this triangle may be constructed in one way only. The proposed problem has thus one solution.

*Note.* The angle :g:`BCD <0043.g1:< B C D )>` of the auxiliary triangle :g:`BCD <0043.g1:< B C D >>` is equal to the angle :g:`C <0043.g1:< C )>` of the triangle :g:`ABC <0043.g1:< A B C >>`, angle :g:`BDC <0043.g1:< B D C )>` :math:`= 90^\circ + \tfrac{1}{2}\,A`, and:

.. math::

   \begin{aligned}
   \angle CBD &= \angle ABC - \angle ABD = B - (90^\circ - \tfrac{1}{2}\,A) \\
              &= B + \tfrac{1}{2}\,A + \tfrac{1}{2}\,C - \tfrac{1}{2}\,C - 90^\circ \\
              &= \tfrac{1}{2}(A + B + C) + \tfrac{1}{2}(B - C) - 90^\circ = \tfrac{1}{2}(B - C).
   \end{aligned}

Also the :g:`altitude <0043.g1:/ B K />` to :g:`CD <0043.g1:[ C D ]>` is the altitude :math:`h_b` of :g:`ABC <0043.g1:< A B C >>`. These relations may be used to solve the following problems.

----

See :ref:`Commentary on § 18. Problem <ch01-art-018-commentary>`.

.. toctree::
   :hidden:

   commentary
