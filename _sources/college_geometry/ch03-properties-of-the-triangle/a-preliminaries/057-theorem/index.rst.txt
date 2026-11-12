:layout: book
:type: item
:order: 4
:canonical_id: Ch.III.57
:title: § 57. Theorem
:folio: 0073
:page: 54
:folios: 0073
:pages: 54

.. _ch03-art-057:

§ 57. Theorem
=============

.. folio:: 0073
   :page: 54

.. enunciation::

   *If the points* :g:`C <0072.g1:C>`\ *,* :g:`D <0072.g1:D>` *divide the segment* :g:`AB <0072.g1:/ A B />` *internally and externally in the ratio* :math:`p : q`\ *, the points* :g:`B <0072.g1:B>`\ *,* :g:`A <0072.g1:A>` *divide the segment* :g:`DC <0072.g1:/ C D />` *internally and externally in the ratio* :math:`(p + q) : (p - q)`\ *.*

.. picture:: 0072.g1.svg
   :alt: Fig. 39 — Internal and external division of segment AB in ratio p : q via parallel lines AF and GBH
   :caption: FIG. 39

We have (Fig. 39):

.. math::

   AC : CB = p : q, \quad AD : DB = p : q;

hence:

.. math::

   \begin{aligned}
   (1) \quad & (AC + CB) : CB = (p + q) : q, & (AD - DB) : DB &= (p - q) : q, \\
   (2) \quad & AC : (AC + CB) = p : (p + q), & AD : (AD - DB) &= p : (p - q).
   \end{aligned}

.. assertion::

   Substituting :g:`AB <0072.g1:/ A B />` for :math:`AC + CB` and for :math:`AD - DB` in (1) and (2), and combining the two proportions in each of these two lines we obtain:

   .. math::

      \begin{aligned}
      DB : BC &= (p + q) : (p - q), \\
      DA : AC &= (p + q) : (p - q).
      \end{aligned}

----

See :ref:`Commentary on § 57. Theorem <ch03-art-057-commentary>`.

.. toctree::
   :hidden:

   commentary
