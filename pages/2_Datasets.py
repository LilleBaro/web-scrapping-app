import pandas as pd
import streamlit as st
import visu_ordi
from wallpaper import set_background

st.markdown("<h1 style='text-align: center; color: white;'> DATASETS </h1>", unsafe_allow_html=True)

st.markdown("""
A partir de cette page vous pouvez telecharger des jeux de données d':violet[ordinateurs], de :violet[telephone portable] ou encore de :violet[home cinema] deja scrapper a partir du site
            https://www.expat-dakar.com/
* **Python libraries** : :violet[Streamlit], :violet[Pandas], :violet[Selenium]  
""")

project = st.sidebar.radio("Datasets",("Ordinateur","Portable","Home cinema"))

# Fonction de loading des données

def load_data(dataframe,title,cleaned_data,key):
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)
    if st.button(title, key):
        st.subheader("Affiche les dimensions du jeu de données")
        st.write(f"Dimension du jeu de données: {str(dataframe.shape[0])} lignes et {str(dataframe.shape[1])} colonnees" )
        st.dataframe(dataframe)
        

        st.subheader("Affiche les dimensions du jeu de données nettoyé")
        st.write(f"Dimension du jeu de données: {str(cleaned_data.shape[0])} lignes et {str(cleaned_data.shape[1])} colonnees" )
        st.dataframe(cleaned_data)



st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)


if project == 'Ordinateur':
    load_data(pd.read_csv("data/ordinateur_expat.csv"), "Laptop data",pd.read_csv("data/cleaned_ordinateur_expat.csv"),"1")
    set_background("C:/Users/msqur/Documents/Data Collection/webscrap_project/backgrounds/ordi_wallpaper.jpeg")
elif project == "Portable":
    load_data(pd.read_csv("data/telephone_expat.csv"), "Smarphone data",pd.read_csv("data/cleaned_telephone.csv"),"2")
    set_background("C:/Users/msqur/Documents/Data Collection/webscrap_project/backgrounds/phone_wallpaper.jpeg")
elif project == "Home cinema":
    load_data(pd.read_csv("data/home_cinema.csv"), "Home cinema data",pd.read_csv("data/cleaned_home_cinema.csv"),"3")
    set_background("C:/Users/msqur/Documents/Data Collection/webscrap_project/backgrounds/home_cinema_wallpaper.jpeg")


