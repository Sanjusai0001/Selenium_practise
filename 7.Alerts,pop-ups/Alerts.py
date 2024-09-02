import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

#opens alert window

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click() # normalize-space() is similar to text()
time.sleep(5)


myAlert = driver.switch_to.alert  # Alert box

print(myAlert.text)
myAlert.send_keys("Hey,Ask Something...")


# myAlert.accept()  # close alert window by using OK button

myAlert.dismiss()   # close alert window by using Cancel button

# time.sleep(2)
# driver.quit()