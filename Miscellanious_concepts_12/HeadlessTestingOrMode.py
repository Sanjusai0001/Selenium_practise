import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.headless = True

    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver


driver = headless_chrome()
driver.get("https://www.dummyticket.com/")
# driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.quit()
