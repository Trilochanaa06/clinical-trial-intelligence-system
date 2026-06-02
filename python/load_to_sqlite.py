import sqlite3
import pandas as pd

conn = sqlite3.connect("clinical_trials.db")

# Load CSVs
trials = pd.read_csv("data/trials.csv")
sites = pd.read_csv("data/sites.csv")
patient_events = pd.read_csv("data/patient_events.csv")
protocol_deviations = pd.read_csv("data/protocol_deviations.csv")

# Write to SQLite
trials.to_sql("trials", conn, if_exists="replace", index=False)
sites.to_sql("sites", conn, if_exists="replace", index=False)
patient_events.to_sql("patient_events", conn, if_exists="replace", index=False)
protocol_deviations.to_sql("protocol_deviations", conn, if_exists="replace", index=False)

conn.close()

print("Database loaded successfully.")