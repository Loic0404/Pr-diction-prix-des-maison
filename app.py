import pandas as pd
import seaborn as sns
import matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
import sklearn as svm
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler , StandardScaler, RobustScaler, PolynomialFeatures
import pickle
import streamlit as st

pickle_in = open("model.pkl", "rb")
model = pickle.load(pickle_in)

st.tritre("Prédiction immobilière")

bedrooms = st.slider('bedrooms :', min_values = 0 , max_values= 20, step = 1 )
bathrooms = st.slider ('bathrooms :', min_values = 0 , max_values = 8, step = 1)
sqft_living = st.slider ('sqft_living :', min_values = 290, max_values = 14000, step = 1)
condition = st.slider ('condition :', min_values = 1, max_values = 5, step = 1)
yr_build = st.slider ('yr_build :', min_values = 1900, max_values = 2015, step = 1)

choix_en_cours = {
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "sqft_living": [sqft_living],
    "condition": [condition],
    "yr_build": [yr_build],
    "price": " Votre prix"
}

choix_en_cours = pd.DataFrame(choix_en_cours)
choix_en_cours = model.predict([[bedrooms, bathrooms , sqft_living, condition, yr_build]])

if st.button('Calcul'):
    st.success(choix_en_cours[0])