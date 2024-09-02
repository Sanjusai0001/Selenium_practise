
# How To Clear a List

#   1

myList1 = [1,2,3,4,5]
print(myList1)

myList1.clear()
print(myList1)

#   2

myList2 = [2,4,5,1.5, 5]
print(myList2)
myList2 = []
print(myList2)

#   3
myList3 = [2,3,4,6,8]
print(myList3)
myList3 *= 0
print(myList3)

#   4

myList4 = [4,5,2,5,1,2]
print(myList4)

# del myList4[2:4]
del myList4[:]
print(myList4)