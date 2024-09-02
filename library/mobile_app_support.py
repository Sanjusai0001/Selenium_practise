from appium import webdriver

from library.application_launch import spotify_app_apk


def launch_mobile_application(app):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'app': '/path/to/app.apk'
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', launch_mobile_application(app))
    driver.quit()

launch_mobile_application(spotify_app_apk)