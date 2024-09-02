

#  Find Maximum & Minimum Elements in an Array


arr = [21,44,73,55,34,9]

# Max
max = arr[0]
n = len(arr)
for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
print("Maximum:",max)

# Min
min = arr[0]
m = len(arr)
for i in range(1, m):
    if arr[i] < min:
        min = arr[i]
print("Minimum:",min)
