import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def ChromeSetup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)

    return driver

def ChromeFunction():
    driver = ChromeSetup()
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(2)

    return driver


def DateDetails():
    PresentTime = time.time()
    details = time.ctime(PresentTime)
    print(details)
    return

# DateDetails()







