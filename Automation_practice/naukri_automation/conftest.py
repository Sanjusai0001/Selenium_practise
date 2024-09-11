import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get("https://www.naukri.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def Chrome(requests):
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    requests.cls.driver = driver
    driver.get("https://www.naukri.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.add_argument("--headless")
    ops.headless = True
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    driver.get("https://www.naukri.com/")
    yield driver
    driver.quit()