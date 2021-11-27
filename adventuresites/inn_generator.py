from roller.roller import Roller
from forbidden_lands.utils import find_key

inn_table = {
    11: ("Violence is in the air", "Cheap diluted beer", "Escaped criminal"),
    13: (
        "Barrels instead of chairs, planks instead of tables",
        "Meat stew",
        "Unhappy farmer",
    ),
    16: ("Big fireplace", "Grilled rodent", "Scarred treasure hunter"),
    23: ("Pelts on walls", "Stewed turnips", "Dirty and sullen hunter"),
    26: ("Long communal table", "Salt bird", "Silent Raven sister"),
    33: ("Gambling den", "Blood soup", "Noisy bandit"),
    36: ("Mediocre bard", "Fiery spice wine", "Old war veteran"),
    43: ("Nice dog", "Roasted piglet", "Noble in disguise"),
    46: ("Grumpy owner", "Swamp stew", "Secretive spellbinder"),
    53: ("Monster head on wall", "Vegetable mush", "Annoying jester"),
    55: ("Singing waiter", "Salted fish", "Dusty traveller"),
    61: ("Stomped floor", "Cooked crow", "Hungry dwarf"),
    63: ("Birthday party", "Bear stew", "Frosty elf"),
    65: ("Drunk adventurers", "Dwarven strong ale", "Scouting thief"),
}

inn_name_table = {
    11: ("Third", "Lantern"),
    12: ("Little", "Swine"),
    13: ("Red", "Wheel"),
    14: ("Misty", "Stoop"),
    15: ("Bloody", "Sparrow"),
    16: ("Old", "Goat"),
    21: ("Golden", "Arrow"),
    22: ("Cold", "Pot"),
    23: ("Refreshing", "Lamb"),
    24: ("Good", "Maid"),
    25: ("Second", "Man"),
    26: ("Last", "Dragon"),
    31: ("Prancing", "Griffin"),
    32: ("Happy", "Boar"),
    33: ("Singing", "Barrel"),
    34: ("Rolling", "Bard"),
    35: ("Rumping", "Dog"),
    36: ("Wailing", "Horse"),
    41: ("Greedy", "Girl"),
    42: ("Round", "Wolf"),
    43: ("Flaming", "Bear"),
    44: ("Last ", "Ghost"),
    45: ("Silver", "Rat"),
    46: ("Black", "Jar"),
    51: ("Dead", "Mug"),
    52: ("Big", "Goblet"),
    53: ("Roaring", "Eagle"),
    54: ("Cheering", "Raven"),
    55: ("Humming", "Hammer"),
    56: ("Meagre", "Spike"),
    61: ("Fat", "Crow"),
    62: ("Thick", "Druid"),
    63: ("Round", "Knight"),
    64: ("Sweet", "Bandit"),
    65: ("Boisterous", "Wild Boar"),
    66: ("Grumpy", "Hunter"),
}


class Inn:
    def __init__(self):
        r = Roller()

        oddity_roll = r.roll("d66")
        key = find_key(oddity_roll, inn_table)
        self.oddity = inn_table.get(key)[0]

        specialty_roll = r.roll("d66")
        key = find_key(specialty_roll, inn_table)
        self.specialty = inn_table.get(key)[1]

        special_guest_roll = r.roll("d66")
        key = find_key(special_guest_roll, inn_table)
        self.special_guest = inn_table.get(key)[2]

        first_roll = r.roll("d66")
        last_roll = r.roll("d66")
        name_type = r.roll("d10")

        key_first = find_key(first_roll, inn_name_table)
        key_last = find_key(last_roll, inn_name_table)

        first = f"The {inn_name_table.get(key_first)[0]}"

        if name_type % 2 == 0:
            last = f"and the {inn_name_table.get(key_last)[0]}"
        else:
            last = inn_name_table.get(key_last)[1]

        self.name = f"{first} {last}"

    def __repr__(self):
        return f"An inn called {self.name} with this oddity: {self.oddity}. Their specialty: {self.specialty}. The special guest: {self.special_guest}."
