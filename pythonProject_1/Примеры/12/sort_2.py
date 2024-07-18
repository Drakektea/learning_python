users = [('Petrov', 19), ('Anna', 16), ('Alina', 28), ('Andrew', 17)]
print(f'{users = }')

users.sort(key=lambda user: -user[-1])
print(f'{users = }')
