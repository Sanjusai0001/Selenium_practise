import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(2)

action = ActionChains(driver)

drag_ele = driver.find_element(By.ID,"draggable")
drop_ele = driver.find_element(By.ID,"droppable")


action.drag_and_drop(drag_ele, drop_ele).perform()   # Drag and Drop

time.sleep(2)


driver.close()










