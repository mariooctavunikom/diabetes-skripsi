import pickle
import streamlit as st

# Load Model
diabetes_model = pickle.load(open('diabetes_model.sav' , 'rb'))

# Judul Halaman
st.title('Cek Prediksi Diabetes')

# Kolom Form
col1, col2 = st.columns(2)

with col1 :
  Pregnancies = st.text_input ('input nilai Pregnancies')

with col2 :
  Glucose = st.text_input ('Masukan data Glukosa')

with col1 :
  BloodPressure = st.text_input ('Masukan data Tekanan Darah')

with col2 :
  SkinThickness = st.text_input ('Masukan data Ketebalan Kulit')

with col1 :
  Insulin = st.text_input ('Masukan data Insulin')

with col2 :
  BMI = st.text_input ('Masukan data BMI')

with col1 :
  DiabetesPedigreeFunction = st.text_input ('Masukan data Pedigree Function')

with col2 :
  Age = st.text_input('Masukan Umur')

# Prediksi
diab_diagnosis = ' '

# Tombol Submit
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 1):
      diab_diagnosis = 'Pasien Mengalami Diabetes'
    else :
        diab_diagnosis = 'Pasien Tidak Mengalami Diabetes'

st. success(diab_diagnosis)