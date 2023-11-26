# Streamlit Documentation: https://docs.streamlit.io/


import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image  # to deal with images (PIL: Python imaging library)

# title of the sidebar
html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">Car Price Prediction </h2>
</div>"""
st.sidebar.markdown(html_temp,unsafe_allow_html=True)

# title of the body
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App</h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)


# defining variables for user input "km", "Gears", "Displacement_cc","Weight_kg", "Type"
hp_kW = st.sidebar.slider("What is the Hourse power in kW?", 40, 294, step=1)
age = st.sidebar.slider("What is the age of your car?", 0, 3, step=1)
km = st.sidebar.slider("What is total KM the your car?", 0, 317000, step=100)
Gears = st.sidebar.slider("How many gears in your car?", 5, 8, step=1)
make_model = st.sidebar.selectbox("what model of your car?", ['Audi A1','Audi A3','Opel Insignia','Opel Astra','Opel Corsa','Renault Clio','Renault Espace' ,'Renault Duster'])
Gearing_Type = st.sidebar.selectbox("What is the Gearing type of yor car?", ['Manual','Automatic' ,'Semi-automatic'])


# converting user inputs into dictionary format
my_dict = {
    "hp_kW": hp_kW,
    "age": age,
    "km": km,
    'Gears': Gears,
    "make_model": make_model,
    "Gearing_Type": Gearing_Type,
}

# To load machine learning model
import pickle
filename = "my_model.pkl"
model=pickle.load(open(filename, "rb"))


df = pd.DataFrame.from_dict([my_dict])
st.table(df)

# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success(result[0])
