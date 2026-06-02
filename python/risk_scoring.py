import pandas as pd

# Load datasets
patients = pd.read_csv("data/patient_events.csv")
deviations = pd.read_csv("data/protocol_deviations.csv")

# -----------------------------
# Dropout rate per trial
# -----------------------------
dropout = (
    patients.groupby("trial_id")
    .apply(lambda x: (x["status"] == "Dropped").mean() * 100)
    .reset_index(name="dropout_rate")
)

# -----------------------------
# Deviation count per trial
# -----------------------------
deviation_counts = (
    deviations.groupby("trial_id")
    .size()
    .reset_index(name="deviation_count")
)

# -----------------------------
# Enrollment volume
# -----------------------------
enrollment = (
    patients.groupby("trial_id")
    .size()
    .reset_index(name="enrollment_count")
)

# -----------------------------
# Merge metrics
# -----------------------------
risk_df = dropout.merge(deviation_counts, on="trial_id")
risk_df = risk_df.merge(enrollment, on="trial_id")

# Normalize
risk_df["deviation_score"] = risk_df["deviation_count"] / risk_df["deviation_count"].max() * 100
risk_df["enrollment_delay"] = 100 - (
    risk_df["enrollment_count"] / risk_df["enrollment_count"].max() * 100
)

# Risk formula
risk_df["risk_score"] = (
    0.4 * risk_df["dropout_rate"] +
    0.3 * risk_df["deviation_score"] +
    0.3 * risk_df["enrollment_delay"]
)

# Categorize risk
def classify(score):
   if score <= 38:
    return "Low Risk"
   elif score <= 42:
    return "Medium Risk"
   return "High Risk"

risk_df["risk_category"] = risk_df["risk_score"].apply(classify)

# Save
risk_df.to_csv("data/trial_risk_scores.csv", index=False)

print(risk_df.sort_values("risk_score", ascending=False))
print("\nRisk scoring completed.")