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
    assert operators.add_two(10) == 12
    assert operators.add_three(10) == 13
    assert operators.add_four(10) == 14

    assert operators.minus_one(10) == 9
    assert operators.minus_two(10) == 8
    assert operators.minus_three(10) == 7
    assert operators.minus_four(10) == 6

    assert operators.times_by_one(10) == 10
    assert operators.times_by_two(10) == 20
    assert operators.times_by_three(10) == 30
    assert operators.times_by_four(10) == 40

    assert operators.divide_by_one(10) == approx(10)
    assert operators.divide_by_two(10) == approx(5)
    assert operators.divide_by_three(10) == approx(10.0 / 3)
    assert operators.divide_by_four(10) == approx(2.5)


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
