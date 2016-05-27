#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script can generate automate scripts for open source python project.
"""

from os.path import join, basename

package_name = "elementary_math"
python_version = "python"
github_username = "MacHu-GWU"


def write(s, path, encoding="utf-8"):
    """Write string to text file.
    """
    with open(path, "wb") as f:
        f.write(s.encode(encoding))

    
def read(path, encoding="utf-8"):
    """Read string from text file.
    """
    with open(path, "rb") as f:
        return f.read().decode(encoding)
    
file_list = [
    "build_dist.bat",
    "build_doc.bat",
    "install-win.bat",
    "install-linux.sh",
    "install-macos.sh",
    "pypi_register.bat",
    "pypi_upload.bat",
    "view_doc.bat",
    "MANIFEST.in",
    "create_doctree.py",
    "setup.py",
    "README.rst",
    "release_history.rst",
    "LICENSE.txt",
    "requirements.txt",
    ".travis.yml",
]
file_list = [join("template", path) for path in file_list]

for path in file_list:
    text = read(path).\
        replace("{{ package_name }}", package_name).\
        replace("{{ python_version }}", python_version).\
        replace("{{ github_username }}", github_username)
    path = basename(path)
    write(text, path)