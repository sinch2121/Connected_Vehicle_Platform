from fastapi import APIRouter
from backend.app.core.feature_pipeline import run_feature_pipeline

router = APIRouter()

@router.post("/features/run")
def run_features():
    df = run_feature_pipeline()
    return {
        "rows_processed": len(df),
        "message": "Feature extraction completed"
    }
