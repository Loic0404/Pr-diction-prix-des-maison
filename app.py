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

# Création du titre

st.title("Prédiction immobilière")

# Création d'une liste contenant tous les départements

zipcode_source = [98001, 98002 ,98003, 98004, 98005, 98006, 98007, 98008, 98010, 98011, 98014, 98019, 98022, 98023, 98024, 98027, 98028, 98029, 98030, 98031, 
98032, 98033, 98034, 98038, 98039, 98040, 98042, 98045, 98052, 98053, 98055, 98056, 98058, 98059, 98065, 98070, 98072, 98074, 98075, 98077, 98092, 98102, 
98103, 98105, 98106, 98107, 98108, 98109, 98112, 98115, 98116, 98117, 98118, 98119, 98122, 98125, 98126, 98133, 98136, 98144, 98146, 98148, 98155, 98166, 
98168, 98177, 98178, 98188, 98198, 98199]

# Création des élements pour que l'utilisateur entre ses informations

bedrooms = st.slider('Nombres de chambres :', min_value = 0 , max_value= 20, step = 1 )
bathrooms = st.slider ('Nombres de salle de bain :', min_value = 0 , max_value = 8, step = 1)
sqft_living = st.slider ("Pied carré de l'espace de vie :", min_value = 290, max_value = 14000, step = 1)
sqft_lot = st.number_input( "Entrez le nombre de pied carré souhaiter pour l'espace terrestre :")
floors = st.slider ("Nombre d'étage :", min_value = 1, max_value = 4, step = 1)
waterfront = st.radio(" Voulez-vous une vue mer? ", (" Oui ", " Non "))
if waterfront == "Oui":
    waterfront = 1
else:
    waterfront = 0
view = st.slider ('Note de la vue :', min_value = 0, max_value = 4, step = 1)
condition = st.slider ("Etat de l'appartement :", min_value = 1, max_value = 5, step = 1)
grade = st.slider ('Qualitée :', min_value = 1, max_value = 13, step = 1)
sqft_above = st.slider ("Pied carré de l'espace intérieur au dessus de la mer :", min_value = 290, max_value = 9500, step = 1)
sqft_basement = st.slider ("Pied carré de l'espace intérieur au dessous de la mer :", min_value = 0, max_value = 4900, step = 1)
yr_build = st.slider ('Année de constuction :', min_value = 1900, max_value = 2015, step = 1)
yr_basement = st.slider ('Année de rénovation :', min_value = 1900, max_value = 2015, step = 1)
zipcode = st.selectbox (" Choisissez le code postal :" , zipcode_source)

# Création d'un dictionnaire pour les choix en cours

choix_en_cours = {
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "sqft_living": sqft_living,
    "sqft_lot": sqft_lot,
    "floors": floors,
    "waterfront": waterfront,
    "view": view,
    "condition": condition,
    "grade": grade,
    "sqft_above": sqft_above,
    "sqft_basement": sqft_basement,
    "yr_build": yr_build,
    "yr_basement": yr_basement
}

# Pour récupérer le code postal
for code in zipcode_source:
    choix_en_cours[code] = 0
choix_en_cours[zipcode] = 1

choix_en_cours = [choix_en_cours[cle] for cle in choix_en_cours]
choix_en_cours = model.predict([choix_en_cours])

# Création du boutton pour que l'utilsateur valide ses choix

if st.button('Calcul'):
    st.success(choix_en_cours[0])