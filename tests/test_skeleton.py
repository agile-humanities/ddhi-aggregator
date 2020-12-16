# -*- coding: utf-8 -*-

import pytest
from ddhi_aggregator.skeleton import fib

__author__ = "Cliff Wulfman"
__copyright__ = "Cliff Wulfman"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
