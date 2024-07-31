class Item:
    def __init__(self, icon, max_item_count,
                 min_item_count=0, current_value=0):
        self.icon = icon
        self.min_value = min_item_count
        self.max_value = max_item_count
        self.current_value = current_value

    @property
    def info_stat(self):
        return f'{self.icon} {self.min_value}/{self.current_value}/{self.max_value}'

    @property
    def in_min_max(self):
        return self.min_value < self.current_value <= self.max_value


class Statistic:
    def __init__(self, *items: Item):
        self.items = items

    @property
    def info_stats(self):
        return ' | '.join(item.info_stat for item in self.items)
