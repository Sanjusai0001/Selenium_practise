import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#  Authentication popups

# driver.get('https://the-internet.herokuapp.com/basic_auth')
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')  # bypassing (injecting the username & password)
driver.maximize_window()
time.sleep(2)




driver.quit()






