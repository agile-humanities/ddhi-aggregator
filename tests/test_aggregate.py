# -*- coding: utf-8 -*-

from ddhi_aggregator.aggregate import aggregate_tei

__author__ = "Cliff Wulfman"
__copyright__ = "Cliff Wulfman"
__license__ = "mit"


def test_aggregate():
    aggregate_tei('/tmp/inputdir', '/tmp/outputdir')
    assert 1 == 1
