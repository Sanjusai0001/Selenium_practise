import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///C:/Users/sanju/OneDrive/Documents/Training/Laundry-site%20Task/Home%20page.html")
driver.maximize_window()
time.sleep(2)

driver.save_screenshot("C:\\Users\sanju\PycharmProjects\SELENIUM\12.Miscellanious_concepts_12\homepage.png")

# driver.save_screenshot(os.getcwd() + "\\homepage.png")

# driver.get_screenshot_as_file(os.getcwd() + "\\homepage.png")

# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64() # binary format


driver.close()
