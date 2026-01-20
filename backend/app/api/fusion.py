from fastapi import APIRouter
from backend.app.core.fusion_pipeline import fuse_risk_and_anomaly

router = APIRouter()

@router.post("/fusion/run")
def run_fusion():
    df = fuse_risk_and_anomaly()
    return {
        "message": "Hybrid fusion completed",
        "records_fused": len(df)
    }
