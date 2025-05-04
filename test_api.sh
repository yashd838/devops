#!/bin/bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
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
}'
