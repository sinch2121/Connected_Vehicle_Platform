from fastapi import APIRouter
from backend.app.core.profiling_pipeline import run_profiling_pipeline

router = APIRouter()

@router.post("/profile/run")
def run_profiling():
    profile = run_profiling_pipeline()
    return {
        "message": "Statistical profiling completed",
        "features_profiled": list(profile.keys())
    }
