# SKRIP VIDEO PRESENTASI UAS MACHINE LEARNING
# Durasi: ±10 menit (1 menit per slide)
# Pembicara: Na'ilah Azfa Zarqarida (A11.2024.15549) / Hafizh Muzani

---

## SLIDE 1 — JUDUL (±45 detik)

"Assalamualaikum Warahmatullahi Wabarakatuh. 

Perkenalkan, nama saya Na'ilah Azfa Zarqarida, NIM A11.2024.15549, dari kelompok A11.4401 dan A11.4410. 

Pada kesempatan ini, saya akan mempresentasikan UAS mata kuliah Pembelajaran Mesin dengan judul: Prediksi Kelulusan Mahasiswa Menggunakan Machine Learning — studi kasus dataset UCI Student Dropout and Academic Success."

---

## SLIDE 2 — LATAR BELAKANG & MASALAH (±1 menit)

"Latar belakang penelitian ini adalah tingginya angka dropout mahasiswa di perguruan tinggi Portugal yang tercatat dalam dataset UCI. Dari 4.424 mahasiswa, sekitar 39% mengalami dropout.

Masalah ini sangat krusial karena dropout berdampak pada Indikator Kinerja Utama institusi, pemborosan sumber daya, dan masa depan mahasiswa itu sendiri.

Tujuan project ini adalah membangun sistem prediksi dini yang bisa membantu institusi mengidentifikasi mahasiswa berisiko dropout SEBELUM terlambat, sehingga intervensi bisa dilakukan lebih awal.

Sesuai prinsip OBE atau Outcome-Based Education, tujuan pembelajaran yang dicapai adalah CPL-8 yaitu keterampilan analitik machine learning, dan CPL-10 yaitu tanggung jawab etis dalam penggunaan teknologi."

---

## SLIDE 3 — DATASET & PREPROCESSING (±1 menit 15 detik)

"Dataset yang digunakan berasal dari UCI Machine Learning Repository, dengan judul Predict Students Dropout and Academic Success. Link-nya ada di laporan dan di repository GitHub kami.

Dataset awalnya berisi 4.424 baris dan 37 kolom fitur. Kami melakukan filtering: menghapus mahasiswa dengan status Enrolled, sehingga menyisakan 3.630 data untuk klasifikasi biner: Graduate atau Dropout.

Preprocessing yang dilakukan meliputi: pertama, seleksi 10 fitur terbaik berdasarkan domain knowledge dan skor Mutual Information. Kedua, train-test split 80-20 stratified. Ketiga, StandardScaler untuk normalisasi — penting agar KNN dan SVM tidak bias ke fitur bernilai besar. Dan keempat, SMOTE untuk menyeimbangkan data latih agar distribusi kelas 1 dan 0 menjadi 50:50.

Yang penting, SMOTE dipasang HANYA pada data latih, bukan data test, untuk mencegah data leakage."

---

## SLIDE 4 — DESAIN EKSPERIMEN (±1 menit)

"Desain eksperimen kami menggunakan 3 model baseline: KNN dengan K=5, Naive Bayes Gaussian, dan SVM dengan kernel RBF dan class_weight balanced.

Untuk optimasi, kami menerapkan 4 strategi: pertama, Hyperparameter Tuning menggunakan GridSearchCV. Kedua, Cross-Validation Stratified K-Fold dengan K=5. Ketiga, Feature Selection menggunakan Mutual Information. Dan keempat, Class Imbalance Handling menggunakan SMOTE.

Scoring utama yang digunakan adalah F1-Macro, bukan accuracy, karena F1-Macro lebih adil untuk mengevaluasi performa di kedua kelas, terutama saat data tidak seimbang."

---

## SLIDE 5 — HASIL EKSPERIMEN (±1 menit 30 detik)

"Berikut hasil perbandingan 6 model: baseline dan optimized.

Untuk KNN, F1-Macro naik dari 0.869 menjadi 0.876 setelah optimasi — peningkatan kecil.

Untuk Naive Bayes, F1-Macro naik dari 0.829 menjadi 0.838 — peningkatan juga kecil.

Untuk SVM Baseline, F1-Macro adalah 0.887 dengan akurasi 89.4%. Ini adalah skor TERTINGGI dari semua model.

SVM Optimized sedikit turun ke 0.884, artinya SVM baseline sudah sangat optimal tanpa perlu tuning berlebihan.

Model terbaik: SVM Baseline dengan F1-Macro 0.887 dan Balanced Accuracy 88.1%.

Kenapa SVM menang? Karena kernel RBF mampu menangkap pola non-linear antar fitur mahasiswa, dan parameter class_weight='balanced' sudah menangani ketidakseimbangan kelas secara built-in."

---

## SLIDE 6 — ERROR ANALYSIS (±1 menit)

"Kami juga melakukan error analysis untuk memahami kelemahan model.

Dari confusion matrix, model menghasilkan 50 False Positive — yaitu mahasiswa dropout yang salah diprediksi sebagai lulus. Dan 27 False Negative — mahasiswa lulus yang salah diprediksi sebagai dropout.

Pola kesalahan yang kami temukan: mahasiswa dropout yang punya SKS semester 1-2 cukup tinggi sering lolos prediksi model. Ini karena fitur SKS adalah prediktor kuat, sehingga ketika dropout terjadi karena alasan non-akademik — misalnya masalah ekonomi atau keluarga — model tidak bisa mendeteksinya.

Ini menjadi insight penting: model machine learning hanya bisa menangkap pola dari data yang tersedia, dan tidak bisa memprediksi alasan di luar data."

---

## SLIDE 7 — PEMBAHASAN & TRADE-OFF (±1 menit)

"Trade-off utama yang kami identifikasi: antara akurasi, kompleksitas, dan interpretabilitas.

SVM dengan kernel RBF memiliki akurasi tertinggi, tapi kurang interpretable dibanding Naive Bayes yang sangat sederhana.

KNN ada di tengah — cukup akurat tapi sensitif terhadap K dan distribusi data.

Implikasi untuk institusi: model ini bisa dipasang sebagai early warning system. Mahasiswa yang diprediksi berisiko dropout bisa diberikan intervensi lebih awal — misalnya konseling akademik, bimbingan, atau bantuan finansial.

Tapi penting diingat: ini adalah DECISION SUPPORT, bukan keputusan final. Keputusan tetap berada pada pihak institusi dan mempertimbangkan faktor-faktor di luar data."

---

## SLIDE 8 — DESAIN APLIKASI (±1 menit)

"Aplikasi kami dibangun dengan 2 interface: Streamlit sebagai UI utama dan FastAPI sebagai backend API.

Di Streamlit, terdapat 4 halaman: pertama, halaman Prediksi — pengguna memasukkan 10 fitur mahasiswa di sidebar, lalu klik tombol prediksi, dan hasilnya berupa kelas prediksi beserta confidence score.

Kedua, halaman Dashboard Data — menampilkan distribusi target dan statistik deskriptif dataset.

Ketiga, halaman Performa Model — menampilkan tabel perbandingan 6 model dan grafik bar chart.

Keempat, halaman Penjelasan Model — menjelaskan cara kerja SVM dalam bahasa Indonesia yang mudah dipahami.

Semua halaman sudah dilengkapi disclaimer etis: bahwa aplikasi ini hanya bersifat decision support."

---

## SLIDE 9 — KESIMPULAN (±45 detik)

"Kesimpulan kami: pertama, SVM Baseline dengan kernel RBF adalah model terbaik dengan F1-Macro 0.887 dan akurasi 89.4%.

Kedua, 10 fitur terpilih yang berbasis domain knowledge dan Mutual Information sudah cukup efektif untuk prediksi.

Ketiga, ada keterbatasan: model dilatih pada dataset dari Portugal, sehingga perlu validasi sebelum diterapkan di konteks Indonesia.

Rekomendasi pengembangan ke depan: validasi dengan data lokal, eksplorasi ensemble methods, implementasi SHAP untuk interpretabilitas, dan deployment production dengan Docker."

---

## SLIDE 10 — PENUTUP (±30 detik)

"Demikian presentasi UAS saya. Semua kode, dataset, laporan, dan aplikasi sudah tersedia di repository GitHub yang link-nya tercantum di slide dan laporan.

Repository: github.com/hafizmuzani011-collab/uas-ml-kelulusan

Terima kasih atas perhatiannya. 
Wassalamualaikum Warahmatullahi Wabarakatuh."

---

## CATATAN UNTUK PEMBICARA

1. **Durasi total**: ±10 menit
2. **Tips**: Baca skrip ini sambil TUNJUKKAN slide yang sesuai. Jangan hanya membaca teks — sesekali lihat kamera.
3. **Tekankan poin penting** dengan nada lebih tegas: "F1-Macro 0.887", "SMOTE hanya di data latih", "decision support, bukan keputusan final".
4. **Jangan lupa**: tunjukkan live demo Streamlit di akhir presentasi jika diperbolehkan (tambah 1-2 menit).
5. **Siapkan jawaban** untuk pertanyaan dosen: kenapa SVM, kenapa bukan Random Forest, apa itu SMOTE, apa itu data leakage, kenapa F1 bukan accuracy.
