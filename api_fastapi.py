"""FastAPI backend for student graduation prediction."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import numpy as np
import os

app = FastAPI(title="Prediksi Kelulusan Mahasiswa — API", version="1.0.0")

MODEL_PATH = "models/best_student_graduation_model.joblib"
SCALER_PATH = "models/scaler.joblib"

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
    """Input data for student graduation prediction."""
    prev_qualification_grade: float = Field(default=120.0, ge=0, le=200, description="Nilai kualifikasi sebelumnya (0-200)")
    admission_grade: float = Field(default=120.0, ge=0, le=200, description="Nilai masuk perguruan tinggi (0-200)")
    age_at_enrollment: int = Field(default=20, ge=17, le=70, description="Usia saat mendaftar")
    cu_1_approved: int = Field(default=6, ge=0, le=30, description="Jumlah SKS lulus Semester 1")
    cu_1_grade: float = Field(default=12.0, ge=0, le=20, description="IP Semester 1 (0-20)")
    cu_2_approved: int = Field(default=6, ge=0, le=30, description="Jumlah SKS lulus Semester 2")
    cu_2_grade: float = Field(default=12.0, ge=0, le=20, description="IP Semester 2 (0-20)")
    tuition_fees_up_to_date: int = Field(default=1, ge=0, le=1, description="Status pembayaran UKT (1=Lancar, 0=Tunggakan)")
    scholarship_holder: int = Field(default=0, ge=0, le=1, description="Penerima beasiswa (1=Ya, 0=Tidak)")
    debtor: int = Field(default=0, ge=0, le=1, description="Status tunggakan (1=Ada tunggakan, 0=Tidak ada)")


@app.get("/")
def read_root():
    return {
        "message": "API Prediksi Kelulusan Mahasiswa aktif.",
        "docs": "/docs",
        "endpoints": {
            "GET /": "Informasi API",
            "POST /predict": "Prediksi kelulusan mahasiswa"
        }
    }


@app.post("/predict")
def predict(data: StudentData):
    """Predict whether a student will graduate on time."""
    if not model or not scaler:
        raise HTTPException(status_code=500, detail="Model/Scaler tidak dapat dimuat.")

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
    status = "Lulus Tepat Waktu" if pred == 1 else "Tidak Lulus"

    try:
        proba = model.predict_proba(input_scaled)[0].tolist()
        confidence = proba[1] if pred == 1 else proba[0]
    except AttributeError:
        proba = None
        confidence = None

    return {
        "prediction": pred,
        "status": status,
        "confidence": confidence,
        "features": {
            f.name: getattr(data, f.name) for f in StudentData.__fields__.values()
        }
    }
