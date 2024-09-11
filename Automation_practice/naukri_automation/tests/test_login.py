import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Automation_practice.naukri_automation.conftest import chrome, headless_chrome
from Automation_practice.naukri_automation.constants import login_btn, \
    uname, pswd, login, name, pwrd, error, google, gname


@pytest.mark.usefixtures("chrome")
def test_login(chrome):
    driver = chrome
    homepage = driver.current_window_handle

    time.sleep(1.2)
    driver.find_element(By.XPATH, login_btn).click()
    time.sleep(.5)
    driver.find_element(By.XPATH, uname).send_keys(name)
    driver.find_element(By.XPATH, pswd).send_keys(pwrd)
    driver.find_element(By.XPATH, login).click()
    time.sleep(.5)
    msg = driver.find_element(By.XPATH, error)
    print("\n", msg.text)
    assert msg.text != None

    driver.find_element(By.XPATH, google).click()
    all_wnds = driver.window_handles
    for wd in all_wnds:
        if wd != homepage:
            driver.switch_to.window(wd)
            time.sleep(2.5)
            # g_name = driver.find_element(By.XPATH, gname)
            # print(name.text)

@pytest.mark.usefixtures("headless_chrome")
def test_login_background(headless_chrome):
    driver = headless_chrome
    time.sleep(.1)
    driver.find_element(By.XPATH, login_btn).click()
    # driver.find_element(By.XPATH, uname).send_keys(name)
    # driver.find_element(By.XPATH, pswd).send_keys(pwrd)
    # driver.find_element(By.XPATH, login).click()
    # time.sleep(.2)
    # msg = driver.find_element(By.XPATH, error)
    # print(msg.text)
    # assert msg.text == None
    # driver.find_element(By.XPATH, google).click()

