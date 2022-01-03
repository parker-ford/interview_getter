from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_geocaching():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://boards.greenhouse.io/embed/job_board?for=geocaching&b=https%3A%2F%2Fwww.geocaching.com%2Fcareers")

    db = TinyDB('db.json')
    job_list = []
    postings = driver.find_elements_by_class_name('opening')
    print(len(postings))
    for posting in postings:
        info = posting.find_element_by_tag_name('a')
        title = info.text
        company = 'Geocaching'
        url = info.get_attribute('href')
        job = create_job(title,company,'',url)
        if len(db.search(where('URL') == url)) == 0:
            db.insert(job)
            job_list.append(job)


    driver.close()
    return job_list
