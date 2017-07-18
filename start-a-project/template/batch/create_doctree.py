#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docfly
from pathlib_mate import Path

# Uncomment this if you follow Sanhe's Sphinx Doc Style Guide
#--- Manually Made Doc ---
doc = docfly.DocTree(
    Path(Path(__file__).absolute().parent.parent, "source").abspath
)
doc.fly(table_of_content_header="Table of Content (目录)")


#--- Api Reference Doc ---
package_name = "{{ package_name }}"
 
doc = docfly.ApiReferenceDoc(
    package_name,
    dst=Path(Path(__file__).absolute().parent.parent, "source").abspath,
    ignored_package=[
        "%s.pkg" % package_name,
        "%s.packages" % package_name,
        "%s.zzz_manual_install.py" % package_name,
    ]
)
doc.fly()