import time
from selenium import webdriver
from selenium.webdriver.common.by import By

wd= webdriver.Chrome()

wd.get("file:///C:/Users/sanju/OneDrive/Documents/Training/Laundry-site%20Task/Home%20page.html")
wd.maximize_window()
# time.sleep(1)

#   ABSOLUTE XPATH

# wd.find_element(By.XPATH,'/html/body/header/nav/ul/li[2]/a').click()
# time.sleep(2)
# wd.find_element(By.XPATH,'/html/body/header/nav/ul/li[1]/a').click()
# time.sleep(2)
#
# wd.find_element(By.XPATH,'/html/body/div[6]/div[1]/img[3]').click()
# time.sleep(2)

#   RELATIVE XPATH
# wd.find_element(By.XPATH,"//*[@id='signup']/a").click()
# txt=wd.find_element(By.XPATH,"//*/input[@id='name']")
# txt.send_keys('clara')
# time.sleep(2)

#       OR
# wd.get('https://www.flipkart.com')
# search_field = wd.find_element(By.XPATH,"//input[@type='text' or @name='q']")
# search_field.send_keys('PETER ENGLAND Analog Watch-For Men PE000017B')
# search_field.clear()
# time.sleep(1)
# wd.find_element(By.XPATH,"//input[@type='tex' or @name='q']").send_keys('Allen Solly Analog Watch-For Men AS000022C')
# time.sleep(2)

#       AND

# wd.get('https://www.facebook.com/')
# time.sleep(1)
# wd.find_element(By.XPATH,"//input[@type='text' and @id='email']").send_keys('9492230694')
# wd.find_element(By.XPATH,"//input[@name='pass' and @type='password']").send_keys('pwsd01234')
# time.sleep(2)
#


#    CONTAINS()

wd.get('https://www.facebook.com/')
wd.find_element(By.XPATH,"//input[contains(@type,'ex')]").send_keys('sundar_05')

#     STARTS()


wd.find_element(By.XPATH,"//input[starts-with(@type,'pas')]").send_keys('sund24205')
time.sleep(2)

#      TEXT()

wd.find_element(By.XPATH,"//a[text()='తెలుగు']").click()
time.sleep(2)


wd.close()


