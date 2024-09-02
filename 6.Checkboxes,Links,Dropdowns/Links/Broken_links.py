import time
import requests as req
from selenium import webdriver
from selenium.webdriver.common.by import By

web_driver = webdriver.Chrome()


web_driver.get("http://www.deadlinkcity.com/")
web_driver.maximize_window()

total_links = web_driver.find_elements(By.TAG_NAME,"a")
count = 0

print(len(total_links))

# using try method for no exceptions

for link in total_links:
    url = link.get_attribute('href')
    try:
        res = req.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is broken link")
        count+=1
    else:
        print(url," is Valid link")


print("Total no. of Broken links -", count)

print("Total no. of links -", len(total_links))

web_driver.close()