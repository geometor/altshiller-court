:navigation: header
:order: 20
:nav_title: Usage

Using This Edition
==================

.. rubric:: Interactive Reader's Guide to Nathan Altshiller-Court's *College Geometry*

This digital critical edition of Nathan Altshiller-Court's *College Geometry* provides a modern, interactive reading environment engineered for geometric deduction, archival witness examination, and algorithmic exploration.

Interactive Features
--------------------

1. Synchronized Reading Tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each article, problem, and locus in *College Geometry* features paired reading tracks accessible via the top track toggle bar:

* **Text Track**: The complete depaginated treatise prose, mathematical statements, constructive steps (*Analysis*, *Construction*, *Proof*, *Discussion*), and inline interactive diagrams.
* **Commentary Track**: In-depth mathematical commentary, historical connections to Euclidean geometry and modern synthetic developments, algebraic representations, and pedagogical notes.

2. Primary-Source Folio Milestones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Marginal milestones (e.g., ``[p. 15]`` or ``[f. 0034]``) and header badges link each section directly to its high-resolution 300 DPI archival witness page scan. Readers can cross-check transcriptions against original printed pages from the 1952 edition.

3. Interactive Diagrams & Deductive Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
All figures are reconstructed as exact Euclidean vector graphics (``.euclid-graphic`` SVGs):

* Hovering over geometric element references or constructive assertions highlights the corresponding diagram elements.
* Visual element anchors (``:g:`` labels and equations) enable bi-directional cross-referencing between text explanations and geometric figures.

4. Full-Text Search with In-Page Highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The full-text search engine scans the complete treatise text, commentary, glossary, and apparatus. Selecting search results navigates directly to matching sections with terms dynamically highlighted via ``?highlight=`` parameters.

5. Categories, Tags, Document Types & Collection Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Every chapter, section, article, problem, and locus is indexed with structured metadata:

* **Taxonomy Facets**: Browse articles by category, geometric tag (e.g. *homothecy*, *nine-point circle*, *inversion*, *symmedians*), and document type (*article*, *problem*, *locus*, *exercise*).
* **Collection View Toggles**: Switch seamlessly between **Cards**, **Banners**, and **List** views on any collection landing page to inspect section hierarchies at varying levels of detail.

6. People, Bibliography & Glossary Tooltips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* **People**: Entity references like :person:`Nathan Altshiller-Court <altshiller-court>` or :person:`Apollonius <apollonius>` trigger rich biographical popovers detailing historical roles, dates, and occurrences across the edition.
* **Bibliography**: Scholarly citations (e.g. :cite:`casey:sequel:1892`) resolve to canonical bibliographic entries with linked source references.
* **Glossary**: Technical geometric terms like :term:`radical axis` or :term:`homothecy` provide instant definitions via hover cards.
* **Theme Switching**: Toggle between Light and Dark display modes in the top navigation bar with color-adapted figures and high-contrast typography.

Command-Line & Python Pipeline
------------------------------

``geometor.altshiller_court`` provides automated pipeline tools for transcription auditing, SVG diagram calibration, and codex compilation:

.. code-block:: bash

   # Verify all 334 archival scans, transcriptions, and SVG calibrations
   uv run altshiller-court-status

   # Compile the multi-level Book Codex into docsrc/college_geometry/
   python3 -m geometor.altshiller_court compile

   # Build the Sphinx HTML documentation site
   publish build
