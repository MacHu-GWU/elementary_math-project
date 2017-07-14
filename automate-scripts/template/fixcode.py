#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib_mate import Path

p = Path(
    Path(__file__).parent, 
    Path(__file__).parent.basename.replace("-project", ""),
)
p.autopep8()

p = Path(Path(__file__).parent, "tests")
p.autopep8()