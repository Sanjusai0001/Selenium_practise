import time
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# mywait = WebDriverWait(driver, 10)
# class AutomatingTheWebsite:

"""

@pytest.fixture(scope="module")
def chrome():
# def setup_chrome_function():

    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)

    driver.get("https://qa-automation-practice.netlify.app/")
    driver.maximize_window()
    yield driver

@pytest.fixture
def teardown_chrome_function(driver):
    driver.close()
"""