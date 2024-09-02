from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import time
from selenium.webdriver.common.by import By


servObj = Service("C:\Windows\Drivers\chromedriver.exe")
webd = webdriver.Chrome(service=servObj)
# servObj = webdriver.Chrome(webd)

# webd=webdriver.Chrome()


webd.get('file:///C:/Users/sanju/OneDrive/Documents/Training/webpage-task/homepage.html')
webd.maximize_window()
time.sleep(1)



# LOCATORS
"""
1. NAME
2. ID
3. TAG_NAME
4. CLASS_NAME
5. LINKED_TEXT
6. PARTIAL_TEXT
"""

#        CUSTOMIZED LOCATORS
"""
                   |
        ___________________________
        |                         |
  CSS selectors                 XPath
        |                         |
    |- TAG and ID             |- ABSOLUTE
    |- TAG and CLASS          |- RELATIVE
    |- TAG and ATTRIBUTE
    |- TAG,CLASS and ATTRIBUTE
"""

#   NAME
# webd.find_element(By.NAME,'explore_here').send_keys('beach side hotel')
# time.sleep(2)

#       ID
# drop_down = webd.find_element(By.ID,'lang')
# drop_down.click()
# time.sleep(2)

#   CLASS_NAME
# webd.find_element(By.CLASS_NAME,'welcome-section').click()

#   TAG_NAME

# no_of_imgs = webd.find_elements(By.TAG_NAME,'img')
# print(len(no_of_imgs))          #52

# li_items=webd.find_elements(By.TAG_NAME,'li')
# print('total li items =',len(li_items))    #31



#    LINKED_TEXT (doesn't work in local)

"""
webd.get("https://www.flipkart.com/")
webd.maximize_window()
time.sleep(2)

product = webd.find_element(By.LINK_TEXT,'Myntra')
product.click()
"""



#    PARTIAL_LINKED_TEXT  (doesn't work in local)
"""
webd.get("https://www.flipkart.com/")
webd.get("https://www.flipkart.com/google-pixel-8a-aloe-128-gb/p/itm9f646ddfbe8f4?pid=MOBGYQ2MKT3SVFCS&lid=LSTMOBGYQ2MKT3SVFCSMCUIQC&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&st=color")
webd.maximize_window()
time.sleep(2)

product = webd.find_element(By.PARTIAL_LINK_TEXT,'Cancel')
product.click()
"""




#   CSS_SELECTOR

#           TAG & ID
# webd.find_element(By.CSS_SELECTOR, 'input#view-details-b').click()
# time.sleep(1)

#           TAG & CLASS
# webd.get("https://www.flipkart.com/google-pixel-8a-aloe-128-gb/p/itm9f646ddfbe8f4?pid=MOBGYQ2MKT3SVFCS&lid=LSTMOBGYQ2MKT3SVFCSMCUIQC&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&st=color")
# webd.maximize_window()
# time.sleep(1)

# ele_text=webd.find_element(By.CSS_SELECTOR, 'button._7Pd1Fp').click() #QqFHMw vslbG+ _3Yl67G _7Pd1Fp(class of button[button])
# time.sleep(2)
# print(ele_text)

#           TAG & ATTRIBUTE

# price=webd.find_element(By.CSS_SELECTOR,'span[class=VU-ZEz]')
# print(price.text)

#           TAG, CLASS & ATTRIBUTE

# storage = webd.find_element(By.CSS_SELECTOR,'li.aJWdJI[id=swatch-1-storage]').click()
# time.sleep(1)
#






# links_in_header = webd.find_elements(By.CSS_SELECTOR,'#navbar-items > li')
# print('total links in header =',len(links_in_header))         # 7

# webd.find_element(By.XPATH,'/html/body/div[1]/ul/li[3]/a').click() # ABSOLUTE_PATH
# webd.find_element(By.TAG_NAME,'a[3]').click()
# time.sleep(2)
# webd.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[]/input').send_keys('Sanju')
# webd.find_element(By.XPATH,'').click()
# time.sleep(2)

# /html/body/div[1]/ul/li[3]/a

time.sleep(2)

webd.close()