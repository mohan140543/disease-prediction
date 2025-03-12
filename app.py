import pickle
import streamlit as st

# Set page config
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# Load the trained model
heart_disease_model = pickle.load(open("heart_disease_model.h5", 'rb'))

# UI Layout
st.title('💓 Heart Disease Prediction using ML')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Age', min_value=1, max_value=120, step=1)
    trestbps = st.number_input('Resting Blood Pressure', min_value=50, max_value=200)
    restecg = st.number_input('Resting Electrocardiographic Results', min_value=0, max_value=2)
    oldpeak = st.number_input('Oldpeak', min_value=0.0, max_value=6.2, format="%.1f")
    thal = st.number_input('Thalassemia', min_value=0, max_value=3)

with col2:
    sex = st.radio('Sex', [0, 1])
    chol = st.number_input('Serum Cholesterol', min_value=100, max_value=600)
    thalach = st.number_input('Max Heart Rate Achieved', min_value=60, max_value=220)
    slope = st.number_input('Slope of Peak Exercise ST Segment', min_value=0, max_value=2)

with col3:
    cp = st.number_input('Chest Pain Type', min_value=0, max_value=3)
    fbs = st.radio('Fasting Blood Sugar > 120 mg/dl', [0, 1])
    exang = st.radio('Exercise Induced Angina', [0, 1])
    ca = st.number_input('Number of Major Vessels Colored by Fluoroscopy', min_value=0, max_value=4)

# Prediction Button
heart_diagnosis = ""

if st.button('💉 Heart Disease Test Result'):
    try:
        user_input = [
            age, sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak, slope,
            ca, thal
        ]

        # Make prediction
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = '❗ The person is likely to have heart disease ❗'
        else:
            heart_diagnosis = '✅ The person is not likely to have heart disease ✅'

        st.success(heart_diagnosis)

    except ValueError:
        st.error("⚠️ Please enter valid numeric values for all fields.")
