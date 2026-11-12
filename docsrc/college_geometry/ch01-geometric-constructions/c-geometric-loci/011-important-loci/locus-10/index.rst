:layout: book
:type: locus
:order: 10
:canonical_id: Ch.I.11.L10
:title: Locus 10
:folio: 0033
:page: 14
:folios: 0033, 0034
:pages: 14, 15

.. _ch01-locus-10:

Locus 10
========

.. folio:: 0033
   :page: 14

.. enunciation::

   *The locus of a point the sum of the squares of whose distances from two given points is equal to a given constant is a circle having for center the midpoint of the given segment.*

.. picture:: 0033.g1.svg
   :alt: Fig. 10 — Triangle ABM with median MO and altitude MD for Locus 10 (sum of squares of distances)
   :caption: FIG. 10

Let :g:`M <0033.g1:M>` (Fig. 10) be a point on the locus. Join :g:`M <0033.g1:M>` to the :eq:`midpoint <0033.g1:/ O A / = 0033.g1:/ O B />` :g:`O <0033.g1:O>` of the segment :g:`AB <0033.g1:/ A B />` determined by the two given points :g:`A <0033.g1:A>`, :g:`B <0033.g1:B>` and drop the perpendicular :g:`MD <0033.g1:/ M D />` from :g:`M <0033.g1:M>` upon :g:`AB <0033.g1:/ A B />`. From the triangles :g:`AOM <0033.g1:< A O M >>` and :g:`BOM <0033.g1:< B O M >>` we have:

.. math::

   AM^2 = OM^2 + OA^2 - 2\,OA \cdot OD, \qquad BM^2 = OM^2 + OB^2 + 2\,OB \cdot OD.

But:

.. math::

   OA = OB = \tfrac{1}{2}\,AB;

hence, adding, we have:

.. math::

   AM^2 + BM^2 = 2\,OM^2 + 2\,OA^2.

Now :math:`AM^2 + BM^2` is, by assumption, equal to a given constant, say :math:`s^2`, and :math:`OA^2 = a^2`, where :math:`2a` represents the length of the known segment :g:`AB <0033.g1:/ A B />`. Hence:

.. math::

   (1) \qquad OM^2 = \tfrac{1}{2}\,s^2 - a^2.

.. assertion::

   Thus the point :g:`M <0033.g1:M>` lies at a fixed distance :g:`OM <0033.g1:/ O M />` from the fixed point :g:`O <0033.g1:O>`, and therefore the locus of :g:`M <0033.g1:M>` is a circle with :g:`O <0033.g1:O>` as center.

The radius :g:`OM <0033.g1:/ O M />` may be constructed from the formula (1) as follows. :g:`OM <0033.g1:/ O M />` is one leg of a right triangle which has for its other leg half the length of the given segment :g:`AB <0033.g1:/ A B />`, and for hypotenuse the side of a square whose diagonal is equal to :math:`s`.

.. folio:: 0034
   :page: 15

----

See :ref:`Commentary on Locus 10 <ch01-locus-10-commentary>`.

.. toctree::
   :hidden:

   commentary
