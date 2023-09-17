import pandas as pd
import streamlit as st
import helper
import training
import numpy as np

st.title("Car Price Prediction")

company = st.selectbox('Company', options=helper.company())
name = st.selectbox('Model', options=helper.name(company))
year = st.selectbox('Year', options=helper.year())
fuel_type = st.selectbox('Fuel Type', options=helper.fuel_type())
kms_driven = st.text_input('Please Provide the approx No. Of kms driven')

year = int(year)
kms_driven = int(kms_driven)

# Create a dictionary for input data
input_data = {
    'name': name,
    'company': company,
    'year': year,
    'kms_driven': kms_driven,
    'fuel_type': fuel_type
}

input_df = pd.DataFrame([input_data])

if st.button('Predict'):
    result = training.modelling(input_df)
    predict = '₹' + str(round(result[0], 2))
    st.text(predict)

