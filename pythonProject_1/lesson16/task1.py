'''
Задание №1
Создайте класс Касса, который хранит текущее количество денег в кассе, у
него есть методы:
● top_up(X) - пополнить на X
● count_1000() - выводит сколько целых тысяч осталось в кассе
● take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не
достаточно денег
'''

class Cashier:
    def __init__(self, cash):
        self.cash = cash
        print(f"открыта касса с деньгами в раземер {cash} едениц")

    def top_up(self, x):
        self.cash += x
        print(f"ваш баланс пополнен на {x}, теперь он составляет {self.cash}")

    def count_1000(self):
        print(f"на балансе целых тысяч осталось {self.cash // 1000}")

    def take_away(self, x):
        if self.cash - x < 0:
            print(f"в кассе не достаточно средств (баланс {self.cash})")
            return
        self.cash -= x
        print(f"со счета кассы снято {x}, теперь на балансе {self.cash}")


dragon = Cashier(cash=15000)
dragon.take_away(x=500)
dragon.top_up(12000)
dragon.count_1000()
dragon.take_away(26500)