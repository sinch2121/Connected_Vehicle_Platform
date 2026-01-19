import pandas as pd

NUMERIC_COLUMNS = [
    "speed",
    "fuel_consumption",
    "engine_temp",
    "brake_events",
    "fuel_efficiency_score"
]

def compute_statistical_profile(df: pd.DataFrame) -> dict:
    profile = {}

    for col in NUMERIC_COLUMNS:
        if col in df.columns:
            series = df[col]

            profile[col] = {
                "mean": series.mean(),
                "std": series.std(),
                "min": series.min(),
                "max": series.max(),
                "p25": series.quantile(0.25),
                "p50": series.quantile(0.50),
                "p75": series.quantile(0.75),
                "p95": series.quantile(0.95)
            }

    return profile
