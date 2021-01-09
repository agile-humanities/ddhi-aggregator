# -*- coding: utf-8 -*-

from ddhi_aggregator.aggregators.aggregators import AggregatorFactory

import os

__author__ = "Cliff Wulfman"
__copyright__ = "Cliff Wulfman"
__license__ = "mit"


def test_aggregate():
    in_dir = os.path.join(os.path.dirname(__file__), "interviews")
    factory = AggregatorFactory()
    aggregator = factory.aggregator_for("DDHI", in_dir, '/tmp')
    aggregator.aggregate()
    assert len(aggregator.interviews) == 3
