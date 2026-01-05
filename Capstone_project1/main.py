from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Load model
with open("XGBoost.pkl", "rb") as f_in:
    model_XGBoost = pickle.load(f_in)

expected_features = [
    "GCS_max", "GCS_mean", "Lactate_min", "Lactate_max", "Lactate_mean",
    "BUN_min", "BUN_mean", "Bilirubin_max", "Bilirubin_mean",
    "AG_MEAN", "AG_MAX", "AG_MEDIAN", "AG_MIN", "AG_STD",
    "SYSBP_MIN", "SYSBP_MEAN", "SYSBP_STD",
    "DIASBP_MIN", "DIASBP_MEAN",
    "AGE",
    "RR_MEAN", "RR_STD", "RR_MAX",
    "TEMP_STD", "TEMP_MIN",
    "HR_MEAN", "HR_MAX",
    "age_adj_comorbidity_score",
]

class Client(BaseModel):
    GCS_max: float = 14.0
    GCS_mean: float = 12.5
    Lactate_min: float = 1.2
    Lactate_max: float = 3.8
    Lactate_mean: float = 2.4
    BUN_min: float = 18.0
    BUN_mean: float = 32.0
    Bilirubin_max: float = 2.1
    Bilirubin_mean: float = 1.4
    AG_MEAN: float = 14.5
    AG_MAX: float = 18.0
    AG_MEDIAN: float = 14.0
    AG_MIN: float = 12.0
    AG_STD: float = 1.9
    SYSBP_MIN: float = 92.0
    SYSBP_MEAN: float = 118.0
    SYSBP_STD: float = 14.0
    DIASBP_MIN: float = 55.0
    DIASBP_MEAN: float = 72.0
    AGE: int = 67
    RR_MEAN: float = 22.0
    RR_STD: float = 4.1
    RR_MAX: float = 30.0
    TEMP_STD: float = 0.6
    TEMP_MIN: float = 36.4
    HR_MEAN: float = 96.0
    HR_MAX: float = 128.0
    age_adj_comorbidity_score: float = 5.0

app = FastAPI()

# ✅ Better local CORS (works reliably)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/predict_XGBoost")
def predict_xgboost(client: Client):
    data_dict = client.dict()
    df = pd.DataFrame([data_dict]).reindex(columns=expected_features)

    prob_mortality = float(model_XGBoost.predict_proba(df)[0, 1])
    pred_class = int(prob_mortality >= 0.5)

    return {
        "model": "XGBoost",
        "predicted_mortality_inhospital": pred_class,
        "mortality_probability": round(prob_mortality, 8),
    }
