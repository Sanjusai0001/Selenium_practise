import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()
driver.implicitly_wait(2)


# CTRL+A ---> CTRL+C ---> TAB ---> CTRL+V

input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

# input1.clear()
input1.send_keys('welcome to Complex')
# print(input1.get_attribute('placeholder'))  # it will print the value in textarea

actn = ActionChains(driver)


# CTRL+A selects the text

# actn.key_down(Keys.CONTROL)
# actn.send_keys('a')
# actn.key_up(Keys.CONTROL)
# actn.perform()

# single line
actn.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()



# CTRL+C Copies the text

actn.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

# time.sleep(1)

# move to other textarea/input box

# actn.send_keys(Keys.TAB)
# actn.perform()
actn.send_keys(Keys.TAB).perform()


# CTRL + V to paste the text

actn.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()



time.sleep(2)
driver.close()
