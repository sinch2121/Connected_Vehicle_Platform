import json
import pandas as pd
from backend.app.services.statistical_profiling import compute_statistical_profile
from backend.app.utils.json_utils import to_native_types

FEATURE_PATH = "data/processed/vehicle_features.csv"
PROFILE_PATH = "data/processed/statistical_profile.json"

def run_profiling_pipeline():
    df = pd.read_csv(FEATURE_PATH)
    profile = compute_statistical_profile(df)

    # ✅ Convert numpy types to native Python types
    profile = to_native_types(profile)

    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=4)

    return profile
