import pandas as pd
from backend.app.models.vehicle_schema import VehicleTelemetry

def parse_and_validate_csv(file_path: str):
    df = pd.read_csv(file_path)

    validated_records = []
    errors = []

    for idx, row in df.iterrows():
        try:
            record = VehicleTelemetry(
                vehicle_id=row["vehicle_id"],
                timestamp=row["timestamp"],
                speed=row["speed"],
                fuel_consumption=row["fuel_consumption"],
                engine_temp=row["engine_temp"],
                brake_events=row["brake_events"],
                road_type=row["road_type"]
            )
            validated_records.append(record)
        except Exception as e:
            errors.append({"row": idx, "error": str(e)})

    return validated_records, errors
