import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


location = os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")


    # download in specific location
    # preferences = {"download.default_directory":"C:\Users\sanju\PycharmProjects\SELENIUM\11. Keyboard Actions"}
    preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Chrome(service=serv_obj,options=ops)
    return driver


def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\Windows\Drivers\edgedriver_win64\msedgedriver.exe")


    # download in specific location
    # preferences = {"download.default_directory":"C:\Users\sanju\PycharmProjects\SELENIUM\11. Keyboard Actions"}
    preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True} # it will won't work for PDF only - 1 bug is there (from selenium side)
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)

    driver = webdriver.Edge(service=serv_obj,options=ops)
    return driver


def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\Windows\Drivers\geckodriver-v0.34.0-win64\geckodriver.exe")
    #settings
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",2) #0-desktop , 1- downloads folder, 2- desired location
    ops.set_preference("browser.download.dir",location)
    ops.set_preference("pdfjs.disabled",True) # for pdf

    driver = webdriver.Firefox(service=serv_obj, options=ops)
    return driver


# code to download
"""
# driver = chrome_setup()
# driver = edge_setup()

driver = firefox_setup()
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
"""

# PDF file download
"""
# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/')
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
"""

# How to upload the files
driver = chrome_setup()
# driver = edge_setup()
# driver = firefox_setup()
#
# driver.get('https://www.remove.bg/uploads')
# driver.maximize_window()
# driver.implicitly_wait(2)

# driver.find_element(By.XPATH,"//button[@type='button' and @xpath='3']").click()
# upload = driver.find_element(By.XPATH,"//button[@type='button' and @xpath='3']")
# upload.send_keys("Fushiguro_sis.jpg")

# for file download & upload most prefer to manual testing



time.sleep(10)
driver.close()