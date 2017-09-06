.. image:: https://travis-ci.org/MacHu-GWU/elementary_math-project.svg?branch=master
    :target: https://travis-ci.org/MacHu-GWU/elementary_math-project?branch=master

.. image:: https://coveralls.io/repos/github/MacHu-GWU/elementary_math-project/badge.svg?branch=master
    :target: https://coveralls.io/github/MacHu-GWU/elementary_math-project?branch=master

.. image:: https://img.shields.io/pypi/v/elementary_math.svg
    :target: https://pypi.python.org/pypi/elementary_math

.. image:: https://img.shields.io/pypi/l/elementary_math.svg
    :target: https://pypi.python.org/pypi/elementary_math

.. image:: https://img.shields.io/pypi/pyversions/elementary_math.svg
    :target: https://pypi.python.org/pypi/elementary_math

.. image:: https://img.shields.io/badge/Star_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/elementary_math-project


Welcome to ``elementary_math`` Documentation
============================================
``elementary_math`` is a project to demonstrate: how to setup environment and toolsets for a python library project on github, includes these **powerful components**:

- virtual environment setup (one command install everything)
- setup.py file (one click **install**/**uninstall**)
- auto Google stylize your code
- fancy sphinx document (one click **build**/**view**/**deploy**)
- unittest suits with pytest
- code coverage test with coverall
- multi python version test with tox
- integration with https://travis-ci.org/
- integration with https://coveralls.io/
- auto deploy to `AWS S3 <http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html>`_
- publish to `PyPI <https://pypi.python.org/pypi/your-package-name>`_


Quick Links
-----------
- `GitHub Homepage <https://github.com/MacHu-GWU/elementary_math-project>`_
- `Online Documentation <http://www.wbh-doc.com.s3.amazonaws.com/elementary_math/index.html>`_
- `PyPI download <https://pypi.python.org/pypi/elementary_math>`_
- `Install <install_>`_
- `Issue submit and feature request <https://github.com/MacHu-GWU/elementary_math-project/issues>`_
- `API reference and source code <http://www.wbh-doc.com.s3.amazonaws.com/elementary_math/py-modindex.html>`_


Usage
-----
1. Clone the repo.
2. Navigate to ``elementary_math-project/start-a-project``, edit ``init_project.py`` and runt.
3. A ``<repo-name>`` directory will be created, you can use this as your github repo directory.

**For MacOS**:

You have to make sure:

- `HomeBrew <https://brew.sh/>`_ is installed.

take a look at ``Makefile``, all magic happens here!


.. _install:

Install
-------

``elementary_math`` is released on PyPI, so all you need is:

.. code-block:: console

   $ pip install elementary_math

To upgrade to latest version:

.. code-block:: console

   $ pip install --upgrade elementary_math