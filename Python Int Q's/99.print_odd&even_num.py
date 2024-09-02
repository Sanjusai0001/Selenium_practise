

#   even

def even_num(n):
    for i in range(1,n):
        if i % 2 == 0:
            print(i)


even_num(15)

print()

#  odd

def odd_num(n):
    for i in range(1, n):
        if i % 2 != 0:
            print(i)

odd_num(9)