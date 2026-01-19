import json
import pandas as pd

from backend.app.services.risk_rules import compute_risk_score
from backend.app.utils.json_utils import to_native_types

FEATURE_PATH = "data/processed/vehicle_features.csv"
PROFILE_PATH = "data/processed/statistical_profile.json"
RISK_PATH = "data/processed/vehicle_risk_scores.csv"

def run_risk_pipeline():
    df = pd.read_csv(FEATURE_PATH)

    with open(PROFILE_PATH, "r") as f:
        stats = json.load(f)

    risk_results = []

    for _, row in df.iterrows():
        risk = compute_risk_score(row.to_dict(), stats)
        record = row.to_dict()
        record.update(risk)
        risk_results.append(record)

    risk_df = pd.DataFrame(risk_results)
    risk_df.to_csv(RISK_PATH, index=False)

    return to_native_types(risk_results)
