# -*- coding: utf-8 -*-
from lxml import etree
from ddhi_aggregator.entities.entities import Entity, Place, Person, Org, Event, Date


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


def test_date_same_as():
    element1 = etree.ElementTree(
        etree.XML('''\
        <date xmlns="http://www.tei-c.org/ns/1.0" when="01-01-2000">
        </date>
        '''))

    element2 = etree.ElementTree(
        etree.XML('''\
        <date xmlns="http://www.tei-c.org/ns/1.0"
        when="01-01-2000">
        </date>
        '''))

    element3 = etree.ElementTree(
        etree.XML('''\
        <date xmlns="http://www.tei-c.org/ns/1.0"
        xml:id="d3" when="01-01-2001">
        </date>
        '''))

    element4 = etree.ElementTree(
        etree.XML('''\
        <date xmlns="http://www.tei-c.org/ns/1.0">01-01-2001</date>
        '''))

    element5 = etree.ElementTree(
        etree.XML('''\
        <date xmlns="http://www.tei-c.org/ns/1.0"
         when-iso= "01-01-2001"></date>
        '''))

    date1 = Date(element1)
    date2 = Date(element2)
    date3 = Date(element3)
    date4 = Date(element4)
    date5 = Date(element5)

    assert date1.same_as(date2) is True
    assert date1.same_as(date3) is False
    assert date4.same_as(date3) is True
    assert date5.same_as(date3) is True
