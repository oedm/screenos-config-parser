#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from ipaddress import ip_network, ip_address
from json import JSONDecoder
from collections import OrderedDict
from pprint import pprint

# Retain policy order when reading in data
custom_decoder = JSONDecoder(object_pairs_hook=OrderedDict)
policy = custom_decoder.decode(open('output/MGT-CLOUD_run_conf.json').read())

pprint(policy)

global_objects = []
global_object_groups = []

for rule in policy:
  for 