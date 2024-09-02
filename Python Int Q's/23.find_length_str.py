
#  23:How To Find Length of a String

# 1

str = "Microsoft Corporation. All rights reserved."
count = 0

for i in str:
    count += 1
print(count)


#   2

while str [count:]:
    count += 1
print(count)

#    3

length = len(str)
print(length)
print(len(str))

#    4

ran_str = "_"

print(ran_str.join(str))
print(ran_str.join(str).count(ran_str)+1)
