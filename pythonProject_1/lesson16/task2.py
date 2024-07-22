'''
Задание №2
Создайте класс Черепашка, который хранит позиции x и y черепашки, а также
s - количество клеточек, на которое она перемещается за ход
у этого класс есть методы:
● go_up() - увеличивает y на s
● go_down() - уменьшает y на s
● go_left() - уменьшает x на s
● go_right() - увеличивает y на s
● evolve() - увеличивает s на 1
● degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может
стать ≤ 0
● count_moves(x2, y2) - возвращает минимальное количество действий, за
которое черепашка сможет добраться до x2 y2 от текущей позиции
'''

class Turtle:
    def __init__(self, x, y, step=1):
        self.x = x
        self.y = y
        self.step = step
        print(f"черепашка была поставлена в координаты ({x}, {y}),\nона может двигаться с шагом в {step} клеточные единицы")

    def go_up(self):
        self.y += self.step
        print(f"Y поднят на {self.step}, черепашка в ({self.x}, {self.y})")

    def go_down(self):
        self.y -= self.step
        print(f"Y опущен на {self.step}, черепашка в ({self.x}, {self.y})")

    def go_right(self):
        self.x += self.step
        print(f"X поднят на {self.step}, черепашка в ({self.x}, {self.y})")

    def go_left(self):
        self.x -= self.step
        print(f"X опущен на {self.step}, черепашка в ({self.x}, {self.y})")

    def evolve(self):
        self.step += 1
        print(f"S увеличен на 1 (S = {self.step})")

    def degrade(self):
        if self.step - 1 < 1:
            print("S нельзя уменьшить (S = 1)")
        self.step -= 1
        print(f"S уменьшен на 1 (S = {self.step})")


t = Turtle(-1, 0)
for i in range(10):
    t.go_up()
    t.evolve()
    t.go_right()
    t.evolve()
    t.go_down()
    t.evolve()
    t.go_left()