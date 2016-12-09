#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
elementary_path unittest.
"""

import pytest
from pytest import approx
from elementary_math import operators

def test_operator():
    assert operator.add_other(1, 2) == 3
    assert operator.minus_other(3, 2) == 1
    assert operator.times(2, 3) == 6
    assert operator.divide_by(6, 3) == approx(2.0)

if __name__ == "__main__":
    import os
    pytest.main([os.path.basename(__file__), "--tb=native", "-s", ])