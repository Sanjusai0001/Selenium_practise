import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


driver.get("https://qa-automation-practice.netlify.app/dropdowns#hover-me")
driver.maximize_window()

drop_down = driver.find_element(By.XPATH,"//select[@id='dropdown-menu']")
drdnCountry = Select(drop_down)


# select option from the dropdown
#            (Using built-in functions)

# drdnCountry.select_by_visible_text('Russia')
# drdnCountry.select_by_value('Morocco')
# drdnCountry.select_by_index(26)


# capture the all elements and print
all_opt = drdnCountry.options
print("Total no.of options",len(all_opt))

# for opt in all_opt:
#     print(opt.text)


# select option from the dropdown

#                ( NOT Using built-in functions)

for opt in all_opt:
    if opt.text == 'Italy':
        opt.click()
        break

# drdn1 = driver.find_element(By.XPATH,"//select[@id='dropdown-menu']//option[@value='Peru']")
# drdn1.click()


time.sleep(1)

driver.quit()