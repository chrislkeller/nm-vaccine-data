#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json
import datetime
from itertools import zip_longest
import os
from os import listdir
from os.path import isfile, join
import logging

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)


class ProcessHtml(object):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")

    dir_current = os.path.dirname(os.path.realpath(__file__))

    dir_html = "daily-html"

    dir_data = "daily-data"

    path = os.path.join(dir_current, dir_html)

    output = []

    def handle(self):
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        self.process(files)
        json_f = {
            "file": "latest-nm-vaccine-dashboard.json"
        }
        self.write_json_file(json_f, self.output)

    def process(self, files):
        for file in files:
            compiled_data = []
            target = os.path.join(self.path, file)
            with open(target, 'r', encoding='utf-8') as f:
                soup = self.get_soup(f)
                acquired_datestamp = file[:17]
                last_updated = soup.find_all("i")[0].get_text().strip().replace("Last Updated: ", "")
                topline = self.get_topline_figures(soup, acquired_datestamp, last_updated)
                compiled_data.append(topline)
                subgroup = self.get_subgroup(soup, last_updated)
                compiled_data.extend(subgroup)
            self.output.extend(compiled_data)
            json_f = {
                "file": "{0}-nm-vaccine-dashboard.json".format(file[:17])
            }
            self.write_json_file(json_f, compiled_data)

    def write_json_file(self, file, data):
        file_saved = os.path.join(
            self.dir_current,
            self.dir_data,
            file['file']
        )
        with open(file_saved, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            logger.debug('File saved to {0}'.format(file_saved))

    def get_subgroup(self, soup, last_updated):
        """Get the manufacturer, age, gender, race and ethnicity figures."""
        output = []
        tables = soup.find_all(
            "table", attrs={"class": "data-table"}
        )
        for table in tables[1:]:
            table_dict = {
                "type": None,
                "date": last_updated,
                "data": []
            }
            keys = [i.get_text().strip() for i in table.find_all('th')]
            rows = table.find_all('tr')
            for row in rows[1:]:
                items = [i.get_text().strip() for i in row.find_all('td')]
                item = dict(zip(keys, items))
                if "Vaccine Manufacturer" in item:
                    table_dict['type'] = 'manufacturer'
                    table_dict['data'].append(item)
                elif "Age Group" in item:
                    table_dict['type'] = 'age_groups'
                    table_dict['data'].append(item)
                elif "Gender" in item:
                    table_dict['type'] = 'gender'
                    table_dict['data'].append(item)
                elif "Race" in item:
                    table_dict['type'] = 'race'
                    table_dict['data'].append(item)
                elif "Ethnicity" in item:
                    table_dict['type'] = 'ethnicity'
                    table_dict['data'].append(item)
                else:
                    logger.debug("Something went really sideways")
            output.append(table_dict)
        return output

    def get_topline_figures(self, soup, acquired_datestamp, last_updated):
        """Get the topline numbers."""
        topline_keys = []
        keys = soup.find_all(
            "div", attrs={"class": "graph-sub-num-title"}
        )
        for key in keys:
            topline_keys.append(key.get_text().strip())
        topline_values = []
        values = soup.find_all(
            "div", attrs={"class": "big-number"}
        )
        for value in values:
            topline_values.append(value.get_text().strip())
        topline_dict = {
            "type": "topline",
            "date": last_updated,
            "data": dict(zip_longest(topline_keys, topline_values))
        }
        topline_dict["data"]["datestamp"] = acquired_datestamp
        return topline_dict

    def get_soup(self, file):
        soup = BeautifulSoup(file, 'lxml')
        return soup


if __name__ == '__main__':
    task_run = ProcessHtml()
    task_run.handle()
