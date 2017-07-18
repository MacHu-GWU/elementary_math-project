.. image:: https://travis-ci.org/{{ github_username }}/{{ package_name }}-project.svg?branch=master

.. image:: https://img.shields.io/pypi/v/{{ package_name }}.svg

.. image:: https://img.shields.io/pypi/l/{{ package_name }}.svg

.. image:: https://img.shields.io/pypi/pyversions/{{ package_name }}.svg


Welcome to {{ package_name }} Documentation
===========================================
This is just a example project for demonstration purpose.


**Quick Links**
---------------
- `GitHub Homepage <https://github.com/{{ github_username }}/{{ package_name }}-project>`_
- `Online Documentation <http://{{ s3_bucket }}.s3.amazonaws.com/{{ package_name }}/index.html>`_
- `PyPI download <https://pypi.python.org/pypi/{{ package_name }}>`_
- `Install <install_>`_
- `Issue submit and feature request <https://github.com/{{ github_username }}/{{ package_name }}-project/issues>`_
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