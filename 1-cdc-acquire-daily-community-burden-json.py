#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import datetime
import os
import logging

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG,
)

"""
This script is the first step in the process
to pull down a copy of the daily county-level json
data published by the CDC to "help communities and
individuals make decisions based on their local context
and their unique needs."

https://www.cdc.gov/coronavirus/2019-ncov/science/community-levels.html
"""

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_json = "daily-json"

file_output = "{0}-cdc-daily-community-burden-by-county.json".format(timestamp)

file_saved = os.path.join(dir_current, dir_json, file_output)

target_url = "https://www.cdc.gov/coronavirus/2019-ncov/modules/science/us-community-levels-by-county.json"

response = requests.get(target_url)

data = json.loads(response.text)

with open(file_saved, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

logger.debug("File saved to {0}".format(file_saved))
