
import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("material_model.pkl")
le_project = joblib.load("le_project.pkl")
le_quality = joblib.load("le_quality.pkl")
le_material = joblib.load("le_material.pkl")

st.title("🏗️ Material Recommendation System")

# User Inputs
project_size = st.selectbox("Project Size", le_project.classes_)
budget = st.number_input("Budget (₹)", min_value=1000)
required_quality = st.selectbox("Required Quality", le_quality.classes_)
labor_cost = st.number_input("Labor Cost (₹)", min_value=1000)
profit_rate = st.slider("Profit Rate (%)", 0, 100, 10)

# Prepare input
input_data = pd.DataFrame([{
    "Project_Size": le_project.transform([project_size])[0],
    "Budget": budget,
    "Required_Quality": le_quality.transform([required_quality])[0],
    "Labor_Cost": labor_cost,
    "Profit_Rate": profit_rate
}])

# Predict material
if st.button("Recommend Material"):
    pred = model.predict(input_data)[0]
    recommended = le_material.inverse_transform([pred])[0]
    st.success(f"✅ Recommended Material: {recommended}")
