import time

from selenium import webdriver
from selenium.webdriver.common.by import By

web_driver = webdriver.Chrome()




#        LINKS


web_driver.get('https://www.nopcommerce.com/en')
web_driver.maximize_window()


# click

# link = web_driver.find_element(By.LINK_TEXT,"Get started").click()
# link = web_driver.find_element(By.PARTIAL_LINK_TEXT,"Get").click()

# find number of links
# links = web_driver.find_elements(By.TAG_NAME,"a")
links = web_driver.find_elements(By.XPATH,"//a")

print('Total no. of links in webpage:',len(links))

# for link in links:
#     print(link.text)



for link in links:
   all_links = link.text
print(all_links)




time.sleep(1)
web_driver.quit()