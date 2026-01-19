import pandas as pd
from backend.app.services.feature_engineering import extract_features

PROCESSED_PATH = "data/processed/vehicle_clean.csv"
FEATURE_PATH = "data/processed/vehicle_features.csv"

def run_feature_pipeline():
    df = pd.read_csv(PROCESSED_PATH)
    feature_df = extract_features(df)
    feature_df.to_csv(FEATURE_PATH, index=False)
    return feature_df
