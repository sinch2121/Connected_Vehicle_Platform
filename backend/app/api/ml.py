from fastapi import APIRouter
from backend.app.core.ml_pipeline import train_isolation_forest, score_anomalies

router = APIRouter()

@router.post("/ml/train")
def train_model():
    train_isolation_forest()
    return {
        "message": "Isolation Forest model trained successfully"
    }

@router.post("/ml/score")
def score_model():
    df = score_anomalies()
    return {
        "message": "Anomaly scoring completed",
        "records_scored": len(df)
    }
