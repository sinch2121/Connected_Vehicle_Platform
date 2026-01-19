from fastapi import APIRouter
from backend.app.core.risk_pipeline import run_risk_pipeline

router = APIRouter()

@router.post("/risk/run")
def run_risk_scoring():
    results = run_risk_pipeline()
    return {
        "message": "Baseline risk scoring completed",
        "records_scored": len(results)
    }
