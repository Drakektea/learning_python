word = input('Слово: ')
step = int(input('Шаг: '))
new_word = ''

for char in word:
    new_word += chr(ord(char) + step)

print(new_word)
