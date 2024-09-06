import time
import pytest
from selenium.webdriver.common.by import By
from Automation_practice.project_website_automation.conftest import chrome
from Automation_practice.project_website_automation.constants import buttons, checkboxes,\
    ckbx, reset, radiobtns, rad_btns


# @pytest.mark.usefixtures()
# class TestButtons:

@pytest.mark.usefixtures("chrome")
class TestButtonsSection(object):

    def test_checkboxes(self):
        self.driver.find_element(By.XPATH, buttons).click()
        self.driver.find_element(By.XPATH, checkboxes).click()
        cbs = self.driver.find_elements(By.XPATH, ckbx)
        print("\n no.of checkboxes is",len(cbs))

        for cb in cbs:
            if cb != cb.is_selected():
                cb.click()
        print("all selected")
        time.sleep(1)
        self.driver.find_element(By.XPATH, reset).click()

    def test_radiobuttons(self):
        self.driver.find_element(By.XPATH, buttons).click()
        self.driver.find_element(By.XPATH, radiobtns).click()
        ra_btns = self.driver.find_elements(By.XPATH, rad_btns)
        print("\n no.of radio buttons in a page is",len(ra_btns))

        count = 0

        for rb in ra_btns:
            count += 1
            rb.click()
            if rb.is_enabled():
                print(f"{count}st radio button is enable")
            else:
                print(f"{count}st radio button is disabled")
            time.sleep(0.5)
