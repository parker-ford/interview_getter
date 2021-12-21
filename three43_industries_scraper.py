from selenium import webdriver
from tinydb import TinyDB, where
import time

def scrape_343_industries():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.343industries.com/careers")

    db = TinyDB('db.json')
    job_list = []

    positions = driver.find_elements_by_class_name('position')
    for pos in positions:
        title = pos.text.strip()
        company = '343 Industries'
        url = pos.find_element_by_tag_name('a').get_attribute('href')
        job = {
            'title' : title,
            'company' : company,
            'description' : '',
            'URL' : url
        }

        if len(db.search(where('URL') == url)) == 0:
            db.insert(job)
            job_list.append(job)

    return job_list
