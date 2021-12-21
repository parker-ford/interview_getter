from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_intercept_games():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.interceptgames.com/#jobs")

    db = TinyDB('db.json')
    job_list = []

    listings = driver.find_elements_by_class_name('jobs__listing')
    for listing in listings:
        title = listing.find_element_by_tag_name('h4').text
        company = 'Intercept Games'
        url = listing.get_attribute('href')
        job = create_job(title,company,'',url)

        if len(db.search(where('URL') == url)) == 0:
            db.insert(job)
            job_list.append(job)


    driver.close()
    return job_list
