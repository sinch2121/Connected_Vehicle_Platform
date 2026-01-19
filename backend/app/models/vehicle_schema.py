from pydantic import BaseModel
from datetime import datetime

class VehicleTelemetry(BaseModel):
    vehicle_id: str
    timestamp: datetime
    speed: float
    fuel_consumption: float
    engine_temp: float
    brake_events: int
    road_type: str
