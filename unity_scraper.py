from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
from tinydb import TinyDB, where


def get_positions(positions, job_list, db):
    try:
        listings = positions.find_elements_by_class_name('component-open-positions__position')
    except:
        print("ERROR: GET UNITY POSITIONS FAILED")
        return

    for item in listings:

        title = item.find_element_by_tag_name('p').text.strip()
        company = 'Unity'
        url = item.find_element_by_tag_name('a').get_attribute('href')

        job = {
            'title' : title,
            'company' : company,
            'description' : '',
            'URL' : url
        }

        if len(db.search(where('URL') == url)) == 0:
            db.insert(job)
            job_list.append(job)

def scrape_unity():

    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://careers.unity.com/location/bellevue")
    
    db = TinyDB('db.json')
    print(len(db.all()))
    job_list = []

    try:
        position_lists = driver.find_elements_by_class_name('component-open-positions__list')
    except:
        print("ERROR: GET UNTIY POSITION LIST FAILED")
        return []
    design_positions = position_lists[1]
    engineering_positions = position_lists[2]
    get_positions(design_positions, job_list, db)
    get_positions(engineering_positions, job_list, db)

    driver.close()
    # print(len(db.all()))
    return job_list

#scrape_unity()