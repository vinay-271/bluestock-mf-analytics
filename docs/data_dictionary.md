# Data Dictionary

## dim_fund

| Column | Data Type | Description | Source |
|--------|-----------|-------------|--------|
| amfi_code | INTEGER | Unique AMFI scheme code | 01_fund_master.csv |
| scheme_name | TEXT | Name of the mutual fund scheme | 01_fund_master.csv |
| fund_house | TEXT | Asset Management Company | 01_fund_master.csv |
| category | TEXT | Fund category | 01_fund_master.csv |
| sub_category | TEXT | Fund sub-category | 01_fund_master.csv |
| plan | TEXT | Direct/Regular plan | 01_fund_master.csv |
| launch_date | DATE | Scheme launch date | 01_fund_master.csv |
| benchmark | TEXT | Benchmark index | 01_fund_master.csv |
| expense_ratio_pct | REAL | Expense ratio (%) | 01_fund_master.csv |
| exit_load_pct | REAL | Exit load (%) | 01_fund_master.csv |
| min_sip_amount | REAL | Minimum SIP investment | 01_fund_master.csv |
| min_lumpsum_amount | REAL | Minimum lump sum investment | 01_fund_master.csv |
| fund_manager | TEXT | Fund manager name | 01_fund_master.csv |
| risk_category | TEXT | Risk classification | 01_fund_master.csv |
| sebi_category_code | TEXT | SEBI category code | 01_fund_master.csv |

## dim_aum
## dim_date

**Description:**
Stores calendar attributes for each unique trading date. This table acts as the date dimension in the star schema and enables efficient time-based analysis such as monthly, quarterly, and yearly aggregations.

| Column    | Data Type | Description                                                                       | Source                            |
| --------- | --------- | --------------------------------------------------------------------------------- | --------------------------------- |
| date_id   | INTEGER   | Surrogate primary key for each unique date. Used as a foreign key in fact tables. | Generated during ETL              |
| full_date | DATE      | Calendar date corresponding to the trading day.                                   | Derived from `02_nav_history.csv` |
| day       | INTEGER   | Day of the month (1–31).                                                          | Generated from `full_date`        |
| month     | INTEGER   | Month number (1–12).                                                              | Generated from `full_date`        |
| quarter   | INTEGER   | Calendar quarter (1–4).                                                           | Generated from `full_date`        |
| year      | INTEGER   | Four-digit calendar year.                                                         | Generated from `full_date`        |

**Primary Key:** `date_id`

**Referenced By:**

* `fact_nav`
* `fact_transactions`


## fact_nav

**Description:**
Stores the historical Net Asset Value (NAV) of each mutual fund scheme for every trading day. This table is the primary fact table used for time-series analysis, return calculations, and performance visualization.

| Column    | Data Type | Description                                                        | Source               |
| --------- | --------- | ------------------------------------------------------------------ | -------------------- |
| nav_id    | INTEGER   | Surrogate primary key for each NAV record.                         | Generated during ETL |
| amfi_code | INTEGER   | Unique AMFI scheme identifier. Foreign key referencing `dim_fund`. | `02_nav_history.csv` |
| date_id   | INTEGER   | Foreign key referencing `dim_date`.                                | Generated during ETL |
| nav       | REAL      | Net Asset Value of the mutual fund on the specified trading date.  | `02_nav_history.csv` |

**Primary Key:** `nav_id`

**Foreign Keys:**

* `amfi_code` → `dim_fund(amfi_code)`
* `date_id` → `dim_date(date_id)`

**Purpose:**

* Daily NAV tracking
* Monthly/Yearly NAV analysis
* Return calculations
* Performance trend visualization

---

## fact_transactions

**Description:**
Stores investor transaction records including investment amount, transaction type, demographic information, and payment details. Used for transaction analytics and investor behavior analysis.

| Column           | Data Type | Description                                                        | Source                         |
| ---------------- | --------- | ------------------------------------------------------------------ | ------------------------------ |
| transaction_id   | TEXT      | Unique transaction identifier.                                     | Generated during ETL           |
| investor_id      | TEXT      | Unique investor identifier.                                        | `08_investor_transactions.csv` |
| amfi_code        | INTEGER   | Mutual fund scheme identifier. Foreign key referencing `dim_fund`. | `08_investor_transactions.csv` |
| date_id          | INTEGER   | Foreign key referencing `dim_date`.                                | Generated during ETL           |
| transaction_type | TEXT      | Type of investment transaction (SIP, Lumpsum, Redemption).         | `08_investor_transactions.csv` |
| amount_inr       | REAL      | Transaction amount in Indian Rupees (₹).                           | `08_investor_transactions.csv` |
| state            | TEXT      | Investor's state of residence.                                     | `08_investor_transactions.csv` |
| city             | TEXT      | Investor's city of residence.                                      | `08_investor_transactions.csv` |
| city_tier        | TEXT      | Classification of city (Tier-1, Tier-2, Tier-3).                   | `08_investor_transactions.csv` |
| payment_mode     | TEXT      | Mode of payment (UPI, Net Banking, Cheque, Mandate, etc.).         | `08_investor_transactions.csv` |
| kyc_status       | TEXT      | Investor KYC verification status.                                  | `08_investor_transactions.csv` |

**Primary Key:** `transaction_id`

**Foreign Keys:**

* `amfi_code` → `dim_fund(amfi_code)`
* `date_id` → `dim_date(date_id)`

**Purpose:**

* Transaction analysis
* SIP growth analysis
* Payment mode trends
* Geographic investment analysis
* Investor behavior analytics

---

## fact_performance

**Description:**
Stores performance and risk metrics for each mutual fund scheme. Used for comparative fund analysis and investment performance evaluation.

| Column             | Data Type | Description                                                        | Source                      |
| ------------------ | --------- | ------------------------------------------------------------------ | --------------------------- |
| performance_id     | INTEGER   | Surrogate primary key for performance records.                     | Generated during ETL        |
| amfi_code          | INTEGER   | Mutual fund scheme identifier. Foreign key referencing `dim_fund`. | `07_scheme_performance.csv` |
| return_1yr_pct     | REAL      | Annual return over the last 1 year (%).                            | `07_scheme_performance.csv` |
| return_3yr_pct     | REAL      | Annualized return over the last 3 years (%).                       | `07_scheme_performance.csv` |
| return_5yr_pct     | REAL      | Annualized return over the last 5 years (%).                       | `07_scheme_performance.csv` |
| benchmark_3yr_pct  | REAL      | Three-year benchmark return (%).                                   | `07_scheme_performance.csv` |
| alpha              | REAL      | Risk-adjusted excess return over the benchmark.                    | `07_scheme_performance.csv` |
| beta               | REAL      | Sensitivity of the fund relative to the benchmark.                 | `07_scheme_performance.csv` |
| sharpe_ratio       | REAL      | Risk-adjusted return measured using the Sharpe Ratio.              | `07_scheme_performance.csv` |
| sortino_ratio      | REAL      | Downside risk-adjusted return.                                     | `07_scheme_performance.csv` |
| std_dev_ann_pct    | REAL      | Annualized standard deviation of returns (%).                      | `07_scheme_performance.csv` |
| max_drawdown_pct   | REAL      | Maximum observed loss from peak to trough (%).                     | `07_scheme_performance.csv` |
| expense_ratio_pct  | REAL      | Annual expense ratio charged by the fund (%).                      | `07_scheme_performance.csv` |
| morningstar_rating | INTEGER   | Morningstar fund rating (1–5 stars).                               | `07_scheme_performance.csv` |

**Primary Key:** `performance_id`

**Foreign Key:**

* `amfi_code` → `dim_fund(amfi_code)`

**Purpose:**

* Fund comparison
* Risk-return analysis
* Performance ranking
* Investment recommendation metrics

---

## fact_aum

**Description:**
Stores historical Assets Under Management (AUM) statistics for each fund house. Used to analyze fund house growth, industry size, and market trends.

| Column         | Data Type | Description                                              | Source                     |
| -------------- | --------- | -------------------------------------------------------- | -------------------------- |
| aum_id         | INTEGER   | Surrogate primary key for each AUM record.               | Generated during ETL       |
| date           | DATE      | Reporting date of the AUM snapshot.                      | `03_aum_by_fund_house.csv` |
| fund_house     | TEXT      | Name of the Asset Management Company (AMC).              | `03_aum_by_fund_house.csv` |
| aum_lakh_crore | REAL      | Total AUM expressed in lakh crore rupees.                | `03_aum_by_fund_house.csv` |
| aum_crore      | REAL      | Total AUM expressed in crore rupees.                     | `03_aum_by_fund_house.csv` |
| num_schemes    | INTEGER   | Number of mutual fund schemes managed by the fund house. | `03_aum_by_fund_house.csv` |

**Primary Key:** `aum_id`

**Purpose:**

* Fund house comparison
* Industry growth analysis
* AUM trend visualization
* Market leadership analysis
