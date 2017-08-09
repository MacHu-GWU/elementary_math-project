This folder includes many batch files can minimize your work in:

- p01-install-win.bat: install the package
- p02-sphinx-quickstart.bat: execute sphinx-quickstart
- p03-build-doc.bat: build html document

.. note::

   if you have multiple sphinx installed on Py27, PY34. You need to edit
   ``Makefile`` and ``make.bat`` file, change ``python`` command to 
   ``python27/python34``.

- p04-view-doc.bat: open html document
- p05-fixcode.bat: stylize your code in pep8
- p06-build-dist.bat: build distribution file
- p07-pypi-upload.bat: upload to pypi