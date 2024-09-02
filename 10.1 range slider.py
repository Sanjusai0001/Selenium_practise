import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
driver.implicitly_wait(2)
# time.sleep(1)


min_slider = driver.find_element(By.XPATH,"//div[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH,"//div[@id='slider-range']/span[2]")

print('Location of sliders before moving...')
print(min_slider.location)   # {'x': 59, 'y': 252}
print(max_slider.location)   # {'x': 612, 'y': 252}

 # silder is horizontal in that case we slider in x-axis and viceversa for y-axis

action = ActionChains(driver)

action.drag_and_drop_by_offset(min_slider,140,0).perform()
action.drag_and_drop_by_offset(max_slider,-270,0).perform()

print()
print('Location of sliders After moving...')
print(min_slider.location)   # {'x': 59, 'y': 252}
print(max_slider.location)   # {'x': 341, 'y': 252}

time.sleep(2)

result = driver.find_element(By.ID,"searchResults")
print()
print(result.text)


driver.close()