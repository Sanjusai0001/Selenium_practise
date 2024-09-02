
#  How To Clone or Copy a List

# 1  -   slicing method

list1 = [1, 3, 6,13]
mylist1 = list1[:]
print(mylist1)

#  2  -   Extend method

list2 = [2, 4, 7,12]
mylist2 = []
mylist2.extend(list2)
print(mylist2)

#  3  -   list method

list3 = [3, 4, 8,16]
mylist3 = []
mylist3 = list(list3)
print(mylist3)

#  4  -   copy method

list4 = [ 4, 8, 6,11]
mylist4 = list4.copy()
print(mylist4)

#  5  -   list comprehension method

list5 = [5, 14, 6,12]
mylist5 = [i for i in list5]
print(mylist5)

