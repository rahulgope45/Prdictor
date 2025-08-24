from fastapi import FastAPI
import joblib
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


#Allowe origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict later to ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Loading Trained model 
model = joblib.load("model.pkl")

# Pydantic model for request body
class TeamStrength(BaseModel):
    team1_strength: int
    team2_strength: int

@app.get("/")
def home():
    return{"message": "Api is running"}

@app.post("/predict")
def predict(data: TeamStrength): 
    arr = np.array([[data.team1_strength,data.team2_strength]])
    prediction = model.predict(arr)[0]
    probabilities =model.predict_proba(arr)[0]


    return{
        "predicted_winner" : int(prediction),
        "probabilities": {
            "team1": float (probabilities[0]),
            "team2": float(probabilities[1])
        }
    }