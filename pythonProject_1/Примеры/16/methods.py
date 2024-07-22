class Tea:
    title = None
    kind = None
    taste = None
    leaf = None

    def info(self, price=None):
        print(f"{self.title} - {self.kind} tea\nWith {self.taste} taste and {self.leaf} leaf")
        if price and price > 0:
            print(f"Всего лишь за {price} долларов")


favourite = Tea()
favourite.title = "erl grey"
favourite.kind = "black"
favourite.taste = "citrus"
favourite.leaf = "large"

favourite.info(1)
