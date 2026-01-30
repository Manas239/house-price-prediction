from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "house_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f) 

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    
    area = data["area"]
    bedrooms = data["bedrooms"]
    bathrooms = data["bathrooms"]

    prediction = model.predict([[area, bedrooms, bathrooms]])

    return jsonify({
        "predicted_price": round(prediction[0], 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
