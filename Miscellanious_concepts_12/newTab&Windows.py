import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


#opens in new tab
driver.get("https://www.dummyticket.com/")
driver.maximize_window()
driver.implicitly_wait(5)

# BT_link = Keys.CONTROL+Keys.RETURN
# driver.find_element(By.LINK_TEXT,"Buy Ticket").send_keys(BT_link)



# new tab - Selenium4 - opens a new tab switches to new tab
"""
driver.get("https://www.dummyticket.com/")
driver.switch_to.new_window('tab') # it will open in new tab
driver.get("https://www.makemytrip.com/")
"""


# new window

driver.get("https://www.dummyticket.com/")
driver.switch_to.new_window('window') # it will open in new window
driver.get("https://www.makemytrip.com/")




time.sleep(4)
driver.quit()