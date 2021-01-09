# -*- coding: utf-8 -*-
# aggregators.py
# from ddhi_encoder.entities.entities import Place
from ddhi_aggregator.entities.entities import Place
import xml.etree.ElementTree as ET
from lxml import etree
from importlib import resources
import logging


logger = logging.getLogger(__name__)


class Aggregator:
    def __init__(self, input_dir, xsl_object):
        self.input_dir = input_dir
        
        self.interviews = []
        self.places = []
        self.interview_stylesheet = etree.XSLT(xsl_object)

    def include(self, interview):
        self.interviews.append(interview)
        places = interview.places()
        [self.places.append(Place(place)) for place in places]

    def formatted_interview(self, interview):
        return self.interview_stylesheet(interview.tei_doc)

    # consider replacing the xslt with native ETree construction
    def formatted_interviews(self):
        interviews = ET.Element("interviews")
        for interview in self.interviews:
            interviews.append(self.formatted_interview(interview))
        return interviews


class AggregatorFactory:
    def xml_object(self, path_to_file):
        try:
            xml_obj = etree.parse(path_to_file)
        except etree.XMLSyntaxError as e:
            logger.error(e)
            raise
        return xml_obj

#            xslt = self.xml_object("/Users/cwulfman/repos/github/agile/ddhi-aggregator/xsl/ddhi-tei2repo.xsl")
    def aggregator_for(self, project, input_dir):
        if project == "DDHI":
            with resources.path("xsl", "ddhi-tei2repo.xsl") as xslt_path:
                xslt = self.xml_object(str(xslt_path))
            aggregator = Aggregator(input_dir, xslt)
            return aggregator
