import streamlit as st
import joblib

model = joblib.load("regression.joblib")

st.title("House Price Prediction")

size = st.number_input("Taille de la maison", min_value=0.0)
nb_rooms = st.number_input("Nombre de chambres", min_value=0)
garden = st.number_input("Présence d'un jardin (0 = non, 1 = oui)", min_value=0, max_value=1)

if st.button("Prédire"):
    prediction = model.predict([[size, nb_rooms, garden]])
    st.write("Prix prédit :", prediction[0])