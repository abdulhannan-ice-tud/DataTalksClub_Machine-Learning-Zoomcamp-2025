# ICU Mortality Prediction System

## Project Overview

This project implements an **ICU in-hospital mortality prediction system** using clinical features derived from ICU data (inspired by MIMIC-III–style datasets).
A trained **XGBoost model** predicts the probability of in-hospital mortality, which is exposed via a **FastAPI backend** and can be accessed through a simple **HTML-based frontend**.

The project is containerized using **Docker** for easy deployment and reproducibility.

---

## Project Structure

```
FINAL_PROJECT1/
│
├── Dockerfile
├── main.py
├── index.html
├── final_project1.ipynb
├── mimiciii_icu_mortality_features_v1.csv
├── XGBoost.pkl
└── __pycache__/
```

### File Descriptions

* **`final_project1.ipynb`**
  Jupyter Notebook containing:

  * Data loading and preprocessing
  * Model training and evaluation
  * Feature selection and experimentation
  * Saving the trained XGBoost model

* **`mimiciii_icu_mortality_features_v1.csv`**
  Feature-engineered dataset containing aggregated ICU clinical variables and the target:

  * `MORTALITY_INHOSPITAL` (0 = survived, 1 = died)

* **`XGBoost.pkl`**
  Serialized trained XGBoost model used for inference in production.

* **`main.py`**
  FastAPI application that:

  * Loads the trained model
  * Accepts patient feature inputs
  * Returns predicted mortality probability

* **`index.html`**
  Simple frontend interface for interacting with the API and submitting patient features.

* **`Dockerfile`**
  Docker configuration to containerize the application.

---

## Model Details

* **Algorithm:** XGBoost (Gradient Boosting Trees)
* **Task:** Binary classification (In-hospital mortality)
* **Target Variable:** `MORTALITY_INHOSPITAL`
* **Features:**
  Clinical summary statistics including:

  * Vital signs (HR, BP, RR, Temperature)
  * Laboratory values (Lactate, BUN, Bilirubin, Anion Gap)
  * Neurological status (GCS)
  * Demographics (Age, Comorbidity Score)

---

## Tech Stack

* **Python 3.10**
* **XGBoost**
* **scikit-learn**
* **pandas / numpy**
* **FastAPI**
* **Uvicorn**
* **HTML / CSS**
* **Docker**

---

## How to Run the Project

### Option 1: Run Locally (Without Docker)

1. Install dependencies:

   ```bash
   pip install pandas numpy scikit-learn xgboost fastapi uvicorn
   ```

2. Start the FastAPI server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

3. Open in browser:

   ```
   http://localhost:8000
   ```

---

### Option 2: Run Using Docker (Recommended)

1. Build the Docker image:

   ```bash
   docker build -t icu-mortality .
   ```

2. Run the container:

   ```bash
   docker run -p 8000:8000 icu-mortality
   ```

3. Open in browser:

   ```
   http://localhost:8000
   ```

---

## API Usage

### Endpoint

```
POST /predict
```

### Input

JSON containing patient features (numerical values).

### Output

```json
{
  "mortality_probability": 0.27
}
```

---

## Future Improvements

* Add SHAP-based model explainability
* Improve frontend UI/UX
* Add input validation and error handling
* Extend to time-series ICU data
* Deploy on cloud (AWS / GCP / Azure)

---

## License

This project is for **academic and educational purposes**.




