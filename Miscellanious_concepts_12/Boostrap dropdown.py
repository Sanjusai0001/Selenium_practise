import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/?wmc-currency=USD")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.XPATH,"//*[@id='select2-billing_country-container']").click()
countries = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countries))

for country in countries:
    if country.text == "Japan":
        country.click()
        break




time.sleep(2)
driver.close()