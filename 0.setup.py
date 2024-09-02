


# SELENIUM-3

# from selenium import webdriver
# driver.webdriver.Chrome(executable_path=""C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")

# SELENIUM-4

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager


# serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)
# serv_obj = webdriver.Chrome(driver)