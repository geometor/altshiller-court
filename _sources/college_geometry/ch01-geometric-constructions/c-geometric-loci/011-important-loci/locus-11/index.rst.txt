:layout: book
:type: locus
:order: 11
:canonical_id: Ch.I.11.L11
:title: Locus 11
:folio: 0034
:page: 15
:folios: 0034, 0035
:pages: 15, 16

.. _ch01-locus-11:

Locus 11
========

.. folio:: 0034
   :page: 15

.. enunciation::

   *The locus of a point the ratio of whose distances from two fixed points is constant, is a circle, called the circle of* :person:`Apollonius <apollonius>`, *or the* :term:`Apollonian circle <apollonian-circle>`.

Let :g:`A <0034.g1:A>`, :g:`B <0034.g1:B>` be the two given points (Fig. 11) and :math:`p : q` the given ratio. Let the points :g:`C <0034.g1:C>`, :g:`D <0034.g1:D>` divide the segment :g:`AB <0034.g1:/ A B />` internally and externally in the given ratio, and let :g:`M <0034.g1:M>` be any point of the locus. We have thus:

.. math::

   AC : CB = AD : DB = AM : MB = p : q.

.. assertion:: [§ 11, Locus 7]

   The lines :g:`MC <0034.g1:/ M C />`, :g:`MD <0034.g1:/ M D />` divide the side :g:`AB <0034.g1:/ A B />` of the triangle :g:`ABM <0034.g1:< A B M >>` internally and externally in the ratio of the sides :g:`MA <0034.g1:/ M A />`, :g:`MB <0034.g1:/ M B />`; hence :g:`MC <0034.g1:/ M C />`, :g:`MD <0034.g1:/ M D />` are the internal and external bisectors of the angle :g:`AMB <0034.g1:< A M B )>`, and therefore are perpendicular to each other. Thus at any point :g:`M <0034.g1:M>` of the required locus the known segment :g:`CD <0034.g1:/ C D />` subtends a :g:`right angle <0034.g1:< C M D )>`; hence :g:`M <0034.g1:M>` lies on the :g:`circle <0034.g1:( C D )>` having :g:`CD <0034.g1:/ C D />` for diameter (§ 11, locus 7).

.. picture:: 0034.g1.svg
   :alt: Fig. 11 — Apollonian circle on diameter CD dividing AB internally and externally in ratio p : q
   :caption: FIG. 11

CONVERSELY. Let us take any point :g:`M <0034.g1:M>` on this :g:`circle <0034.g1:( C D )>` and show that this point belongs to the required locus. Through the point :g:`B <0034.g1:B>` draw the parallels :g:`BE <0034.g1:/ B E />`, :g:`BF <0034.g1:/ B F />` to the lines :g:`MC <0034.g1:/ M C />`, :g:`MD <0034.g1:/ M D />` meeting :g:`AM <0034.g1:[ A M ]>` in :g:`E <0034.g1:E>`, :g:`F <0034.g1:F>`, respectively. We thus have:

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

Thus :g:`M <0034.g1:M>` is the :eq:`midpoint <0034.g1:/ M E / = 0034.g1:/ M F />` of the segment :g:`EF <0034.g1:/ E F />`. But :g:`EBF <0034.g1:< E B F )>` is a right angle, for its sides are parallel to the sides of the right angle :g:`CMD <0034.g1:< C M D )>`, and in the right triangle :g:`EBF <0034.g1:< E B F >>` the line :g:`MB <0034.g1:/ M B />` is :eq:`equal <0034.g1:/ M B / = 0034.g1:/ M E / = 0034.g1:/ M F />` to half the hypotenuse :g:`EF <0034.g1:/ E F />`; hence, replacing in the first proportion of (1) the segment :g:`ME <0034.g1:/ M E />` by the :eq:`equal <0034.g1:/ M E / = 0034.g1:/ M B />` segment :g:`MB <0034.g1:/ M B />`, we obtain:

.. math::

   AM : MB = AC : CB = p : q,

which shows that :g:`M <0034.g1:M>` belongs to the locus.

Where, in this converse proof, has the fact been used that :g:`M <0034.g1:M>` is a point of the :g:`circle <0034.g1:( C D )>`?

*Note.* The point :g:`C <0034.g1:C>` divides the segment :g:`AB <0034.g1:/ A B />` internally so that :math:`AC : CB = p : q`. But we may also construct the point :math:`C'` such that :math:`BC' : C'A = p : q`. Similarly for the external point of division. Thus the locus actually consists of two :term:`Apollonian circles <apollonian-circle>`, unless the order in which the two given points are to be taken is specified in the statement of the locus. In actual applications the nature of the problem often indicates the order in which the points are to be considered.

----

See :ref:`Commentary on Locus 11 <ch01-locus-11-commentary>`.

.. toctree::
   :hidden:

   commentary
