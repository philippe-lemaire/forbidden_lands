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

problem_table = {
    11: "Nightwargs",
    14: "Widespread Drunkenness",
    21: "Power Struggle",
    24: "Secret Cult",
    31: "Schism",
    34: "Undead",
    41: "Disease",
    44: "Sinkhole",
    51: "Bandits",
    54: "Terrorizing Monster",
    61: "Slave Trade",
    64: "Haunted by Ghoul or Ghost",
}

fame_table = {
    11: "Excellent Wine",
    14: "Delicious Bread",
    21: "Craftsmanship",
    24: "Beautiful Location",
    31: "A Horrible Massacre",
    34: "Decadence",
    41: "Well–Brewed Beer",
    44: "Hidden Riches",
    51: "Strange Disappearances",
    54: "Worshipping Demons",
    61: "Suspicion of Strangers",
    64: "Hospitality",
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

        problem_roll = r.roll("d66")
        for key in problem_table:
            if key <= problem_roll:
                candidate = key
        self.problem = problem_table.get(candidate).lower()

        fame_roll = r.roll("d66")
        for key in fame_table:
            if key <= fame_roll:
                candidate = key
        self.fame = fame_table.get(candidate).lower()

    def __repr__(self):
        return f"""{self.type} with {self.inhabitants} inhabitants. 
    Built {self.build_time}, {self.age} years ago. Ruled by {self.ruler}. 
    The problem: {self.problem}.
    Their fame is {self.fame}.
    """
