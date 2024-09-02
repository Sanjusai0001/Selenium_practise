import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# time.sleep(2)


#  mm/dd/yyyy

# driver.find_element(By.XPATH,"//input[@class='datepicker']").send_keys('08/14/2024')
# time.sleep(2)


# add date with logic

year='2021'
month='July'
date='20'


driver.find_element(By.XPATH,"//input[@id='datepicker']").click()  # date-picker

# Useful in travel applications

# Expected month and date

while True:
    m = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    y = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if m == month and y == year:
        break;
    else:
        # driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()  # next
        # future
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()  # previous
        # past
time.sleep(2)

# Expected Day

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tr//td//a")

for dt in dates:
    if dt.text==date:
        dt.click()
        break

time.sleep(2)

driver.close()