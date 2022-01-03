from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_hair_brained_schemes():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.set_window_position(-1000,100)
    driver.maximize_window()
    driver.get("https://harebrained-schemes.com/careers/")

    db = TinyDB('db.json')
    job_list = []

    try:

        positions = driver.find_element_by_class_name('BambooHR-ATS-Jobs-List').find_elements_by_tag_name('li')
        for position in positions:
            info = position.find_element_by_tag_name('a')
            title = info.text
            company = 'Hair Brained Schemes'
            url = info.get_attribute('href')
            job = create_job(title, company, '', url)
            if len(db.search(where('URL') == url)) == 0:
                    db.insert(job)
                    job_list.append(job)

    except:
        print('Error getting hair brained schemes jobs')

    driver.close()
    return job_list
