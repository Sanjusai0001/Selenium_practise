import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(1)


ryt_clk = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

action = ActionChains(driver)

action.context_click(ryt_clk).perform()  # rightclick
driver.find_element(By.XPATH,"//ul[@class='context-menu-list context-menu-root']/li[2]").click()
time.sleep(1)

driver.switch_to.alert.accept()

time.sleep(2)


driver.close()










