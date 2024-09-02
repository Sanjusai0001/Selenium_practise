import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#        FRAMES

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

driver.switch_to.frame('frame-one796456169')  # entering into frame

driver.find_element(By.ID,"RESULT_TextField-0").send_keys('karan')

driver.switch_to.default_content()   # exiting from frame and into main webpage

# we can use this method in multiple frames

time.sleep(2)


driver.close()