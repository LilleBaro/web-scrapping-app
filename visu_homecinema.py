import pandas as pd 
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def visualisation_home():
    df = pd.read_csv("C:/Users/msqur/Documents/Data Collection/webscrap_project/data/cleaned_home_cinema.csv")
    plt.figure(figsize=(16,10))
    scatter = sns.scatterplot(data=df,x="prix",y='dimension',hue="marque")
    plt.legend()
    plt.xlabel("Prix")
    plt.ylabel("Dimension en pouce")
    plt.title(" Scatter plot des prix en fonction de la dimension de l'ecran")
    st.pyplot(scatter.get_figure())

    plt.figure(figsize=(16,10))
    scatter_etat = sns.scatterplot(data=df,x="prix",y='dimension',hue="etat")
    plt.legend()
    plt.xlabel("Prix")
    plt.ylabel("Dimension en pouce")
    st.pyplot(scatter_etat.get_figure())
    
    

visualisation_home()
