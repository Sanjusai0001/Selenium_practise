from telnetlib import EC

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementNotSelectableException, ElementNotVisibleException
web_d = webdriver.Chrome()


#                             COMMANDS

#              APPLICATION COMMANDS
# web_d.get('https://www.imdb.com/')
# web_d.maximize_window()
# print(web_d.title)
# print(web_d.current_url)
# print(web_d.page_source)


#              CONDITIONAL COMMANDS

# search_bar = web_d.find_element(By.XPATH,"//input[@name='q']")
#
# print('display status:',search_bar.is_displayed())
# print('enable status:',search_bar.is_enabled())

# web_d.get('https://qa-automation-practice.netlify.app/radiobuttons.html')
# web_d.maximize_window()
#
# btn = web_d.find_element(By.XPATH,"//input[@type='radio' and @id='radio-button1']")
# btn1 = web_d.find_element(By.XPATH,"//input[@type='radio' and @id='radio-button3']")
#
# print('btn status :',btn.is_selected())
# print('btn1 status :',btn1.is_selected())
#
#
# btn.click()
#
# #       AFTER
# print('btn status :',btn.is_selected())
# print('btn1 status :',btn1.is_selected())

#               BROWSER  COMMANDS

# web_d.get('https://www.flipkart.com/')
# web_d.maximize_window()
# web_d.find_element(By.PARTIAL_LINK_TEXT,"Mynt").click()
# time.sleep(5)
# web_d.close()              # close the parent/first browser window

# web_d.quit()    #      close all browser windows



#           NAVIGATIONAL  COMMANDS


# web_d.get('https://www.flipkart.com/')
# web_d.maximize_window()
# web_d.get('https://www.amazon.com/')
# web_d.get('https://www.myntra.com/')
#
#
# web_d.back()
# web_d.forward()
# web_d.refresh()
#
# time.sleep(3)




#                WAIT COMMANDS

web_d.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwi4yIz4qPuGAxWA2jgGHWZGCGkQPAgJ")
web_d.maximize_window()
# web_d.implicitly_wait(6)


wewait=WebDriverWait(web_d,5, ignored_exceptions=[NoSuchElementException,
                                                         ElementNotVisibleException,
                                                         ElementNotSelectableException,
                                                         Exception

]) # wewait = variable


search = web_d.find_element(By.XPATH,"//textarea[@name='q']")
search.send_keys("titan")
search.submit()

# time.sleep(5)     #it will wait for 10 sec, whether element is found or not

# titan_link = web_d.find_element(By.XPATH,"//span[@class='VuuXrf' or @xpath='1']")


titan_link = wewait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='VuuXrf' or @xpath='1']")))
titan_link.click()




web_d.close()