# -*- coding: utf-8 -*-

from ddhi_aggregator.aggregators.aggregators import Aggregator
from ddhi_encoder.interview import Interview

from ddhi_aggregator.aggregate import aggregate_tei
import os

__author__ = "Cliff Wulfman"
__copyright__ = "Cliff Wulfman"
__license__ = "mit"


def test_aggregate():
    in_dir = os.path.join(os.path.dirname(__file__), "interviews")
    aggregator = Aggregator()
    for f in os.listdir(in_dir):
        if f.endswith(".tei.xml"):
            interview = Interview()
            interview.read(os.path.join(in_dir, f))
            aggregator.include(interview)

    assert len(aggregator.interviews) == 3
