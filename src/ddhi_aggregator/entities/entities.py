# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from lxml import etree


class Entity(object):
    TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
    TEI = "{%s}" % TEI_NAMESPACE
    XML_NAMESPACE = "http://www.w3.org/XML/1998/namespace"
    XML = "{%s}" % XML_NAMESPACE
    NSMAP = {None: TEI_NAMESPACE, "xml": XML_NAMESPACE}

    def __init__(self, element):
        self.namespaces = {"tei": "http://www.tei-c.org/ns/1.0",
                           "xml": "http://www.w3.org/XML/1998/namespace"}
        self._xml = element
        self.id = element.xpath('./@xml:id',
                                namespaces=self.namespaces)[0]
        self.idno = {}
        idnos = element.xpath('./tei:idno',
                              namespaces=self.namespaces)
        for idno in idnos:
            type = idno.get("type")
            if type:
                self.idno[type] = idno.text

    def same_as(self, entity):
        if (type(self) == type(entity) and
                [k for k in entity.idno.keys() if k in self.idno.keys() and
                 entity.idno[k] == self.idno[k]]):
            return True
        else:
            return False


class Place(Entity):
    def __init__(self, element):
        super().__init__(element)

        name = element.xpath('./tei:placeName', namespaces=self.namespaces)
        if name:
            self.name = name[0].text
        self.coordinates = ""
        geo = element.xpath('./tei:location/tei:geo',
                            namespaces=self.namespaces)
        if geo:
            self.coordinates = geo[0].text

        description = element.xpath('./tei:desc',
                                    namespaces=self.namespaces)
        if description:
            self.description = description[0].text


class Person(Entity):
    def __init__(self, element):
        super().__init__(element)
        name = element.xpath('./tei:persName', namespaces=self.namespaces)
        if name:
            self.name = name[0].text


class Event(Entity):
    def __init__(self, element):
        super().__init__(element)
        description = element.xpath('./tei:desc',
                                    namespaces=self.namespaces)
        if description:
            self.description = description[0].text


class Org(Entity):
    def __init__(self, element):
        super().__init__(element)
        name = element.xpath('./tei:orgName', namespaces=self.namespaces)
        if name:
            self.name = name[0].text


'''
Dates are different from the other entities: they do not have ids.  So
they are not a subclass of the Entity class, and must duplicate some of
Entity's init code.
'''


class Date():
    TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
    TEI = "{%s}" % TEI_NAMESPACE
    XML_NAMESPACE = "http://www.w3.org/XML/1998/namespace"
    XML = "{%s}" % XML_NAMESPACE
    NSMAP = {None: TEI_NAMESPACE, "xml": XML_NAMESPACE}
   
    def __init__(self, element):
        self.namespaces = {"tei": "http://www.tei-c.org/ns/1.0",
                           "xml": "http://www.w3.org/XML/1998/namespace"}
        self._xml = element
        when = element.xpath('./@when', namespaces=self.namespaces)
        when_iso = element.xpath('./@when-iso', namespaces=self.namespaces)
        if when:
            self.when = when[0]
        elif when_iso:
            self.when = when_iso[0]
        else:
            self.when = element.xpath('./text()',
                                      namespaces=self.namespaces)[0]

    def same_as(self, entity):
        if (type(self) == type(entity) and entity.when == self.when):
            return True
        else:
            return False
