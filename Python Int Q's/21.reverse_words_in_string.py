
# 21:How To Reverse Words in a String

str = "we don't have any enimies left"
# str = input("Enter a string: ")

words = str.split(" ")
print(words)      #  ['we', "don't", 'have', 'any', 'enimies']

words = words[::-1]
print(words)      #   ['enimies', 'any', 'have', "don't", 'we']

outputstr =  " ".join(words)
print(outputstr)  #   left enimies any have don't we

str1 = outputstr

str1 = outputstr.split(" ")
print(str1)         #  ['left', 'enimies', 'any', 'have', "don't", 'we']

modified_str = str1[::-1]
print(modified_str)   #  ['we', "don't", 'have', 'any', 'enimies', 'left']

last_str = " ".join(modified_str)
print(last_str)          #  we don't have any enimies left
