===============
ddhi-aggregator
===============


A command-line tool for aggregating various bits of data from
DDHI-encoded Interviews into a set of files that can be ingested by
the DDHI's Drupal application.


Description
===========

There is a single command, *ddhi_aggregate*, which takes two arguments: a directory of TEI-encoded interviews to be processed, and a directory for the output:

ddhi_aggregate -i interviews/ -o aggregated_data/


Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
