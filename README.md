# Mutual Fund Analytics Project

## Overview

This project aims to build a complete Mutual Fund Analytics platform using Python, SQL, and interactive dashboards. The objective is to collect, process, analyze, and visualize mutual fund performance data to generate actionable investment insights.

---

## Project Goals

* Collect historical mutual fund NAV data
* Build a structured data pipeline
* Perform data quality validation
* Calculate returns and risk metrics
* Compare funds against benchmarks
* Create interactive dashboards
* Generate investment insights and reports

---

# Day 1: Data Ingestion & Project Setup

## Tasks Completed

### Project Structure Created

```text
mutual-fund-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
├── sql/
├── dashboard/
├── reports/
├── scripts/
│   ├── data_ingestion.py
│   └── live_nav_fetch.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Environment Setup

* Created Python virtual environment (`.venv`)
* Installed required dependencies
* Configured project structure
* Initialized Git repository

### Dependencies Installed

* pandas
* numpy
* matplotlib
* seaborn
* plotly
* sqlalchemy
* requests
* scipy
* jupyter

### Data Collection

Historical NAV data was downloaded using the MFAPI endpoint:

```text
https://api.mfapi.in/mf/{scheme_code}
```

Data was collected for selected mutual fund schemes and stored as individual CSV files in:

```text
data/raw/
```

### Scripts Developed

#### data_ingestion.py

Responsible for:

* Downloading NAV history
* Parsing API responses
* Saving raw datasets
* Creating a reproducible ingestion pipeline

#### live_nav_fetch.py

Responsible for:

* Fetching latest NAV values
* Saving current NAV snapshots
* Supporting future real-time analysis

---

## Data Quality Observations

### Available Data

The project currently contains:

* Historical NAV data
* Scheme metadata available from MFAPI

### Missing Data Sources

The original task referenced:

* fund_master dataset
* AMFI scheme master
* category information
* risk grades

These datasets were not provided.

Therefore:

* Full AMFI validation could not be performed
* Category-level analysis is deferred
* Risk-grade analysis is deferred

### Assumptions

A lightweight fund master table will be generated from API metadata where available.

Future versions of the project will incorporate the complete AMFI scheme master dataset.

---

## Deliverables

* Project directory structure
* Python virtual environment
* requirements.txt
* data_ingestion.py
* live_nav_fetch.py
* Raw NAV datasets
* Git repository initialized

---

## Next Steps (Day 2)

### Data Engineering

* Build consolidated NAV history table
* Create master scheme dataset
* Convert date columns
* Handle missing values

### Analytics

* Daily returns
* Rolling returns
* CAGR
* Volatility
* Sharpe Ratio

### Dashboard Preparation

* Fund comparison views
* NAV trend visualizations
* Risk-return analysis

---

## Tech Stack

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn
* Plotly

### Storage

* CSV
* SQL (planned)

### Version Control

* Git
* GitHub

---

## Author

Vinay Kumar

B.Tech Computer Science (AI/ML)

Building a data-driven mutual fund analytics platform for performance evaluation, risk analysis, and investment insights.
