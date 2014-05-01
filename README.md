REST Crawler Overview
======================

This project is intended to provide a base resource that allows someone to crawl an ArcGIS Server REST endpoint using Python, and retrieve all of the service URLs that are either publicly available, or available via a token. The functions.py script contains functions that perform an optional token generation and the actual crawling of the REST endpoint. getServices.py takes the results from functions.py and writes them to a text file (services.txt) that can be parsed by downstream scripts or processes to send additional requests, check status, or administrate.

This repository uses the *urllib* libraries so as to be compatible with out-of-the-box functionality. Upon request, this sample can be converted to use the much more pythonic *requests* module instead.
