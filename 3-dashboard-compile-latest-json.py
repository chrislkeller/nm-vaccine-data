#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
import os
from os import listdir
from os.path import isfile, join
import logging

logger = logging.getLogger("root")
logging.basicConfig(
    format="\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)


class BuildLatestJson(object):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
    dir_current = os.path.dirname(os.path.realpath(__file__))
    dir_html = "daily-html"
    dir_data = "daily-data"
    path = os.path.join(dir_current, dir_html)

    def handle(self):
        latest_output = []
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in files:
            datestamp = file[:10]
            if file.endswith(".json"):
                target = os.path.join(self.path, file)
                with open(target, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    data[0]['date'] = datestamp
                    latest_output.append(data[0])
        self.write_json_file("latest-nm-vaccine-dashboard.json", latest_output)

    def write_json_file(self, file, data):
        file_saved = os.path.join(
            self.dir_current,
            self.dir_data,
            file
        )
        with open(file_saved, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            logger.debug('File saved to {0}'.format(file_saved))


if __name__ == '__main__':
    task_run = BuildLatestJson()
    task_run.handle()
