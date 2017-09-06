#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script can generate automate scripts for open source python project.

Scroll to ``if __name__ == "__main__":`` for more info.
"""

from __future__ import print_function
import sys
import datetime
from os import walk, mkdir
from os.path import join, abspath, dirname, basename


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


def initiate_project(
        package_name,
        repo_name,
        python_version,
        github_username,
        author_name,
        author_email,
        maintainer_name,
        maintainer_email,
        year,
        s3_bucket,
    ):
    """
    Generate project start files.
    """
    print("Initate '%s-project' from template ..." % package_name)

    template_dir = join(dirname(abspath(__file__)), "template")
    output_dir = join(dirname(abspath(__file__)), "%s-project" % package_name)
    for src_dir, dir_list, file_list in walk(template_dir):
        # destination directory
        dst_dir = src_dir.replace(template_dir, output_dir, 1)
        if basename(dst_dir) == "__package__":
            dst_dir = join(dirname(dst_dir), package_name)

        # make destination directory
        try:
            print("    Create '%s' ..." % dst_dir)
            mkdir(dst_dir)
        except:
            pass

        # files
        for filename in file_list:
            src = join(src_dir, filename)
            dst = join(dst_dir, filename)

            content = read(src).\
                replace("{{ package_name }}", package_name).\
                replace("{{ repo_name }}", repo_name).\
                replace("{{ python_version }}", python_version).\
                replace("{{ github_username }}", github_username).\
                replace("{{ author_name }}", author_name).\
                replace("{{ author_email }}", author_email).\
                replace("{{ maintainer_name }}", maintainer_name).\
                replace("{{ maintainer_email }}", maintainer_email).\
                replace("{{ year }}", year).\
                replace("{{ s3_bucket }}", s3_bucket)

            print("    Create '%s' ..." % dst)
            write(content, dst)
    print("    Complete!")


if __name__ == "__main__":
    # --- EDIT THESE VARIABLE based on your own situation ---
    package_name = "elementary_math"  # IMPORTANT
    repo_name = "{package_name}-project".format(package_name=package_name)
    python_version = "python%s%s" % (
    sys.version_info.major, sys.version_info.minor)
    github_username = "MacHu-GWU"  # IMPORTANT
    author_name = "Sanhe Hu"  # IMPORTANT
    author_email = "husanhe@gmail.com"  # IMPORTANT
    maintainer_name = author_name
    maintainer_email = author_email
    year = str(datetime.datetime.utcnow().year)
    s3_bucket = "www.wbh-doc.com"  # IMPORTANT

    initiate_project(
        package_name,
        repo_name,
        python_version,
        github_username,
        author_name,
        author_email,
        maintainer_name,
        maintainer_email,
        year,
        s3_bucket,
    )