import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException



def scrapping_ordi(pages):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)  # Ajout des options ici
    data =[]
    for i in range(1,pages+1):
        driver.get(f"https://www.expat-dakar.com/ordinateurs?page={i}")
        containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listing-card listing-card--tab listing-card--has-contact listing-card--has-content']")
        for container in containers:
            link_element = container.find_element(By.CSS_SELECTOR, 'a')
            header = container.find_element(By.CSS_SELECTOR,"[class= 'listing-card__header__tags']")
            img_link= container.find_element(By.CSS_SELECTOR,"[class='listing-card__image__resource vh-img']")
            try:
                details = link_element.get_attribute('data-t-listing_title')
                etat = header.find_element(By.CSS_SELECTOR, "[class^='listing-card__header__tags__item listing-card__header__tags__item--condition']").text
                marque = header.find_element(By.CSS_SELECTOR, "[class^='listing-card__header__tags__item listing-card__header__tags__item--make listing-card__header__tags__item--make']").text
                adresse = link_element.get_attribute("data-t-listing_location_title")
                prix = link_element.get_attribute("data-t-listing_price")
                image_lien = img_link.get_attribute('src')
                dic = {'details':details,'etat':etat,'marque':marque,'prix':prix,"adresse":adresse,"lien image":image_lien}
                data.append(dic)
            except NoSuchElementException as e:
                print(f"Elements introuvable")
        df_ordi = pd.DataFrame(data)
    return df_ordi

def scrapping_home(pages):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)  # Ajout des options ici

    data =[]
    for i in range(1,pages+1):
        driver.get(f"https://www.expat-dakar.com/tv-home-cinema?page={i}")
        containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listing-card listing-card--tab listing-card--has-contact listing-card--has-content']")
        for container in containers:
            img_link= container.find_element(By.CSS_SELECTOR,"[class='listing-card__image__resource vh-img']")
            link_element = container.find_element(By.CSS_SELECTOR, 'a')
            header = container.find_element(By.CSS_SELECTOR,"[class= 'listing-card__header__tags']")
            try:
                details = link_element.get_attribute('data-t-listing_title')
                etat = header.find_element(By.CSS_SELECTOR, "[class^='listing-card__header__tags__item listing-card__header__tags__item--condition']").text
                marque = header.find_element(By.CSS_SELECTOR, "[class^='listing-card__header__tags__item listing-card__header__tags__item--make listing-card__header__tags__item--make']").text
                adresse = link_element.get_attribute("data-t-listing_location_title")
                prix = link_element.get_attribute("data-t-listing_price")
                lien_image = img_link.get_attribute("src")
                dic = {'details':details,'etat':etat,'marque':marque,'prix':prix,"adresse":adresse,"lien image":lien_image}
                data.append(dic)
            except NoSuchElementException as e:
                print(f"Elements introuvable")
        df_home_cine = pd.DataFrame(data)
    return df_home_cine  

def scrapping_portable(pages):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)  # Ajout des options ici

    data =[]
    for i in range(1,pages+1):
        driver.get(f"https://www.expat-dakar.com/telephones?page={i}")
        containers = driver.find_elements(By.CSS_SELECTOR, "[class= 'listing-card listing-card--tab listing-card--has-contact listing-card--has-content']")
        for container in containers:
            link_element = container.find_element(By.CSS_SELECTOR, 'a')
            header = container.find_element(By.CSS_SELECTOR,"[class= 'listing-card__header__tags']")
            img_link= container.find_element(By.CSS_SELECTOR,"[class='listing-card__image__resource vh-img']")
            try:
                details = link_element.get_attribute('data-t-listing_title')
                etat = header.find_element(By.CSS_SELECTOR, "[class^='listing-card__header__tags__item listing-card__header__tags__item--condition']").text
                marque = header.find_element(By.CSS_SELECTOR, "[class^='listing-card__header__tags__item listing-card__header__tags__item--make listing-card__header__tags__item--make']").text
                adresse = link_element.get_attribute("data-t-listing_location_title")
                prix = link_element.get_attribute("data-t-listing_price")
                lien_image = img_link.get_attribute("src")
                dic = {'details':details,'etat':etat,'marque':marque,'prix':prix,"adresse":adresse,"lien image":lien_image}
                data.append(dic)
            except NoSuchElementException as e:
                print(f"Elements introuvable")
        df_portable = pd.DataFrame(data)
    return df_portable


