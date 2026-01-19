from fastapi import FastAPI
from backend.app.api import ingestion

app = FastAPI(
    title="Connected Vehicle Intelligence Platform",
    description="Backend API for connected vehicle data ingestion and analysis",
    version="1.0.0"
)

app.include_router(ingestion.router, prefix="/api")

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
