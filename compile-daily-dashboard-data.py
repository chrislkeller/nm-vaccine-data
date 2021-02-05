#! /usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import json
import csv
import datetime
from itertools import zip_longest
import os
from os import listdir
from os.path import isfile, join
import locale
import logging

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

class CompileJsonFiles(object):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    dir_current = os.path.dirname(os.path.realpath(__file__))
    dir_html = "daily-html"
    dir_data = "daily-data"
    path = os.path.join(dir_current, dir_html)

    def handle(self):
        latest_output = []
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in files:
            daily_output = []
            target = os.path.join(self.path, file)
            with open(target, 'r', encoding='utf-8') as f:
                soup = self.get_soup(f)
                processed_data = self.process(file, soup)
                daily_output.append(processed_data)
                latest_output.append(processed_data)
            self.write_json_file("{0}-nm-vaccine-dashboard.json".format(file[:17]), daily_output)
        self.write_json_file("latest-nm-vaccine-dashboard.json", daily_output)

    def write_json_file(self, file, data):
        file_saved = os.path.join(
            self.dir_current,
            self.dir_data,
            file
        )
        with open(file_saved, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            logger.debug('File saved to {0}'.format(file_saved))

    def process(self, file, soup):
        html_date = soup.find_all("i")[0].get_text().strip()
        last_updated = html_date.replace("Last Updated: ", "")
        topline = self.get_topline_figures(soup, last_updated, file)
        subgroups = self.get_subgroup_figures(soup, last_updated, file)
        return {
            "topline": topline,
            "subgroups": subgroups
        }

    def get_topline_figures(self, soup, last_updated, file):
        """Get the topline numbers."""
        output = {
            "type": None,
            "date": last_updated,
            "acquired_datestamp": file[:17],
            "data": []
        }
        element = soup.find_all(
            "div", attrs={"class": "element"}
        )
        compiled = {}
        for e in element:
            key = e.find(
                "div", attrs={"class": "graph-sub-num-title"}
            ).get_text().strip()
            value = e.find(
                "div", attrs={"class": "big-number"}
            ).get_text().strip()
            compiled[key] = value
            compiled["acquired_datestamp"] = output['acquired_datestamp']
        output["data"].append(compiled)
        output["type"] = "topline"
        return output

    def get_subgroup_figures(self, soup, last_updated, file):
        """Get the manufacturer, age, gender, race and ethnicity figures."""
        output = {
            "type": None,
            "date": last_updated,
            "acquired_datestamp": file[:17],
            "data": []
        }
        tables = soup.find_all(
            "table", attrs={"class": "data-table"}
        )
        for table in tables[1:]:
            keys = [i.get_text().strip() for i in table.find_all('th')]
            rows = table.find_all('tr')
            for row in rows[1:]:
                items = [i.get_text().strip() for i in row.find_all('td')]
                """
                modify list entries during for loop
                """
                for i, s in enumerate(items):
                    new_value = self._to_num(s)
                    if new_value:
                        items[i] = new_value['value']
                    else:
                        pass
                compiled = dict(zip(keys, items))
                compiled["acquired_datestamp"] = output['acquired_datestamp']
                if "Vaccine Manufacturer" in compiled:
                    output['type'] = 'manufacturer'
                    output['data'].append(compiled)
                elif "Age Group" in compiled:
                    output['type'] = 'age_groups'
                    output['data'].append(compiled)
                elif "Gender" in compiled:
                    output['type'] = 'gender'
                    output['data'].append(compiled)
                elif "Race" in compiled:
                    output['type'] = 'race'
                    output['data'].append(compiled)
                elif "Ethnicity" in compiled:
                    output['type'] = 'ethnicity'
                    output['data'].append(compiled)
                else:
                    logger.debug("Something went really sideways")
            output["data"].append(compiled)
        return output

    def get_soup(self, file):
        soup = BeautifulSoup(file, 'lxml')
        return soup

    def _to_num(self, value):
        """
        given a value can it be converted to an int
        http://stackoverflow.com/a/16464365
        """
        output = {}
        NoneType = type(None)
        # actually integer values
        if isinstance(value, (int)):
            output["convert"] = True
            output["value"] = value
            output["type"] = type(value)
        # some floats can be converted without loss
        elif isinstance(value, float):
            output["convert"] = (int(value) == float(value))
            output["value"] = value
            output["type"] = type(value)
        # we can't convert nonetypes
        elif isinstance(value, NoneType):
            output["convert"] = False
            output["value"] = None
            output["type"] = type(value)
        # we can't convert non-string
        elif not isinstance(value, str):
            output["convert"] = False
            output["value"] = "Nonstring"
            output["type"] = type(value)
        else:
            value = value.strip()
            try:
                # try to convert value to float
                float_value = float(value)
                output["convert"] = True
                output["value"] = float_value
                output["type"] = type(float_value)
            except ValueError:
                # if fails try to convert value to int
                try:
                    # int_value = int(value)
                    int_value = locale.atoi(value)
                    output["convert"] = True
                    output["value"] = int_value
                    output["type"] = type(int_value)
                # if fails it's a string
                except ValueError:
                    output["convert"] = False
                    output["value"] = None
                    output["type"] = type(value)
        if output["convert"] != False:
            return output
        else:
            return False

if __name__ == '__main__':
    task_run = CompileJsonFiles()
    task_run.handle()
