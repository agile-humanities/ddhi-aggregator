# -*- coding: utf-8 -*-
# test_aggregators.py

from ddhi_aggregator.aggregators.aggregators import Aggregator, AggregatorFactory
from ddhi_aggregator.entities.entities import Place
from ddhi_encoder.interview import Interview
from lxml import etree
import os


def test_include():
    factory = AggregatorFactory()
    input_dir = os.path.dirname(__file__)
    subject = factory.aggregator_for("DDHI", input_dir)
    interview = Interview()
    interview.read(os.path.join(os.path.dirname(__file__), "test1.tei.xml"))
    subject.include(interview)

    assert(len(subject.interviews)) == 1
    assert(len(subject.places)) == 2

    subject.include(interview)
    assert(len(subject.interviews)) == 2
    assert(len(subject.places)) == 4
    assert subject.places[0].coordinates == "43.702222 -72.206111"

    output = subject.formatted_interview(subject.interviews[0])
    assert(etree.tostring(output)) == b'<interview><identifier>dvp_test1</identifier><title>test transcript</title><primary_audio_URI/><interview_body>foo</interview_body><participants><participant><name/><role/></participant><participant><name/><role/></participant></participants></interview>'
