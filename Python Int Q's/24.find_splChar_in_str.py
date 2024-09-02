
#  24:Check if a string contains any special character

#     1

import re

str1 = "welcome#@$to*^%the#@#@world|?of!*&^AI"
str2 = "welcome"

regex = re.compile('[@_! #$%^&*()<>?/\|}{~:]')

if (regex.search(str1) == None):
    print("No special characters in a string")
else:
    print("String contains special characters")


#   2

pattern = r'[\$\%\^\&\*\(\)\!]'

if (re. findall(pattern, str2) == []):
    print("No special characters in a string")
else:
    print("String contains special characters")

# matches = re.findall(regex, str1)
# print(matches)

