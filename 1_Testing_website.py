from selenium import webdriver


# SELENIUM-4

import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager

serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# serv_obj = webdriver.Chrome(driver)

#SAVED IN SCRIPTS(C:\Python310\Scripts)***
# driver=webdriver.Chrome()

# driver.get("https://www.flipkart.com")
driver.get("file:///C:/Users/sanju/OneDrive/Documents/Training/Laundry-site%20Task/Home%20page.html")
# driver.get("https://www.google.co.in")
driver.maximize_window()

#TITLE

org_title = driver.title
exp_title = 'BlackBundle'
if exp_title == org_title:
    print('title is matched')
else:
    print('title is not matched' )

driver.find_element(By.XPATH,'//*[@id="signup"]/a').click()

time.sleep(2)

driver.find_element(By.ID,'name').send_keys("sanju00")
driver.find_element(By.ID,'password').send_keys("sanjusai012")

time.sleep(2)

driver.find_element(By.TAG_NAME,'button').click

time.sleep(1)



driver.close()

