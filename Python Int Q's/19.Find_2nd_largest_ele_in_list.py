
#   Find 2nd Largest Number in a List

#   1    -  sort()

li = [3, 23, 79, 54, 16, 23]
print(li, '\n')

li.sort()
print("2nd largest number:", li[-2])

# alternative

# li.remove(max(li))
# print(li[-1])

#   2  -  set()

new_li = set(li)   # duplicate values will be removed

print(new_li)


#  3  -  2nd max()


first = max(li)
# print("1st largest element is",first)
new_li.remove(max(new_li))
second = max(new_li)
print("2nd largest element is",second)

