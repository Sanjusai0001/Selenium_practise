import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://www.orangehrm.com/")
driver.maximize_window()
time.sleep(1)


# windowID = driver.current_window_handle
# print(windowID) #EA23EDAFA7E337305E3FCBC108DF70FE  - 1st ID
#                 #C26806B379667726175D7E91BA57C5F9  - 2nd ID



driver.find_element(By.LINK_TEXT,"OrangeHRM").click()
Wind_ID = driver.window_handles

# 1st Approach

# parent_Wind = Wind_ID[0]
# child_Wind = Wind_ID[1]

# WINDOW ID's WILL CHANGE AFTER EVERY TIME WE BROWSE

# print(parent_Wind)  #32AECC097D9ABA9A5A553B3CA755BDBA
# print(child_Wind)   #FCDF211803A625711314D9548AEF952A


# driver.switch_to.window(child_Wind)
# print('title of the child window -',driver.title)
#
# driver.switch_to.window(parent_Wind)
# print('title of the parent window -',driver.title)


# 2nd Approach

# for wd in Wind_ID:
#     driver.switch_to.window(wd)
#     print(driver.title)

#     OUTPUT
# Human Resources Management Software | OrangeHRM
# Get to Know Us | Innovating HR Solutions | OrangeHRM


time.sleep(2)

for wd in Wind_ID:
    driver.switch_to.window(wd)
    if driver.title == 'Human Resources Management Software | OrangeHRM':
        driver.close()


driver.close()