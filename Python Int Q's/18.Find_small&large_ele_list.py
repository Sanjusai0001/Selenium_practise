
#   Find Smallest & Largest Number small in a List

#   1   -  sort()
li = [54, 10, 23, 11, 2 ]

li.sort()
print("smal:", li[0], "large:",li[-1])



#   2  -   using min()  &  max()

mini = min(li)
max = max(li)
print(" smallest:", mini ," \n largest:", max)


#   3

li  = [22 , 6, 32, 13, 1]

small = li[0]
large = li[0]

for i in range(0, len(li)):
    if li[i] > small:
        small = li[i]
    if large > i:
        large = li[i]

print( " largest:", large, " \n smallest:", small)
