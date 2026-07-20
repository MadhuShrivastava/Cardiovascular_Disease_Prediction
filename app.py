# Libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

df = pd.read_csv("CVD_cleaned.csv")

# Machine Learning preprocessing
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, StandardScaler
model = joblib.load("cardiovascular_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")
ord_enc = joblib.load("ordinal_encoder.pkl")

general_health = st.selectbox(
    "General Health",
    df["General_Health"].unique()
)

checkup = st.selectbox(
    "Checkup",
    df["Checkup"].unique()
)

exercise = st.selectbox(
    "Exercise",
    df["Exercise"].unique()
)

skin_cancer = st.selectbox(
    "Skin Cancer",
    df["Skin_Cancer"].unique()
)

other_cancer = st.selectbox(
    "Other Cancer",
    df["Other_Cancer"].unique()
)

depression = st.selectbox(
    "Depression",
    df["Depression"].unique()
)

diabetes = st.selectbox(
    "Diabetes",
    df["Diabetes"].unique()
)

arthritis = st.selectbox(
    "Arthritis",
    df["Arthritis"].unique()
)

sex = st.selectbox(
    "Sex",
    df["Sex"].unique()
)

age_category = st.selectbox(
    "Age Category",
    df["Age_Category"].unique()
)

smoking_history = st.selectbox(
    "Smoking History",
    df["Smoking_History"].unique()
)

alcohol_consumption = st.number_input(
    "Alcohol Consumption",
    min_value=0
)

fruit_consumption = st.number_input(
    "Fruit Consumption",
    min_value=0
)

green_vegetables_consumption = st.number_input(
    "Green Vegetables Consumption",
    min_value=0
)

friedpotato_consumption = st.number_input(
    "Fried Potato Consumption",
    min_value=0
)

if st.button("Predict"):

    # Create input DataFrame
    input_df = pd.DataFrame({
        "General_Health": [general_health],
        "Checkup": [checkup],
        "Exercise": [exercise],
        "Skin_Cancer": [skin_cancer],
        "Other_Cancer": [other_cancer],
        "Depression": [depression],
        "Diabetes": [diabetes],
        "Arthritis": [arthritis],
        "Sex": [sex],
        "Age_Category": [age_category],
        "Smoking_History": [smoking_history],
        "Alcohol_Consumption": [alcohol_consumption],
        "Fruit_Consumption": [fruit_consumption],
        "Green_Vegetables_Consumption": [green_vegetables_consumption],
        "FriedPotato_Consumption": [friedpotato_consumption]
    })

    # Encode binary columns
    binary_cols = [
        'Exercise', 'Skin_Cancer', 'Other_Cancer',
        'Depression', 'Diabetes', 'Arthritis',
        'Sex', 'Smoking_History'
    ]

    for col in binary_cols:
        input_df[col] = label_encoders[col].transform(input_df[col])

    # Encode ordinal columns
    ordinal_cols = ['General_Health', 'Checkup', 'Age_Category']
    input_df[ordinal_cols] = ord_enc.transform(input_df[ordinal_cols])

    # Scale
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ High risk of Heart Disease")
    else:
        st.success("✅ Low risk of Heart Disease")