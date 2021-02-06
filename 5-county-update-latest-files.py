#! /usr/bin/env python
# -*- coding: utf-8 -*-

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


class UpdateLatestCsv(object):

    """
    This script is the fifth step in the process
    to process county-level json used to power
    New Mexico's vaccine dashboard

    It updates the `latest-nm-vaccine-counties.csv` file
    in the daily-data directory with the contents of the newest
    json file of the data in the same directory
    """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    dir_current = os.path.dirname(os.path.realpath(__file__))
    dir_json = "daily-json"
    dir_data = "daily-data"
    path = os.path.join(dir_current, dir_json)

    def handle(self):
        latest_csv = "latest-nm-vaccine-counties.csv"
        latest_json = "latest-nm-vaccine-counties.json"
        latest_output = []
        files = [os.path.join(self.path, f) for f in listdir(self.path) if isfile(join(self.path, f))]
        target = max(files, key=os.path.getctime)
        with open(target, encoding='utf-8') as f:
            raw_json = json.load(f)
            for item in raw_json['data']:
                item['acquired_datestamp'] = os.path.basename(target)[:17]
                latest_output.append(item)
        self.update_csv(latest_csv, latest_output)
        self.create_json(latest_csv, latest_json, latest_output)

    def update_csv(self, file, data):
        file_saved = os.path.join(self.dir_current, self.dir_data, file)
        csv_data = pd.DataFrame(data)
        csv_data.to_csv(file_saved, mode='a', header=False, encoding='utf-8', index=False)
        logger.debug('Data appended to {0}'.format(file_saved))

    def create_json(self, csv, json, data):
        target = os.path.join(self.dir_current, self.dir_data, csv)
        file_saved = os.path.join(self.dir_current, self.dir_data, json)
        data = pd.read_csv(target)
        data.to_json(file_saved, orient='records')
        logger.debug('Latest data saved to {0}'.format(file_saved))


if __name__ == '__main__':
    task_run = UpdateLatestCsv()
    task_run.handle()
