import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


# driver.get("https://opensource-demo.orangehrmlive.com")
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
time.sleep(1)

# driver.find_element(By.XPATH,"//input[@name='username']").send_keys('Admin')
# driver.find_element(By.XPATH,"//input[@name='password']").send_keys('admin123')
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
#
# time.sleep(3)
#
# # Admin --> User management --> Users
#
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
#
# time.sleep(1)
#
# driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
# time.sleep(1)
#
#
# driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/header[1]/div[2]/nav[1]/ul[1]/li[1]/ul[1]/li[1]").click()
# time.sleep(2)


rows = len(driver.find_elements(By.XPATH,"//table[@id='countries']/tbody//tr"))
# print('total no.of rows ',rows)

f_count = 0
e_count = 0
a_count = 0

for l in range(1, rows+1):
    lang = driver.find_element(By.XPATH,"//table[@id='countries']/tbody/tr["+str(l)+"]/td[5]").text
    # print(lang)
    if lang == "French":
        f_count = f_count+1
    if lang == "English":
        e_count = e_count+1
    if lang == "Arabic":
        a_count = a_count+1

print('Analysing the languages in different countries')
print('')
print('Total Countries :',rows)
print('French Spoken Countries:', f_count)
print('English Spoken Countries:', e_count)
print('Arabic Spoken Countries:', a_count)
print('Except French :', rows-f_count)
print('Except English :', rows-e_count)
print('Except Hindi :', rows-a_count)
print('Except French, English & Arabic :', rows -(e_count+f_count+a_count))



driver.close()