from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load trained model
model = joblib.load("model.pkl")

# Define request body schema
class Shipment(BaseModel):
    Warehouse_block: str
    Mode_of_Shipment: str
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: float
    Prior_purchases: int
    Product_importance: str
    Gender: str
    Discount_offered: float
    Weight_in_gms: float

# Encoding mappings (must match training)
warehouse_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}
mode_map = {'Flight': 0, 'Road': 1, 'Ship': 2}
importance_map = {'low': 1, 'medium': 2, 'high': 0}
gender_map = {'F': 0, 'M': 1}

@app.post("/predict")
def predict(data: Shipment):
    try:
        input_data = [
            warehouse_map[data.Warehouse_block],
            mode_map[data.Mode_of_Shipment],
            data.Customer_care_calls,
            data.Customer_rating,
            data.Cost_of_the_Product,
            data.Prior_purchases,
            importance_map[data.Product_importance],
            gender_map[data.Gender],
            data.Discount_offered,
            data.Weight_in_gms
        ]
        prediction = model.predict([input_data])
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
