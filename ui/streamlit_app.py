import streamlit as st
import requests

st.title("🏠 House Price Prediction")

area = st.number_input("Area (sq ft)", 500, 5000)
bedrooms = st.number_input("Bedrooms", 1, 10)
bathrooms = st.number_input("Bathrooms", 1, 10)

if st.button("Predict Price"):
    response = requests.post(
        "http://127.0.0.1:5000/predict",
        json={
            "area": area,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms
        }
    )

    price = response.json()["predicted_price"]
    st.success(f"Estimated Price: ₹ {price}")
