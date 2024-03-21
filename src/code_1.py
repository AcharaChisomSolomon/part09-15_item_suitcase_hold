class Item:
    def __init__(self, name: str, weight: int) -> None:
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"
    

class Suitcase:
    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.items = []

    def add_item(self, item: Item):
        if self.get_total_weight() + item.weight() <= self.max_weight:
            self.items.append(item)

    def get_total_weight(self):
        return sum([item.weight() for item in self.items])

    def print_items(self):
        for item in self.items:
            print(item)

    def heaviest_item(self):
        if len(self.items) == 0: return None

        curr_heaviest = 0
        curr_item = None

        for item in self.items:
            if item.weight() > curr_heaviest:
                curr_heaviest = item.weight()
                curr_item = item

        return curr_item

    def weight(self):
        return self.get_total_weight()

    def __str__(self) -> str:
        length = len(self.items)
        return f"{length} {'item' if length == 1 else 'items'} ({self.get_total_weight()} kg)"


class CargoHold:
    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.suitcases = []

    def __get_total_weight(self):
        return sum([suitcase.get_total_weight() for suitcase in self.suitcases])
    
    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.get_total_weight() + self.__get_total_weight() <= self.max_weight:
            self.suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.suitcases:
            suitcase.print_items()

    def __str__(self) -> str:
        length = len(self.suitcases)
        return f"{length} suitcase{'' if length == 1 else 's'}, space for {self.max_weight - self.__get_total_weight()} kg"
    


# book = Item("ABC Book", 2)
# phone = Item("Nokia 3210", 1)
# brick = Item("Brick", 4)

# adas_suitcase = Suitcase(10)
# adas_suitcase.add_item(book)
# adas_suitcase.add_item(phone)

# peters_suitcase = Suitcase(10)
# peters_suitcase.add_item(brick)

# cargo_hold = CargoHold(1000)
# cargo_hold.add_suitcase(adas_suitcase)
# cargo_hold.add_suitcase(peters_suitcase)

# print("The suitcases in the cargo hold contain the following items:")
# cargo_hold.print_items()