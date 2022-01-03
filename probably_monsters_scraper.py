from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_probably_monsters():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.set_window_position(-1000,100)
    driver.maximize_window()
    driver.get("https://www.probablymonsters.com/careers/")

    db = TinyDB('db.json')
    job_list = []

    time.sleep(1)

    position_list = driver.find_element_by_class_name('et_pb_accordion_item_3')
    position_list.click()
    time.sleep(1)
    positions = position_list.find_elements_by_class_name('job-item')
    for position in positions:
        title = position.find_element_by_class_name('job-title').text
        company = "Probably Monsters"
        url = 'https://www.probablymonsters.com/job/#' + position.find_element_by_class_name('view-job-button').get_attribute('id')

        job = create_job(title, company, '', url)
        if len(db.search(where('URL') == url)) == 0:
                    db.insert(job)
                    job_list.append(job)

    driver.close()
    return job_list
