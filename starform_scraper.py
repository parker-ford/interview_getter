from selenium import webdriver
from tinydb import TinyDB, where
import time
from scraper_helper import create_job


def starform_scraper():
    PATH = "D:\Downloads\chromedriver_win32\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(5)
    driver.set_window_position(-1000,100)
    driver.maximize_window()
    driver.get("https://starform.co/careers")

    db = TinyDB('db.json')
    job_list = []

    