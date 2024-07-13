item = 'Лампочка'
print(item[3:5] + item[3:])

print(item[slice(3, 5)] + item[slice(3, len(item))])
