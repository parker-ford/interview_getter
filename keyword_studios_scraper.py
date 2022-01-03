from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job

def scrape_keyword_studio():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.set_window_position(-1000,100)
    driver.maximize_window()
    driver.get('https://www.keywordsstudios.com/careers/')

    db = TinyDB('db.json')
    job_list = []

    try:
        time.sleep(3)
        driver.find_element_by_xpath('//button[@aria-label="Accept"]').click()

        country = driver.find_element_by_id('country')
        country.click()
        options = country.find_elements_by_tag_name('option')
        time.sleep(1)
        options[38].click()
        time.sleep(1)
        department = driver.find_element_by_id('department')
        department.click()
        departments = department.find_elements_by_tag_name('option')
        departments[10].click()
        time.sleep(1)
        driver.find_element_by_id('ajax-search').click()
        time.sleep(2)
        postings = driver.find_element_by_class_name('careers-grid')
        visible_postings = postings.find_elements_by_xpath('//div[@style="display: block;"]')
        print(len(visible_postings))
        for posting in visible_postings:
            title = posting.find_element_by_tag_name('h5').text
            company = 'Keyword Studio'
            url = posting.find_element_by_tag_name('a').get_attribute('href')
            job = create_job(title, company, '', url)

            if len(db.search(where('URL') == url)) == 0:
                    db.insert(job)
                    job_list.append(job)
    except:
        print('error getting keyword studio jobs')

    driver.close()
    return job_list
