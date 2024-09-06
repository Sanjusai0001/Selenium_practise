# import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from Miscellanious_concepts_12.HeadlessTestingOrMode import headless_chrome

website = "https://www.thesun.co.uk/"
# path = "'C:\Windows\Drivers\chromedriver-win64\chromedriver.exe'"
# options = Options()
# options.headless = True
# service_obj = Service(executable_path='C:\Windows\Drivers\chromedriver-win64\chromedriver.exe')
# driver = webdriver.Chrome(service = service_obj, options=options)

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Windows\Drivers\chromedriver-win64\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.headless = True

    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver

driver = headless_chrome()

driver.get(website)
driver.maximize_window()
driver.implicitly_wait(4)

# xpaths
# topics = '// h3[@class="teaser__subdeck"]'
# details = '// span[@class="teaser__headline teaser__kicker t-p-color"] '
# links =  '// a[@class="text-anchor-wrap"]'
# containers =  '//div[@class="teaser__copy-container"]'

# containing elements
main_container = driver.find_elements(By.XPATH, '//div[@class="teaser__copy-container"]' )
# print(len(main_container))

# serial_number = []
headlines = []
contents = []
urls = []
count = 0

# loop through the container
for containter in main_container:
    title = containter.find_element(By.XPATH, './a/span').text
    subtopic = containter.find_element(By.XPATH, './a').get_attribute('data-headline')
    link = containter.find_element(By.XPATH, './a').get_attribute('href')

    # count += 1
    # no = count
    # print(n, '.' , title, subtopic, link)
    headlines.append(title)
    contents.append(subtopic)
    urls.append(link)
    # serial_number.append(no)


dict = {"Headline": headlines, "Content": contents, "URL": urls}
daily_news = pd.DataFrame(dict)
daily_news.to_csv('Trending_news_HeadlessMode.csv')


driver.close()