from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import pandas as pd

# Load the trained Decision Tree model
with open('Decision_Tree.pkl', 'rb') as f_in:
    model = pickle.load(f_in)

# Expected features based on model training
expected_features = [
    'Engine_Size_L', 'Mileage_KM', 'Price_USD'
]

# Request schema
class Client(BaseModel):
    Engine_Size_L: float
    Mileage_KM: int
    Price_USD: int

# Create FastAPI app
app = FastAPI()

# Prediction endpoint
@app.post("/predict")
def predict(client: Client):
    # Convert input into a DataFrame to match model format
    data_dict = client.dict()
    df = pd.DataFrame([data_dict], columns=expected_features)

    # Make prediction
    prediction = model.predict(df)[0]

    return {"predicted_sales_classification": prediction}


