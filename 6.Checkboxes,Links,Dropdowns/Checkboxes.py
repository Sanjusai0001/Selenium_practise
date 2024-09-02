import time

from selenium import webdriver
from selenium.webdriver.common.by import By

web_driver = webdriver.Chrome()


# web_driver.get('https://testautomationpractice.blogspot.com/')
# web_driver.maximize_window()


#        CHECKBOXES


# 1) Select one Specific checkbox

# web_driver.find_element(By.XPATH,"//input[@id='wednesday']").click()



# 2) Select all checkboxes

total_checkboxes = web_driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(total_checkboxes)) # 7

# Approach-1

# for i in total_checkboxes:
#     i.click()

# Approach-2

# for cb in range(len(total_checkboxes)):
#     total_checkboxes[cb].click()


# 3) Select multiple checkboxes by choice

# for checkbox in total_checkboxes:
#     name = checkbox.get_attribute('id')
#     if name == 'thursday' or name == 'tuesday':
#         checkbox.click()

# Another way

# 4) last 3 checkboxes  (total no.of elements - last 3 = ? --> index of number +1 (b'cause of range))

# 7 - 3 =5

# for i in range(len(total_checkboxes) - 3,len(total_checkboxes)):
#     total_checkboxes[i].click()


# 5) first 4 checkboxes just use if condition & less than

# for i in range(len(total_checkboxes)):
#     if i<4:
#         total_checkboxes[i].click()

# 6) clearing all checkboxes

# for check_box in total_checkboxes:
#     check_box.click()
#
# time.sleep(2)
#
# for checkboxes in total_checkboxes:
#     if checkboxes.is_selected():  # We want to know whether it is selected or not
#         checkboxes.click()


time.sleep(2)
web_driver.quit()