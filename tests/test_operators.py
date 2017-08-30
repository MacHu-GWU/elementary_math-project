#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
elementary_path unittest.
"""

import pytest
from pytest import raises, approx
from elementary_math import operators


def test_operator():
    assert operators.add_one(10) == 11
    assert operators.minus_one(10) == 9
    assert operators.times_by_one(10) == 10
    assert operators.divide_by_two(10) == approx(5)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
