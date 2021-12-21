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

def scrape_epic_games():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.epicgames.com/site/en-US/careers/jobs?country=United%20States&state=Washington&page=1")
    
    db = TinyDB('db.json')
    job_list = []

    try:
        jobs_container = driver.find_element_by_class_name('JobsViewstyles__FilteredResults-sc-xcdagw-2')
        job_postings = jobs_container.find_elements_by_tag_name('a')
    except:
        print("ERROR: GET EPIC GAME JOBS FAILED")
        return []

    for item in job_postings:
        try:
            title = item.find_elements_by_tag_name('div')[0].find_elements_by_tag_name('div')[0].text
        except:
            print("ERROR: GET EPIC GAMES JOB TITLE FAILED")
            return job_list
        company = 'Epic Games'
        url = item.get_attribute('href')
        print(url)
        job = {
            'title' : title,
            'company' : company,
            'description' : '',
            'URL' : url,
        }
        if len(db.search(where('URL') == url)) == 0:
            db.insert(job)
            job_list.append(job)

    # print(len(job_postings))

    print(len(job_list))

    driver.close()
    return job_list

# scrape_epic_games()