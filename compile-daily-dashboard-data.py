#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import csv
import json
import datetime
from itertools import zip_longest
from collections import OrderedDict
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

dir_html = "daily-html"

dir_data = "daily-data"

file_path = os.path.join(dir_current, dir_html)

files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

output = []

for file in files:

    compiled_data = []

    target = os.path.join(file_path, file)
    with open(target, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'lxml')

        last_updated = soup.find_all("i")[0].get_text().strip()
        last_updated = last_updated.replace("Last Updated: ", "")

        # get the topline numbers
        topline_keys = []
        keys = soup.find_all(
            "div", attrs={"class" : "graph-sub-num-title"}
        )
        for key in keys:
            topline_keys.append(key.get_text().strip())

        topline_values = []
        values = soup.find_all(
            "div", attrs={"class" : "big-number"}
        )
        for value in values:
            topline_values.append(value.get_text().strip())

        compiled_topline = dict(zip_longest(topline_keys, topline_values))
        compiled_topline['acquired_datestamp'] = file[:17]
        toplineDict = {
            "type": "topline",
            "date": last_updated,
            "data": compiled_topline
        }
        compiled_data.append(toplineDict)

        # get the manufacturer, age, gender, race and ethnicity figures
        subgroup_output = []
        subgroup_data = []
        tables = soup.find_all(
            "table", attrs={"class" : "data-table"}
        )
        for table in tables[1:]:
            keys =[i.get_text().strip() for i in table.find_all('th')]
            rows = table.find_all('tr')
            vals = []
            for row in rows[1:]:
                items = [i.get_text().strip() for i in row.find_all('td')]
                my_dict = dict(zip(keys, items))
                subgroup_data.append(my_dict)

        newDict = {
            "type": None,
            "date": last_updated,
            "data": []
        }

        for item in subgroup_data:

            if "Vaccine Manufacturer" in item:
                logger.debug(item)
                newDict['type'] = 'manufacturer'
                newDict['data'].append(item)

            # elif "Age Group" in item:
            #     newDict['type'] = 'age_groups'
            #     newDict['data'].append(item)
            # elif "Gender" in item:
            #     newDict['type'] = 'gender'
            #     newDict['data'].append(item)
            # elif "Race" in item:
            #     newDict['type'] = 'race'
            #     newDict['data'].append(item)
            # elif "Ethnicity" in item:
            #     newDict['type'] = 'ethnicity'
            #     newDict['data'].append(item)
            # else:
            #     logger.debug(item)

        subgroup_output.append(newDict)


        logger.debug(subgroup_output)





    # compile everything from one file into one big list
    # compiled_data.extend(subgroup_data)
    # logger.debug(compiled_data)

    # output_json = [
    #     # {"file": "latest-nm-vaccine-dashboard.json"},
    #     {"file": "{0}-nm-vaccine-dashboard.json".format(file[:17])},
    # ]

    # output_csv = [
    #     # {"file": "latest-nm-vaccine-dashboard.csv"},
    #     {"file": "{0}-nm-vaccine-dashboard.csv".format(file[:17])},
    # ]

    # for f in output_json:
    #     file_saved = os.path.join(dir_current, dir_data, f['file'])
    #     with open(file_saved, 'w', encoding='utf-8') as f:
    #         json.dump(compiled_data, f, ensure_ascii=False, indent=4)
    #         logger.debug('File saved to {0}'.format(file_saved))

# for f in output_csv:
#     file_saved = os.path.join(dir_current, dir_data, f['file'])
#     csv_data = pd.DataFrame(output)
#     csv_data.to_csv(file_saved, encoding='utf-8', index=False)
#     logger.debug('File saved to {0}'.format(file_saved))
