import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


@pytest.fixture(scope="module")
def Chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://qa-automation-practice.netlify.app/")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def chrome(request):
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    request.cls.driver = driver
    driver.get("https://qa-automation-practice.netlify.app/")
    driver.maximize_window()
    yield driver
    action = ActionChains(driver)
    driver.quit()

# @pytest.fixture(scope="class")
# def chrome(request):
#     from selenium.webdriver.chrome.service import Service
#     serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
#     request.cls.driver = webdriver.Chrome(service=serv_obj)
#
#     request.cls.driver.get("https://qa-automation-practice.netlify.app/")
#     request.cls.driver.maximize_window()
#     yield request.cls.driver
#     request.cls.driver.quit()


@pytest.fixture(scope="module")
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    ops.headless = True
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    # return driver

    driver.get("https://qa-automation-practice.netlify.app/")
    yield driver
    driver.quit()