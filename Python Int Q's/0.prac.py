# arr = [2,3,52,22,0,12, -12]
#
# print(sum(arr, -43))
# import numpy as np
#
# # 1D Array
# one_d_array_np = np.array([1, 2, 3, 4, 5])
# print("1D Array (NumPy):", one_d_array_np)
#
# # 2D Array
# two_d_array_np = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print("2D Array (NumPy):\n", two_d_array_np)
#
# # 3D Array
# three_d_array_np = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])
# print("3D Array (NumPy):\n", three_d_array_np)
#
#
# num3D =  np.array([[[12,3,4],[ [2,3],[23,5,2]]]])
# print(num3D)
#

# print(int(eval(input("Enter the number: "))))

a = [1, 2, 3]
b = a  # Both 'a' and 'b' reference the same list object
del a  # Reference count decreases but is not zero
del b  # Reference count becomes zero, and memory is freed



import gc

gc.collect(a)

