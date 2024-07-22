'''
Задание №1
Есть родительский класс:

class Transport:
    def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

Создайте объект Autobus, который унаследует все переменные и методы
родительского класса Transport и выведете его.

Ожидаемый результат вывода:
Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12
'''

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show_info(self):
        print(f"Title: {self.name}\nMax speed: {self.max_speed}\nMileage: {self.mileage}")


Autobus = Transport("Reno Logan", 180, 12)
Autobus.show_info()


'''
Задание №2
Создайте класс Autobus, который наследуется от класса Transport.
Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
Используйте переопределение метода.
Используйте следующий код для родительского класса транспортного
средства:

class Transport:
    def __init__(self, name, max_speed, mileage):
    self.name = name
    self.max_speed = max_speed
    self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity}
        пассажиров"

Ожидаемый результат вывода:
Вместимость одного автобуса Renaul Logan: 50 пассажиров
'''


class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show_info(self):
        print(f"Title: {self.name}\nMax speed: {self.max_speed}\nMileage: {self.mileage}")


class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name} составляет {capacity} пассажиров"


some_transport = Autobus("Reno Logan", 180, 12)
some_transport.show_info()
print(some_transport.seating_capacity())
