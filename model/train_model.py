import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
data = pd.read_csv("housing.csv")

X = data[['area', 'bedrooms', 'bathrooms']]
y = data['price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("house_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained & saved!")
