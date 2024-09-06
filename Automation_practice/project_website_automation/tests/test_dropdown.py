import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Automation_practice.project_website_automation.conftest import headless_chrome, Chrome, chrome
from Automation_practice.project_website_automation.constants import dpdn, dpdn_menu, opts, multi_btn, level1, level2, \
    level3, level4


@pytest.mark.usefixtures("Chrome")
def test_dropdown(Chrome):

    driver = Chrome
    driver.find_element(By.ID, dpdn).click()
    driver.find_element(By. ID, dpdn_menu).click()
    options = driver.find_elements(By. XPATH, opts)
    print(len(options))

    for opt in options:
        if opt.text == "Nepal":
            opt.click()
            break

    driver.find_element(By. ID, dpdn_menu).click()
    time.sleep(1)

@pytest.mark.usefixtures("chrome")
class TestMultiDropDown:

    def test_data(self, chrome):
        driver = chrome
        self.dpdnsec= driver.find_element(By.ID, dpdn).click()
        self.multiBtn = driver.find_element(By.XPATH, multi_btn).click()
        time.sleep(2)
        self.items1 = driver.find_elements(By.XPATH, level1)
        self.items2 = driver.find_elements(By.XPATH, level2)
        self.items3 = driver.find_elements(By.XPATH, level3)
        self.items4 = driver.find_elements(By.XPATH, level4)
        print(len(self.items1), len(self.items2), len(self.items3), len(self.items4))

    @pytest.mark.parametrize("text1, text2, text3, text4",[("Hover me for more options", "Even More..","another level", "4th level - 3")])
    def test_multidropdown(self, chrome, text1, text2, text3, text4):

        self.test_data(chrome)
        actions = ActionChains(chrome)

        try:
            for op in self.items1:
                if op.text == text1:
                   actions.move_to_element(op).perform()
                   for opt in self.items2:
                       if opt.text == text2:
                           actions.move_to_element(opt).perform()
                           for optn in self.items3:
                               if optn.text == text3:
                                   actions.move_to_element(optn).perform()
                                   for optns in self.items4:
                                       if optns.text == text4:
                                           actions.move_to_element(optns).perform()
                                   time.sleep(1)
        finally:
            print("chased the element")

        time.sleep(1.5)