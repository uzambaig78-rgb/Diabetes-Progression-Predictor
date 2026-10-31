import streamlit as st
import joblib
import numpy as np

model = joblib.load("best_diabetes_model.joblib")

st.set_page_config(page_title="Diabetes Progression Predictor", page_icon="🩺", layout="centered")

st.title("🩺 Diabetes Progression Predictor")
st.markdown("Enter patient data below to predict disease progression score.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (normalized)", value=0.0, format="%.4f", help="Standardized age value")
    sex = st.number_input("Sex (normalized)", value=0.0, format="%.4f", help="Standardized sex value")
    bmi = st.number_input("BMI (normalized)", value=0.0, format="%.4f", help="Standardized body mass index")
    bp  = st.number_input("Blood Pressure (normalized)", value=0.0, format="%.4f", help="Standardized average blood pressure")
    s1  = st.number_input("S1 - TC (normalized)", value=0.0, format="%.4f", help="Total serum cholesterol")

with col2:
    s2  = st.number_input("S2 - LDL (normalized)", value=0.0, format="%.4f", help="Low-density lipoproteins")
    s3  = st.number_input("S3 - HDL (normalized)", value=0.0, format="%.4f", help="High-density lipoproteins")
    s4  = st.number_input("S4 - TCH (normalized)", value=0.0, format="%.4f", help="Total cholesterol / HDL")
    s5  = st.number_input("S5 - LTG (normalized)", value=0.0, format="%.4f", help="Log of serum triglycerides")
    s6  = st.number_input("S6 - GLU (normalized)", value=0.0, format="%.4f", help="Blood sugar level")

st.divider()

if st.button("🔍 Predict", use_container_width=True, type="primary"):
    features = np.array([[age, sex, bmi, bp, s1, s2, s3, s4, s5, s6]])
    prediction = model.predict(features)[0]
    st.success(f"### Predicted Disease Progression Score: {prediction:.2f}")
    st.info("Higher values indicate greater diabetes progression.")