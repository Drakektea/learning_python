nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for j in range(len(nums)):
    for k in range(j, len(nums[j])):
        nums[j][k], nums[k][j] = nums[k][j], nums[j][k]

for j in range(len(nums)):
    for k in range(len(nums[j])):
        print(nums[j][k], end=' ')
    print()
