import streamlit as st
import pandas as pd



st.markdown("<h1 style='text-align: center; color: black;'>MY DATA APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app allows you to download scraped data on motocycles from expat-dakar 
**Python libraries:** base64, pandas, streamlit
**Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
""")


# Fonction de loading des données
def load_data(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# Fonction faisant appel au fichier style.css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Stocker les données dans des variables
motos_scooters1 = pd.read_csv('data/motos_scooters1.csv')
motos_scooters2 = pd.read_csv('data/motos_scooters2.csv')
motos_scooters3 = pd.read_csv('data/motos_scooters3.csv')
motos_scooters4 = pd.read_csv('data/motos_scooters4.csv')
motos_scooters5 = pd.read_csv('data/motos_scooters5.csv')


    
local_css('style.css') #         

# Charger les données 
load_data(motos_scooters1, 'Motocycles data 1', '1')
load_data(motos_scooters2, 'Motocycles data 2', '2')
load_data(motos_scooters3, 'Motocycles data 3', '3')
load_data(motos_scooters4, 'Motocycles data 4', '4')
load_data(motos_scooters5, 'Motocycles data 5', '5')




 


