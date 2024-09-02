
#   How To Swap 2 Numbers

# 1 using commas

a = 4
b = 5
print('Before swapping', a, b)

a,b = b,a
print('After swapping', a, b)

# 2 - Using arthmetic operators

x = 6.3
y = 8.2

print('Before swapping', x, y)

# swap code
x = x + y      #  14.5
y = x - y       #  6.3
x = x - y       #  8.2

print('After swapping', x, y)
# print('After swapping', x, round(y,1))
