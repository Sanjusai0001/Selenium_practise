
# How To Find Factorial of A Number

#   1

fact = 1
num = 5

for i in range(1, num+1):
    fact = fact * i
print('The Factorial value of ',num, 'is', fact)

#    2

def factorial_number(n):
    f = 1
    if n < 0:
        print("The Value must be positive")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, n+1):
            f *= i  #  f = f * i
        print('The Factorial value of ', n, 'is', f)

factorial_number(4)



#     3
# recursive function

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n - 1)

    #Using Ternary operator

    # return 1 if ( n == 0 or n == 1) else n * factorial(n-1)

number = 15

print(factorial(7))
print("The Factorial value", number,"is",factorial(number))