import time

from selenium import webdriver
from selenium.webdriver.common.by import By

cwd = webdriver.Chrome()



cwd.get('https://money.rediff.com/gainers')
cwd.maximize_window()

# companies = cwd.find_elements(By.XPATH,"")
# print('Total Companies -',len(companies))
# print('Total Companies List :',companies.text)

# time.sleep(1)

#       self-node

# company=cwd.find_element(By.XPATH,"//a[contains(text(),'SW Investments')]/self::a").text
# print(company)     #SW Investments

#        parent node

# elem = cwd.find_element(By.XPATH,"//a[contains(text(),'India Cements Lt')]/parent::td").text
# print(elem)         #India Cements Lt

#         child node


# elements = cwd.find_element(By.XPATH,"//a[contains(text(),'Minaxi Textiles')]/ancestor::tr/child::td[3]").text
# print(elements)
elements = cwd.find_elements(By.XPATH,"//a[contains(text(),'Minaxi Textiles')]/ancestor::tr/child::td")
print(len(elements))    # 6



#      ancestor node


# elements = cwd.find_element(By.XPATH,"//a[contains(text(),'Minaxi Textiles')]/ancestor::tr")
# print(elements.text)    # Minaxi Textiles XT 3.74 4.11 + 9.89 Buy  |  Sell

elements1 = cwd.find_element(By.XPATH,"//a[contains(text(), 'Nimbus Projects')]/ancestor::tr").text
print(elements1)    # CESC Ltd. A 151.35 165.85 + 9.58 Buy  |  Sell


#   descendent

descendents = cwd.find_element(By.XPATH,"//a[contains(text(),'Nimbus Projects')]/ancestor::tr/descendant::*").text
print('no of descendents -',len(descendents))

#   following

followings = cwd.find_elements(By.XPATH,"//a[contains(text(),'Nimbus Projects')]/ancestor::tr/following::*")
print('no of followings -',len(followings))    # 19698


#   following-sibling

following_siblings = cwd.find_elements(By.XPATH,"//a[contains(text(),'Nimbus Projects')]/ancestor::tr/following-sibling::*")
print('no of following siblings -',len(following_siblings))     # 1775


#   preceding

precedings = cwd.find_elements(By.XPATH,"//a[contains(text(),'Nimbus Projects')]/ancestor::tr/preceding::*")
print('no of precedings -',len(precedings))     # 549



#   preceding-siblings

preceding_siblings = cwd.find_elements(By.XPATH,"//a[contains(text(),'Nimbus Projects')]/ancestor::tr/preceding-sibling::*")
print('no of preceding siblings -',len(preceding_siblings)) # 35
