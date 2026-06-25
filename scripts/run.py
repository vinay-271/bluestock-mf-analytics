import pandas as pd

df = pd.read_csv("data/processed/03_aum_by_fund_house.csv")

print(df.columns.tolist())
print(df.head())