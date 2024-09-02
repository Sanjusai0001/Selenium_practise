import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
# time.sleep(2)


# if send_keys() method won't work use this method

driver.find_element(By.XPATH,"//input[@id='dob']").click()


dp_month = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectMonth']"))
dp_month.select_by_visible_text("Jul")

dp_year = Select(driver.find_element(By.XPATH,"//select[@data-handler='selectYear']"))
dp_year.select_by_visible_text("2000")

dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in dates:
    if date.text=='04':
        date.click()
        break

# 04.07.2000
# driver.find_element(By.XPATH,"//button[@data-handler='hide']").click()
time.sleep(2)

driver.close()