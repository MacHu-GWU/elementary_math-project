#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docfly

# Uncomment this if you follow Sanhe's Sphinx Doc Style Guide
#--- Manually Made Doc ---
# doc = docfly.DocTree("source")
# doc.fly()

#--- Api Reference Doc ---
package_name = "{{ package_name }}"

doc = docfly.ApiReferenceDoc(
    package_name,
    dst="source",
    ignore=[
        "%s.packages" % package_name,
        "%s.zzz_manual_install.py" % package_name,
    ]
)
doc.fly()