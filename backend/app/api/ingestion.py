
from fastapi import APIRouter, UploadFile, File
import shutil
import os

from backend.app.services.data_parser import parse_and_validate_csv
from backend.app.core.data_store import store_processed_data

router = APIRouter()


UPLOAD_DIR = "data/raw"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/ingest")
async def ingest_vehicle_data(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    records, errors = parse_and_validate_csv(file_path)

    # ✅ STORE CLEAN DATA FOR ML PIPELINE
    store_processed_data(records)

    return {
        "total_rows": len(records) + len(errors),
        "valid_rows": len(records),
        "invalid_rows": len(errors),
        "errors": errors[:5]  # show only first 5
    }
