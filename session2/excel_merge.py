# pip install pandas
import os
import pandas as pd

os.chdir("/Users/valentin/Documents/VHS Kurse/Automatisierung mit Python/Excel Demo")

print(os.getcwd())

merged_data = pd.DataFrame()

for f in os.listdir():
    #print(f)
    if f.startswith("."): continue
    if f.startswith("~"): continue
    if "2023" in f: continue

    imported_data = pd.read_excel(f)
    print(imported_data.head())

    merged_data = pd.concat([merged_data, imported_data], ignore_index=True)

merged_data = merged_data.rename(columns={"Tag": "Datum"})

merged_data["Wochentag"] = merged_data["Datum"].dt.dayofweek

merged_data["Datum"] = merged_data["Datum"].dt.date

print(merged_data)

merged_data.to_excel("besuche_2023.xlsx", index=False, sheet_name="2023")