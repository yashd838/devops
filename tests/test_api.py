import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_predict_endpoint():
    payload = {
        "Warehouse_block": "D",
        "Mode_of_Shipment": "Flight",
        "Customer_care_calls": 4,
        "Customer_rating": 2,
        "Cost_of_the_Product": 177,
        "Prior_purchases": 3,
        "Product_importance": "low",
        "Gender": "F",
        "Discount_offered": 44,
        "Weight_in_gms":1233
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json()["prediction"] in [0, 1]
