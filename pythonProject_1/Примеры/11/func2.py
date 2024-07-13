def say_hello():
    print('hello, world!')


say_hello()


def greet(name):
    print(f"Hi, {name}.")


greet("Dragon")


def add(num1, num2):
    return num1 + num2


print(add(2, 5))


def calculate_area(width, length):
    return width * length


print(calculate_area(length=5, width=3))


def greeting(name='Dragon', message='Приветик,'):
    print(message, name)


greeting()
greeting(name='Cat')
greeting(message='Самый лучший, милый, классный, любимый котиком')


def square1(x):
    return x ** 2


square2 = lambda x: x ** 2

print(square1(3), square2(3))
