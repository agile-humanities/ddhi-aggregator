# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = ddhi_aggregator.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging
import os
from ddhi_aggregator import __version__
from ddhi_aggregator.aggregators.aggregators import Aggregator, AggregatorFactory
from ddhi_encoder.interview import Interview


__author__ = "Cliff Wulfman"
__copyright__ = "Cliff Wulfman"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def aggregate_tei(in_path, out_path):
    _logger.info("aggregation starting")
    factory = AggregatorFactory()
    
    aggregator = factory.aggregator_for("DDHI", in_path)
    for f in os.listdir(in_path):
        if f.endswith("*.tei.xml"):
            interview = Interview()
            interview.read(f)
            aggregator.include(interview)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Aggregate info from TEI documents for Drupal ingest")

    parser.add_argument(
        "--version",
        action="version",
        version="ddhi-aggregator {ver}".format(ver=__version__))

    parser.add_argument('-i' '--source_dir',
                        dest='source_dir',
                        help='path to TEI files')

    parser.add_argument('-o', '--target_dir',
                        dest='target_dir',
                        help='where you want to store the aggregation files')

    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)

    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting aggregation...")
    aggregate_tei(args.source_dir, args.target_dir)
    _logger.info("Aggregation finished.")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
