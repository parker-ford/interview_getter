from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_rec_room():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.set_window_position(-1000,100)
    driver.maximize_window()
    driver.get("https://recroom.com/careers#openings")

    db = TinyDB('db_test.json')
    job_list = []

    driver.find_element_by_id('dropdownButton').click()
    time.sleep(1)
    dropdown = driver.find_element_by_id('departmentDropdown')
    items = dropdown.find_elements_by_tag_name('div')
    items[3].click()
    time.sleep(1)
    poitions = driver.find_elements_by_class_name('job-item')
    for position in positions:
        #yui_3_17_2_1_1641184594955_131 4760465003
    time.sleep(9999)

    driver.close()
    return job_list

scrape_rec_room()