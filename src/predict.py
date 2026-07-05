"""CLI prediction script — load model + predict from input JSON."""
import sys, json
import joblib
import pandas as pd

FEATURES = [
    "Previous qualification (grade)", "Admission grade",
    "Age at enrollment", "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)", "Curricular units 2nd sem (approved)",
    "Curricular units 2nd sem (grade)", "Tuition fees up to date",
    "Scholarship holder", "Debtor"
]

def predict(input_dict: dict, model_path="models"):
    model = joblib.load(f"{model_path}/best_student_graduation_model.joblib")
    scaler = joblib.load(f"{model_path}/scaler.joblib")
    df = pd.DataFrame([{k: input_dict[k] for k in FEATURES}])
    scaled = scaler.transform(df)
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0].tolist() if hasattr(model, "predict_proba") else None
    return {"prediction": int(pred), "label": "Lulus Tepat Waktu" if pred == 1 else "Tidak Lulus Tepat Waktu", "probabilities": prob}

if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file) as f:
        data = json.load(f)
    print(json.dumps(predict(data), indent=2))
