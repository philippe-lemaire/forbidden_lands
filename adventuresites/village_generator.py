import random

from roller.roller import Roller

size_table = {
    1: ("Outpost", (5, 20)),
    3: ("Hamlet", (20, 100)),
    6: ("Village", (100, 400)),
}


class Village:
    def __init__(self):
        r = Roller()
        size_roll = r.roll("d6")
        for key in size_table.keys():
            if key <= size_roll:
                candidate = key
        self.type = size_table.get(candidate)[0]
        size_range = size_table.get(candidate)[1]
        self.inhabitants = random.randint(*size_range)

    def __repr__(self):
        return f"{self.type} with {self.inhabitants} inhabitants."
