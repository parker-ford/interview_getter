from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_bigfish():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.set_window_position(-1000,100)
    driver.maximize_window()
    driver.get("https://careers.aristocrat.com/aristocratdigital/au/en/big-fish-jobs")

    db = TinyDB('db.json')
    job_list = []

    time.sleep(1)

    driver.find_element_by_xpath('//button[@data-ph-at-id="cookie-close-link"]').click()

    time.sleep(1)

    driver.find_element_by_xpath('//button[@data-ph-tevent-attr-trait47="City"]').click()
    time.sleep(5)
    #cities = driver.find_elements_by_class_name('result-text')
    cities = driver.find_element_by_xpath('//ul[@data-ph-at-id="facet-results-list"]').find_elements_by_tag_name('li')
    print(len(cities))
    cities[5].find_element_by_tag_name('input').click()
    print('test')
    time.sleep(9999)

scrape_bigfish()