
-- 1 — Top 5 Funds by AUMj
SELECT
    fund_house,
    MAX(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;


-- 2 — Average NAV per Month
SELECT
    fund_house,
    MAX(aum_crore) AS total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 3 — SIP YoY Growth
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS sip_amount
FROM (
    SELECT
        ft.amount_inr,
        dd.full_date AS transaction_date
    FROM fact_transactions ft
    JOIN dim_date dd
    ON ft.date_id = dd.date_id
    WHERE ft.transaction_type='SIP'
)
GROUP BY year;

-- 4 — Transactions by State
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS sip_amount
FROM (
    SELECT
        ft.amount_inr,
        dd.full_date AS transaction_date
    FROM fact_transactions ft
    JOIN dim_date dd
    ON ft.date_id = dd.date_id
    WHERE ft.transaction_type='SIP'
)
GROUP BY year;

-- 5 — Funds with Expense Ratio < 1%
SELECT
    df.scheme_name,
    fp.expense_ratio_pct
FROM fact_performance AS fp
JOIN dim_fund AS df
    ON fp.amfi_code = df.amfi_code
WHERE fp.expense_ratio_pct < 1
ORDER BY fp.expense_ratio_pct;

-- 6 — Top 5 Funds by Sharpe Ratio
SELECT
    df.scheme_name,
    fp.sharpe_ratio
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY fp.sharpe_ratio DESC
LIMIT 5;


-- 7 — Top 5 Funds by 5-Year Return
SELECT
    df.scheme_name,
    fp.return_5yr_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY fp.return_5yr_pct DESC
LIMIT 5;

-- 8. Lowest Maximum Drawdown
SELECT
    df.scheme_name,
    fp.max_drawdown_pct
FROM fact_performance fp
JOIN dim_fund df
ON fp.amfi_code = df.amfi_code
ORDER BY fp.max_drawdown_pct ASC
LIMIT 5;

-- 9. Average Transaction Amount by Payment Mode
SELECT
    payment_mode,
    ROUND(AVG(amount_inr), 2) AS average_amount
FROM fact_transactions
GROUP BY payment_mode
ORDER BY average_amount DESC;

-- 10. Number of Schemes by Fund House
SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;