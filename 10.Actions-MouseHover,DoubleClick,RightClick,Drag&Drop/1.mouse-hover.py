import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("file:///C:/Users/sanju/OneDrive/Documents/Training/webpage-task/homepage.html")
driver.maximize_window()
time.sleep(2)


#   MEMBERSHIP PROGRAMS ---> THE CHAMBERS

membership =  driver.find_element(By.XPATH,"//*[@id='membership-p']/a")
business = driver.find_element(By.XPATH,"//*[@id='membership-p']/div/ul/li[2]/a")

# MouseHover
action = ActionChains(driver)  # we must pass the driver instance


operation = action.move_to_element(membership).move_to_element(business).click()  # its just action
operation.perform()  # it will perform the action





time.sleep(2)


driver.close()