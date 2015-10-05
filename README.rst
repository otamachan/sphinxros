sphinx.ros
==========

About
-----

All packages and messages documentation using sphinxcontrib.ros

indigo:
  http://otamachan.github.io/sphinxros/indigo

  .. image:: https://travis-ci.org/otamachan/sphinxros.svg?branch=indigo
     :target: https://travis-ci.org/otamachan/sphinxros

jade:
  http://otamachan.github.io/sphinxros/jade

  .. image:: https://travis-ci.org/otamachan/sphinxros.svg?branch=jade
     :target: https://travis-ci.org/otamachan/sphinxros


sphinx.ext.intersphinx
-----------------------

You can refer to them in your Sphinx documenation by adding following lines in your ``conf.py``.

.. code-block:: python

   extensions += ['sphinx.ext.intersphinx']
   intersphinx_mapping = {'ros':
       ('http://otamachan.github.io/sphinxros/indigo/', None)}
