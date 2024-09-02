import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
driver.maximize_window()
driver.implicitly_wait(2)

# scrolling ( we use Javascript functions )

# 1) scroll down page by pixel

# driver.execute_script("window.scroll(0,6300)","")
# value = driver.execute_script("return window.pageYOffset","")
# print('number of pixels moved:',value) # 6300


# 2) scroll down the page till the element is visible

# country = driver.find_element(By.XPATH,"//div[@class='row']//div[87]")
# name = driver.find_element(By.XPATH,"//div[@class='row']//div[87]/div/div")
#
# driver.execute_script("arguments[0].scrollIntoView();",country)
# value = driver.execute_script("return window.pageYOffset","")
# print('number of pixels moved:',value,name.text)  # number of pixels moved: 4858.39990234375 Japan


#  3) scroll down page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)  # 11372.7998046875

time.sleep(2)

# bottom to up

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value1 = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value1)  # 0




time.sleep(1)
driver.close()