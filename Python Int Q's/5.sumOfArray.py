
#  Find Sum Of Elements in an Array



arr = [3,-3,2,13]

sum = 0
for i in arr:
    sum += i
print(sum)

# print(sum(arr))
# print(sum(arr, -13))
# print(sum(arr, 11))

# 1.Write a program to create a 1- D array of n elements and print the sum and average of them in python.
# 2. write a program to create a 1-D array of n elements and print the total number of elements which are above than average in python.
# 3. Write a program to create a 1- D array of n elements and print the total number of even and odd elements in python.
# 4. Write a program to create a 1- D array of n elements and print the largest element exists in the list in python.
# 5. Write a program to create a 1- D array of n elements  and print the   smallest element exist in the list in python.
# 6.write a program to create a 1 -D array of n elements and print the second largest element exists in the list in python.


# 7.write a program to create a 1-D array of n elements and print the second smallest elements exists in the list in python .

#  1
def find_second_smallest(arr):
    if len(arr) < 2:
        return None  # Not enough elements to find the second smallest

    # Initialize the smallest and second smallest elements
    smallest = second_smallest = float('inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

    return second_smallest if second_smallest != float('inf') else None


def main():
    n = int(input("Enter the number of elements in the list: "))
    if n < 2:
        print("List must contain at least two elements.")
        return

    arr = []
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        arr.append(element)

    second_smallest = find_second_smallest(arr)
    if second_smallest is not None:
        print("The second smallest element in the list is:", second_smallest)
    else:
        print("No second smallest element found.")

# if __name__ == "__main__":
#     main()

