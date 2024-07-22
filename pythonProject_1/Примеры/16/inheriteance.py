class Tea:
    def __init__(self, title):
        self.title = title

    def show_title(self):
        print(f"It\'s {self.title} tea")


class Puer(Tea):
    def __init__(self, title, kind='black'):
        super().__init__(title)
        self.kind = kind

    def show_title(self):
        print(f"It\'s Puer {self.title} tea")


black = Tea('black')
tasty = Puer('Dragon')

black.show_title()
tasty.show_title()
