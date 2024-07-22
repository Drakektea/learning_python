class Tea:
    def __init__(self, title, kind, taste, leaf):
        self.title = title
        self.kind = kind
        self.taste = taste
        self.leaf = leaf

    def info(self, price=None):
        print(f"{self.title} - {self.kind} tea\nWith {self.taste} taste and {self.leaf} leaf")
        if price and price > 0:
            print(f"Всего лишь за {price} долларов")


favourite = Tea('erl grey', 'black', 'cutrus', 'large')

favourite.info(1)
