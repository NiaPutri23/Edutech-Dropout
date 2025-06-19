import streamlit as st
import joblib
import numpy as np

model = joblib.load('model_dropout.pkl')
feature_order = joblib.load('features.pkl') 

st.title("🎓 Prediksi Risiko Dropout Mahasiswa")
st.write("Masukkan data akademik mahasiswa berikut untuk memprediksi kemungkinan dropout.")

# Input user untuk variabel penting
curricular_units_2nd_sem_approved = st.number_input("Jumlah mata kuliah disetujui semester 2", min_value=0)
curricular_units_2nd_sem_grade = st.number_input("Rata-rata nilai semester 2", min_value=0.0, max_value=20.0)
curricular_units_1st_sem_approved = st.number_input("Jumlah mata kuliah disetujui semester 1", min_value=0)
tuition_fees_up_to_date = st.selectbox("Status pembayaran uang kuliah", options=[0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
curricular_units_1st_sem_grade = st.number_input("Rata-rata nilai semester 1", min_value=0.0, max_value=20.0)
age_at_enrollment = st.number_input("Usia saat masuk", min_value=15, max_value=100)
admission_grade = st.number_input("Nilai masuk (0-200)", min_value=0.0, max_value=200.0)
curricular_units_2nd_sem_evaluations = st.number_input("Jumlah evaluasi semester 2", min_value=0)
scholarship_holder = st.selectbox("Penerima beasiswa", options=[0, 1], format_func=lambda x: "Ya" if x == 1 else "Tidak")
previous_qualification_grade = st.number_input("Nilai kualifikasi sebelumnya", min_value=0.0, max_value=200.0)
course = st.selectbox("Kode jurusan", options=[9119, 9130, 9147, 9853, 9991], format_func=lambda x: f"Course {x}")

# Mapping input user ke dictionary
input_data = {
    "Curricular_units_2nd_sem_approved": curricular_units_2nd_sem_approved,
    "Curricular_units_2nd_sem_grade": curricular_units_2nd_sem_grade,
    "Curricular_units_1st_sem_approved": curricular_units_1st_sem_approved,
    "Tuition_fees_up_to_date": tuition_fees_up_to_date,
    "Curricular_units_1st_sem_grade": curricular_units_1st_sem_grade,
    "Age_at_enrollment": age_at_enrollment,
    "Admission_grade": admission_grade,
    "Curricular_units_2nd_sem_evaluations": curricular_units_2nd_sem_evaluations,
    "Scholarship_holder": scholarship_holder,
    "Previous_qualification_grade": previous_qualification_grade,
    "Course": course
}

final_input = []
for col in feature_order:
    if col in input_data:
        final_input.append(input_data[col])
    else:
        final_input.append(0)  # default jika tidak diinput

input_array = np.array([final_input])

# Prediksi
if st.button("🔍 Prediksi Risiko Dropout"):
    prediction = model.predict(input_array)[0]
    probs = model.predict_proba(input_array)[0]
    
    if prediction == 1:
        st.error("⚠️ Mahasiswa diprediksi BERISIKO DROPOUT.")
    else:
        st.success("✅ Mahasiswa diprediksi TIDAK berisiko dropout.")

    st.markdown("### Probabilitas:")
    st.write({
        "Dropout": f"{probs[1]*100:.2f}%",
        "Non Dropout": f"{probs[0]*100:.2f}%"
    })