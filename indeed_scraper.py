# import requests
# from bs4 import BeautifulSoup
# from requests.api import request
# import time


# search_terms = [
#     ["entry", "software", "engineer"],
#     ["technical", "artist"],
#     ["graphic", "engineer"],
#     [" unity"],
#     ["hlsl"],
#     ["glsl"],
#     ["shader"],
#     ["three", "js"],
#     ["new" , "grad", "software", "engineer"],
#     ["new", "grad" , "computer", "science"],
#     ["opengl"],

# ]
# found_jobs = []

# def search_job(job):
#     desc = job["desc"]
#     for term in search_terms:
#         search = True
#         for item in term:
#             search = search and item in desc.lower()
#         if search == True:
#             found_jobs.append(job)

# def test_indeed(URL):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
#     soup = BeautifulSoup(requests.get(URL, headers=headers).content, "html.parser")

#     job = {
#         "name" : "",
#         "company" : "",
#         "URL" : URL,
#         "desc" : ""
#     }

#     try:
#         name = soup.find(id="jobDescriptionText")
#         name = soup.find('h1')
#         job["name"] = name.text
#     except:
#         job["name"] = ''

#     company = soup.find("div", class_ ='jobsearch-InlineCompanyRating')
#     try:
#         job["company"] = company.text
#     except:
#         job["company"] = ''

#     try:
#         job_description = soup.find(id="jobDescriptionText")
#         desc_elements = job_description.find_all()
#         try:
#             job["desc"] += job_description.text.strip()
#         except:
#             job["desc"] += ''
#         for item in desc_elements:
#             job["desc"] += " "
#             job["desc"] += item.text.strip()
#     except:
#         job["desc"] += ''


#     search_job(job)


# def get_indeed_jobs(URL, num_jobs,page):
#     print("PAGE SEARCH: " , str(page))
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
#     soup = BeautifulSoup(requests.get(URL, headers=headers).content, "html.parser")
#     links = soup.find_all("a", class_ = 'tapItem')
#     for link in links:
#         test_indeed("http://indeed.com"+link["href"])
#         num_jobs = num_jobs + 1
#         print("number of jobs searched: " + str(num_jobs))
#     return num_jobs


# def scrape_indeed(num_jobs):
#     #start = time.time()
#     page = 0
#     for i in range(30):
#         URL = "https://www.indeed.com/jobs?l=Washington%20State&fromage=1&start=" + str(page) +"&vjk=c1458cde1cf2dd85"
#         num_jobs = get_indeed_jobs(URL,num_jobs,page)
#         page += 10

    
#     #end = time.time()
#     #print(end - start)

# test_list =[
#     {"name": "youtube", "company":"youtube", "URL":"https://youtube.com"},
#     {"name": "google", "company":"google", "URL":"https://google.com"},
#     {"name": "reddit", "company":"reddit", "URL":"https://reddit.com"},

# ]

# def scrape():
#     num_jobs = 0
#     scrape_indeed(num_jobs)

#     return found_jobs
#     #return test_list

#===========================================================================================================


# import csv
# from datetime import datetime
# from msedge.selenium_tools import Edge, EdgeOptions
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from scraper_helper import *

PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"





#get indeed url based on position and location
def get_url(position,location):
    template = 'https://www.indeed.com/jobs?q={}&l={}'
    position = position.replace(' ', '+')
    location = location.replace(' ', '+')
    url = template.format(position, location)
    return url
    #return 'https://www.indeed.com/jobs?q&l=Washington%20State&fromage=1&vjk=3578003a2d347d00'
    #return 'https://www.indeed.com/jobs?q&l=Washington%20State&fromage=1&vjk=6ab8f40d53af4b1a'

def get_record(card,driver):
    "TODO: get job-title, company, description, url"

    job = {
        "title" : "",
        "company" : "",
        "description" : "",
        "URL" : ""
    }

    try:
        job_title = card.find_element_by_class_name('jobTitle').find_elements_by_tag_name('span')[-1].text
        job["title"] = job_title
    except:
        job["title"] = ''

    try:
        job_company = card.find_element_by_class_name('companyName').text
        job["company"] = job_company
    except:
        job["company"] = ''

    if job["company"] != 'Indeed Gigs':
        try:
            link = card.find_element_by_xpath("../../..")
            job["URL"] = link.get_attribute('href')
            link.send_keys(Keys.CONTROL + Keys.ENTER)
            p = driver.current_window_handle
            chwd = driver.window_handles
            for w in chwd:
                if(w!=p):
                    driver.switch_to_window(w)
            time.sleep(.5)
            job_desc = driver.find_element_by_id('jobDescriptionText').text
            job["description"] = job_desc
            driver.close()
            time.sleep(.5)
            driver.switch_to_window(p)
        except:
            job["description"] = ''

    return job

def get_page_records(cards, job_list, link_set, driver):
    for card in cards:
        job = get_record(card,driver)
        #revert to:
        # if record[0]:
        if search_job(job, link_set):
            job_list.append(job)
            link_set.add(job["URL"])

def scrape():

    start = time.time()

    scraped_jobs = []
    link_set = set()

    url = get_url('software engineer','Washington State')
    # print(url)
    # options = EdgeOptions()
    # options.use_chromium = True
    # driver = Edge(options=options)
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.get(url)
    print(url)
    time.sleep(1)
    driver.find_element_by_id('filter-dateposted').click()
    time.sleep(1)
    driver.find_element_by_class_name('yosegi-FilterPill-dropdownListItem').click()
    time.sleep(5)

    i = 0
    while True:
        #TODO find card class
        #print("cards")
        try:
             driver.find_element_by_id('popover-x-button-close').click()
        except:
            pass
        cards = driver.find_elements_by_class_name("slider_item")
        get_page_records(cards, scraped_jobs, link_set, driver)
        try:
            driver.find_element_by_xpath('//a[@aria-label="Next"]').click()
        except NoSuchElementException:
            print("No such element")
            break
        except ElementNotInteractableException:
            driver.find_element_by_id('popover-x-button-close').click()
            get_page_records(cards, scraped_jobs,driver)
        i = i + 1

    # print("Jobs:")
    # for job in scraped_jobs:
    #     print( job["title"] + " | " + job["company"] )
    #     print(job["description"][0:250])
    #     print(job["URL"])
    #     print("=================================================================\n")

    # print(len(scraped_jobs))

    end = time.time()

    total_time = end - start
    try:
        f  = open("test.txt","w")
        for job in scraped_jobs:
            f.write("TITLE: " + job["title"] + "\n")
            f.write("COMPANY: " + job["company"] + "\n")
            f.write("\n" + job["URL"] + "\n")
            f.write("============================================================================\n")
    
        f.write("\n\n Number of jobs scraped: " + str(len(scraped_jobs)))
        f.write("\n Number of pages searched: " + str(i))
        f.write("\n Time to complete: " + str(total_time))

        f.close()
    except:
        print("error in writing to test")

    driver.quit()


scrape()


#https://www.youtube.com/watch?v=eN_3d4JrL_w&t=110s&ab_channel=IzzyAnalytics
#https://github.com/israel-dryer/Indeed-Job-Scraper/blob/master/indeed-job-scraper-selenium.ipynb

