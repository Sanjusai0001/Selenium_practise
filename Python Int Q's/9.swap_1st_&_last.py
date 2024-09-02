
#   How To Swap First & Last Elements of a List

#    1

list = [2, 4, 52, 11, 25, 6]
total = len(list)
print(list)

dup = list[0]             # a = b
list[0] = list[total-1]   # b = c
list[total-1] = dup      # c = a

print(list)


#     2

li = [14, 34, 26, 66, 42, 99, 73]
print('\n', li)

li[0], li[-1] = li[-1], li[0]          # a, b = b, a
# li[0], li[-2] = li[-2], li[0]          # a, b = b, a

print(li)


#     3  (tuple approach)

lst = [1,2,3,4]
print('\n', lst)

set1 = (lst[-1], lst[0])        # c = a, b
lst[0], lst[-1] = set1          # a, b = c

print(lst)

#    4    -  using  *  operator

lists = [11, 22, 33, 44, 55, 77]
print('\n', lists)


start, *middle, end = lists
lists = [end, *middle, start]
print(lists)


#       5  -    using pop()

myList = [0,1,2,3,9]
print('\n', myList)

first = myList.pop(0)
last = myList.pop(-1)

myList.insert(0, last)
myList.append(first)

print(myList)