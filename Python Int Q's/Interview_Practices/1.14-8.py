"""
  1  -  input = India
        Outptut = a , Indi, aidnI
"""
str = "India"

print(str[4:])
print(str[:4])
print(str[::-1])


"""
 2  -   Input = li=["my", "name"], li=["is","john"]  
            output = my name is john
"""

li1 = ["my", "name"]
li2 = ["is", "john"]

  #  2 - 1
li3 = li1 + li2
# print(li3)
print(" ".join(li3))
  #  2 - 2
li1.extend(li2)
# print(li1)
print( " ".join(li1))


"""
3   -  input = ["a", "b", "c"], [1,2,3]   
output = {'a': 1, 'b': 2, 'c': 3}
"""

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

#  3  -  1  =  dict(zip())

dict1 = dict(zip(list1, list2))
print(dict1)

# 3  -  2 = for loop
dict2 = {list1[i] : list2[i]  for i in range(len(list1)) }
print(dict2)

# 3  -  3 = for loop key & for loop value
dict3 = {}
for key in list1:
    for value in list2:
        dict3[key] = value
        list2.remove(value)
        break
print(dict3)

"""
4  - Write a Python program to count the number of times a class is called
                                                    (or)
             How to count number of instances of a class in Python?
"""

#  1
class one:
    count = 0
    def __init__(self):
        one.count += 1
        print("class one is called")

a1 = one()
c1 = one()

print(one.count)
#   2
count = 0
class two:
    def __init__(self):
        global count
        count += 1
        print("class two is called")

b2 = two()
c4 = two()
b3 = two()

print(count)


""""
5. write a python program to find duplicate characters in the below list
"""

list = ["Happiness", "is","a", "Decision"]
str = "".join(list)
print(str)

duplicates = []

for char in str:
    if str.count(char) > 1 and char not in duplicates:
        duplicates.append(char)

print(duplicates)   #    ['a', 'p', 'i', 'n', 'e', 's']


"""
6. write a python program to find unique characters in the below list
"""

str = "DEVARA"
unique = []

for char in str:
    if str.count(char) == 1 and char not in unique:
        unique.append(char)

print(unique)

"""
7. print the ouput of below function
"""

class A:
    def demo(self):
        print("In class A")

class C(A):
    def demo(self):
        print("In class C")

class B(A):
    def demo(self):
        print("In class B")

class D(B, C):
    pass

test = D()
test.demo()

# It's depends on order of calling

'''''"
8. Write a one line for loop to print all the words in below list which starts with character 'i'
""'''
list = ["i'm", "from", "india"]

list2 = [word for word in list if word.startswith("i")] #or [("none")]
print(list2)

li = 2.3
print(type(li))