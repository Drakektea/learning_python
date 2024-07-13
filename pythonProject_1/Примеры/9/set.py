nums1 = [1, 1, 3, 3, 2, 2,]
print(nums1)

num2 = {3, 3, 3, 2, 2, 1}
num2.add("4")
print(num2)
num2.discard(1)
print(num2)

num1 = {1, 2, 3}
num2 = {2, 3, 4}
print(num1.intersection(num2))
print(num1 & num2)
print(num1.union(num2))
print(num1 | num2)
print(num1.difference(num2))
print(num2.difference(num1))
print(num1 ^ num2)

num3 = set()
