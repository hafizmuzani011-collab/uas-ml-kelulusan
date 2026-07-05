import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import os

st.set_page_config(page_title="Prediksi Kelulusan", layout="wide")

MODEL_PATH = "models/best_student_graduation_model.joblib"
SCALER_PATH = "models/scaler.joblib"
DATA_PATH = "data/dataset_kelulusan.csv"
RESULTS_PATH = "reports/classification_reports.json"

@st.cache_resource
def load_artifacts():
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        return model, scaler
    except Exception as e:
        st.error(f"Error load model/scaler: {e}")
        return None, None

model, scaler = load_artifacts()

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

page = st.sidebar.selectbox("Pilih Halaman", ["Prediksi", "Dashboard Data", "Performa Model", "Penjelasan Model"])

if page == "Prediksi":
    st.title("Prediksi Kelulusan Mahasiswa")
    st.write("Masukkan data mahasiswa di sidebar untuk melihat prediksi kelulusan.")

    st.sidebar.header("Input Data Mahasiswa")
    
    # 8 used features
    prev_grade = st.sidebar.number_input('Previous qualification (grade)', min_value=0.0, max_value=200.0, value=120.0)
    admission_grade = st.sidebar.number_input('Admission grade', min_value=0.0, max_value=200.0, value=120.0)
    age = st.sidebar.number_input('Age at enrollment', min_value=15, max_value=80, value=20)
    cu_1_app = st.sidebar.number_input('Curricular units 1st sem (approved)', min_value=0, max_value=30, value=5)
    cu_1_grade = st.sidebar.number_input('Curricular units 1st sem (grade)', min_value=0.0, max_value=20.0, value=12.0)
    cu_2_app = st.sidebar.number_input('Curricular units 2nd sem (approved)', min_value=0, max_value=30, value=5)
    cu_2_grade = st.sidebar.number_input('Curricular units 2nd sem (grade)', min_value=0.0, max_value=20.0, value=12.0)
    tuition = st.sidebar.selectbox('Tuition fees up to date', [0, 1], index=1)
    scholarship = st.sidebar.selectbox('Scholarship holder', [0, 1], index=0)
    debtor = st.sidebar.selectbox('Debtor', [0, 1], index=0)

    if st.sidebar.button("Prediksi Sekarang"):
        if model and scaler:
            input_df = pd.DataFrame([[
                prev_grade, admission_grade, age, cu_1_app, cu_1_grade,
                cu_2_app, cu_2_grade, tuition, scholarship, debtor
            ]], columns=SCALER_FEATURES)
            input_scaled = scaler.transform(input_df)
            
            pred = model.predict(input_scaled)[0]
            
            try:
                proba = model.predict_proba(input_scaled)[0]
                max_prob = max(proba)
            except:
                max_prob = None
                
            if pred == 1:
                st.success("🎉 Prediksi: **Lulus Tepat Waktu**")
            else:
                st.error("⚠️ Prediksi: **Tidak Lulus / Drop Out**")
                
            if max_prob:
                st.info(f"Probabilitas/Kepercayaan Model: {max_prob:.2%}")
                
            st.caption("ℹ️ Hasil prediksi ini hanya bersifat *decision support* — bukan keputusan final. Keputusan akhir tetap berada pada pihak institusi.")

elif page == "Dashboard Data":
    st.title("Dashboard Data Dataset")
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH, sep=';')
        st.write(f"Total Data: {len(df)} baris")
        st.dataframe(df.head())
        
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Distribusi Target")
            st.bar_chart(df['Target'].value_counts())
        with col2:
            st.subheader("Statistik Deskriptif")
            st.dataframe(df[SCALER_FEATURES].describe())
    else:
        st.warning("Data tidak ditemukan.")

elif page == "Performa Model":
    st.title("Visualisasi Metrik Model")
    if os.path.exists(RESULTS_PATH):
        with open(RESULTS_PATH, 'r') as f:
            results = json.load(f)
            
        df_res = pd.DataFrame(results)
        st.dataframe(df_res[['Model', 'Accuracy', 'F1-Score (Macro)', 'Train Time (s)']])
        
        st.subheader("Akurasi Model")
        st.bar_chart(df_res.set_index('Model')['Accuracy'])
    else:
        st.warning("Hasil eksperimen tidak ditemukan.")

elif page == "Penjelasan Model":
    st.title("Penjelasan Model")
    st.write("""
    ### Support Vector Machine (SVM)
    Model terbaik yang terpilih adalah SVM. SVM bekerja dengan mencari hyperplane (garis/bidang pembatas) terbaik 
    yang dapat memisahkan data mahasiswa yang Lulus dan Tidak Lulus dengan margin (jarak) paling besar.
    
    ### Fitur Utama
    Model menggunakan 8 fitur terpenting untuk prediksi:
    1. **Curricular units 2nd sem (approved)**: Jumlah SKS/MK lulus semester 2
    2. **Curricular units 1st sem (approved)**: Jumlah SKS/MK lulus semester 1
    3. **Curricular units 2nd sem (grade)**: Nilai rata-rata semester 2
    4. **Curricular units 1st sem (grade)**: Nilai rata-rata semester 1
    5. **Tuition fees up to date**: Status pembayaran SPP (1=Lunas)
    6. **Scholarship holder**: Penerima beasiswa (1=Ya)
    7. **Age at enrollment**: Usia saat mendaftar
    8. **Admission grade**: Nilai masuk
    """)
