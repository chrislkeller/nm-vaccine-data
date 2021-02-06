#! /usr/bin/env python
# -*- coding: utf-8 -*-

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


class BuildLatestCsv(object):

    """
    This script is the third step in the process
    to process county-level json used to power
    New Mexico's vaccine dashboard

    For each csv file in the daily-data directory
    it uses pandas to concatenate them into
    `latest-nm-vaccine-counties.csv` file
    """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    dir_current = os.path.dirname(os.path.realpath(__file__))
    # dir_json = "daily-json"
    dir_data = "daily-data"
    path = os.path.join(dir_current, dir_data)

    def handle(self):
        latest_output = []

        # get a list of files
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]

        # loop through each
        for file in files:

            # if the naming convention matches
            if len(file) == 41:
                target = os.path.join(self.path, file)

                # convert the file to a data frame
                df = pd.read_csv(target, index_col=None, header=0)

                # append it to a list
                latest_output.append(df)
        latest_csv = "latest-nm-vaccine-counties.csv"

        # write the data to a file
        self.write_csv(latest_csv, latest_output)

    def write_csv(self, file, data):
        file_saved = os.path.join(self.dir_current, self.dir_data, file)
        csv_data = pd.concat(data, axis=0, ignore_index=True)
        csv_data.to_csv(file_saved, encoding='utf-8', index=False)
        logger.debug('File saved to {0}'.format(file_saved))


if __name__ == '__main__':
    task_run = BuildLatestCsv()
    task_run.handle()
