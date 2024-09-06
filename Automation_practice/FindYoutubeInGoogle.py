import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH,"//a[@aria-label='Google apps']").click()

iframe = driver.find_element(By.XPATH,"//iframe[@role='presentation' and @name='app']")


driver.switch_to.frame(iframe)

# driver.find_element(By.XPATH,"//*[@id='yDmH0d']/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/ul/li[4]").click()
# driver.find_element(By.XPATH,"/html/body/div/c-wiz/div/div/c-wiz/div/div/div[2]/div[2]/div[1]/ul/li[4]").click()

driver.find_element(By.XPATH, "//span[text()='Maps']").click()




print("Test passed")

time.sleep(2)

driver.close()
