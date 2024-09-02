import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Login or sign-in popups

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Sign in']").click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(2)

driver.quit()