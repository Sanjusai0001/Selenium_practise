# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x
#     def test_two(self):
#         x = "hello"
#         assert hasattr(x, "check")
#
# class TestClassDemoInstance:
#     value = 0
#
#     def test_one(self):
#         self.value = 1
#         assert self.value == 1
#
#     def test_two(self):
#         assert self.value == 1

class OPS:
    def __init__(self, array, n, k):
        self.array = array
        self.n = n
        self.k = k


    @staticmethod
    def dweight(mid, array, n, k):
        count = 0
        sum = 0
        for i in range(n):
            if(array[i] > mid):
                return  False
            sum = sum + array[i]
            if (sum > mid):
                count = count + 1
                sum = array[i]

        count = count + 1
        if  (count <= k):
            return True
        return False

ops = OPS(1,5,3)
# out_ = ops.dweight()
# print(out_)

array = [1, 2, 3, 4, 5]
n = 5
k = 3
ops = OPS(array, n, k)
mid = 5  # You need to provide a value for `mid`
out_ = ops.dweight(mid, array, n, k)
print(out_)