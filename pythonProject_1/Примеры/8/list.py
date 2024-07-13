nums = [5, 1, 1, 2, 3, 4]
nums.sort(reverse=True)  # [5, 4, 3, 2, 1, 1]
print(nums.count(1))  # 2
print(nums)
nums.reverse() # [1, 1, 2, 3, 4, 5]
print(nums)
item = nums.pop(0)
print(nums, item)  # [1, 2, 3, 4, 5] 1
del nums[0]
print(nums)  # [2, 3, 4, 5]
nums.insert(0, 1)
print(nums)  # [1, 2, 3, 4, 5]
nums.append(6)
print(nums)  # [1, 2, 3, 4, 5, 6]
nums.extend([7, 8, 9])
print(nums)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums + [10, 11, 12])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
nums.remove(9)
print(nums)  # [1, 2, 3, 4, 5, 6, 7, 8]
print(nums.index(3))  # 2


a = [1, 2, [3, 4]]
b = a.copy()
a[2][0] = 999
a[0] = 1123
print(a , b)  # [1123, 2, [999, 4]] [1, 2, [999, 4]]
