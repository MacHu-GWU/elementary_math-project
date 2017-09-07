.. image:: https://travis-ci.org/MacHu-GWU/elementary_math-project.svg?branch=master
    :target: https://travis-ci.org/MacHu-GWU/elementary_math-project?branch=master

.. image:: https://codecov.io/gh/MacHu-GWU/elementary_math-project/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/MacHu-GWU/elementary_math-project

.. image:: https://img.shields.io/pypi/v/elementary_math.svg
    :target: https://pypi.python.org/pypi/elementary_math

.. image:: https://img.shields.io/pypi/l/elementary_math.svg
    :target: https://pypi.python.org/pypi/elementary_math

.. image:: https://img.shields.io/pypi/pyversions/elementary_math.svg
    :target: https://pypi.python.org/pypi/elementary_math

.. image:: https://img.shields.io/badge/Star_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/elementary_math-project

.. contents::


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
- integration with https://codecov.io/
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
2. Navigate to ``elementary_math-project/start-a-project``, edit ``init_project.py`` and run it.
3. A ``<repo-name>`` directory will be created, you can use this as your github repo directory.
4. Take a look at ``Makefile``, all magic happens here!


AWS Command Line (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use `AWS S3 <http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html>`_ to host your doc site is a good idea!

We need `awscli <https://aws.amazon.com/cli/>`_ to automate the deployment.

1. Install `awscli <https://aws.amazon.com/cli/>`_, just ``pip install awscli``.
2. `Configure your API token <http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html>`_, just ``aws configure`` and follow the instruction.


Config PyPI (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you want to publish your package to `PyPI <https://pypi.python.org/pypi>`_ or `new PyPI <https://pypi.org/>`_, you need a pypi account and `Configure your credential <https://docs.python.org/2/distutils/packageindex.html#pypirc>`_.

1. Create a ``${HOME}/.pypirc`` file.
2. put these contents::

    [distutils]
    index-servers =
        pypi

    [pypi]
    username:<username>
    password:<password>


CI (Continues Integration) (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. `Test with travis-ci <https://docs.travis-ci.com/user/languages/python/>`_, basically you just need to:
    - sign in using GitHub account.
    - toggle on your repo.
2. `Code Coverage Test with codecov <https://github.com/codecov/example-python>`_.


For Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Because Windows doesn't have ``shell script`` and ``make`` command, so we have to install some third-party software to make it works.

**Install Git Bash as shell emulator**

1. `Download and install git <https://git-scm.com/downloads>`_.
2. Now you can use ``C:\Program Files\Git\git-bash.exe`` like the terminal in MacOS/Linux.

**Install MinGW**

1. `Download and install <http://www.mingw.org/>`_, use the installer to install ``MinGW Base``.
2. Find ``C:\MinGW\bin\mingw32-make.exe``, copy and paste and rename as ``C:\MinGW\bin\make.exe``.
3. Add ``C:\MinGW\bin`` to $PATH (environment variable).

Now you can use ``make <target>`` in ``git-bash.exe`` now.


For MacOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You have to make sure:

- `HomeBrew <https://brew.sh/>`_ is installed.

There's two way of using virtualenv in MacOS:

1. Use generic `virtualenv <https://virtualenv.pypa.io/en/stable/>`_.
2. Use `pyenv <https://github.com/pyenv/pyenv>`_ + `pyenv-virtualenv <https://github.com/pyenv/pyenv-virtualenv>`_.

I prefer ``pyenv`` + ``pyenv-virtualenv``, because it allows you:

1. use tox to test against multiple python version locally before using cloud CI (continues integration).
2. will not mess up your global python environment.
3. the ``Makefile`` will do the ``pyenv`` + ``pyenv-virtualenv`` setup for you, just make sure that you have  `HomeBrew <https://brew.sh/>`_ installed.


.. _install:

Install
-------

``elementary_math`` is released on PyPI, so all you need is:

.. code-block:: console

   $ pip install elementary_math

To upgrade to latest version:

.. code-block:: console

   $ pip install --upgrade elementary_math