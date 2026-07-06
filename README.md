# Proyek UAS Pembelajaran Mesin - Prediksi Kelulusan Mahasiswa

Proyek ini merupakan implementasi model Machine Learning untuk klasifikasi kelayakan kelulusan mahasiswa ("Lulus Tepat Waktu" vs "Tidak Lulus/Dropout") menggunakan dataset dari UCI Machine Learning Repository. Proyek disusun untuk memenuhi kriteria evaluasi UAS Pembelajaran Mesin berbasis Outcome-Based Education (OBE).

## Identitas Mahasiswa & Kelompok
* **Nama:** Na'ilah Azfa Zarqarida
* **NIM:** A11.2024.15549
* **Kelompok:** A11.4401 & A11.4410
* **Universitas:** Universitas Dian Nuswantoro (UDINUS)
* **Semester:** Genap 2025/2026

---

## 📂 Struktur Repositori

Repositori ini telah ditata rapi mengikuti spesifikasi pengumpulan UAS:

```text
uas-ml-kelulusan-A11.2024.15549-A11.4401_A11.4410/
├── data/
│   ├── dataset_kelulusan.csv     # Dataset biner 3.630 baris (Graduate vs Dropout)
│   ├── data_dictionary.md        # Deskripsi 35 kolom fitur dan tipe datanya
│   └── source_dataset.md         # Sumber referensi (UCI URL, DOI, Lisensi)
├── notebooks/
│   └── uas_ml_graduation_knn_nb_svm_optimization.ipynb # Notebook utama (1 cell code)
├── src/
│   ├── data_generator.py         # Loader dataset, filtering target, & generator data
│   ├── ml_core.py                # Pipeline preprocessing, training, & validasi silang
│   ├── train.py                  # CLI Script untuk melatih dan mengevaluasi model
│   └── predict.py                # CLI Script untuk melakukan prediksi dari input JSON
├── models/
│   ├── best_student_graduation_model.joblib # Model SVM RBF Baseline terbaik (F1=0.887)
│   └── scaler.joblib             # File scaler StandardScaler ter-fit
├── reports/
│   ├── audit_dataset.json        # Laporan validitas data (duplikat, missing value)
│   ├── all_experiment_results.csv # Tabel metrik 6 varian model (baseline vs optimized)
│   ├── classification_reports.json # Laporan metrik evaluasi lengkap per kelas
│   ├── target_distribution.png   # Visualisasi sebaran kelas Graduate vs Dropout
│   ├── feature_importance_mi.png # Bar chart fitur terpenting Mutual Information (top 10)
│   ├── performance_comparison.png # Grafik komparasi F1-Macro 6 model
│   ├── roc_curve_comparison.png  # Kurva ROC perbandingan 6 model dengan nilai AUC
│   └── confusion_matrix.png      # Matriks kebingungan model terbaik (SVM)
├── app_streamlit.py              # Aplikasi antarmuka interaktif utama (Streamlit)
├── app_gradio.py                 # Antarmuka pengujian cepat alternatif (Gradio)
├── api_fastapi.py                # API Backend inferensi siap produksi (FastAPI)
├── requirements.txt              # Daftar dependensi modul Python yang digunakan
├── README.md                     # Panduan navigasi proyek ini
├── presentation/
│   ├── presentasi_uas_ml.pdf     # Slide presentasi dalam format PDF
│   ├── presentasi_uas_ml.pptx    # Slide presentasi PowerPoint akademis bergambar
│   ├── SKRIP_VIDEO_PRESENTASI.md # Panduan naskah presentasi video (±10 menit)
│   └── TIPS_TANYA_JAWAB_DOSEN.md # Kumpulan prediksi Q&A akademis penguji UAS
└── report/
    └── laporan_uas_ml_kelulusan.pdf # Dokumen Laporan Akhir Akademik UAS (14 halaman)
```

---

## 🚀 Cara Menjalankan Program

### 1. Inisialisasi Environment (zsh/bash/cmd)
Pastikan Anda berada di direktori root proyek ini, kemudian jalankan:
```bash
# Membuat virtual environment
python3 -m venv .venv

# Mengaktifkan virtual environment
source .venv/bin/activate  # di macOS/Linux/Git Bash
# ATAU di Windows CMD: .venv\Scripts\activate

# Install dependensi
pip install -r requirements.txt
```

### 2. Menjalankan Aplikasi Antarmuka (Streamlit UI)
Streamlit menyediakan visualisasi performa model, dashboard data, penjelasan model, dan form prediksi interaktif:
```bash
streamlit run app_streamlit.py
```

### 3. Menjalankan Aplikasi Alternatif (Gradio UI)
Gradio menyediakan antarmuka minimalis untuk tes prediksi:
```bash
python app_gradio.py
```

### 4. Menjalankan Backend API (FastAPI)
FastAPI mengekspos endpoint `/predict` berbasis JSON untuk kebutuhan integrasi (SIAKAD):
```bash
uvicorn api_fastapi:app --reload
```
Akses dokumentasi interaktif Swagger API di `http://127.0.0.1:8000/docs`.

### 5. Melatih Model Baru Lewat CLI (train.py)
Jika ingin melakukan training ulang semua varian model (KNN, NB, SVM baseline & optimized):
```bash
python src/train.py
```

### 6. Melakukan Prediksi Lewat CLI (predict.py)
Jalankan prediksi cepat menggunakan input JSON lokal:
```bash
python src/predict.py --input '{"Previous qualification (grade)": 120.0, "Admission grade": 120.0, "Age at enrollment": 20, "Curricular units 1st sem (approved)": 5, "Curricular units 1st sem (grade)": 12.0, "Curricular units 2nd sem (approved)": 5, "Curricular units 2nd sem (grade)": 12.0, "Tuition fees up to date": 1, "Scholarship holder": 0, "Debtor": 0}'
```

---

## 🏆 Ringkasan Hasil Eksperimen

Metrik utama yang dievaluasi adalah **F1-Macro** demi menjamin keadilan model pada dataset yang tidak seimbang. 

| Model Klasifikasi | F1-Macro | Accuracy | Keterangan |
|---|---|---|---|
| K-Nearest Neighbors (Baseline) | 0.869 | 0.879 | K=5, Euclidean |
| Naive Bayes (Baseline) | 0.829 | 0.844 | GaussianNB |
| **Support Vector Machine (Baseline) 🏆** | **0.887** | **0.894** | **Best Model (Kernel RBF)** |
| K-Nearest Neighbors (Optimized) | 0.876 | 0.884 | GridSearchCV (K=9) |
| Naive Bayes (Optimized) | 0.838 | 0.853 | Tuning var_smoothing |
| Support Vector Machine (Optimized) | 0.884 | 0.891 | GridSearchCV |

*Catatan: SVM Baseline dengan parameter pembobotan kelas penyeimbang internal (class_weight='balanced') memberikan performa F1-Macro tertinggi (0.8869) dengan AUC sebesar 0.94.*

---

## 🛡️ Desain Etis dan Disclaimer
Sesuai dengan capaian pembelajaran OBE (CPL-10), seluruh antarmuka aplikasi dan API dalam proyek ini dirancang sebagai **Decision Support System (Sistem Pendukung Keputusan)**. Model AI ini tidak diperbolehkan secara otomatis mengeksekusi status kelayakan akademik mahasiswa (dropout). Keputusan akhir administratif dan akademis secara mutlak harus divalidasi oleh otoritas pendidik (Dosen Wali/Kaprodi) guna memelihara keadilan dan tanggung jawab sosial AI.
