import pickle
import streamlit as st

# Set page config
st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

# Load the trained model
heart_disease_model = pickle.load(open("heart_disease_model.sav", 'rb'))

# Apply Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #1e1e1e;
        }
        
        /* Title */
        .stMarkdown h1 {
            color: white;
            text-align: center;
        }
        
        /* Input Box Styling */
        .stTextInput > div > div > input {
            font-size: 18px !important;
            padding: 10px;
        }
        
        /* Button Styling */
        .stButton > button {
            background-color: #ff4b4b;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            border-radius: 5px;
        }
        
        /* Center Button */
        .stButton {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# UI Layout
st.title('💓 Heart Disease Prediction using ML')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Age')
    trestbps = st.text_input('Resting Blood Pressure')
    restecg = st.text_input('Resting Electrocardiographic Results')
    oldpeak = st.text_input('Oldpeak')
    thal = st.text_input('Thalassemia')

with col2:
    sex = st.text_input('Sex')
    chol = st.text_input('Serum Cholesterol')
    thalach = st.text_input('Max Heart Rate Achieved')
    slope = st.text_input('Slope of Peak Exercise ST Segment')

with col3:
    cp = st.text_input('Chest Pain Type')
    fbs = st.text_input('Fasting Blood Sugar')
    exang = st.text_input('Exercise Induced Angina')
    ca = st.text_input('Number of Major Vessels Colored by Fluoroscopy')

# Prediction Button
heart_diagnosis = ""

if st.button('💉 Heart Disease Test Result'):
    try:
        # Convert inputs to float
        user_input = [
            float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs),
            float(restecg), float(thalach), float(exang), float(oldpeak), float(slope),
            float(ca), float(thal)
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
