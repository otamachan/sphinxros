sphinx.ros
==========

All packages and messages documentation using sphinxcontrib.ros

indigo: http://otamachan2.github.io/sphinxros/indigo
jade: http://otamachan2.github.io/sphinxros/jade

You can refer to them in your Sphinx documenation by adding following lines in your ``conf.py``.

.. code-block:: python

   extensions += ['sphinx.ext.intersphinx']
   intersphinx_mapping = {'ros':
       ('http://otamachan2.github.io/sphinxros/indigo/', None)}
