import pandas as pd

ML_FEATURE_COLUMNS = [
    "speed",
    "fuel_consumption",
    "engine_temp",
    "brake_events",
    "fuel_efficiency_score"
]

def select_ml_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Select and clean features for ML models.
    """
    return df[ML_FEATURE_COLUMNS].copy()
