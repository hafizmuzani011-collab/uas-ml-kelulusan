"""Gradio UI application for Student Graduation prediction."""
import gradio as gr
import joblib
import pandas as pd

FEATURES = [
    "Previous qualification (grade)", "Admission grade",
    "Age at enrollment", "Curricular units 1st sem (approved)",
    "Curricular units 1st sem (grade)", "Curricular units 2nd sem (approved)",
    "Curricular units 2nd sem (grade)", "Tuition fees up to date",
    "Scholarship holder", "Debtor"
]

model = joblib.load("models/best_student_graduation_model.joblib")
scaler = joblib.load("models/scaler.joblib")

def make_prediction(*args):
    data = {k: v for k, v in zip(FEATURES, args)}
    df = pd.DataFrame([data])
    scaled = scaler.transform(df)
    pred = model.predict(scaled)[0]
    prob = model.predict_proba(scaled)[0] if hasattr(model, "predict_proba") else [0.0, 1.0] if pred == 1 else [1.0, 0.0]
    
    res_label = "Lulus Tepat Waktu" if pred == 1 else "Tidak Lulus Tepat Waktu"
    confidence = prob[1] if pred == 1 else prob[0]
    
    disclaimer = "\n\n⚠️ Disclaimer: Aplikasi ini hanya berfungsi sebagai *decision support* untuk membantu institusi melakukan deteksi dini, bukan sebagai penentu kelulusan akhir."
    return f"Hasil Prediksi: {res_label} (Confidence: {confidence:.2%}){disclaimer}"

inputs = [
    gr.Number(label="Previous qualification (grade)", value=120.0),
    gr.Number(label="Admission grade", value=120.0),
    gr.Slider(label="Age at enrollment", minimum=17, maximum=70, step=1, value=20),
    gr.Number(label="Curricular units 1st sem (approved)", value=6),
    gr.Number(label="Curricular units 1st sem (grade)", value=12.0),
    gr.Number(label="Curricular units 2nd sem (approved)", value=6),
    gr.Number(label="Curricular units 2nd sem (grade)", value=12.0),
    gr.Radio(label="Tuition fees up to date (1=Yes, 0=No)", choices=[0, 1], value=1),
    gr.Radio(label="Scholarship holder (1=Yes, 0=No)", choices=[0, 1], value=0),
    gr.Radio(label="Debtor (1=Yes, 0=No)", choices=[0, 1], value=0)
]

demo = gr.Interface(
    fn=make_prediction,
    inputs=inputs,
    outputs=gr.Textbox(label="Hasil Analisis & Prediksi"),
    title="Prediksi Kelulusan Mahasiswa — UAS ML",
    description="Interface pendukung keputusan berbasis Machine Learning (SVM RBF)."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
