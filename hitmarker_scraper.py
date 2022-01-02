from selenium import webdriver
from tinydb import TinyDB, where
import time

from tinydb.utils import T
from scraper_helper import create_job

def scrape_hitmarker():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://hitmarker.net/jobs?location=alaska,usa+arizona,usa+california,usa+colorado,usa+hawaii,usa+idaho,usa+montana,usa+nevada,usa+new-mexico,usa+oregon,usa+utah,usa+washington,usa+wyoming,usa+remote-americas,remote+remote-north-america,remote+remote-usa,remote&level=entry+junior&contract=fullTime+partTime+contract+temp+freelance+commission+internship")

    job_list = []

    time.sleep(2)

    button = driver.find_element_by_xpath( "//*[text()='Load More'] " )
    print(button.text)
    button.click()
    time.sleep(2)

    button = driver.find_element_by_xpath( "//*[text()='Load More'] " )
    print(button.text)
    button.click()
    time.sleep(2)

    postings = driver.find_elements_by_class_name('mb-4')
    print(len(postings))
    for posting in postings:
        try:
            date = posting.find_element_by_class_name('text-echo').text
            title = posting.find_element_by_class_name('font-bold').text + ' (' + date + ')'
            company = posting.find_element_by_class_name('text-foxtrot').text
            url = posting.find_element_by_tag_name('a').get_attribute('href')
            # print(title)
            # print(company)
            # print(url)
            # print('======================')
            job = create_job(title, company, '', url)
            job_list.append(job)
        except:
            pass


    driver.close()
    return job_list

#scrape_hitmarker()