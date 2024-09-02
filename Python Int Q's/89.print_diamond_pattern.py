



def print_diamond(n):
    if n % 2 == 0:
        print("Please enter an odd number for a symmetric diamond pattern.")
        return n

    # Top half of the diamond
    for i in range(n // 2 + 1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

    # Bottom half of the diamond
    for i in range(n // 2 - 1, -1, -1 ):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

print_diamond(7)