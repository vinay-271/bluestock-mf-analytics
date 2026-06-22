import requests
import pandas as pd
from pathlib import Path

scheme_codes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

for fund_name, scheme_code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data["data"])

    output_file = RAW_DIR / f"{fund_name}.csv"

    df.to_csv(output_file, index=False)

    print(f"Saved -> {output_file}")