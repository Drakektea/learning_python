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
