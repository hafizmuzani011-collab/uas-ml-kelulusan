# PANDUAN TANYA JAWAB UAS MACHINE LEARNING (CONTOH Q&A DOSEN)

Gunakan jawaban taktis, percaya diri, dan berbasis data empiris.

---

### Q1: Kenapa menggunakan metrik F1-Macro atau Balanced Accuracy sebagai scoring utama, bukan Accuracy?
* **Jawaban:** "Karena terdapat ketidakseimbangan kelas (class imbalance) pada dataset (61% Graduate vs 39% Dropout). Jika menggunakan akurasi biasa, model yang memprediksi mayoritas saja bisa terlihat bagus padahal gagal mendeteksi mahasiswa dropout. F1-Macro menghitung rata-rata F1-score kedua kelas secara setara tanpa memedulikan jumlah sampelnya, sehingga menjamin model adil dalam memprediksi mahasiswa lulus maupun dropout."

### Q2: Bagaimana Anda memastikan tidak terjadi data leakage (kebocoran data) selama preprocessing?
* **Jawaban:** "Kami menerapkan 3 aturan ketat:
  1. Train-Test Split (80/20) dilakukan di awal sebelum preprocessing apa pun.
  2. Oversampling dengan SMOTE hanya dilakukan pada training set. Data test tidak boleh di-SMOTE agar evaluasi tetap mencerminkan data riil.
  3. Scaling (`StandardScaler`) dan feature selection (`Mutual Information`) di-fit hanya menggunakan data training, kemudian data test ditransform menggunakan parameter dari training."

### Q3: Kenapa model SVM (RBF) Baseline terpilih sebagai yang terbaik dibandingkan model yang di-optimize?
* **Jawaban:** "Secara empiris (lihat tabel eksperimen), SVM Baseline menghasilkan F1-Macro tertinggi (0.8869) dan akurasi (0.8939). Kernel RBF mampu menangkap hubungan non-linear yang kompleks dari data akademik mahasiswa, dan parameter `class_weight='balanced'` menangani imbalance secara internal. Sementara SVM Optimized (F1-Macro 0.8841) yang menggunakan SMOTE + seleksi 8 fitur mengalami sedikit degradasi performa karena penghapusan 2 fitur penting."

### Q4: Jelaskan kegunaan SMOTE dan kenapa ia penting dalam project ini?
* **Jawaban:** "SMOTE (Synthetic Minority Over-sampling Technique) digunakan untuk membuat sampel sintetis baru pada kelas minoritas (Dropout) agar seimbang (50:50) dengan kelas mayoritas (Graduate) di data training. Ini penting agar algoritma machine learning (terutama KNN dan SVM) tidak condong memprediksi kelas mayoritas dan meningkatkan sensitivitas (recall) terhadap mahasiswa yang berisiko dropout."

### Q5: Apa kesimpulan penting dari Error Analysis yang Anda lakukan?
* **Jawaban:** "Model sering melakukan kesalahan prediksi (False Positive) pada mahasiswa yang sebenarnya dropout tetapi diprediksi lulus. Analisis data menunjukkan mahasiswa tersebut memiliki nilai akademik (SKS & IPK) semester 1 & 2 yang tinggi. Mereka dropout bukan karena masalah akademis, melainkan faktor eksternal (seperti masalah ekonomi atau keluarga) yang tidak terekam dalam dataset. Ini membuktikan batasan model ML yang hanya bisa memprediksi berdasarkan riwayat akademik yang diinput."

### Q6: Bagaimana relevansi etika (CPL-10) diimplementasikan pada aplikasi Streamlit/Gradio Anda?
* **Jawaban:** "Model diposisikan hanya sebagai **Decision Support System (sistem pendukung keputusan)**, bukan pengambil keputusan final. Di aplikasi, kami menyertakan *disclaimer* etis yang menegaskan bahwa keputusan akhir evaluasi kelayakan akademik tetap di tangan dosen wali dan program studi. Model tidak boleh digunakan untuk men-drop out mahasiswa secara otomatis."

### Q7: Jika diberikan waktu lebih, apa rekomendasi Anda untuk pengembangan sistem ini ke depan?
* **Jawaban:** "1. Menggunakan data lokal mahasiswa Udinus untuk validasi silang (cross-validation).
  2. Mencoba model ensemble tingkat lanjut seperti XGBoost atau LightGBM.
  3. Menerapkan XAI (Explainable AI) menggunakan SHAP atau LIME agar dosen wali tahu *kenapa* mahasiswa tertentu diprediksi dropout (misalnya karena IPK semester 2 rendah)."
