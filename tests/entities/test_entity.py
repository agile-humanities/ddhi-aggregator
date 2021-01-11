# -*- coding: utf-8 -*-
from lxml import etree
from ddhi_aggregator.entities.entities import Entity, Place, Person, Org, Event


def test_simple():
    entity = etree.ElementTree(
        etree.XML('''\
        <person xmlns="http://www.tei-c.org/ns/1.0" xml:id="foo">
        <persName>Cliff</persName>
        <idno type="WD">Q12345</idno>
        <idno type="DDHI">7890</idno>
        </person>
        '''))

    subject = Entity(entity)
    assert subject.idno['DDHI'] == '7890'
    assert subject.idno['WD'] == 'Q12345'
    assert subject.id == "foo"


def test_place():
    entity = etree.ElementTree(
        etree.XML('''\
       <place xml:id="place1" xmlns="http://www.tei-c.org/ns/1.0">
            <placeName>Hanover, New Hampshire</placeName>
            <location>
               <geo>43.702222 -72.206111</geo>
            </location>
            <desc>The project may wish to provide descriptions of
            entities, if none are available elsewhere; but you will
            gain great extensibility if you can link these entities to
            global authority databases, like WikiData. The idno
            element (with type WD, for WikiData) provides that link.</desc>
            <idno type="WD">Q131908</idno>
         </place>
        '''))
    subject = Place(entity)
    assert subject.idno['WD'] == "Q131908"
    assert subject.coordinates == "43.702222 -72.206111"
    assert subject.description.split()[0:2] == ["The", "project"]


def test_person():
    entity = etree.ElementTree(
        etree.XML('''\
        <person xml:id="dvp_013_person1" xmlns="http://www.tei-c.org/ns/1.0">
            <persName>Emily Burack</persName>
         </person>
        '''))
    subject = Person(entity)
    assert(subject.name) == 'Emily Burack'


def test_org():
    entity = etree.ElementTree(
        etree.XML('''\
        <org xml:id="an_id" xmlns="http://www.tei-c.org/ns/1.0">
        <orgName>Princeton University</orgName>
        <idno type="WD">Q11111</idno>
         </org>'''))
    subject = Org(entity)
    assert(subject.name) == 'Princeton University'
    assert(subject.idno['WD']) == 'Q11111'


def test_event():
    entity = etree.ElementTree(
        etree.XML('''\
        <event xml:id="an_id" xmlns="http://www.tei-c.org/ns/1.0">
        <desc>1964 World's Fair</desc>
        <idno type="WD">Q12345</idno>
        </event>'''))
    subject = Event(entity)
    assert(subject.description) == "1964 World's Fair"
    assert(subject.idno['WD']) == 'Q12345'
    
