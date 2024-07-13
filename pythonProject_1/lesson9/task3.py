'''
Задание №3
Во входную строку водится последовательность чисел через пробел. Для
каждого числа выведите слово ”YES” (в отдельной строке), если это число
ранее встречалось в последовательности или ”NO”, если не встречалось.
'''

nums = [int(num) for num in input("введите список чисел через пробел: ").split()]

exist_nums = set()
for num in nums:
    if num in exist_nums:
        print(f"{num}(YES)", end=" ")
    else:
        print(f"{num}(NO)", end=" ")
    exist_nums.add(num)
