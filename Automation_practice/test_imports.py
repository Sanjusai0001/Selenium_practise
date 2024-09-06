import pytest

import exports as file
import time
from selenium.webdriver.common.by import By

from CONSTANTS import GOOGLE_APP_XPATH, IFRAME, LIST_ITEMS, GMAIL_ICON_XPATH


# file.DateDetails()

# driver = file.ChromeFunction()


def test_1():
    driver = file.ChromeFunction()
    driver.find_element(By.XPATH, GOOGLE_APP_XPATH).click()

    driver.switch_to.frame(driver.find_element(By.XPATH, IFRAME))
    # print(len(iframes))

    li_items = driver.find_elements(By.XPATH, LIST_ITEMS)

    # print(len(li_items))
    # for li in li_items:
    #     if li.text == "chat":
    #         print('entered into loop')
    #         assert li.text == "chat", "Test Failed as its not finding the correct element"

    list_of_elements = []
    for i in li_items:
        list_of_elements.append(i.text)
    assert "Gmail" in list_of_elements, "Gmail is not available in the list of elements"
    i.click()
    print(list_of_elements)

    # driver.find_element(By.XPATH, GMAIL_ICON_XPATH).click()
    print("  Test Passed   ")

    driver.close()





