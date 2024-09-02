
# Multiply All Numbers in the List

#    1  - Traversal
import numpy

list = [5,2,4,6]
value = 1

for i in list:
    value = value * i

print(value)


#    2  - using numpy

import numpy

myList = [7, 5, 10]

output = numpy.prod(myList)
print(output)