#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docfly
from pathlib_mate import Path

# Uncomment this if you follow Sanhe's Sphinx Doc Style Guide
#--- Manually Made Doc ---
source_dir = Path(__file__).absolute().parent.append_parts("source").abspath
doc = docfly.DocTree(source_dir)
doc.fly(table_of_content_header="Table of Content")


#--- Api Reference Doc ---
package_name = "elementary_math"

doc = docfly.ApiReferenceDoc(
    package_name,
    dst=Path(__file__).absolute().parent.parent.append_parts("source").abspath,
    ignored_package=[
        "%s.pkg" % package_name,
        "%s.zzz_ezinstall.py" % package_name,
    ]
)
doc.fly()