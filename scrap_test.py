import pandas as pd
import streamlit as st
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager



# Initialisation du navigateur Selenium
options = Options()
options.add_argument("--headless")  # Mode sans interface graphique
service = Service(executable_path="chromedriver")  # Assurez-vous que chromedriver est installé
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URLs des différentes catégories
URLS = {
    "Computers": "https://www.expat-dakar.com/ordinateurs?page=",
    "Telephones": "https://www.expat-dakar.com/telephones?page=",
    "Cinema": "https://www.expat-dakar.com/cinema?page="
}

# Fonction de scraping
def scrape_expats_dakar(category, pages):
    url_base = URLS[category]
    data = []

    for p in range(1, pages + 1):
        url = f"{url_base}{p}"
        driver.get(url)  # Charger la page
        time.sleep(3)  # Pause pour le chargement
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "listings-cards__list-item"))
        )
        soup = bs(driver.page_source, 'html.parser')
        infos = soup.find_all('div', class_='listings-cards__list-item')

        for info in infos:
            try:
                details = info.find('div', class_='listing-card_header_title').text.strip()
                etat = info.find('span', class_='listing-card_headertagsitem listing-cardheadertagsitem--condition listing-cardheadertags_item--condition_new').text.strip()
                marque = info.find('div', class_='listing-card_header_tags').text.strip().replace(etat, '') 
                prix = info.find('span', class_='listing-card__price').text.strip().replace('F Cfa', '').replace(' ', '')
                adresse = ' '.join(info.find('div', class_="listing-card_header_location").text.strip().split()).replace(',', '')
                image_tag = info.find('img', class_='listing-card_image_resource vh-img')
                image_lien = image_tag['src'] if image_tag else "N/A"

                data.append({
                    'details': details,
                    'etat': etat,
                    'marque': marque,
                    'prix': prix,
                    'adresse': adresse,
                    'image_lien': image_lien
                })

            except Exception as e:
                print(f"Erreur lors du scraping : {e}")
                pass

    return pd.DataFrame(data)

# Interface Streamlit
st.markdown("<h1 style='text-align: center; color: black;'>MY DATA SCRAPER APP</h1>", unsafe_allow_html=True) 
st.markdown("This app scrapes and downloads data from Expat-Dakar.")

st.sidebar.markdown("*User Input Features*")
category = st.sidebar.selectbox("Choose category", list(URLS.keys()))
pages = st.sidebar.number_input("Number of pages to scrape", min_value=1, value=2)
scrape_button = st.sidebar.button("Start Scraping")

if scrape_button:
    st.write(f"Scraping *{category}* data... This may take a few minutes.")
    df = scrape_expats_dakar(category, pages)
    
    if not df.empty:
        st.dataframe(df)
        st.success(f"Scraped {len(df)} items!")
        
        # Télécharger les données en CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv, f"{category}_data.csv", "text/csv")
    else:
        st.warning("No data found. Try again later.")

# Fermer le driver après utilisation
driver.quit()