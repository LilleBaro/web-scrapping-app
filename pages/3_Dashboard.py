import pandas as pd
import streamlit as st
import numpy as np
import visu_ordi
import visu_portable
import visu_homecinema

st.markdown("<h1 style='text-align: center; color: white;'>Visualisation des differents datasets</h1>", unsafe_allow_html=True)

project = st.sidebar.radio("Datasets",("Ordinateur","Portable","Home cinema"))

if project == "Ordinateur":
    visu_ordi.visualisation_ordi()
elif project == "Portable":
    visu_portable.visualisation_portable()
elif project == "Home cinema":
    visu_homecinema.visualisation_home()