from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

#Loading Trained model 
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return{"message": "Api is running"}

@app.post("/predict")
def predict(team1_strength: int, team2_strength: int):
    data = np.array([[team1_strength,team2_strength]])
    prediction = model.predict(data)[0]
    probabilities =model.predict_proba(data)[0]


    return{
        "predicted_winner" : int(prediction),
        "probabilities": {
            "team1": probabilities[0],
            "team2": probabilities[1]
        }
    }