a = 1
b = 3

print(f'{a = }  {b = }')

a, b = b, a

print(f'{a = }  {b = }')


nums = [1, 2, 3, 4]
print(f'{nums = }')

nums[0], nums[1], nums[2], nums[3] = nums[3], nums[2], nums[1], nums[0]
print(f'{nums = }')
