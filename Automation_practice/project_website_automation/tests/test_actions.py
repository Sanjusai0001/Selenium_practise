import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Automation_practice.project_website_automation.conftest import headless_chrome, Chrome, chrome
from Automation_practice.project_website_automation.constants import acnts, db_clk, scroll, btn2, end, txt, mouseHover, \
    showHide, para, SHbtn


@pytest.mark.usefixtures("chrome")
class TestActions(object):

    def test_doubleclick(self, chrome):
        chrome.find_element(By.XPATH, acnts).click()
        chrome.find_element(By.XPATH, db_clk).click()
        dbBtn = chrome.find_element(By.ID, btn2)
        action = ActionChains(chrome)
        action.double_click(dbBtn).perform()
        time.sleep(1)
        msg = chrome.find_element(By.ID, "double-click-result")
        output = 'Congrats, you double clicked!'
        assert msg.text == output

    def test_scroll(self):
        self.driver.find_element(By.XPATH, acnts).click()
        self.driver.find_element(By.XPATH, scroll).click()
        bottom = self.driver.find_element(By.ID, end)
        self.driver.execute_script("arguments[0].scrollIntoView();",bottom)
        value = self.driver.execute_script("return window.pageYOffset","")
        print('number of pixels moved:', value, bottom.text)  # number of pixels moved:  8307
        time.sleep(1)

    def test_moushover(self):

        self.driver.find_element(By.XPATH, acnts).click()
        self.driver.find_element(By.XPATH, mouseHover).click()
        before_hover = self.driver.find_element(By.ID, txt)
        val = before_hover.text

        action = ActionChains(self.driver)
        action.move_to_element(before_hover).perform()
        after_hover = self.driver.find_element(By.ID, txt)
        time.sleep(1)

        assert val != after_hover.text

    def test_show_hide(self):
        self.driver.find_element(By.XPATH, acnts).click()
        self.driver.find_element(By.ID, showHide).click()
        btn = self.driver.find_element(By.ID, SHbtn)
        state = self.driver.find_element(By.ID, para)
        """
        btn.click()
        time.sleep(1)
        print(state.get_attribute('display'))
        action = ActionChains(self.driver)
        action.double_click(btn).perform()
        time.sleep(1)
        print(state.get_attribute('display'))
        btn.click()
        time.sleep(1)
        print(state.get_attribute('display'))
        """
        # First click to hide/show
        # btn.click()
        # time.sleep(1)
        """Use JavaScript to get the computed style for 'display' """
        displayVal = self.driver.execute_script("return window.getComputedStyle(arguments[0]).display;", state)
        print(f"\n Display state: {displayVal}")
        # action = ActionChains(self.driver)
        # action.double_click(btn).perform()
        # time.sleep(1)
        # displayVal1 = self.driver.execute_script("return window.getComputedStyle(arguments[0]).display;", state)
        # print(f"Display after double-click: {displayVal1}")
        btn.click()
        time.sleep(1)
        displayVal2 = self.driver.execute_script("return window.getComputedStyle(arguments[0]).display;", state)
        print(f"Display after second click: {displayVal2}")

        assert displayVal != displayVal2

