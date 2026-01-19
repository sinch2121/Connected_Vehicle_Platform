import pandas as pd

def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create derived features from raw vehicle telemetry.
    """

    df = df.copy()

    # Speed behavior
    df["speed_squared"] = df["speed"] ** 2

    # Thermal stress indicator
    df["engine_temp_high"] = df["engine_temp"] > 100

    # Aggressive braking indicator
    df["aggressive_braking"] = df["brake_events"] >= 3

    # Fuel inefficiency proxy
    df["fuel_efficiency_score"] = df["speed"] / (df["fuel_consumption"] + 1e-5)

    return df
