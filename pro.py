import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load('loan_approval_model.pkl')

st.title("Loan Approval Prediction App")

st.write("Enter Applicant Details")

# User Inputs
no_of_dependents = st.number_input("Number of Dependents", 0, 10)

education = st.selectbox("Education", ["Graduate", "Not Graduate"])

self_employed = st.selectbox("Self Employed", ["Yes", "No"])

income_annum = st.number_input("Annual Income")

loan_amount = st.number_input("Loan Amount")

loan_term = st.number_input("Loan Term")

cibil_score = st.number_input("CIBIL Score")

residential_assets_value = st.number_input("Residential Assets Value")

commercial_assets_value = st.number_input("Commercial Assets Value")

luxury_assets_value = st.number_input("Luxury Assets Value")

bank_asset_value = st.number_input("Bank Asset Value")

# Encoding
education = 0 if education == "Graduate" else 1
self_employed = 1 if self_employed == "Yes" else 0

# Prediction Button
if st.button("Predict Loan Status"):

    input_data = pd.DataFrame([[
        1,  # Dummy loan_id value
        no_of_dependents,
        education,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value
    ]], columns=[
        'loan_id',
        'no_of_dependents',
        'education',
        'self_employed',
        'income_annum',
        'loan_amount',
        'loan_term',
        'cibil_score',
        'residential_assets_value',
        'commercial_assets_value',
        'luxury_assets_value',
        'bank_asset_value'
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
