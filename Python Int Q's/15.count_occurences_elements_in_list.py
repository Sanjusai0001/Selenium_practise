
#   Count Occurrences of an element in a list

#  1  -   loop  method

list = [5, 10, 2, 3, 5, 15, 5, 25, 5, 15]
print(list)

ele = 5
count = 0

for i in list:
    if (ele == i):
        count += 1 # or count = count + 1

# print("{} has {} times present in list".format(ele,count))
print(ele, "appeared",count)

#    2  - count() method

mylist = [0, 10, 0,2, 11, 0, 1, 0,5, 11,0 ]
print('\n', mylist)

times = mylist.count(0)
print(' 0 has appeared', times, 'times')

x = 0
print(" {} has occured {} times".format(x, mylist.count(x)))
print()
#   3  -   using  counter()

from collections import Counter

li = [3, 1, 2, 3, 5, 2, 2,1,0]
i = 3
item = Counter(li)
print(item)            #  Counter({2: 3, 3: 2, 1: 2, 5: 1, 0: 1})
print()
# 4

print("{} has appeared {} times".format(i, item[i]))