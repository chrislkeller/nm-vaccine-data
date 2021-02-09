# Tracking New Mexico Covid-19 Vaccine Data

## What is this?

An attempt to inventory daily changes to data that details vaccine distribution in New Mexico.

## Why is this necessary?

Coming soon...

## What do we know about the data?

### Doses Administered Per Age Group

* Data from the New Mexico Department of Health is based on age brackets listed in the the [phased distribution plan](https://cv.nmhealth.org/wp-content/uploads/2021/02/2021.1.28-DOH-Phase-Guidance.pdf): "16-59", "60-74", and "75+"

* Cumulative is the total number of doses administered to individuals in that age group. First and second doses are combined into the cumulative number.

* Population figures come from [New Mexico Indicator-Based Information System](https://ibis.health.state.nm.us/).

## Who is working on this?

* [Chris Keller](https://chrislkeller.com/)

## How do I get started?

These instructions will be fleshed out, so right now they only make sense to Chris. But he needs to make this repo public so he can access some data so...

* If running this for the first time:
  * To bootstrap county-level data:
    * `1-county-acquire-daily-json.py`
    * `2-county-compile-daily-csv.py`
  * Once county-level data is bootstrapped, these only needs to run each day:
    * `1-county-acquire-daily-json.py`
    * `5-county-update-latest-files.py`
