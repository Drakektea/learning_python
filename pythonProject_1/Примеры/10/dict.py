user = {
    'name': 'Милый дракоша',
    'age': 31,
    'city': 'Moscow',
    'color': 'black and white',
}

user['name'] = '<=======3'
print(user['name'])

color = user.pop('color')
print(user, color)

print(user.get('namee', 'Not found'))

print(user.keys())
print(user.values())

print(user.items())

city = user.popitem()
print(user, city)

# user.update(city='Moscow')
user['city'] = 'Moscow'
print(user)
