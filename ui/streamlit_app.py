import streamlit as st
import requests

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# ================= CUSTOM CSS =================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            rgba(255, 255, 255, 0.92),
            rgba(255, 255, 255, 0.92)
        ),
        url("https://images.unsplash.com/photo-1568605114967-8130f3a36994");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.15);
        margin-bottom: 25px;
    }

    h1 {
        text-align: center;
        color: #2c3e50;
    }

    .subtitle {
        text-align: center;
        color: #7f8c8d;
        font-size: 16px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================= HEADER =================
st.markdown("<h1>🏠 House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>ML-based house price estimation with smart preview</div>",
    unsafe_allow_html=True
)

# ================= INPUT CARD =================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🔢 Enter House Details")

col1, col2, col3 = st.columns(3)

with col1:
    area = st.number_input("📐 Area (sq ft)", min_value=400, max_value=6000, step=100)

with col2:
    bedrooms = st.number_input("🛏 Bedrooms", min_value=1, max_value=8, step=1)

with col3:
    bathrooms = st.number_input("🛁 Bathrooms", min_value=1, max_value=6, step=1)

st.markdown("</div>", unsafe_allow_html=True)

# ================= SMART HOUSE PREVIEW =================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("🏡 House Preview (Based on Your Inputs)")

# ---- Classification Logic ----
if area < 800:
    house_type = "Compact Apartment"
    size_label = "Small"
    house_img = "https://images.unsplash.com/photo-1523217582562-09d0def993a6"

elif area < 1500 and bedrooms <= 2:
    house_type = "Modern Apartment"
    size_label = "Medium"
    house_img = "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688"

elif area < 2500 and bedrooms <= 4:
    house_type = "Independent House"
    size_label = "Spacious"
    house_img = "https://images.unsplash.com/photo-1600585154340-be6161a56a0c"

else:
    house_type = "Luxury Villa"
    size_label = "Luxury"
    house_img = "https://images.unsplash.com/photo-1576941089067-2de3c901e126"

# ---- Display Preview ----
st.image(house_img, use_container_width=True)

st.markdown(
    f"""
    <div style="text-align:center; margin-top:10px;">
        <h4>{house_type}</h4>
        <p style="color:gray;">
            🏷 Size: <b>{size_label}</b> &nbsp; | &nbsp;
            📐 Area: <b>{area} sq ft</b> &nbsp; | &nbsp;
            🛏 {bedrooms} Beds &nbsp; | &nbsp;
            🛁 {bathrooms} Baths
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ================= PREDICTION =================
st.markdown("<div class='card'>", unsafe_allow_html=True)

if st.button("💰 Predict Price", use_container_width=True):
    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json={
                "area": area,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms
            }
        )

        price = response.json()["predicted_price"]

        st.success(f"🏷 Estimated House Price: ₹ {price:,.2f}")

    except Exception:
        st.error("⚠️ Flask backend is not running. Please start api/app.py")

st.markdown("</div>", unsafe_allow_html=True)
