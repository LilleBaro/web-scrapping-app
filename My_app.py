import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

page = st.sidebar.radio("Sommaire :",("Scrapping","Jeu de données","Evaluation"))

if page == "Scrapping":
    st.write("""
Le :red[web scraping], également connu sous le terme de harvesting, désigne une technique avancée d’extraction et d’organisation automatisées des données issues du Web. Il s’agit d’un procédé permettant de collecter des informations à partir de sites internet grâce à des scripts ou des programmes spécifiques, dans le but de les traiter, de les structurer et de les exploiter selon divers besoins.

Cette approche représente l’une des méthodes les plus répandues du data mining appliqué aux données en ligne. Elle permet d’accéder à de vastes quantités d’informations disséminées sur le Web, souvent non structurées, et de les transformer en données exploitables pour différents usages. L’extraction de ces données peut servir à enrichir des bases de données, optimiser le référencement sur les moteurs de recherche, alimenter des modèles d’intelligence artificielle, ou encore mener des études approfondies en analyse de données.

Loin d’être une simple collecte d’informations, le web scraping trouve des applications variées dans de nombreux domaines. Dans le secteur commercial, il est fréquemment utilisé pour surveiller la concurrence, analyser les tendances du marché ou encore automatiser l’agrégation de contenus. Dans le cadre scientifique, cette technique permet de récupérer des données essentielles à la recherche, notamment en sciences sociales, en économie ou en biologie. Enfin, sur le plan politique, le web scraping peut être employé pour analyser l’opinion publique, détecter des tendances électorales ou encore surveiller la diffusion d’informations sur les réseaux sociaux.
             """)

if page == "Jeu de données":
    st.write(""" Les 3 :red[jeux de données] disponoble sur la page Datasets sont des données du site internet
            https://www.expat-dakar.com/ scrapper à l'aide de l'extension google Webscrapper. Les jeux de données disponibles sont tous visualisable et telechargeable.
            L'onglet Scrapping data quant a elle permet de scapper en temps reel les données du site internet https://www.expat-dakar.com/ """)
    
if page == "Evaluation":
    st.write(""" L'onglet evaluation vous permet d'evaluer notre application web afin de l'améliorer dans le futur,
            ce formulaire a été fais à partir de Kobo Toolbox. """)
    