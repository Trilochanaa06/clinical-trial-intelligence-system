import pandas as pd
import random
from datetime import datetime, timedelta

trials = []

trial_phases = ["Phase II", "Phase III"]
therapeutic_areas = ["Oncology", "Cardiology", "Neurology", "Immunology"]

for i in range(1, 11):
    trials.append({
        "trial_id": f"T{i:03}",
        "phase": random.choice(trial_phases),
        "therapeutic_area": random.choice(therapeutic_areas),
        "target_enrollment": random.randint(150, 600),
        "planned_duration_days": random.randint(180, 720)
    })

trials_df = pd.DataFrame(trials)

sites = []
cities = ["Chennai", "Bangalore", "Hyderabad", "Mumbai", "Delhi"]

site_count = 1
for trial in trials_df["trial_id"]:
    for _ in range(5):
        sites.append({
            "site_id": f"S{site_count:03}",
            "trial_id": trial,
            "city": random.choice(cities),
            "investigator": f"Dr_{site_count}",
            "enrollment_target": random.randint(30, 120)
        })
        site_count += 1

sites_df = pd.DataFrame(sites)

patient_events = []

statuses = ["Active", "Completed", "Dropped"]
dropout_reasons = [
    "Adverse Event",
    "Withdrawal",
    "Lost Follow-up",
    "Protocol Non-compliance"
]

for i in range(1, 2001):
    site = sites_df.sample(1).iloc[0]
    status = random.choice(statuses)

    patient_events.append({
        "patient_id": f"P{i:04}",
        "trial_id": site["trial_id"],
        "site_id": site["site_id"],
        "enrolled_date": datetime(2025, 1, 1) + timedelta(days=random.randint(0, 365)),
        "status": status,
        "dropout_reason": random.choice(dropout_reasons) if status == "Dropped" else None,
        "adverse_event": random.choice(["Yes", "No"])
    })

patient_df = pd.DataFrame(patient_events)

deviations = []

deviation_types = [
    "Missing Visit",
    "Dosage Error",
    "Data Entry Delay",
    "Eligibility Violation"
]

severity_levels = ["Minor", "Major", "Critical"]

for i in range(1, 501):
    site = sites_df.sample(1).iloc[0]

    deviations.append({
        "deviation_id": f"D{i:04}",
        "trial_id": site["trial_id"],
        "site_id": site["site_id"],
        "deviation_type": random.choice(deviation_types),
        "severity": random.choice(severity_levels)
    })

deviation_df = pd.DataFrame(deviations)

trials_df.to_csv("data/trials.csv", index=False)
sites_df.to_csv("data/sites.csv", index=False)
patient_df.to_csv("data/patient_events.csv", index=False)
deviation_df.to_csv("data/protocol_deviations.csv", index=False)
print("Dataset created successfully.")