name = 'alEX: alEX, alEX!'

print(name.title())  # Alex: Alex, Alex!
print(name.capitalize())  # Alex: alex, alex!
print(name.casefold())  # alex: alex, alex!
print(name.center(40))  #            alEX: alEX, alEX!
print(name.endswith('0'))  # False
print(len(name))  # 17
print(' + '.join('123'))  # 1 + 2 + 3
print(name.split())  # ['alEX:', 'alEX,', 'alEX!']

print(f"{name = }")
