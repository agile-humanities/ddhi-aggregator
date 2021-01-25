# -*- coding: utf-8 -*-
from lxml import etree
from ddhi_aggregator.entities.entities import Entity, Place, Person, Org, Event


def test_same_as():
    element1 = etree.ElementTree(
        etree.XML('''\
        <person xmlns="http://www.tei-c.org/ns/1.0" xml:id="p1">
        <persName>Cliff Wulfman</persName>
        <idno type="DDHI">an_id</idno>
        </person>
        '''))

    element2 = etree.ElementTree(
        etree.XML('''\
        <person xmlns="http://www.tei-c.org/ns/1.0" xml:id="p2">
        <persName>Clifford Wulfman</persName>
        <idno type="DDHI">an_id</idno>
        </person>
        '''))

    element3 = etree.ElementTree(
        etree.XML('''\
        <person xmlns="http://www.tei-c.org/ns/1.0" xml:id="p3">
        <persName>Clifford Wulfman</persName>
        <idno type="DDHI">a_different_id</idno>
        </person>
        '''))

    person1 = Entity(element1)
    person2 = Entity(element2)
    person3 = Entity(element3)

    assert person1.same_as(person2) is True
    assert person2.same_as(person3) is False
