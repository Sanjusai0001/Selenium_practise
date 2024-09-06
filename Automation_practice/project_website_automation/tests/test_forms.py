import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Automation_practice.project_website_automation.constants import forms, login, email,\
    pwd, submit, register, fname, lname, phone_no, country, options, reg_email, reg_pwd,\
    checkbox, reg_btn, recovery_pwd


@pytest.fixture(scope="function")
def chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://qa-automation-practice.netlify.app/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.usefixtures("chrome")
def test_login(chrome):

    # driver = chrome()
    chrome.find_element(By.XPATH, forms).click()
    chrome.find_element(By.XPATH, login).click()

    chrome.find_element(By.XPATH, email).send_keys("admin@admin.com")
    chrome.find_element(By.XPATH, pwd).send_keys("admin123")

    chrome.find_element(By.XPATH, submit).click()

    msg = chrome.find_element(By.XPATH, '//div[@id="message"]')
    assert msg.text == "admin@admin.com, you have successfully logged in!"

    time.sleep(1)


@pytest.mark.usefixtures("chrome")
def test_register(chrome):

    driver = chrome

    driver.find_element(By.XPATH, forms).click()
    driver.find_element(By.XPATH, register).click()

    driver.find_element(By.XPATH, fname).send_keys("sanju")
    driver.find_element(By.XPATH, lname).send_keys("sai")
    driver.find_element(By.XPATH,phone_no).send_keys("9490345683")
    driver.find_element(By.XPATH, country).click()
    driver.find_element(By.XPATH, options).click()
    driver.find_element(By.XPATH, reg_email).send_keys("johndoe34@gmail.com")
    driver.find_element(By.XPATH, reg_pwd).send_keys("JohnDoe23")
    driver.find_element(By.XPATH, checkbox).click()

    driver.find_element(By.XPATH, reg_btn).click()
    time.sleep(1)
    # mywait = WebDriverWait(driver, 5, ignored_exceptions="NoSuchElementException")
    # submit_btn = mywait.until(EC.element_to_be_clickable((By.XPATH, reg_btn)))
    # submit_btn.click()

    msg = driver.find_element(By.XPATH, '//div[@id="message"]')
    assert msg.text == "The account has been successfully created!"

    time.sleep(2)



@pytest.mark.skip(reason="being skipped temporarily")
def test_recovery_pwd(chrome):

    driver = chrome

    driver.find_element(By.XPATH, forms).click()
    driver.find_element(By.XPATH, recovery_pwd).click()

    driver.find_element(By.XPATH, email).send_keys("admin@admin.com")
    driver.find_element(By.XPATH, submit).click()

    msg = driver.find_element(By.XPATH, '//div[@id="message"]')
    assert msg.text == "An email with the new password has been sent to admin@admin.com. Please verify your inbox!"
    time.sleep(2)

