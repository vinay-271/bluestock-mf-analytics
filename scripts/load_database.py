import sqlite3
from pathlib import Path

import pandas as pd
from config import PROCESSED_DATA

df = pd.read_csv(
    PROCESSED_DATA /
    "01_fund_master.csv"
)
print(df.columns.tolist())


import pandas as pd
from sqlalchemy import create_engine

from config import (
    DATABASE_FILE,
    PROCESSED_DATA,
    PROJECT_ROOT
)


engine = create_engine(
    f"sqlite:///{DATABASE_FILE}"
)

def create_database():

    conn = sqlite3.connect(DATABASE_FILE)

    schema = (
        PROJECT_ROOT /
        "sql" /
        "schema.sql"
    )

    with open(schema, "r") as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()

    print("Database schema created.")

def load_dim_fund():

    df = pd.read_csv(
        PROCESSED_DATA /
        "01_fund_master.csv"
    )

    df = df[
        [
            "amfi_code",
            "scheme_name",
            "fund_house",
            "category",
            "sub_category",
            "plan",
            "launch_date",
            "benchmark",
            "expense_ratio_pct",
            "exit_load_pct",
            "min_sip_amount",
            "min_lumpsum_amount",
            "fund_manager",
            "risk_category",
            "sebi_category_code"
        ]
    ]

    df.to_sql(
        "dim_fund",
        engine,
        if_exists="append",
        index=False
    )

    print("dim_fund loaded.")

def load_dim_date():

    nav = pd.read_csv(
        PROCESSED_DATA /
        "02_nav_history.csv"
    )

    nav["date"] = pd.to_datetime(nav["date"])

    dates = (
        pd.DataFrame({
            "full_date":
            sorted(nav["date"].unique())
        })
    )

    dates["day"] = dates["full_date"].dt.day
    dates["month"] = dates["full_date"].dt.month
    dates["quarter"] = dates["full_date"].dt.quarter
    dates["year"] = dates["full_date"].dt.year

    dates.to_sql(
        "dim_date",
        engine,
        if_exists="append",
        index=False
    )

    print("dim_date loaded.")

def load_fact_nav():

    nav = pd.read_csv(PROCESSED_DATA / "02_nav_history.csv")

    nav["date"] = pd.to_datetime(nav["date"])

    date_dim = pd.read_sql(
        "SELECT date_id, full_date FROM dim_date",
        engine
    )

    date_dim["full_date"] = pd.to_datetime(date_dim["full_date"])

    nav = nav.merge(
        date_dim,
        left_on="date",
        right_on="full_date",
        how="left"
    )

    fact_nav = nav[
        [
            "amfi_code",
            "date_id",
            "nav"
        ]
    ]

    fact_nav.to_sql(
        "fact_nav",
        engine,
        if_exists="append",
        index=False
    )

    print("fact_nav loaded.")

def load_fact_transactions():

    df = pd.read_csv(
        PROCESSED_DATA /
        "08_investor_transactions.csv"
    )

    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    date_dim = pd.read_sql(
        "SELECT date_id, full_date FROM dim_date",
        engine
    )

    date_dim["full_date"] = pd.to_datetime(date_dim["full_date"])

    df = df.merge(
        date_dim,
        left_on="transaction_date",
        right_on="full_date",
        how="left"
    )

    fact = df[
        [
            "investor_id",
            "amfi_code",
            "date_id",
            "transaction_type",
            "amount_inr",
            "state",
            "city",
            "city_tier",
            "payment_mode",
            "kyc_status"
        ]
    ]

    fact.to_sql(
        "fact_transactions",
        engine,
        if_exists="append",
        index=False
    )

    print("fact_transactions loaded.")

def load_fact_performance():
    df = pd.read_csv(
        PROCESSED_DATA/
        "07_scheme_performance.csv"
    )

    fact = df[
        [
            "amfi_code",
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
            "expense_ratio_pct",
            "morningstar_rating"
        ]
    ]

    fact.to_sql(
        "fact_performance",
        engine,
        if_exists="append",
        index=False
    )

    print("fact_performance loaded.")

def load_fact_aum():

    df = pd.read_csv(
        PROCESSED_DATA /
        "03_aum_by_fund_house.csv"
    )

    df["date"] = pd.to_datetime(df["date"])

    fact = df[
        [
            "date",
            "fund_house",
            "aum_lakh_crore",
            "aum_crore",
            "num_schemes"
        ]
    ]

    fact.to_sql(
        "fact_aum",
        engine,
        if_exists="append",
        index=False
    )

    print("fact_aum loaded.")

def verify_database():

    tables = [
        "dim_fund",
        "dim_date",
        "fact_nav",
        "fact_transactions",
        "fact_performance",
        "fact_aum"
    ]

    print("\n" + "=" * 60)
    print("DATABASE VERIFICATION")
    print("=" * 60)

    for table in tables:
        query = f"SELECT COUNT(*) AS rows FROM {table}"
        rows = pd.read_sql(query, engine)

        print(f"{table:<22} {rows.iloc[0,0]:>10}")

def main():
    create_database()
    load_dim_fund()
    load_dim_date()
    load_fact_nav()
    load_fact_transactions()
    load_fact_performance()
    load_fact_aum()
    verify_database()



if __name__ == "__main__":
    main()