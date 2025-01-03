#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import logging
import pandas as pd

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)


class BuildLatestJson(object):

    """
    This script is the fourth step in the process
    to process county-level json used to power
    New Mexico's vaccine dashboard

    It takes the `latest-nm-vaccine-counties.csv` file
    in the daily-data directory and uses pandas to create
    a json file of the data in the same directory

    In the event that the latest csv already exists,
    this script only needs to run after new data is acquired.
    """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    dir_current = os.path.dirname(os.path.realpath(__file__))
    dir_data = "daily-data"
    path = os.path.join(dir_current, dir_data)

    def handle(self):
        latest_csv = "latest-nm-vaccine-counties.csv"
        target = os.path.join(self.path, latest_csv)
        latest_json = "latest-nm-vaccine-counties.json"
        file_saved = os.path.join(self.path, latest_json)
        data = pd.read_csv(target)
        data.to_json(file_saved, orient='records')
        logger.debug('File saved to {0}'.format(file_saved))


if __name__ == '__main__':
    task_run = BuildLatestJson()
    task_run.handle()
