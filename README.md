Tracking New Mexico Covid-19 Vaccine Data
=========================================

## What is this?

## Why is this necessary?

## What do we know?

## Who is working on this?

## How do I get started?

**Note to self**

* If running this for the first time:
    * To process county-level data:
        * run `acquire-json.py`
        * run `compile-daily-county-csv.py` to loop through each json file in the `daily-json` directory and builds a .csv file for each one.
        * run the `build-latest-county-csv.py` script to loop through each csv file in the `daily-data` directory and builds one .csv containing each file titled `latest-nm-vaccine-counties.csv`.
        * run the `build-latest-county-json.py` script to write the contents of `latest-nm-vaccine-counties.csv` to a json file titled `latest-nm-vaccine-counties.json`.
