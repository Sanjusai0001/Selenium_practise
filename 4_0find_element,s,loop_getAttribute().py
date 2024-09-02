import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# driver.get("https://www.flipkart.com/")
# driver.maximize_window()

#  FIND ELEMENT()  - returns single web element


# 1. Locator matching with single web elemnent

# ele = driver.find_element(By.NAME,"q")
# ele.send_keys('Alen solly')


# 2. Locator matching with multiple elements
# ele1 = driver.find_element(By.XPATH,"//footer[@class='TKplD7']//a")
# print(ele1.text)   #    Brand Directory  - prints only first link text

# 3. Element not available then throw NoSuchElementException
# ele2 = driver.find_element(By.LINK_TEXT,"Securit")
# ele2.click()




#                FIND_ELEMENTS -  returns multiple elements

#  1. Locator matching with single element

# ele3 = driver.find_elements(By.XPATH,"//input[@name='q']")
# print(len(ele3))
# ele3[0].send_keys('Peter England Analog Watch')

#   2. Locator matching with multiple web elements
"""
ele4 = driver.find_elements(By.XPATH,"//footer[@class='TKplD7']//a")
print(len(ele4))
# print(ele4[4].text)
# print(ele4.text)  # its not gonna for more than one elements

    # printing elements with loop

for el in ele4:
    print(el.text)
"""

#  3. If Element is not available - it'll returns zero

# ele5 = driver.find_elements(By.LINK_TEXT,"Securit")
# print('elements matched :',len(ele5))







#  TEXT() vs GET_ATTRIBUTE('VALUE')


driver.get('https://qa-automation-practice.netlify.app/login')
driver.maximize_window()

searchBox = driver.find_element(By.XPATH,"//input[@type='email']")


searchBox.send_keys('Allen@gmail.com')



print('output -',searchBox.text)
print('output -',searchBox.get_attribute('value'))

time.sleep(2)
searchBox.clear()

searchBox.clear()
searchBox.send_keys('Peter@gmail.com')

print('output -',searchBox.text)
print('output -',searchBox.get_attribute('value'))




time.sleep(2)
driver.close()









