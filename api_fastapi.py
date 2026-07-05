from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
import os

app = FastAPI(title="Student Graduation Prediction API")

MODEL_PATH = "models/best_student_graduation_model.joblib"
SCALER_PATH = "models/scaler.joblib"

# Load artifacts
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    model = None
    scaler = None
    print(f"Failed to load model/scaler: {e}")

SCALER_FEATURES = [
    'Previous qualification (grade)',
    'Admission grade',
    'Age at enrollment',
    'Curricular units 1st sem (approved)',
    'Curricular units 1st sem (grade)',
    'Curricular units 2nd sem (approved)',
    'Curricular units 2nd sem (grade)',
    'Tuition fees up to date',
    'Scholarship holder',
    'Debtor'
]

class StudentData(BaseModel):
    cu_2_approved: int
    cu_1_approved: int
    cu_2_grade: float
    cu_1_grade: float
    tuition_fees_up_to_date: int
    scholarship_holder: int
    age_at_enrollment: int
    admission_grade: float
    prev_qualification_grade: float = 120.0
    debtor: int = 0

@app.get("/")
def read_root():
    return {"message": "API Prediksi Kelulusan Aktif. POST ke /predict."}

@app.post("/predict")
def predict(data: StudentData):
    if not model or not scaler:
        raise HTTPException(status_code=500, detail="Model/Scaler not loaded.")
        
    # DataFrame 10 fitur → scaler → predict
    input_df = pd.DataFrame([[
        data.prev_qualification_grade,
        data.admission_grade,
        data.age_at_enrollment,
        data.cu_1_approved,
        data.cu_1_grade,
        data.cu_2_approved,
        data.cu_2_grade,
        data.tuition_fees_up_to_date,
        data.scholarship_holder,
        data.debtor
    ]], columns=SCALER_FEATURES)
    
    input_scaled = scaler.transform(input_df)
    pred = int(model.predict(input_scaled)[0])
    
    try:
        proba = model.predict_proba(input_scaled)[0].tolist()
        max_prob = max(proba)
    except:
        proba = None
        max_prob = None
        
    status = "Lulus Tepat Waktu" if pred == 1 else "Tidak Lulus"
    
    return {
        "prediction": pred,
        "status": status,
        "probability": max_prob
    }
