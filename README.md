# House-price-prediction
End-to-end machine learning project for house price prediction using Flask REST API and Streamlit UI. Includes model training, API-based inference, and interactive frontend for real-world ML deployment.


🏠 House Price Prediction (Flask + Streamlit)

An end-to-end Machine Learning deployment project that predicts house prices using a trained ML model.
The model is deployed using a Flask REST API and accessed through an interactive Streamlit web application.

This project demonstrates the complete ML workflow from training to deployment with proper project structure and version control.

🚀 Project Overview

Trained a Machine Learning regression model for house price prediction

Served the model using a Flask REST API

Built an interactive Streamlit UI for user input and predictions

Followed a decoupled backend–frontend architecture

Implemented using virtual environment and GitHub best practices

🧠 Tech Stack

Python

Machine Learning (scikit-learn)

Flask – Backend API

Streamlit – Frontend UI

Pandas & NumPy – Data processing

Pickle – Model serialization

Git & GitHub – Version control

🏗️ Project Structure
house-price-prediction/
│
├── api/
│   └── app.py                 # Flask API
│
├── model/
│   ├── train_model.py         # Model training script
│   ├── housing.csv            # Dataset
│   └── house_model.pkl        # Trained ML model
│
├── ui/
│   └── streamlit_app.py       # Streamlit frontend
│
├── .gitignore
├── README.md

📊 Dataset Description

The dataset includes the following features:

area – Area of the house (in square feet)

bedrooms – Number of bedrooms

bathrooms – Number of bathrooms

price – House price (target variable)

⚙️ How It Works

Model Training

Housing data is used to train a regression model

The trained model is saved as house_model.pkl

Flask API

Loads the trained model

Exposes a /predict endpoint

Accepts input as JSON and returns predicted price

Streamlit UI

Takes user input (area, bedrooms, bathrooms)

Sends request to Flask API

Displays predicted house price

▶️ How to Run the Project
1️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install flask streamlit scikit-learn pandas numpy requests

3️⃣ Train the Model
cd model
python train_model.py

4️⃣ Run Flask API
cd api
python app.py


Flask runs at:

http://127.0.0.1:5000

5️⃣ Run Streamlit App (New Terminal)
cd ui
streamlit run streamlit_app.py

🧪 Sample API Request

POST /predict

{
  "area": 1200,
  "bedrooms": 3,
  "bathrooms": 2
}


Response:

{
  "predicted_price": 6500000
}

🎯 Key Learnings

End-to-end ML deployment

REST API development using Flask

Frontend–backend communication

Model serialization and reuse

Git and project structuring best practices

🔮 Future Improvements

Replace Flask with FastAPI

Add Docker support

Deploy on cloud platforms

Improve model accuracy

Add authentication and logging

👨‍💻 Author

Manas Machindra Doltade
Aspiring Data Scientist | ML & AI Enthusiast

⭐ If you like this project, feel free to star the repository!

If you want next:

🔥 Resume bullet points

🚀 Deployment guide

🧠 Interview explanation

Just tell me 💯

give text that i will copy

Got it 👍
Below is ONLY the README text, clean and ready to copy–paste (no extra explanation).

🏠 House Price Prediction (Flask + Streamlit)

An end-to-end Machine Learning deployment project that predicts house prices using a trained ML model. The model is deployed using a Flask REST API and accessed through an interactive Streamlit web application.

This project demonstrates the complete ML workflow from model training to deployment with proper project structure and version control.

🚀 Project Overview

• Trained a machine learning regression model for house price prediction
• Deployed the model using a Flask REST API
• Built an interactive Streamlit user interface
• Implemented backend–frontend communication using HTTP requests
• Followed best practices for project structure and GitHub usage

🧠 Tech Stack

Python
Machine Learning (scikit-learn)
Flask (Backend API)
Streamlit (Frontend UI)
Pandas & NumPy
Pickle
Git & GitHub

🏗 Project Structure

house-price-prediction/
│
├── api/
│ └── app.py
│
├── model/
│ ├── train_model.py
│ ├── housing.csv
│ └── house_model.pkl
│
├── ui/
│ └── streamlit_app.py
│
├── .gitignore
└── README.md

📊 Dataset Description

The dataset contains the following features:

area – Area of the house (square feet)
bedrooms – Number of bedrooms
bathrooms – Number of bathrooms
price – House price (target variable)

⚙ How It Works

The machine learning model is trained using housing data and saved as a pickle file

The Flask API loads the trained model and exposes a /predict endpoint

The Streamlit application collects user input and sends it to the Flask API

The predicted house price is displayed on the UI

▶ How to Run the Project

Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

Install required packages

pip install flask streamlit scikit-learn pandas numpy requests

Train the model

cd model
python train_model.py

Run Flask API

cd api
python app.py

Run Streamlit application (new terminal)

cd ui
streamlit run streamlit_app.py

🧪 Sample API Request

POST /predict

{
"area": 1200,
"bedrooms": 3,
"bathrooms": 2
}

Response

{
"predicted_price": 6500000
}

🎯 Key Learnings

End-to-end ML deployment
Flask REST API development
Frontend and backend integration
Model serialization and reuse
Professional GitHub project structure

🔮 Future Enhancements

Switch to FastAPI
Add Docker support
Deploy on cloud platforms
Improve model performance
Add authentication and logging

👨‍💻 Author

Manas Machindra Doltade
Aspiring Data Scientist | ML & AI Enthusiast

⭐ If you like this project, feel free to star the repository!
