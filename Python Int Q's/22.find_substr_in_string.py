
# 22:Find Sub string Presence in a String

str = "welcome to khansar world"
substr = "khansar"

print(str.find(substr))   # 11

# if (str.find(substr) != 11):
if (str.find(substr) == -1):
    print("not found")
else:
    print("found")