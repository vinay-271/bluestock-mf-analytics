## Day 1 – Project Setup & Data Ingestion

### Completed

- Created project directory structure
- Configured Python virtual environment
- Installed required dependencies
- Initialized Git repository and connected GitHub
- Loaded all 10 provided datasets
- Built reusable data ingestion script
- Downloaded live NAV data for 6 mutual fund schemes using mfapi.in
- Explored fund master dataset
- Validated AMFI codes against NAV history

### Validation Summary

- Total datasets: 10
- Total schemes: 40
- Total NAV records: 46,000
- Missing values: None detected
- Duplicate rows: None detected
- AMFI validation: Passed

### Deliverables

- `scripts/data_ingestion.py`
- `scripts/live_nav_fetch.py`
- `requirements.txt`
- Initial project documentation

## Day 2 – Data Cleaning, ETL Pipeline & SQLite Data Warehouse

### Tasks Completed

* Developed a reusable ETL data cleaning pipeline.
* Cleaned and validated `nav_history.csv`.
* Parsed and standardized date columns.
* Sorted NAV history by AMFI code and trading date.
* Removed duplicate records and validated positive NAV values.
* Standardized investor transaction types (`SIP`, `Lumpsum`, `Redemption`).
* Validated transaction amounts and KYC status values.
* Cleaned and validated scheme performance metrics.
* Verified numeric performance indicators and expense ratio ranges.
* Saved cleaned datasets to `data/processed/`.

### SQLite Data Warehouse

Designed and implemented a star schema in SQLite consisting of:

#### Dimension Tables

* `dim_fund`
* `dim_date`

#### Fact Tables

* `fact_nav`
* `fact_transactions`
* `fact_performance`
* `fact_aum`

### ETL Pipeline

Implemented database loading scripts to:

* Create the SQLite database from `schema.sql`
* Populate dimension tables
* Populate fact tables
* Generate a reusable date dimension
* Verify successful data loading through automated row count validation

### Database Verification

| Table             | Rows Loaded |
| ----------------- | ----------: |
| dim_fund          |          40 |
| dim_date          |       1,150 |
| fact_nav          |      46,000 |
| fact_transactions |      32,778 |
| fact_performance  |          40 |
| fact_aum          |          90 |

### SQL Analytics

Created `queries.sql` containing analytical SQL queries for:

* Top funds by Assets Under Management (AUM)
* Monthly average NAV
* Year-over-Year SIP growth
* Transactions by state
* Funds with low expense ratios
* Top Sharpe Ratio funds
* Top 5-Year return performers
* Lowest maximum drawdown
* Average transaction amount by payment mode
* Number of schemes managed by each fund house

### Documentation

Created a comprehensive data dictionary documenting:

* Table descriptions
* Column definitions
* Data types
* Primary and foreign keys
* Source datasets
* Business purpose of each table

### Deliverables

* `scripts/data_cleaning.py`
* `scripts/load_database.py`
* `sql/schema.sql`
* `sql/queries.sql`
* `data/db/bluestock_mf.db`
* Cleaned datasets in `data/processed/`
* `docs/data_dictionary.md`

### Outcome

Successfully transformed raw mutual fund datasets into a validated SQLite star-schema data warehouse, establishing a reusable ETL pipeline and analytics-ready database for subsequent exploratory data analysis, financial metric computation, and dashboard development.