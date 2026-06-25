import pandas as pd

from config import RAW_DATA, PROCESSED_DATA
from utils.io import load_csv, save_csv
from utils.validation import (
    remove_duplicates,
    validate_positive,
    report_missing,
    report_duplicates
)

def clean_nav_history():

    print("\nCleaning nav_history.csv...")

    df = load_csv(RAW_DATA / "02_nav_history.csv")

    # Parse dates
    df["date"] = pd.to_datetime(
        df["date"],
        format="%Y-%m-%d",
        errors="coerce"
    )

    # Sort by scheme and date
    df = df.sort_values(
        ["amfi_code", "date"]
    )

    # Remove duplicate rows
    df = remove_duplicates(df)

    # Keep only positive NAV
    df = validate_positive(df, "nav")

    # Forward fill missing NAV within each scheme
    df["nav"] = (
        df.groupby("amfi_code")["nav"]
        .ffill()
    )

    print("Missing Values")
    print(report_missing(df))

    print("Duplicate Rows")
    print(report_duplicates(df))

    save_csv(
        df,
        PROCESSED_DATA / "02_nav_history.csv"
    )

    print("nav_history cleaned.")


def clean_transactions():

    print("\nCleaning investor_transactions.csv...")

    df = load_csv(RAW_DATA / "08_investor_transactions.csv")

    # Parse dates
    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    # Standardize transaction types
    mapping = {
        "sip": "SIP",
        "lumpsum": "Lumpsum",
        "redemption": "Redemption"
    }

    df["transaction_type"] = (
        df["transaction_type"]
            .str.strip()
            .str.lower()
            .map(mapping)
    )

    # Validate positive investment amount
    df = validate_positive(df, "amount_inr")

    # Remove duplicates
    df = remove_duplicates(df)

    print("\nKYC Status Values:")
    print(df["kyc_status"].unique())

    print("\nTransaction Types:")
    print(df["transaction_type"].unique())

    print("\nMissing Values")
    print(report_missing(df))

    print("\nDuplicate Rows")
    print(report_duplicates(df))

    save_csv(
        df,
        PROCESSED_DATA / "08_investor_transactions.csv"
    )

    print("investor_transactions cleaned.")

def clean_scheme_performance():

    print("\nCleaning scheme_performance.csv...")

    df = load_csv(RAW_DATA / "07_scheme_performance.csv")

    # -----------------------------
    # Remove duplicates
    # -----------------------------
    df = remove_duplicates(df)

    # -----------------------------
    # Validate numeric columns
    # -----------------------------

    numeric_cols = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "aum_crore",
        "expense_ratio_pct"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # -----------------------------
    # Expense Ratio Validation
    # -----------------------------

    invalid_expense = df[
        (df["expense_ratio_pct"] < 0.1)
        | (df["expense_ratio_pct"] > 2.5)
    ]

    print("\nInvalid Expense Ratios:", len(invalid_expense))

    # -----------------------------
    # Flag Return Anomalies
    # -----------------------------

    anomalies = df[
        (df["return_1yr_pct"] < -100)
        | (df["return_3yr_pct"] < -100)
        | (df["return_5yr_pct"] < -100)
    ]

    print("Return Anomalies:", len(anomalies))

    # -----------------------------
    # Reports
    # -----------------------------

    print("\nMissing Values")
    print(report_missing(df))

    print("\nDuplicate Rows")
    print(report_duplicates(df))

    save_csv(
        df,
        PROCESSED_DATA / "07_scheme_performance.csv"
    )

    print("scheme_performance cleaned.")

def main():
    clean_nav_history()
    clean_transactions()
    clean_scheme_performance()


if __name__ == "__main__":
    main()