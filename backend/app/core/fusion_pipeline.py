import pandas as pd
import os

RISK_PATH = "data/processed/vehicle_risk_scores.csv"
ANOMALY_PATH = "data/processed/vehicle_anomaly_scores.csv"
OUTPUT_PATH = "data/processed/vehicle_fused_risk.csv"


def fuse_risk_and_anomaly():
    if not os.path.exists(RISK_PATH) or not os.path.exists(ANOMALY_PATH):
        raise RuntimeError("Risk or anomaly data missing")

    risk_df = pd.read_csv(RISK_PATH)
    anomaly_df = pd.read_csv(ANOMALY_PATH)

    df = risk_df.merge(anomaly_df, on="vehicle_id", how="inner")

    # Normalize anomaly score (0–1)
    min_score = df["anomaly_score"].min()
    max_score = df["anomaly_score"].max()

    df["anomaly_norm"] = (
        (df["anomaly_score"] - min_score) /
        (max_score - min_score + 1e-6)
    )

    # Hybrid fusion formula
    df["fused_risk"] = (
        0.6 * df["risk_score"] +
        0.4 * (1 - df["anomaly_norm"])
    )

    def classify(risk):
        if risk < 0.3:
            return "LOW"
        elif risk < 0.6:
            return "MEDIUM"
        elif risk < 0.8:
            return "HIGH"
        return "CRITICAL"

    df["risk_category"] = df["fused_risk"].apply(classify)

    df.to_csv(OUTPUT_PATH, index=False)
    return df
