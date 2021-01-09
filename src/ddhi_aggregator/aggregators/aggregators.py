# -*- coding: utf-8 -*-
# aggregators.py
# from ddhi_encoder.entities.entities import Place
from ddhi_aggregator.entities.entities import Place
from ddhi_encoder.interview import Interview
import xml.etree.ElementTree as ET
from lxml import etree
from importlib import resources
import logging
import os

logger = logging.getLogger(__name__)


class Aggregator:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.interviews = []
        self.places = []

    def aggregate(self):
        for f in os.listdir(os.path.abspath(self.input_dir)):
            if f.endswith(".tei.xml"):
                interview = Interview()
                interview.read(os.path.join(self.input_dir, f))
                self.include(interview)

    def dump_interviews(self):
        print(etree.tostring(self.formatted_interviews(), pretty_print=True,
                             encoding='unicode'))

    def dump_interviews_old(self):
        for interview in self.interviews:
            formatted = self.formatted_interview(interview)
            print(etree.tostring(formatted, pretty_print=True,
                                 encoding='unicode'))

    def include(self, interview):
        self.interviews.append(interview)
        places = interview.places()
        [self.places.append(Place(place)) for place in places]

    def formatted_interview(self, interview):
        try:
            result = self.interview_stylesheet(interview.tei_doc)
        except etree.XMLSyntaxError as e:
            logger.error(e)
        if result:
            foo = ET.ElementTree(bytes(result))
            root = foo.getroot()
            return etree.fromstring(root)

    # consider replacing the xslt with native ETree construction
    def formatted_interviews(self):
        # interviews = ET.Element("interviews")
        interviews = etree.Element("interviews")
        for interview in self.interviews:
            interview = self.formatted_interview(interview)
            interviews.append(interview)
        return interviews


class AggregatorFactory:
    def aggregator_for(self, project, input_dir, output_dir):
        if project == "DDHI":
            with resources.path("xsl", "ddhi-tei2repo.xsl") as xslt_path:
                try:
                    xslt = etree.parse(str(xslt_path))
                except etree.XMLSyntaxError as e:
                    logger.error(e)
            aggregator = Aggregator(input_dir, output_dir)
            aggregator.interview_stylesheet = etree.XSLT(xslt)
            return aggregator
