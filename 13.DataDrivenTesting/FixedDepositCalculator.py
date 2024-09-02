import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import XLutilities as data


driver = webdriver.Chrome()

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
# driver.implicitly_wait(10)

# alert = Alert(driver)
# alert.accept()

# driver.refresh()
# driver.find_element(By.ID,"wzrk-cancel").click()


# def test_cal_datadriventesting_from_excel():
#
#     file = "C:/Users/sanju/PycharmProjects/SELENIUM/report_data.xlsx"
#     rows = data.getRowCount(file,'Sheet1')
#     print(rows)
#
#     for r in range(2, rows+1):
#
#         #reading data from Excel
#         price = data.readData(file,'Sheet1',r,1)
#         roi = data.readData(file,'Sheet1',r,2)
#         p1 = data.readData(file,'Sheet1',r,3)
#         p2 = data.readData(file,'Sheet1',r,4)
#         freq = data.readData(file,'Sheet1',r,5)
#         exp_mval = data.readData(file,'Sheet1',r,6)
#
#         # passing data to the application
#         driver.find_element(By.XPATH,"//*[@id='principal']").send_keys(price)
#         driver.find_element(By.XPATH,"//*[@id='interest']").send_keys(roi)
#         driver.find_element(By.XPATH,"//*[@id='tenure']").send_keys(p1)
#         period = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
#         period.select_by_visible_text(p2)
#         frequency = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
#         frequency.select_by_visible_text(freq)
#         driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
#
#         act_mval = driver.find_element(By.XPATH,"//*[@id='resp_matval'']/strong").text
#
#         # validation
#         if float(exp_mval) == float(act_mval):
#             print("Test Passed")
#             data.writeData(file,'Sheet',r,8,"passed")
#             data.fillGreenColor(file,'Sheet1',r,8)
#
#         else:
#             print("Test Failed")
#             data.writeData(file,'Sheet',r,8,"Failed")
#             data.fillRedColor(file,'Sheet1',r,8)
#
#         driver.find_element(By.XPATH, "//*[@id='fdMatVal'']/div[2]/a[2]/img").click()
#         time.sleep(2)
#     return


def test_cal_datadriventesting_from_excel():

    file = "C:/Users/sanju/PycharmProjects/SELENIUM/report_data.xlsx"
    rows = data.getRowCount(file, 'Sheet1')
    print(rows)

    # driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    # driver.find_element(By.XPATH, "//*[@id='fdMatVal'']/div[2]/a[1]/img").click()
    try:
        # Navigate to the website
        driver.get(
            "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
        driver.maximize_window()

        # Wait for the overlay to be present and close it if it exists
        wait = WebDriverWait(driver, 10)
        try:
            overlay_close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='wzrk-button wzrk-button-secondary']")))
            overlay_close_button.click()
        except Exception as e:
            print("No overlay present or unable to close overlay:", e)

        for r in range(2, rows + 1):

            # reading data from Excel
            price = data.readData(file, 'Sheet1', r, 1)
            roi = data.readData(file, 'Sheet1', r, 2)
            p1 = data.readData(file, 'Sheet1', r, 3)
            p2 = data.readData(file, 'Sheet1', r, 4)
            freq = data.readData(file, 'Sheet1', r, 5)
            exp_mval = data.readData(file, 'Sheet1', r, 6)

            # passing data to the application
            driver.find_element(By.XPATH, "//*[@id='principal']").send_keys(price)
            driver.find_element(By.XPATH, "//*[@id='interest']").send_keys(roi)
            driver.find_element(By.XPATH, "//*[@id='tenure']").send_keys(p1)
            period = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
            period.select_by_visible_text(p2)
            frequency = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
            frequency.select_by_visible_text(freq)

            # driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
            # Wait for the calculate button to be clickable and click it
            calculate_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html[1]/body[1]/div[12]/div[2]/div[1]/div[5]/div[1]/div[1]/div[3]/form[1]/div[2]/a[1]")))
            calculate_button.click()

            act_mval = driver.find_element(By.XPATH, "//*[@id='resp_matval']/strong").text

            # validation
            if float(exp_mval) == float(act_mval):
                print("Test Passed")
                data.writeData(file, 'Sheet1', r, 8, "passed")
                data.fillGreenColor(file, 'Sheet1', r, 8)
            else:
                print("Test Failed")
                data.writeData(file, 'Sheet1', r, 8, "Failed")
                data.fillRedColor(file, 'Sheet1', r, 8)

            # driver.find_element(By.XPATH, "//*[@id='fdMatVal'']/div[2]/a[2]/img").click()
            # Wait for the calculate button to be clickable and click it
            clear_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html[1]/body[1]/div[12]/div[2]/div[1]/div[5]/div[1]/div[1]/div[3]/form[1]/div[2]/a[2]")))
            clear_button.click()

            time.sleep(1)

    finally:
        # Close the browser
        driver.quit()
    return