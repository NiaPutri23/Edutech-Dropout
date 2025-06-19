# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

### Latar Belakang
Jaya Jaya Institut adalah institusi pendidikan tinggi yang berdiri sejak tahun 2000. Dalam beberapa tahun terakhir, pihak manajemen mencatat jumlah siswa yang dropout meningkat secara signifikan. Hal ini mencoreng reputasi akademik dan menimbulkan kerugian finansial serta kepercayaan masyarakat.

### Permasalahan Bisnis
Jaya Jaya Institut, sebagai institusi pendidikan yang telah berdiri sejak tahun 2000, tengah menghadapi permasalahan serius terkait tingginya angka siswa yang tidak menyelesaikan pendidikan alias mengalami dropout. Fenomena ini tidak hanya berdampak pada menurunnya angka kelulusan dan efektivitas penyelenggaraan pendidikan, tetapi juga berpotensi merusak citra dan reputasi institusi di mata masyarakat dan calon siswa baru.

### Cakupan Proyek
- Melakukan analisis eksploratif terhadap data siswa.
- Membangun sistem prediksi siswa dropout berbasis Machine Learning.
- Membangun dashboard untuk memantau performa siswa dan faktor dropout.
- Deploy model prediksi dan dashboard untuk digunakan manajemen Jaya Jaya Institut.

### Persiapan

Sumber data: [Student Performance Github](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:
```python
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Menjalankan Dashboard:
1. Jalankan Docker
2. Akses Metabase di browser dengan:
**URL:** http://localhost:3010/ 
**Login credential:**  
- Email: root@mail.com
- Password: KrY8igkJRaXG_1

## Business Dashboard
Public dashboard dapat diakses pada: [Dashboard Edutech](http://localhost:3010/public/dashboard/80fb6453-44f1-439b-b9d5-f362e788671c)
![ichinisannyaw-dashboard](ichinisannyaw-dashboard.png)
![ichinisannyaw-dashboard-1](ichinisannyaw-dashboard-1.png)
![ichinisannyaw-dashboard-2](ichinisannyaw-dashboard-2.png)

## Menjalankan Sistem Machine Learning
Prototype sistem Machine learning dapat dijalankan secara lokal ataupun dengan mengakses link public.

Secara lokal:
1. Masuk ke dalam folder Proyek 8 Edutech 
2. Jalankan 
```
streamlit run app.py
```

atau

Akses melalui link public: 
https://niaputri23-edutech-dropout-app-prumsn.streamlit.app/

## Conclusion
Terdapat 4.424 total siswa dengan 32% nya terkena dropout dan sisanya adalah siswa yang masih enrolled dan graduated. Usia terbanyak adalah pada umur 15-22 tahun dan semakin naik usia semakin menurun banyaknya siswa.

Berdasarkan visualisasi data performa akademik mahasiswa antara yang Dropout dan Non-Dropout, berikut insight yang dapat ditarik:

1. Curricular Units Approved (Semester 1 & 2):
- Mahasiswa Non-Dropout cenderung memiliki jumlah mata kuliah yang disetujui (approved) lebih tinggi.
- Mahasiswa yang hanya menyelesaikan sedikit atau bahkan tidak lulus mata kuliah semester 1 & 2 memiliki kecenderungan lebih besar untuk dropout.
- Ini menandakan early academic performance sangat berpengaruh terhadap kelanjutan studi.

2. Curricular Grade Semester 1 & 2:
- Rata-rata nilai mahasiswa Non-Dropout lebih tinggi dibandingkan dengan yang dropout.
- Banyak mahasiswa dropout memiliki nilai rendah (<10), yang menunjukkan potensi akademik rendah atau kurangnya kesiapan.

3. Previous Qualification Grade:
- Mahasiswa dengan nilai kualifikasi sebelumnya lebih tinggi (sekitar 140 ke atas) cenderung tidak dropout.
- Ini menandakan bahwa riwayat pendidikan sebelumnya bisa menjadi indikator risiko dropout.

4. Admission Grade:
- Nilai masuk (admission grade) juga berhubungan positif dengan keberhasilan studi.
- Mahasiswa dengan admission grade yang rendah (<120) cenderung lebih banyak dropout.

5. Pengaruh course: 
- Terdapat beberapa course yang memiliki jumlah dropoutnya lebih banyak daripada jumlah non-dropout seperti pada course nomor 9119 dan 9130. 

6. Pemegang beasiswa
- Siswa yang menerima beasiswa cenderung tidak dropout dibandingkan siswa yang tidak menerima beasiswa

### Rekomendasi Action Items
Berdasarkan insight tersebut, berikut beberapa action items yang bisa dilakukan oleh Jaya Jaya Institut:

- Lakukan pemantauan ketat terhadap jumlah mata kuliah yang disetujui di semester awal.
- Terapkan program intervensi akademik seperti remedial, tutoring, atau mentoring bagi mahasiswa dengan capaian rendah.
- Implementasikan sistem deteksi dini mahasiswa berisiko berdasarkan capaian SKS semester 1 dan 2.
- Gunakan nilai kualifikasi sebelumnya sebagai salah satu indikator untuk seleksi masuk atau kebutuhan program matrikulasi.
- Tawarkan kelas dasar atau penguatan konsep untuk mahasiswa dengan nilai awal yang rendah.
- Kembangkan sistem asesmen awal untuk memetakan kesiapan akademik mahasiswa baru.
- Revisi standar nilai masuk agar mencerminkan kesiapan akademik yang lebih baik.
- Sediakan jalur alternatif dengan pelatihan prakuliah untuk calon mahasiswa dengan nilai rendah.
- Evaluasi konten, metode ajar, dan beban studi dari course dengan angka dropout tinggi.
- Lakukan review kinerja dosen pengampu dan berikan pelatihan.
- Terapkan penyesuaian kurikulum atau model belajar aktif untuk course yang bermasalah.
- Perluas akses beasiswa untuk mahasiswa yang berisiko tinggi dropout.
