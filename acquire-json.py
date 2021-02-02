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
    level=logging.DEBUG
)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_html = "daily-json"

file_output = '{0}-nm-vaccine-counties.json'.format(timestamp)

file_saved = os.path.join(dir_current, dir_html, file_output)

target_url = "https://cvvaccine.nmhealth.org/api/GetCounties"

response = requests.get(target_url)

data = json.loads(response.text)

with open(file_saved, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

logger.debug('File saved to {0}'.format(file_saved))
