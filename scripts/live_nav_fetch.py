from pathlib import Path
import pandas as pd
import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "data" / "raw" / "live_nav"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

scheme_codes = {
    "HDFC_Top_100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data["data"])

    df["scheme_code"] = scheme_code
    df["scheme_name"] = data["meta"]["scheme_name"]

    output_file = OUTPUT_DIR / f"{fund_name}.csv"

    df.to_csv(output_file, index=False)

    print(f"Downloaded {fund_name}")