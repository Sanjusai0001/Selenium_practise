
#  Print Fibonacci Series

# 0,1,1, 2, 3, 5, 8, 13, 21,

#  1

x = 0
y = 1
# print(x,y)

for i in range(0, 7):
    add = x + y
    print(add)
    x = y
    y = add


#  2

n = 5
a = 0
b = 1
c = b
count = 0

print("\n Fibonacci Series : ")

while count < n:
    print(c, end=', ')
    count += 1
    a, b = b, c
    c = a + b


#  3

def fibonacci_series(x):

    p, q = 0, 1
    counts = 0
    if x <= 0:
        print("\n please enter a positive number")

    elif x == 1:
        print("\n Fibonacci series upto x:")
        print(p)
    else:
        print("\n Fibonacci series:")
        print(p, q, end=', ')
        while counts < (x - 2):
            r = p + q
            print(r, end=', ')
            counts += 1
            p = q
            q = r



nth = 12
fibonacci_series(nth)