import streamlit as st
from selenium import webdriver 
from selenium.webdriver.common.by import By 
import scrapping
from wallpaper import set_background

project = st.sidebar.selectbox("Quelles données voulez vous scrapper?",("Scrapping d'ordinateurs","Scrapping de telephone","Scrapping de home cinema"))

def show_scrapping_page():
    st.title("Scrapping de données d'ordinateur")
    pages_scrapper = st.slider("Combien de pages voulez-vous scrapper?",
                                    1,100,1)
    click = st.button("Lancer scrapping")
    if click:
        st.write("Scrapping de données........")
        df = scrapping.scrapping_ordi(pages_scrapper)
        st.dataframe(df)

def show_tel_scrapping_page():
    st.title("Scrapping de données de téléphone portable")
    pages_scrapper = st.slider("Combien de pages voulez-vous scrapper?",
                                    1,100,1)
    click = st.button("Lancer scrapping")
    if click:
        st.write("Scrapping de données........")
        df = scrapping.scrapping_portable(pages_scrapper)
        st.dataframe(df)

def show_home_scrapping_page():
    st.title("Scrapping de données de home cinema")
    pages_scrapper = st.slider("Combien de pages voulez-vous scrapper?",
                                    1,100,1)
    click = st.button("Lancer scrapping")
    if click:
        st.write("Scrapping de données........")
        df = scrapping.scrapping_home(pages_scrapper)
        st.dataframe(df)

if project == "Scrapping d'ordinateurs":
    show_scrapping_page()
    set_background("backgrounds/ordi_wallpaper.jpeg")
elif project == "Scrapping de telephone":
    show_tel_scrapping_page()
    set_background("backgrounds/phone_wallpaper.jpeg")
elif project == "Scrapping de home cinema":
    show_home_scrapping_page()
    set_background("backgrounds/home_cinema_wallpaper.jpeg")

