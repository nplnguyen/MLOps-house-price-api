from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("regression.joblib")


class House(BaseModel):
    size: float
    nb_rooms: int
    garden: int


@app.get("/predict")
def predict_get(size: float, nb_rooms: int, garden: int):
    prediction = model.predict([[size, nb_rooms, garden]])
    return {"y_pred": prediction[0]}


@app.post("/predict")
def predict_post(house: House):
    prediction = model.predict([[house.size, house.nb_rooms, house.garden]])
    return {"y_pred": prediction[0]}