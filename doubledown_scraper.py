from selenium import webdriver
from tinydb import TinyDB, where
import time

def scrape_doubledown():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://jobs.jobvite.com/doubledowninteractive/?nl=1&fr=true")
    
    db = TinyDB('db.json')
    job_list = []

    job_lists = driver.find_elements_by_class_name('jv-job-list-name')
    for pos_list in job_lists:
        title = pos_list.text
        company = "Doubledown Interactive"
        url = pos_list.find_element_by_tag_name('a').get_attribute('href')
        job = {
            'title' : title,
            'company' : company,
            'description' : '',
            'URL' : url
        }

        if len(db.search(where('URL') == url)) == 0:
            db.insert(job)
            job_list.append(job)


        #print(url)
        # print(title)

    return job_list
