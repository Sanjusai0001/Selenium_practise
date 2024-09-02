
# 25:Check for URL in a String

#   1
import re


# str = "Selenium with Python & PyTest  https://shorturl.at/ELW09"
# str = "404"
# str = "https://www.instagram.com/profile.html/"
str = "Selenium with Python & PyTest********************************► https://shorturl.at/ELW09Selenium with python using Robot framework **************************************** ► https://shorturl.at/bcDPZ"

url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
print(url)


#   2
pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

if (re.findall(pattern, str) ==  []):
    print("Not found any link")
else:
    print(url)