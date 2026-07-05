# Data Dictionary

## Dataset: UCI Predict Students Dropout and Academic Success

### Sumber
- URL: https://archive.ics.uci.edu/ml/datasets/ Predict+Students+Dropout+and+Academic+Success
- Paper: Realinho et al. (2022), "Predicting Student Dropout and Academic Success"
- Lisensi: CC BY 4.0

### Target (Label)
| Nama Kolom | Tipe | Deskripsi |
|---|---|---|
| Target | categorical | Target klasifikasi: Graduate, Dropout, Enrolled |

### Fitur Prediktor (8+ fitur)
| No | Nama Kolom | Tipe | Deskripsi |
|---|---|---|---|
| 1 | Marital_status | categorical | Status perkawinan |
| 2 | Application_mode | integer | Metode pendaftaran |
| 3 | Application_order | integer | Urutan pendaftaran |
| 4 | Course | integer | Program studi |
| 5 | Daytime_evening_attendance | binary | Waktu kuliah (pagi/sore) |
| 6 | Previous_qualification | integer | Kualifikasi sebelumnya |
| 7 | Previous_qualification_grade | float | Nilai kualifikasi sebelumnya |
| 8 | Mothers_qualification | integer | Kualifikasi pendidikan ibu |
| 9 | Fathers_qualification | integer | Kualifikasi pendidikan ayah |
| 10 | Mothers_occupation | integer | Pekerjaan ibu |
| 11 | Fathers_occupation | integer | Pekerjaan ayah |
| 12 | Admission_grade | float | Nilai masuk |
| 13 | Displaced | binary | Status pindah domisili |
| 14 | Educational_special_needs | binary | Kebutuhan khusus |
| 15 | Debtor | binary | Status pembayaran |
| 16 | Tuition_fees_up_to_date | binary | Pembayaran SPP |
| 17 | Gender | binary | Jenis kelamin |
| 18 | Scholarship_holder | binary | Penerima beasiswa |
| 19 | Age_at_enrollment | integer | Usia saat masuk |
| 20 | International | binary | Mahasiswa internasional |
| 21 | Curricular_units_1st_sem_credited | integer | SKS semester 1 dikredit |
| 22 | Curricular_units_1st_sem_enrolled | integer | SKS semester 1 diambil |
| 23 | Curricular_units_1st_sem_evaluations | integer | SKS semester 1 evaluasi |
| 24 | Curricular_units_1st_sem_approved | integer | SKS semester 1 lulus |
| 25 | Curricular_units_1st_sem_grade | float | IP semester 1 |
| 26 | Curricular_units_1st_sem_without_evaluations | integer | SKS tanpa evaluasi |
| 27 | Curricular_units_2nd_sem_credited | integer | SKS semester 2 dikredit |
| 28 | Curricular_units_2nd_sem_enrolled | integer | SKS semester 2 diambil |
| 29 | Curricular_units_2nd_sem_evaluations | integer | SKS semester 2 evaluasi |
| 30 | Curricular_units_2nd_sem_approved | integer | SKS semester 2 lulus |
| 31 | Curricular_units_2nd_sem_grade | float | IP semester 2 |
| 32 | Curricular_units_2nd_sem_without_evaluations | integer | SKS tanpa evaluasi |
| 33 | Unemployment_rate | float | Tingkat pengangguran |
| 34 | Inflation_rate | float | Tingkat inflasi |
| 35 | GDP | float | GDP |

### Fitur yang Digunakan dalam Project (Minimal 8)
1. Previous_qualification_grade
2. Admission_grade
3. Age_at_enrollment
4. Curricular_units_1st_sem_approved
5. Curricular_units_1st_sem_grade
6. Curricular_units_2nd_sem_approved
7. Curricular_units_2nd_sem_grade
8. Tuition_fees_up_to_date
9. Scholarship_holder
10. Debtor