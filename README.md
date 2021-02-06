Tracking New Mexico Covid-19 Vaccine Data
=========================================

## What is this?

## Why is this necessary?

## What do we know?

## Who is working on this?

## How do I get started?

**Note to self**

* If running this for the first time:
    * To bootstrap county-level data:
        * `acquire-daily-json.py`
        * `compile-daily-county-csv.py`
        * `build-latest-county-csv.py`
        * `build-latest-county-json.py`

    * Once county-level data is bootstrapped:
        * `acquire-daily-json.py`
        * `update-latest-county-csv.py`
        * `build-latest-county-json.py`