

#  1

str = input("Enter something:" )

print(str[0:3])
print(str[:5])
print(str[0:4])
print(str[3:6:2])  # 2 -  elements will be skipped / removed
print(str[::-1])


rev = str[::-1]

if rev == str:
    print("It's a Palindrome")
else:
    print("Not a Palindrome")