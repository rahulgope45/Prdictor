import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

def train_model():
    # load dataset
    data = pd.read_csv("data.csv")

    #Features and target
    x = data[["team1_strength", "team2_strength"]]
    y= data["winner"]

    # Split
    X_train, X_test, y_train, y_test =train_test_split(x,y, test_size=0.2, random_state=42 )

    #Logistic Regression
    model = LogisticRegression()
    model.fit(X_train,y_train)




    #saving
    joblib.dump(model,"model.pkl")
    print("Model Trained and saved in model.pkl")

if __name__ == "__main__":
  train_model()