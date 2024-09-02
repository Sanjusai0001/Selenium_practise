
#   Find Sum of Elements in the List

#   1

list = [22, 43, 23, 42, 11, 29]
print(list)

total = 0

for i in range(0, len(list)):
    total = total + list[i]

print("Total no.of items =", total)
print()


#   2  -  using sum

li = [1,2, 34,999, -453, 58]
print(li)

total = sum(li)
print(total)