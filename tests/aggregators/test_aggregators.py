# -*- coding: utf-8 -*-
# test_aggregators.py

from ddhi_aggregator.aggregators.aggregators import Aggregator
from ddhi_aggregator.entities.entities import Place
from ddhi_encoder.interview import Interview
import os


def test_include():
    subject = Aggregator()
    interview = Interview()
    interview.read(os.path.join(os.path.dirname(__file__), "test1.tei.xml"))
    subject.include(interview)
    assert(len(subject.interviews)) == 1
    assert(len(subject.places)) == 2

    subject.include(interview)
    assert(len(subject.interviews)) == 2
    assert(len(subject.places)) == 4
    assert subject.places[0].coordinates == "43.702222 -72.206111"
