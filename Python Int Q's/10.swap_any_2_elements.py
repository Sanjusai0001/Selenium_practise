
# How To Swap Any 2 Elements of a List

# 1

li = [11,22,33,44,55,66,77,88]
print(li)

p1, p2 = 2, 6
li[p1], li[p2] = li[p2], li[p1]

print(li)
print()

#  2 (using pop & insert)

li1 = [1, 2, 3, 4, 5, 6, 7]
print(li1)

first = li1.pop(2)
last = li1.pop(5)
# print(li1)

li1.insert(5, first)
li1.insert(2,last)
print(li1)

print()


#  3 ( using tuple)

list = [2, 4, 6, 8,10]
print(list)

ele = (list[1], list[2], list[3])
(list[3], list[2], list[1]) = ele
print(list)
