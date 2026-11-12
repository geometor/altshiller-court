:layout: book
:type: item
:order: 1
:canonical_id: Ch.I.15
:title: § 15. Problem
:folio: 0040
:page: 21
:folios: 0040, 0041
:pages: 21, 22

.. _ch01-art-015:

§ 15. Problem
=============

.. folio:: 0040
   :page: 21

.. enunciation::

   *Construct a* :g:`triangle <0040.g1:< A B C >>` *given the* :g:`perimeter <0040.g1:/ E F />`\ *, the* :g:`angle <0040.g1:< B A C )>` *opposite the* :g:`base <0040.g1:/ B C />`\ *, and the* :g:`altitude <0040.g1:/ A D />` *to the base* :math:`(2p, A, h_a)`.

.. picture:: 0040.g1.svg
   :alt: Fig. 17 — Auxiliary triangle AEF of base EF = 2p unfolded from triangle ABC by laying off BE = BA and CF = CA
   :caption: FIG. 17

Let :g:`ABC <0040.g1:< A B C >>` (Fig. 17) be the required triangle. Produce :g:`BC <0040.g1:[ B C ]>` on both sides and lay off :eq:`BE = BA <0040.g1:/ B E / = 0040.g1:/ B A />`, :eq:`CF = CA <0040.g1:/ C F / = 0040.g1:/ C A />`. Thus :g:`EF <0040.g1:/ E F />` :math:`= 2p`.

The triangles :g:`EAB <0040.g1:< E A B >>`, :g:`FCA <0040.g1:< F C A >>` are isosceles, hence:

.. math::

   \angle E = \angle EAB = \tfrac{1}{2}\,\angle ABC, \qquad \angle F = \angle FAC = \tfrac{1}{2}\,\angle ACB;

hence:

.. math::

   \angle EAF = \tfrac{1}{2}\,B + A + \tfrac{1}{2}\,C = \tfrac{1}{2}(A + B + C) + \tfrac{1}{2}\,A = 90^\circ + \tfrac{1}{2}\,A,

.. folio:: 0041
   :page: 22

and therefore the angle :g:`EAF <0040.g1:< E A F )>` is known. The altitude :g:`AD <0040.g1:/ A D />` of the triangle :g:`ABC <0040.g1:< A B C >>` is also the altitude of :g:`AEF <0040.g1:< A E F >>`. Thus in the triangle :g:`AEF <0040.g1:< A E F >>` we know the base :g:`EF <0040.g1:/ E F />` :math:`= 2p`, the opposite angle :g:`EAF <0040.g1:< E A F )>` :math:`= 90^\circ + \tfrac{1}{2}\,A`, and the altitude :g:`AD <0040.g1:/ A D />` :math:`= h_a`; hence this triangle may be constructed. The vertex :g:`A <0040.g1:A>` of this triangle also belongs to the required triangle :g:`ABC <0040.g1:< A B C >>`. Since :eq:`BA = BE <0040.g1:/ B A / = 0040.g1:/ B E />`, :eq:`CA = CF <0040.g1:/ C A / = 0040.g1:/ C F />`, the vertices :g:`B <0040.g1:B>`, :g:`C <0040.g1:C>` are the traces on :g:`EF <0040.g1:/ E F />` of the :term:`mediators <mediator>` of :g:`AE <0040.g1:/ A E />` and :g:`AF <0040.g1:/ A F />`.

The problem may have two solutions symmetrical with respect to the :term:`mediator` of :g:`EF <0040.g1:/ E F />`, or one solution, or none.

*Note.* In order to construct the required triangle :g:`ABC <0040.g1:< A B C >>` we have constructed another triangle :g:`AEF <0040.g1:< A E F >>`, as an intermediate step. Use of an auxiliary triangle is often very helpful.

----

See :ref:`Commentary on § 15. Problem <ch01-art-015-commentary>`.

.. toctree::
   :hidden:

   commentary
