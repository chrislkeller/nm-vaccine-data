# New Mexico Department of Health vaccine data

## What is this?

## What is here?

### [nm-covid-19-vaccine-administered-by-age.csv](./nm-covid-19-vaccine-administered-by-age.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-administered-by-county.csv](./nm-covid-19-vaccine-administered-by-county.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-administered-by-gender.csv](./nm-covid-19-vaccine-administered-by-gender.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-administered-by-race.csv](./nm-covid-19-vaccine-administered-by-race.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-by-dose-number.csv](./nm-covid-19-vaccine-by-dose-number.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-doses-administered.csv](./nm-covid-19-vaccine-doses-administered.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-doses-by-day.csv](./nm-covid-19-vaccine-doses-by-day.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-doses-by-provider-type.csv](./nm-covid-19-vaccine-doses-by-provider-type.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-doses-by-provider.csv](./nm-covid-19-vaccine-doses-by-provider.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-doses-delivered.csv](./nm-covid-19-vaccine-doses-delivered.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-ltcf-doses-delivered.csv](./nm-covid-19-vaccine-ltcf-doses-delivered.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-ltcf-program-cumulative.csv](./nm-covid-19-vaccine-ltcf-program-cumulative.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-manufacturer-doses-by-day.csv](./nm-covid-19-vaccine-manufacturer-doses-by-day.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-orders-and-shipments.csv](./nm-covid-19-vaccine-orders-and-shipments.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

### [nm-covid-19-vaccine-percent-of-population.csv](./nm-covid-19-vaccine-percent-of-population.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

| field              | type    | description                                                                                                                                                                 |
|--------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date_of_data       | date    | Column added by recipient to show the date data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                |
| category           | varchar | Category designation. It is unclear what other potential values are, or how the data is stored. For instance, is this a freeform text field of options that can be selected |
| calculated_percent | string  | String formatted as a percent to show percent of population receiving one or two doses of the Covid-19 vaccine                                                              |
| percent            | float   | A decimal version to show the percent of population receiving one or two doses                                                                                              |
| source             | varchar | Column added by recipient to show the source of the data                                                                                                                    |

### [nm-covid-19-vaccine-spoiled-wasted-expired.csv](./nm-covid-19-vaccine-spoiled-wasted-expired.csv)

**What we know**:

**What we don't know**:

#### Data dictionary

| field        | type    | description                                                                                                                                                                                           |
|--------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date_of_data | date    | Column added by recipient to show the date data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                          |
| category     | varchar | Category to disclose what happened to vaccines. It is unclear what other potential values are, or how the data is stored. For instance, is this a freeform text field of options that can be selected |
| moderna      | integer | Amount of Moderna vaccine that fits the category New Mexico                                                                                                                                           |
| pfizer       | integer | Amount of Pfizer vaccine that fits the category New Mexico                                                                                                                                            |
| source       | integer | Column added by recipient to show the source of the data                                                                                                                                              |
