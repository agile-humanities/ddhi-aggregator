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
    subject = factory.aggregator_for("DDHI", input_dir, '/tmp')
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
    assert(etree.tostring(output)) == b'<interview>\n  <identifier>dvp_test1</identifier>\n  <title>test transcript</title>\n  <primary_audio_URI/>\n  <interview_body>foo</interview_body>\n  <participants>\n    <participant>\n      <name/>\n      <role/>\n    </participant>\n    <participant>\n      <name/>\n      <role/>\n    </participant>\n  </participants>\n  <named_persons>\n    <name>Emily Burack</name>\n    <id type="DDHI"/>\n    <name>Beirne [pronounced BUR-nee] Lovely</name>\n    <id type="DDHI"/>\n  </named_persons>\n  <named_places>\n    <place>Hanover, New Hampshire</place>\n    <id type="DDHI">Q131908</id>\n    <place>Boston</place>\n    <id type="DDHI"/>\n  </named_places>\n  <named_events/>\n  <named_orgs/>\n</interview>'
