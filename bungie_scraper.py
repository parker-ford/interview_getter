from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_bungie():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://careers.bungie.com/jobs")

    db = TinyDB('db.json')
    job_list = []
    try:
        time.sleep(1)
        driver.find_element_by_id('department').click()
        time.sleep(1)
        driver.find_element_by_xpath('//option[@data-id="22334"]').click()
        time.sleep(1)
        posting_list = driver.find_element_by_class_name('sc-1jrbkrf-2')
        postings = posting_list.find_elements_by_tag_name('a')
        for posting in postings:
            title = posting.find_element_by_tag_name('p').text
            company = "Bungie"
            url = posting.get_attribute('href')
            job = create_job(title,company,'',url)
            if len(db.search(where('URL') == url)) == 0:
                    db.insert(job)
                    job_list.append(job)

    except:
        print("Error getting bungie jobs")
        return []


    driver.close()
    return job_list
    