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

"""
This script is the first step in the process
to pull down a copy of the county-level json
used to power New Mexico's vaccine dashboard
"""

counties = [
"Bernalillo",
"Catron",
"Chaves",
"Cibola",
"Colfax",
"Curry",
"De Baca",
"Doña Ana",
"Eddy",
"Grant",
"Guadalupe",
"Harding",
"Hidalgo",
"Lea",
"Lincoln",
"Los Alamos",
"Luna",
"McKinley",
"Mora",
"Otero",
"Quay",
"Rio Arriba",
"Roosevelt",
"Sandoval",
"San Juan",
"San Miguel",
"Santa Fe",
"Sierra",
"Socorro",
"Taos",
"Torrance",
"Union",
"Valencia"
]

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
dir_current = os.path.dirname(os.path.realpath(__file__))
dir_html = "daily-phases-json"
file_output = f'statewide-{timestamp}-nm-vaccine-phases.json'
file_saved = os.path.join(dir_current, dir_html, file_output)
target_url = f"https://cvvaccine.nmhealth.org/api/GetPhaseDashboardData"
response = requests.get(target_url)
data = json.loads(response.text)
with open(file_saved, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
logger.debug('File saved to {0}'.format(file_saved))
for county in counties:
    file_output = f'{county}-{timestamp}-nm-vaccine-phases-counties.json'
    file_saved = os.path.join(dir_current, dir_html, file_output)
    target_url = f"https://cvvaccine.nmhealth.org/api/GetPhaseDashboardData?county={county}"
    response = requests.get(target_url)
    data = json.loads(response.text)
    with open(file_saved, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logger.debug('File saved to {0}'.format(file_saved))