from fastapi import FastAPI
from backend.app.api import ingestion
from backend.app.api import features
from backend.app.api import profiling
from backend.app.api import risk


app = FastAPI(
    title="Connected Vehicle Intelligence Platform",
    description="Backend API for connected vehicle data ingestion and analysis",
    version="1.0.0"
)

app.include_router(ingestion.router, prefix="/api")
app.include_router(features.router, prefix="/api")
app.include_router(profiling.router, prefix="/api")
app.include_router(risk.router, prefix="/api")

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "Connected Vehicle Backend is live"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }
