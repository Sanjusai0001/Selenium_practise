import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

#        IFRAMES (Inner Frames)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outer_frame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")  # OUTER IFRAME
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")    # INNER IFRAME
driver.switch_to.frame(inner_frame)


driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys('Hello')

time.sleep(2)

# driver.switch_to.parent_frame() # to Parent frame

driver.close()