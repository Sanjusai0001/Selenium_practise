import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(1)


# 1) Count no.of rows & columns

rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
# print(' no.of  rows =',rows)      # 7
#
columns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
# print('no.of columns =',columns)  # 4


#  2) Specific row and column data

# data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[6]/td[1]")
# print(data.text)  # Master In Java


# 3) Read all rows & columns data

# print("All the rows and columns data..........")
#
# for row in range(2,rows+1):
#     for column in range(1,columns+1):
#         data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(row)+"]/td["+str(column)+"]").text     # adding string for getting the data
#         print(data, end='           ')
#     print('')




# 4) Read data based on condition (List books name whose author is Amit)
# Retrieve Data

for row in range(2, rows+1):
    author = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(row)+"]/td[2]").text
    if author == "Amit":
        book = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row) + "]/td[4]").text
        print(book,"        ",author,"      ",price)


driver.close()