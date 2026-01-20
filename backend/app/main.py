from fastapi import FastAPI
from backend.app.api import ingestion
from backend.app.api import features
from backend.app.api import profiling
from backend.app.api import risk
from backend.app.api import ml
from backend.app.api import fusion
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Connected Vehicle Intelligence Platform",
    description="Backend API for connected vehicle data ingestion and analysis",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(ingestion.router, prefix="/api")
app.include_router(features.router, prefix="/api")
app.include_router(profiling.router, prefix="/api")
app.include_router(risk.router, prefix="/api")
app.include_router(ml.router, prefix="/api")
app.include_router(fusion.router, prefix="/api")

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
