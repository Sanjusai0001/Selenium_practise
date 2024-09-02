from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'app': '/path/to/app.apk'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.quit()
