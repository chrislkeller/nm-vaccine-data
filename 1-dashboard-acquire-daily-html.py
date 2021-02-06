#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
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

dir_html = "daily-html"

file_output = '{0}-nm-vaccine-dash.html'.format(timestamp)

file_saved = os.path.join(dir_current, dir_html, file_output)

target_url = "https://cvvaccine.nmhealth.org/public-dashboard.html"

response = requests.get(target_url)

raw_html = response.content

soup = BeautifulSoup(raw_html, 'lxml')

with open(file_saved, 'w', encoding='utf-8') as f:
    f.write(soup.prettify())

logger.debug('File saved to {0}'.format(file_saved))
