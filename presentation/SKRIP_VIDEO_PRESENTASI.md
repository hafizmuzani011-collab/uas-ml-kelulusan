# SKRIP VIDEO PRESENTASI UAS MACHINE LEARNING (BAHASA AKADEMIS FORMAL)
# Pembicara: Na'ilah Azfa Zarqarida / Kelompok A11.2024.15549

---

## SLIDE 1 — PENDAHULUAN (Durasi: ±45 Detik)

"Selamat pagi / siang Bapak/Ibu Dosen Penguji. 

Perkenalkan, nama saya Na'ilah Azfa Zarqarida, NIM A11.2024.15549, mewakili kelompok A11.4401 dan A11.4410.

Pada kesempatan kali ini, saya akan mempresentasikan laporan proyek akhir mata kuliah Pembelajaran Mesin yang berjudul: 'Prediksi Kelulusan Mahasiswa Menggunakan Pendekatan Machine Learning dan Implementasi Outcome-Based Education (OBE)'."

---

## SLIDE 2 — LATAR BELAKANG & URGENSI MASALAH (Durasi: ±1 Menit 15 Detik)

"Latar belakang utama dari penelitian ini adalah tingginya tingkat dropout atau putus kuliah di lingkungan akademis, di mana data empiris menunjukkan persentase yang signifikan, yakni sebesar 39 persen dari total 4.424 mahasiswa pada basis data UCI. Masalah ini tidak hanya merugikan masa depan mahasiswa, tetapi juga berdampak buruk bagi reputasi institusi karena menurunkan skor Indikator Kinerja Utama universitas dan memicu inefisiensi alokasi anggaran operasional.

Oleh karena itu, kami merancang sebuah sistem deteksi dini atau Early Warning System yang memanfaatkan model klasifikasi Machine Learning untuk memetakan probabilitas mahasiswa yang terancam dropout sebelum masa studi mereka selesai.

Proyek ini juga diselaraskan dengan standar Outcome-Based Education atau OBE, khususnya dalam memenuhi Capaian Pembelajaran Lulusan CPL-8 mengenai kecakapan analitik pemodelan machine learning, dan CPL-10 terkait tanggung jawab etis pemanfaatan teknologi."

---

## SLIDE 3 — DATASET & PIPELINE PREPROCESSING (Durasi: ±1 Menit 30 Detik)

"Dataset yang digunakan adalah basis data kelulusan mahasiswa dari UCI Machine Learning Repository. Pada tahap awal pra-pemrosesan, data mahasiswa berstatus 'Enrolled' kami saring keluar untuk mereduksi target kelas menjadi klasifikasi biner, menyisakan 3.630 baris data valid untuk status Graduate dan Dropout.

Kami menerapkan empat alur preprocessing utama:
Pertama, seleksi fitur menggunakan metode kuantitatif Mutual Information untuk menyaring 10 fitur akademis dan demografis paling prediktif, seperti indeks prestasi semester awal dan status pembiayaan kuliah.
Kedua, pemisahan data latih dan data uji dengan rasio 80 berbanding 20 secara stratified untuk memelihara proporsi kelas asli.
Ketiga, standarisasi fitur numerik menggunakan StandardScaler untuk menghilangkan bias skala pada algoritma berbasis jarak seperti KNN dan SVM.
Dan keempat, penanganan imbalance data menggunakan SMOTE pada data training secara terisolasi guna menghindari kebocoran data atau data leakage pada proses evaluasi."

---

## SLIDE 4 — DESAIN EKSPERIMEN & STRATEGI OPTIMASI (Durasi: ±1 Menit 15 Detik)

"Dalam desain eksperimen, kami membandingkan kinerja tiga model klasifikasi dasar, yaitu K-Nearest Neighbors, Naive Bayes Gaussian, dan Support Vector Machine dengan basis kernel RBF.

Proses optimasi dilakukan melalui empat instrumen, yaitu: penyetelan hyperparameter menggunakan algoritma GridSearchCV, pengujian validasi silang berupa 5-Fold Stratified Cross Validation, seleksi fitur berbasis signifikansi Mutual Information, serta oversampling kelas minoritas.

Mengingat dataset ini memiliki tingkat ketidakseimbangan kelas, kami memilih metrik evaluasi prioritas F1-Macro dan Balanced Accuracy dibandingkan Akurasi biasa. Hal ini memastikan evaluasi model mencerminkan keandalan yang adil untuk mengenali kelas minoritas mahasiswa yang dropout."

---

## SLIDE 5 — HASIL EKSPERIMEN KOMPARATIF (Durasi: ±1 Menit 30 Detik)

"Berikut adalah visualisasi grafik performa dan tabel perbandingan dari enam model eksperimen yang telah dieksekusi.

Dari data komparasi ini, model terbaik yang terpilih adalah Support Vector Machine Baseline. Model ini menunjukkan metrik tertinggi dengan skor F1-Macro sebesar 0.8869 dan Akurasi umum mencapai 89.39 persen.

Penyebab SVM unggul adalah karena penggunaan kernel Radial Basis Function (RBF) yang sangat tangguh dalam memetakan batas keputusan non-linear, ditambah dengan optimasi pembobotan kelas internal (class_weight='balanced') yang efisien. 

Optimasi eksternal sekunder seperti integrasi SMOTE eksternal justru menyebabkan sedikit degradasi performa pada SVM menjadi 0.884, dikarenakan hilangnya sebagian data variansi asli saat reduksi parameter ke 8 fitur."

---

## SLIDE 6 — ANALISIS KESALAHAN EMPIRIS (Durasi: ±1 Menit 15 Detik)

"Kami melakukan analisis kesalahan empiris terhadap hasil klasifikasi model SVM Baseline. Dari data test, model menghasilkan 50 kesalahan tipe False Positive atau mahasiswa dropout yang keliru diprediksi sebagai lulus, dan 27 kesalahan tipe False Negative.

Melalui penyelidikan sampel, kami mendapati pola bahwa mahasiswa yang memiliki kinerja akademis sangat memuaskan di semester 1 dan 2, namun mendadak dropout di akhir semester, menjadi penyebab utama terjadinya kesalahan prediksi.

Kasus ini membuktikan batasan inheren dari data tabular akademis. Model tidak memiliki visibilitas terhadap anomali non-akademik di dunia nyata, seperti penurunan kondisi finansial keluarga secara mendadak atau krisis kesehatan pribadi, yang menjadi pemicu utama kegagalan studi mereka."

---

## SLIDE 7 — PEMBAHASAN ANALITIS & IMPLIKASI PRAKTIS (Durasi: ±1 Menit 15 Detik)

"Dalam pembahasan proyek ini, kami mengidentifikasi trade-off klasik dalam machine learning: antara kompleksitas, akurasi, dan interpretabilitas. SVM RBF menempati posisi akurasi tertinggi namun bersifat black-box. Sementara Naive Bayes menawarkan transparansi penuh namun memiliki sensitivitas deteksi yang rendah pada kelas dropout.

Secara implikasi praktis, model SVM Baseline ini sangat layak diposisikan sebagai Decision Support System atau sistem penunjang keputusan bagi para dosen wali. Deteksi dini ini mempermudah alokasi preventif bantuan bimbingan konseling akademik serta bantuan pengajuan beasiswa finansial bagi mahasiswa yang rentan.

Meskipun demikian, ada batasan etis mutlak yang kami tekankan dalam laporan: sistem kecerdasan buatan ini dilarang digunakan untuk melakukan eksekusi drop out mahasiswa secara otomatis. Keputusan administratif tertinggi tetap wajib diputuskan melalui verifikasi manusia."

---

## SLIDE 8 — DESAIN APLIKASI ANTARMUKA PENGGUNA (Durasi: ±1 Menit)

"Untuk membuktikan fungsionalitas model dalam skenario produksi, kami membangun antarmuka pengguna berbasis Streamlit dan Gradio, yang terhubung dengan backend REST API berbasis FastAPI.

Pada web dashboard Streamlit, kami merancang empat menu utama: panel prediksi dengan luaran hasil klasifikasi beserta confidence score-nya, visualisasi data deskriptif, tab visualisasi performa komparasi metrik model, dan halaman edukasi model SVM dalam bahasa Indonesia yang mudah dipahami.

FastAPI menyediakan backend andal yang mengekspos endpoint inferensi `/predict` berbasis JSON, siap untuk diintegrasikan secara langsung dengan Sistem Informasi Akademik atau SIAKAD di tingkat universitas."

---

## SLIDE 9 — KESIMPULAN & REKOMENDASI (Durasi: ±45 Detik)

"Sebagai kesimpulan:
Pertama, model SVM Baseline terbukti paling tangguh dengan skor F1-Macro 0.8869.
Kedua, pemilihan 10 fitur utama memberikan batas keputusan yang efisien tanpa mengorbankan waktu pemrosesan data.
Ketiga, generalisasi model saat ini terbatas pada demografi mahasiswa Portugal, sehingga memerlukan validasi demografis lokal sebelum diterapkan luas.

Rekomendasi kami untuk pengembangan masa depan mencakup pemanfaatan ensemble stacking, integrasi framework Explainable AI seperti nilai SHAP untuk transparansi model, serta pembungkusan infrastruktur deployment dengan sistem Docker."

---

## SLIDE 10 — PENUTUP (Durasi: ±30 Detik)

"Demikian presentasi laporan proyek akhir UAS Machine Learning saya. Seluruh dokumen laporan, dataset, basis kode, dan aplikasi demonstrasi telah kami dokumentasikan secara terbuka pada repositori GitHub di link yang tertera pada layar.

Link repositori: github.com/hafizmuzani011-collab/uas-ml-kelulusan

Terima kasih atas perhatian Bapak dan Ibu Dosen. Kurang lebihnya mohon maaf.
Wassalamualaikum Warahmatullahi Wabarakatuh."
