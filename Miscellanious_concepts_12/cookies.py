import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.dummyticket.com/")
driver.maximize_window()
time.sleep(2)



cookies = driver.get_cookies()
print('Total cookies in site:',len(cookies))


# printing details of cookies

# for cookie in cookies:
#     print(cookie.get('name'),' - ',cookie.get('value'))


# Add a new Cookie (in a dictionary format)
driver.add_cookie({
    "name":"myCookie",
    "value":"536%64%672%565%",
})
cookies=driver.get_cookies()
print('after adding new one :',len(cookies))


# delete cookie

driver.delete_cookie('myCookie')
cookies=driver.get_cookies()
print('after deleted new one :',len(cookies))

# Delete all Cookies

driver.delete_all_cookies()
cookies=driver.get_cookies()
print('after cookies deleted :',len(cookies))



driver.quit()