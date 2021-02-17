# New Mexico Department of Health vaccine data

## What is this?

## What is here?

### [nm-covid-19-vaccine-administered-by-age.csv](./nm-covid-19-vaccine-administered-by-age.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

| field                                        | type    | description                                                                                                                  |
|----------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------|
| date_of_data                                 | date    | Column added by recipient to show the date data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| Age Group                                    |         |                                                                                                                              |
| Cumulative Doses (all phases)                |         |                                                                                                                              |
| Population Total (16 and over)               |         |                                                                                                                              |
| Doses per 100 Population                     |         |                                                                                                                              |
| First Doses                                  |         |                                                                                                                              |
| Percent of Population Receiving Initial Dose |         |                                                                                                                              |
| Second Doses                                 |         |                                                                                                                              |
| Percent of Population Completing Vaccination |         |                                                                                                                              |
| source                                       | varchar | Column added by recipient to show the source of the data                                                                     |

### [nm-covid-19-vaccine-administered-by-county.csv](./nm-covid-19-vaccine-administered-by-county.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

| field                                        | type    | description                                                                                                                  |
|----------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------|
| date_of_data                                 | date    | Column added by recipient to show the date data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |
| county                                       |         |                                                                                                                              |
| cumulative_doses_all_phases)                 |         |                                                                                                                              |
| population_total_16_and_over                 |         |                                                                                                                              |
| doses_per_100_population                     |         |                                                                                                                              |
| first_doses                                  |         |                                                                                                                              |
| percent_of_population_receiving_initial_dose |         |                                                                                                                              |
| second_doses                                 |         |                                                                                                                              |
| percent_population_completing_vaccination    |         |                                                                                                                              |
| source                                       | varchar | Column added by recipient to show the source of the data                                                                     |

### [nm-covid-19-vaccine-administered-by-gender.csv](./nm-covid-19-vaccine-administered-by-gender.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- gender
- cumulative doses (all phases)
- population total (16 and over)
- doses per 100 population
- first doses
- percent of population receiving initial dose
- second doses
- percent of population completing vaccination
- source

### [nm-covid-19-vaccine-administered-by-race.csv](./nm-covid-19-vaccine-administered-by-race.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- Race Group
- Cumulative Doses (all phases)
- Population Total (16 and over)
- Doses per 100 Population
- First Doses
- Percent of Population Receiving Initial Dose
- Second Doses
- Percent of Population Completing Vaccination
- source

### [nm-covid-19-vaccine-by-dose-number.csv](./nm-covid-19-vaccine-by-dose-number.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- dose_num
- cumulative_doses_all_phases
- source

### [nm-covid-19-vaccine-doses-administered.csv](./nm-covid-19-vaccine-doses-administered.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- cumulative_doses_administered
- doses_administered_last_7 days (2/4 to 2/10)
- average daily doses administered in last 7 days
source

### [nm-covid-19-vaccine-doses-by-day.csv](./nm-covid-19-vaccine-doses-by-day.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- date
- primary_dose
- booster_dose
- total	source

### [nm-covid-19-vaccine-doses-by-provider-type.csv](./nm-covid-19-vaccine-doses-by-provider-type.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- provider_type
- frequency
- percent
- source

### [nm-covid-19-vaccine-doses-by-provider.csv](./nm-covid-19-vaccine-doses-by-provider.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- provider_desc
- clinic_desc
- vaccination_date
- practice_type
- distinct_patient_count
- source

### [nm-covid-19-vaccine-doses-delivered.csv](./nm-covid-19-vaccine-doses-delivered.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- state_jurisdiction_pharmacy
- federal
- source

### [nm-covid-19-vaccine-ltcf-doses-delivered.csv](./nm-covid-19-vaccine-ltcf-doses-delivered.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- transfer - total dose transferred to ltcf
- ltcf program - first doses transferred
- ltcf program - second doses transferred
- source

### [nm-covid-19-vaccine-ltcf-program-cumulative.csv](./nm-covid-19-vaccine-ltcf-program-cumulative.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- cumulative_staff_doses_adminstered
- cumulative_resident_doses
- cumulative_second_doses_administered
- cumulative_first_doses_adminstered
- cumulative_total_doses_administered
- date
- first_doses
- second_doses
- total_doses
- staff
- residents
- source

### [nm-covid-19-vaccine-manufacturer-doses-by-day.csv](./nm-covid-19-vaccine-manufacturer-doses-by-day.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

- date_of_data
- date
- moderna
- pfizer
- uf
- cumulative
- source

### [nm-covid-19-vaccine-orders-and-shipments.csv](./nm-covid-19-vaccine-orders-and-shipments.csv)

**What we know**:

**What we don't know**:

**Data dictionary**


| field                 | type    | description                                                                                                                                                                 |
|-----------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date_of_data          | date    | Column added by recipient to show the date data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                |
| category              | varchar | Category designation. It is unclear what other potential values are, or how the data is stored. For instance, is this a freeform text field of options that can be selected |
| doses_ordered_total   | integer | Integer to show how many vaccine doses the state of New Mexico has ordered as of Feb. 10, 2021.                                                                             |
| doses_shipped_total   | integer | Integer to show how many vaccine doses the state of New Mexico has shipped as of Feb. 10, 2021.                                                                             |
| doses_delivered_total | integer | Integer to show how many vaccine doses the state of New Mexico has delivered as of Feb. 10, 2021.                                                                           |
| source                | varchar | Column added by recipient to show the source of the data                                                                                                                    |

### [nm-covid-19-vaccine-percent-of-population.csv](./nm-covid-19-vaccine-percent-of-population.csv)

**What we know**:

**What we don't know**:

**Data dictionary**

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

**Data dictionary**

| field        | type    | description                                                                                                                                                                                           |
|--------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| date_of_data | date    | Column added by recipient to show the date data were retrieved in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                                                                          |
| category     | varchar | Category to disclose what happened to vaccines. It is unclear what other potential values are, or how the data is stored. For instance, is this a freeform text field of options that can be selected |
| moderna      | integer | Amount of Moderna vaccine that fits the category New Mexico                                                                                                                                           |
| pfizer       | integer | Amount of Pfizer vaccine that fits the category New Mexico                                                                                                                                            |
| source       | integer | Column added by recipient to show the source of the data                                                                                                                                              |
