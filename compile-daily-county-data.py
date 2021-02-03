#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import datetime
import os
from os import listdir
from os.path import isfile, join
import logging
import pandas as pd

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

dir_current = os.path.dirname(os.path.realpath(__file__))

dir_json = "daily-json"

dir_data = "daily-data"

file_path = os.path.join(dir_current, dir_json)

files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

output = []

for file in files:
    logger.debug(file)
    target = os.path.join(file_path, file)
    with open(target, encoding='utf-8') as f:
        raw_json = json.load(f)
        for item in raw_json['data']:
            item['acquired_datestamp'] = file[:17]
            output.append(item)

    output_json = [
        {"file": "latest-nm-vaccine-counties.json"},
        {"file": "{0}-nm-vaccine-counties.json".format(file[:17])},
    ]

    output_csv = [
        {"file": "latest-nm-vaccine-counties.csv"},
        {"file": "{0}-nm-vaccine-counties.csv".format(file[:17])},
    ]

    for f in output_json:
        file_saved = os.path.join(dir_current, dir_data, f['file'])
        with open(file_saved, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=4)
            logger.debug('File saved to {0}'.format(file_saved))

    for f in output_csv:
        file_saved = os.path.join(dir_current, dir_data, f['file'])
        csv_data = pd.DataFrame(output)
        csv_data.to_csv(file_saved, encoding='utf-8', index=False)
        logger.debug('File saved to {0}'.format(file_saved))
