from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_suckerpunch():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://jobs.suckerpunch.com/?host=jobs.suckerpunch.com")

    db = TinyDB('db.json')
    job_list = []

    jobs_list = driver.find_element_by_class_name('sc-tilXH')
    jobs = jobs_list.find_elements_by_tag_name('a')
    for job in jobs:
        title = job.find_element_by_tag_name('div').find_element_by_tag_name('div').text
        company = 'Suckerpunch'
        url = job.get_attribute('href')
        job = create_job(title, company, '', url)
        if len(db.search(where('URL') == url)) == 0:
            db.insert(job)
            job_list.append(job)

    driver.close()
    return job_list