.. image:: https://travis-ci.org/{{ github_username }}/{{ repo_name }}.svg?branch=master
    :target: https://travis-ci.org/{{ github_username }}/{{ repo_name }}?branch=master

.. image:: https://codecov.io/gh/{{ github_username }}/{{ repo_name }}/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/{{ github_username }}/{{ repo_name }}

.. image:: https://img.shields.io/pypi/v/{{ package_name }}.svg
    :target: https://pypi.python.org/pypi/{{ package_name }}

.. image:: https://img.shields.io/pypi/l/{{ package_name }}.svg
    :target: https://pypi.python.org/pypi/{{ package_name }}

.. image:: https://img.shields.io/pypi/pyversions/{{ package_name }}.svg
    :target: https://pypi.python.org/pypi/{{ package_name }}

.. image:: https://img.shields.io/badge/Star_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/{{ github_username }}/{{ repo_name }}


Welcome to ``{{ package_name }}`` Documentation
==============================================================================

Documentation for ``{{ package_name }}``.


Quick Links
-----------
- `GitHub Homepage <https://github.com/{{ github_username }}/{{ repo_name }}>`_
- `Online Documentation <http://{{ s3_bucket }}.s3.amazonaws.com/{{ package_name }}/index.html>`_
- `PyPI download <https://pypi.python.org/pypi/{{ package_name }}>`_
- `Install <install_>`_
- `Issue submit and feature request <https://github.com/{{ github_username }}/{{ repo_name }}/issues>`_
- `API reference and source code <http://{{ s3_bucket }}.s3.amazonaws.com/{{ package_name }}/py-modindex.html>`_


.. _install:

Install
-------

``{{ package_name }}`` is released on PyPI, so all you need is:

.. code-block:: console

	$ pip install {{ package_name }}

To upgrade to latest version:

.. code-block:: console

	$ pip install --upgrade {{ package_name }}