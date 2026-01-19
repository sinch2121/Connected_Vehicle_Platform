import pandas as pd

PROCESSED_PATH = "data/processed/vehicle_clean.csv"

def store_processed_data(records):
    df = pd.DataFrame([r.dict() for r in records])
    df.to_csv(PROCESSED_PATH, index=False)
