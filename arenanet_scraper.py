from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_arenanet():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.arena.net/en/careers#listings")

    db = TinyDB('db.json')
    job_list = []

    try:
        try:
            driver.find_element_by_class_name('accept').click()
            time.sleep(1)
        except:
            pass
        lists = driver.find_element_by_class_name('mc5fe12b60_jobsList').find_elements_by_class_name('mca0efd9d2_headlineH4')
        for list in lists:
            jobs = list.find_elements_by_tag_name('li')
            for job in jobs:
                title = job.text
                company = "Arenanet"
                url = job.find_element_by_tag_name('a').get_attribute('href')
                print(title)
                print(url)
                job = create_job(title, company, '', url)
                if len(db.search(where('URL') == url)) == 0:
                        db.insert(job)
                        job_list.append(job)
    except:
        print("Error getting arena net jobs")
        return[]

    driver.close()
    return job_list
