import pandas as pd 
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

def visualisation_ordi():
    df = pd.read_csv("data/cleaned_ordinateur_expat.csv")  
    
    sampled_df = df.sample(frac=0.1, replace=True)
    plt.figure(figsize=(20, 10))
    hist = sns.histplot(data=df, x="marque",hue="marque",bins=20)
    plt.title("Frequence des ordinateurs par marque")
    st.pyplot(hist.get_figure())

    plt.figure(figsize=(20, 10))
    scatter = sns.scatterplot(data=df, x="RAM", y="stockage", hue="marque")
    plt.title("Scatter plot des prix en fonction du stockage")
    plt.xlabel("Ram")
    plt.ylabel("Stockage")
    plt.legend()
    st.pyplot(scatter.get_figure())


    # plt.figure(figsize=(20, 10))
    # scatter = sns.scatterplot(data=df, x="prix", )


visualisation_ordi()
