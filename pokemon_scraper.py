from selenium import webdriver
from tinydb import TinyDB, where
import time


def scrape_pokemon():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://boards.greenhouse.io/pokemoncareers")

    db = TinyDB('db.json')
    job_list = []
    time.sleep(1)
    department = driver.find_element_by_id('s2id_departments-select')
    department.click()
    time.sleep(1)
    departments = driver.find_elements_by_class_name('select2-results-dept-0')
    technology = departments[29]
    technology.click()
    time.sleep(1)
    office = driver.find_element_by_id('s2id_offices-select')
    office.click()
    time.sleep(1)
    offices = driver.find_elements_by_class_name('select2-results-dept-0')
    bellevue = offices[1]
    bellevue.click()
    time.sleep(1)
    openings = driver.find_elements_by_class_name('opening')
    for opening in openings:
        a = opening.find_element_by_tag_name('a')
        title = a.text.strip()
        if title != '':
            company = "Pokemon"
            url = a.get_attribute('href')
            job = {
                'title' : title,
                'company' : company,
                'description' : '',
                'URL' : url
            }
            if len(db.search(where('URL') == url)) == 0:
                db.insert(job)
                job_list.append(job)


    driver.close()
    return job_list
