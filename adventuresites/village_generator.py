import random

from roller.roller import Roller

size_table = {
    1: ("Outpost", (5, 20)),
    3: ("Hamlet", (20, 100)),
    6: ("Village", (100, 400)),
}

age_table = {
    11: ("before the Blood Mist", (300, 1100)),
    21: ("buring the Alder Wars", (305, 360)),
    26: ("buring the Blood Mist", (5, 280)),
    61: ("after the Blood Mist", (1, 6)),
}

ruler_table = {
    11: ("Bickering", "Council"),
    14: ("Cruel", "Despot"),
    21: ("Weak", "Elder"),
    24: ("Greedy", "Mayor"),
    31: ("Wise", "Druid"),
    34: ("Eccentric", "Sorcerer"),
    41: ("Confused" "No one"),
    44: ("Brutal", "Commander"),
    51: ("Cunning", "Trader"),
    54: ("Stern", "Rust Brother"),
    61: ("Secretive", "Artisan"),
    64: ("Drunkard", "Bandit Chief"),
}


class Village:
    def __init__(self):
        r = Roller()
        size_roll = r.roll("d6")
        for key in size_table:
            if key <= size_roll:
                candidate = key
        self.type = size_table.get(candidate)[0]
        size_range = size_table.get(candidate)[1]
        self.inhabitants = random.randint(*size_range)

        age_roll = r.roll("d66")
        for key in age_table:
            if key <= age_roll:
                candidate = key
        self.build_time = age_table.get(candidate)[0]
        age_range = age_table.get(candidate)[1]
        self.age = random.randint(*age_range)

        ruler_oddity_roll = r.roll("d66")
        ruler_type_roll = r.roll("d66")
        for key in ruler_table:
            if key <= ruler_oddity_roll:
                candidate = key
        oddity = ruler_table.get(candidate)[0]
        for key in ruler_table:
            if key <= ruler_type_roll:
                candidate = key
        ruler_type = ruler_table.get(candidate)[1]

        if ruler_type == ruler_table.get(41)[1]:
            self.ruler = "no one"
        else:
            self.ruler = f"a {oddity.lower()} {ruler_type.lower()}"

    def __repr__(self):
        return f"{self.type} with {self.inhabitants} inhabitants. Built {self.build_time}, {self.age} years ago. Ruled by {self.ruler}."
