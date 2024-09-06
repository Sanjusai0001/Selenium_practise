import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Automation_practice.project_website_automation.conftest import headless_chrome, Chrome
from Automation_practice.project_website_automation.constants import tab_wd, \
    new_tab, new_tab_btn, new_wd, new_wd_btn


# @pytest.fixture(scope="function")
# def chrome():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=serv_obj)
#     driver.get("https://qa-automation-practice.netlify.app/")
#     driver.maximize_window()
#     yield driver
#     driver.quit()


@pytest.mark.usefixtures("Chrome")
def test_new_window(Chrome):
    global driver
    driver = Chrome
    homepage = driver.current_window_handle

    try:
        driver.find_element(By.XPATH, tab_wd).click()
        driver.find_element(By.XPATH, new_tab).click()
        driver.find_element(By.XPATH, new_tab_btn).click()
        time.sleep(.5)
        print("\n passed...")
    except NameError as e:
        print(e)
    finally:
        driver.switch_to.window(homepage)
        time.sleep(1)
        print("Back to Homepage...")


# @pytest.mark.usefixtures("headless_chrome")
def test_window(headless_chrome):
    driver = headless_chrome
    homepage = driver.current_window_handle

    if (driver.title == "QA Practice | Learn with RV"):
        driver.find_element(By.XPATH, tab_wd).click()
        driver.find_element(By.XPATH, new_wd).click()
        driver.find_element(By.XPATH, new_wd_btn).click()
        # time.sleep(1)
        all_wds = driver.window_handles
        for window in all_wds:
            if window != homepage:
                driver.switch_to.window(window)
                print("\n Switched to new window:", driver.current_url)

                driver.close()
                print("Closed new window")

                driver.switch_to.window(homepage)
                print("Switched back to original window:", driver.current_url)
                break
        # time.sleep(2)
    else:
        print("\n Failed....")
