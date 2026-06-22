# Mutual Fund Analytics Project

## Overview

A data analytics project focused on collecting, processing, analyzing, and visualizing mutual fund performance data to generate actionable investment insights.

---

## Project Objectives

* Collect mutual fund NAV data
* Build a clean data pipeline
* Perform return and risk analysis
* Compare funds against benchmarks
* Create interactive dashboards
* Generate investment insights

---

## Tech Stack

| Category        | Tools                       |
| --------------- | --------------------------- |
| Language        | Python                      |
| Data Processing | Pandas, NumPy               |
| Visualization   | Matplotlib, Seaborn, Plotly |
| Data Storage    | CSV, SQL                    |
| Version Control | Git, GitHub                 |
| Development     | Jupyter Notebook            |

---

## Project Structure

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
|   └── live_nav_fetch.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Development Log

This section tracks project progress day-by-day.

---

## Day 1 — Data Ingestion & Environment Setup

### Tasks Completed

* Created project directory structure
* Created Python virtual environment
* Installed project dependencies
* Initialized Git repository
* Built data ingestion scripts
* Downloaded mutual fund NAV history from MFAPI
* Stored raw datasets in `data/raw`

### Files Added

```text
scripts/data_ingestion.py
scripts/live_nav_fetch.py
requirements.txt
```

### Data Sources

MFAPI Endpoint:

```text
https://api.mfapi.in/mf/{scheme_code}
```

### Notes

* Historical NAV data successfully collected.
* Fund master dataset was not provided.
* AMFI master scheme dataset was not provided.
* Validation tasks requiring fund_master have been deferred until metadata is available.

### Commit

```bash
git commit -m "Day 1: Data ingestion complete"
```

---

## Day 2 — Data Cleaning & Consolidation

### Tasks Completed

*To be updated*

### Files Added

*To be updated*

### Findings

*To be updated*

### Commit

```bash
git commit -m "Day 2: Data cleaning and preprocessing"
```

---

## Day 3 — Exploratory Data Analysis

### Tasks Completed

*To be updated*

### Files Added

*To be updated*

### Findings

*To be updated*

### Commit

```bash
git commit -m "Day 3: Exploratory data analysis"
```

---

## Future Milestones

### Phase 1 — Data Collection

* [x] Project setup
* [x] NAV data ingestion
* [ ] Fund metadata acquisition
* [ ] Data validation

### Phase 2 — Data Processing

* [ ] Data cleaning
* [ ] Missing value handling
* [ ] Feature engineering

### Phase 3 — Analytics

* [ ] Return calculations
* [ ] CAGR
* [ ] Rolling returns
* [ ] Volatility
* [ ] Sharpe ratio

### Phase 4 — Dashboard

* [ ] Fund comparison dashboard
* [ ] Risk-return visualization
* [ ] Performance tracking

### Phase 5 — Reporting

* [ ] Automated reports
* [ ] Investment insights
* [ ] Final documentation

```
```
