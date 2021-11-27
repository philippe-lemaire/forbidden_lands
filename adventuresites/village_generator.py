import random

from roller.roller import Roller
from .inn_generator import Inn
from forbidden_lands.utils import find_key

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

oddity_table = {
    11: "Eccentric Clothing",
    14: "Incomprehensible Accent",
    16: "Smells Bad",
    22: "Full of Flowers",
    24: "Muddy",
    26: "Odd Building Materials",
    32: "Tent Village",
    33: "Built on Steep Hill",
    35: "Old Tower in the Middle",
    36: "Grand Building",
    41: "Windy",
    43: "Inbreeding",
    44: "Strange Eating Habits",
    46: "Built on Marshland",
    52: "Cut Out of a Cliff",
    53: "Old Burial Site",
    55: "Wandering Cattle",
    61: "Mostly Inhabited by Women",
    63: "Allied with Monster",
    65: "Preparing Wedding",
}

institution_table = {
    11: "Nothing",
    21: "Inn",
    31: "Mill",
    36: "Smith",
    44: "Forester",
    51: "Trading Post",
    54: "Temple",
    56: "Militia",
    63: "Tavern",
    65: "Stable",
}


class Village:
    def __init__(self):
        r = Roller()
        size_roll = r.roll("d6")
        key = find_key(size_roll, size_table)
        self.type = size_table.get(key)[0]
        size_range = size_table.get(key)[1]
        self.inhabitants = random.randint(*size_range)

        age_roll = r.roll("d66")
        key = find_key(age_roll, age_table)
        self.build_time = age_table.get(key)[0]
        age_range = age_table.get(key)[1]
        self.age = random.randint(*age_range)

        ruler_oddity_roll = r.roll("d66")
        ruler_type_roll = r.roll("d66")
        key = find_key(ruler_oddity_roll, ruler_table)
        oddity = ruler_table.get(key)[0]

        key = find_key(ruler_type_roll, ruler_table)
        ruler_type = ruler_table.get(key)[1]

        if ruler_type == ruler_table.get(41)[1]:
            self.ruler = "no one"
        else:
            self.ruler = f"a {oddity.lower()} {ruler_type.lower()}"

        problem_roll = r.roll("d66")

        key = find_key(problem_roll, problem_table)
        self.problem = problem_table.get(key).lower()

        fame_roll = r.roll("d66")
        key = find_key(fame_roll, fame_table)
        self.fame = fame_table.get(key).lower()

        oddity_roll = r.roll("d66")
        key = find_key(oddity_roll, oddity_table)
        self.oddity = oddity_table.get(key).lower()

        num_institution_dict = {"Outpost": 1, "Hamlet": 3, "Village": r.roll("d6+5")}

        num_institution = num_institution_dict.get(self.type)
        self.institutions = set()

        for _ in range(num_institution):
            institution_roll = r.roll("d66")
            key = find_key(institution_roll, institution_table)
            if key != 11:
                self.institutions.add(institution_table.get(key))

        self.inn = Inn()

    def __repr__(self):
        return f"""{self.type} with {self.inhabitants} inhabitants. 
    Built {self.build_time}, {self.age} years ago. Ruled by {self.ruler}. 
    The problem: {self.problem}.
    Their fame is {self.fame}.
    Their oddity is {self.oddity}.
    Their institutions are {self.institutions}.
    Their in is {self.inn}.
    """
