from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job



def scrape_wizards_of_the_coast():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://company.wizards.com/en/careers")

    db = TinyDB('db.json')
    job_list = []
    try:
        location_list = driver.find_element_by_class_name('css-wH-46')
        locations = location_list.find_elements_by_tag_name('li')
        bellevue = locations[2]
        renton = locations[8]
        time.sleep(1)

        try:
            cookie = driver.find_element_by_class_name('css-2ISnN')
            cookie.click()
            time.sleep(1)
        except:
            pass
        
        bellevue.click()

        posting_list = driver.find_element_by_class_name('css-1Duux')
        postings = posting_list.find_elements_by_tag_name('a')
        for posting in postings:
            title = posting.find_element_by_tag_name('p').text
            company = 'Wizards of the Coast'
            url = posting.get_attribute('href')
            job = create_job(title,company,'',url)

            if len(db.search(where('URL') == url)) == 0:
                db.insert(job)
                job_list.append(job)

        time.sleep(1)
        renton.click()

        posting_list = driver.find_element_by_class_name('css-1Duux')
        postings = posting_list.find_elements_by_tag_name('a')
        for posting in postings:
            title = posting.find_element_by_tag_name('p').text
            company = 'Wizards of the Coast'
            url = posting.get_attribute('href')
            job = create_job(title,company,'',url)
            if len(db.search(where('URL') == url)) == 0:
                db.insert(job)
                job_list.append(job)

    except:
        print("ERROR: GET WIZARDS OF THE COAST JOBS FAILED")
        return []

    driver.close()
    return job_list


