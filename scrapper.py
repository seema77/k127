from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  

START_URL = "https://science.nasa.gov/exoplanets/exoplanet-catalog/"
browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(2)
planets_data=[]

def scrape():
    for i in range(0,10):
        print(f'Scrapping page {i+1}....')
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for planet in soup.find_all("div",class_ = 'hds-content-item'):
            planet_info=[]
            planet_info.append(planet.find('h3',class_='heading-22').text.strip())
            information_to_extract=["Light-Years From Earth","Planet Mass","Stellar Magnitude"
                                    ,"Discovery Date"]
            for info_name in information_to_extract:
                try:
                    planet_info.append(planet.select_one(f'span:-soup-contains("{info_name}")')
                    .find_next_sibling('span').text.strip())

                except:
                    planet_info.append("Unknown")
            planets_data.append(planet_info)
        print(planets_data)

scrape()

