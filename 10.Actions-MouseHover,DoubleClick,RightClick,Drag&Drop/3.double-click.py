import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://qa-automation-practice.netlify.app/double-click")
driver.maximize_window()
time.sleep(1)


button = driver.find_element(By.ID,"double-click-btn")
button.click()  # single click
time.sleep(1)


action = ActionChains(driver)

action.double_click(button).perform()  # double click
time.sleep(2)

result = driver.find_element(By.ID,"double-click-result")
print(result.text)

driver.close()










