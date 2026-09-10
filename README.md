\# MLOps - House Price Prediction API



\## Description



Ce projet consiste à déployer un modèle de Machine Learning permettant de prédire le prix d'une maison à partir de trois caractéristiques :



\- `size` : taille de la maison

\- `nb\_rooms` : nombre de chambres

\- `garden` : présence d'un jardin (`0` ou `1`)



Le modèle utilisé est une régression linéaire entraînée avec Scikit-learn.



\## Architecture



Le projet utilise :



\- Python

\- Scikit-learn

\- FastAPI

\- Streamlit

\- Docker

\- Uvicorn



Le modèle entraîné est sauvegardé dans `regression.joblib`.



\## Structure du projet



```text

MLOps-house-price-api/

│

├── main.py                  # API FastAPI

├── model\_app.py             # Application Streamlit

├── train\_model.py           # Entraînement du modèle

├── regression.joblib        # Modèle entraîné

├── houses.csv               # Jeu de données

├── requirements.txt         # Dépendances Python

├── Dockerfile               # Configuration Docker

├── quantization\_II.ipynb    # Notebook du TP

└── .gitignore

