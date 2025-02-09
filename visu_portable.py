import pandas as pd 
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def visualisation_portable():
    df = pd.read_csv("data/cleaned_telephone.csv")
    sampled_df = df.sample(frac=0.1,replace=True)
    sns.set_theme()
    plt.figure(figsize=(30,20))
    scatter = sns.scatterplot(data=sampled_df,x="prix",y="stockage",hue="marque")
    plt.title("Scatter plot du stockag en fonction des prix")
    plt.xlabel("prix")
    plt.ylabel("stockage")
    stockage_values = sorted(sampled_df["stockage"].unique())  
    plt.yticks([s for s in stockage_values if s % 64 == 0])  
    plt.xticks([p for p in range(0,1000000,10000)])
    plt.legend()
    st.pyplot(scatter.get_figure())


    
    
visualisation_portable()
