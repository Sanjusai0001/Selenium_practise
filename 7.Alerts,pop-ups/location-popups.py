import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
opts = webdriver.ChromeOptions()
opts.add_argument('--disable-notifications')  # adding this we can disable location-popups


serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=opts)
# serv_obj = webdriver.Chrome(driver)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(2)


# driver.refresh()
# time.sleep(2)




driver.close()