#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
elementary_path unittest.
"""

from elementary_math import operator

def test_all():
    assert operator.add_other(1, 2) == 3
    assert operator.minus_other(3, 2) == 1
    assert operator.times(2, 3) == 6
    assert abs(operator.divide_by(6, 3) - 2.0) <= 0.0001

if __name__ == "__main__":
    import py
    py.test.cmdline.main("--tb=native") # use native python trace back