import requests
import pandas as pd
import os

# Create raw data folder if it doesn't exist
raw_folder = "../data/raw"
os.makedirs(raw_folder, exist_ok=True)

# Mutual fund schemes and AMFI codes
schemes = {
    "HDFC_Top100": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    print(f"\nFetching {fund_name} ({scheme_code})...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"{raw_folder}/{fund_name}_NAV.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"Saved successfully: {file_name}")
        print(f"Rows downloaded: {len(nav_df)}")

    except Exception as e:
        print(f"Error fetching {fund_name}: {e}")

print("\nAll downloads completed.")