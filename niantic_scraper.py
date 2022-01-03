from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_niantic():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.set_window_position(-1000,100)
    driver.maximize_window()
    driver.get('https://careers.nianticlabs.com/openings/?office=seattle-area-bellevue-wa&department=engineering#positions')

    db = TinyDB('db_test.json')
    job_list = []

    time.sleep(1)

    #try:
    # try:
    driver.find_element_by_class_name('ark-cookiebar-buttons').find_element_by_tag_name('button').click()
    # except:
    #     pass

    #driver.find_element_by_xpath('//button[@data-control-name="filter_show_results"]').click()

    departments = driver.find_elements_by_class_name('positions-department')

    positions = departments[5].find_elements_by_xpath('//nc-filter-target[@calss="positions-position"]')
    print(len(positions))
    # for position in positions:
    #     info = position.find_element_by_tag_name('a')
    #     title = info.text
    #     company = 'Niantic'
    #     url = info.get_attribute('href')
    #     print(title)
    #     print(url)

    # except:
    #     print("error getting niantic jobs")

    driver.close()
    return job_list

scrape_niantic()