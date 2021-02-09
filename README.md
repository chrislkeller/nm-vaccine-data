Tracking New Mexico Covid-19 Vaccine Data
=========================================

## What is this?

## Why is this necessary?

## What do we know about the data?

From Matt at DOH.

* New Mexico Department of Health is reporting age brackets according to the [phased distribution plan](https://cv.nmhealth.org/wp-content/uploads/2021/02/2021.1.28-DOH-Phase-Guidance.pdf).

* We’ll be revising the dashboard so it reflects 16-59, 60-74, and 75+.

* Right now, the first of those categories on the dashboard runs 16-65, and 65 isn’t a relevant number in our current plan.

* Population figures come from [New Mexico Indicator-Based Information System](https://ibis.health.state.nm.us/).


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