'''
Задание №2
Дано слово из маленьких латинских букв. Сколько там согласных и гласных
букв? Гласными называют буквы «a», «e», «i», «o», «u».
Для решения задачи создайте переменную и в неё положите слово с
помощью input()
А также определите количество каждой из этих гласных букв Если какой-то из
перечисленных букв нет - Выведите False
'''

word = input("введите слово: ")

a = word.count('a') or False
e = word.count('e') or False
i = word.count('i') or False
o = word.count('o') or False
u = word.count('u') or False

vowels = a + e + i + o + u
consonansts = len(word) - vowels

print(f"Гласных - {vowels}\nСогласных - {consonansts}\n")
print(f"{a = }\n{e = }\n{i = }\n{o = }\n{u = }")
