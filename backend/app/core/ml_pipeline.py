import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

from backend.app.services.ml_features import select_ml_features

FEATURE_PATH = "data/processed/vehicle_features.csv"
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "isolation_forest.pkl")

def train_isolation_forest():
    os.makedirs(MODEL_DIR, exist_ok=True)

    df = pd.read_csv(FEATURE_PATH)
    X = select_ml_features(df)

    model = IsolationForest(
        n_estimators=200,
        contamination=0.1,
        random_state=42
    )

    model.fit(X)

    joblib.dump(model, MODEL_PATH)

    return model

def score_anomalies():
    """
    Score vehicle records using trained Isolation Forest.
    """
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError("Model not trained. Train model before scoring.")

    df = pd.read_csv(FEATURE_PATH)
    X = select_ml_features(df)

    model = joblib.load(MODEL_PATH)

    # Isolation Forest outputs:
    #  1  -> normal
    # -1  -> anomaly
    df["anomaly_label"] = model.predict(X)

    # Higher = more normal, Lower = more anomalous
    df["anomaly_score"] = model.decision_function(X)

    OUTPUT_PATH = "data/processed/vehicle_anomaly_scores.csv"
    df.to_csv(OUTPUT_PATH, index=False)

    return df
