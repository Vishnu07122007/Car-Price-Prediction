import pandas as pd
import numpy as np
import datetime
import xgboost as xgb
import streamlit as st

def main():
    html_temp = """<h1>Car Price Prediction</h1>"""

    model = xgb.XGBRegressor()
    model.load_model("xg_model.json")
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("This Website help you to predict your car selling price.")

    p1 = st.number_input("Please enter ex-showroom pricr(In Lakhs)" , 2.5,25.0, step=1.0)
    p2 = st.number_input("Please enter car driven distance(In Kms)"  ,100,500000 ,step=100)

    s1 = st.selectbox("Please select car fuel type", ["Petrol", "Diesel", "CNG"])
    if s1 == "Petrol":
        p3 = 0
    elif s1 == "Diesel":
        p3 = 1
    elif s1 == "CNG":
        p3 = 2

    s2 = st.selectbox("select seller type", ("Dealer", "Individual"))
    if s2 == "Dealer":
        p4 = 0
    elif s2 == "Individual":
        p4 = 1

    s3 = st.selectbox("please select transmission type", ("Automatic", "Manual"))
    if s3 == "Manual":
        p5 = 0
    elif s3 == "Automatic":
        p5 = 1

    p6 =  st.slider("How many owner ", 0, 3, step=1)   


    date_time = datetime.datetime.now()
    years = st.number_input("Car Purchase year" , 1990, date_time.year, step=1)
    p7 = date_time.year - years

    data_new = pd.DataFrame({
        'Present_Price': p1,
        'Kms_Driven': p2,
        'Fuel_Type': p3,
        'Seller_Type': p4,
        'Transmission': p5,
        'Owner': p6,
        'Age': p7
    },index=[0])

    if st.button("Predict"):
        pred = model.predict(data_new)
        st.success('The predicted selling price of your car is: {:.2f} Lakhs'.format(round(pred[0])))

if __name__ == '__main__':
    main()