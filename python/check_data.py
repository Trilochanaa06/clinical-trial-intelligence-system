import pandas as pd

files = [
    "data/trials.csv",
    "data/sites.csv",
    "data/patient_events.csv",
    "data/protocol_deviations.csv"
]

for file in files:
    df = pd.read_csv(file)
    print(f"\n{file}")
    print("-" * 50)
    print(df.head())
    print(f"Rows: {len(df)}")