from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_undead_labs():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.set_window_position(-1000,100)
    driver.maximize_window()
    driver.get("https://undeadlabs.com/jobs/#")

    db = TinyDB('db.json')
    job_list = []

    try:
        postings = driver.find_elements_by_class_name('BambooHR-ATS-Jobs-Item')
        for posting in postings:
            info = posting.find_element_by_tag_name('a')
            title = info.text
            company = "Undead Labs"
            url = info.get_attribute('href')
            job = create_job(title, company, '', url)
            if len(db.search(where('URL') == url)) == 0:
                db.insert(job)
                job_list.append(job)
    except:
        print("Error getting undead labs jobs")


    driver.close()
    return job_list

