from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import re as re
import time
import pandas as pd
from scraper_helper import *


search_terms = [
    "technical artist",
    "game dev",
    "software engineer",
]


def linkedin_search(driver, job_list, link_set, search_term, f2):
    #search_term = "software engineer"
    #search = driver.find_element_by_id('global-nav-typeahead')
    time.sleep(2)
    search = driver.find_element_by_xpath('//input[@aria-label="Search"]')
    search.send_keys(search_term)
    time.sleep(2)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_class_name('search-results__cluster-bottom-banner').click()
    time.sleep(3)
    search = driver.find_element_by_xpath('//input[@aria-label="City, state, or zip code"]')
    for i in range(20):
        search.send_keys(Keys.BACK_SPACE)
        time.sleep(.1)

    search.send_keys("Washington, United States")
    time.sleep(.1)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_class_name('search-reusables__filter-trigger-and-dropdown').click()
    time.sleep(.5)
    driver.find_elements_by_class_name('search-reusables__collection-values-item')[3].find_element_by_tag_name('label').click()
    time.sleep(2)
    driver.find_element_by_xpath('//button[@data-control-name="filter_show_results"]').click()
    time.sleep(3)

    page = 1
    while True:
        
        time.sleep(2)
        cards = driver.find_elements_by_class_name('jobs-search-results__list-item')

        for card in cards:

            job = {
                "title" : '',
                "company" : '',
                "description" : '',
                "URL" : ''
            }

            #card.click()
            #card.find_element_by_class_name('flex-grow-1').find_elements_by_tag_name('div')[0].click()
            try:
                card.find_element_by_tag_name('img').click()
            except ElementNotInteractableException:
                card.click()
            time.sleep(.75)
            job["title"] = card.find_element_by_class_name('flex-grow-1').find_elements_by_tag_name('div')[0].text
            job["company"] = card.find_element_by_class_name('flex-grow-1').find_elements_by_tag_name('div')[1].text
            job["description"] = driver.find_element_by_class_name('jobs-description').text
            job["URL"] = card.find_element_by_class_name('flex-grow-1').find_element_by_tag_name('a').get_attribute('href')

            if search_job(job, link_set, f2) == True:
                job_list.append(job)
                link_set.add(job["URL"])


        page = page + 1
        time.sleep(.5)
        try:
            driver.find_element_by_xpath(f' //button[@aria-label="Page {page}"]').click()
        except:
            break
    driver.find_element_by_class_name('global-nav__logo').click()

def scrape_linkedin():

    start = time.time()
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    f3 = open('login.txt', 'r')
    USERNAME = f3.readline().strip()
    PASSWORD = f3.readline().strip()
    job_list = []
    link_set = set()
    f2  = open("results.txt","w")

    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.linkedin.com/uas/login")
    time.sleep(2)

    email=driver.find_element_by_id("username")
    email.send_keys(USERNAME)
    password=driver.find_element_by_id("password")
    password.send_keys(PASSWORD)
    time.sleep(2)
    password.send_keys(Keys.RETURN)


    for term in search_terms:
        linkedin_search(driver, job_list, link_set, term, f2)

    
    end = time.time()
    total_time = end - start

    # print("Number of jobs: " + str(len(job_list)))
    # print("Time taken: ")

    try:
        f  = open("linkedin_jobs.txt","w")
        for job in job_list:
            f.write("TITLE: " + job["title"] + "\n")
            f.write("COMPANY: " + job["company"] + "\n")
            f.write("DESCC: " + job["description"][0:100] + '\n')
            f.write("" + job["URL"] + "\n")
            f.write("============================================================================\n")

        f.write("\n\n Number of jobs scraped: " + str(len(job_list)))
        f.write("\n Time to complete: " + str(total_time))

        f.close()
    except:
        print("error writing to jobs txt file")
    f2.close()

    driver.quit()

    return job_list

# for job in job_list:
#     print(job["title"])
#     print(job["company"])
#     print(job["description"][0:200])
#     print(job["URL"])