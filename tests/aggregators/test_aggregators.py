# -*- coding: utf-8 -*-
# test_aggregators.py

from ddhi_aggregator.aggregators.aggregators import AggregatorFactory
from ddhi_encoder.interview import Interview
from lxml import etree
import os


factory = AggregatorFactory()
input_dir = os.path.dirname(__file__)
subject = factory.aggregator_for("DDHI", input_dir, '/tmp')
interview = Interview()
interview.read(os.path.join(os.path.dirname(__file__), "test1.tei.xml"))
subject.include(interview)
interview2 = Interview()
interview2.read(os.path.join(os.path.dirname(__file__), "test2.tei.xml"))


def test_include():

    assert(len(subject.interviews)) == 1
    assert(len(subject.places)) == 2
    assert subject.places[0].coordinates == "43.702222 -72.206111"

    subject.include(interview2)
    assert(len(subject.interviews)) == 2
    # interview 2 has a duplicate place; aggregate should clear dupes
    assert(len(subject.places)) == 3


def test_places():
    place = subject.places[0]
    output = subject.formatted_place(place)
    assert(etree.tostring(output)) == b'<place><name>Hanover, New Hampshire</name><id type="WD">Q131908</id><location>43.702222 -72.206111</location></place>'


def test_persons():
    person = subject.persons[0]
    output = subject.formatted_person(person)
    assert(etree.tostring(output)) == b'<person><name>Emily Burack</name><id type="DDHI">dvp_013_person1</id></person>'


def test_orgs():
    org = subject.orgs[0]
    output = subject.formatted_org(org)
    assert(etree.tostring(output)) == b'<org><name>Collegiate School</name><id type="WD">Q5146978</id></org>'


def test_events():
    event = subject.events[0]
    output = subject.formatted_event(event)
    assert(etree.tostring(output)) == b'<event><name>1964 New York World\'s Fair</name><id type="WD">Q1189910</id></event>'


def test_dates():
    date = subject.dates[0]
    output = subject.formatted_date(date)
    assert(etree.tostring(output)) == b'<date>2016-02-10</date>'
