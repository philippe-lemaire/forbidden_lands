from roller.roller import Roller

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
    11: ("The Third", "Lantern"),
    12: ("The Little", "Swine"),
    13: ("The Red", "Wheel"),
    14: ("The Misty", "Stoop"),
    15: ("The Bloody", "Sparrow"),
    16: ("The Old", "Goat"),
    21: ("The Golden", "Arrow"),
    22: ("The Cold", "Pot"),
    23: ("The Refreshing", "Lamb"),
    24: ("The Good", "Maid"),
    25: ("The Second", "Man"),
    26: ("The Last", "Dragon"),
    31: ("The Prancing", "Griffin"),
    32: ("The Happy", "Boar"),
    33: ("The Singing" "Barrel"),
    34: ("The Rolling", "Bard"),
    35: ("The Rumping", "Dog"),
    36: ("The Wailing", "Horse"),
    41: ("The Greedy", "Girl"),
    42: ("The Round", "Wolf"),
    43: ("The Flaming", "Bear"),
    44: ("The Last ", "Ghost"),
    45: ("The Silver", "Rat"),
    46: ("The Black", "Jar"),
    51: ("The Dead", "Mug"),
    52: ("The Big", "Goblet"),
    53: ("The Roaring", "Eagle"),
    54: ("The Cheering", "Raven"),
    55: ("The Humming", "Hammer"),
    56: ("The Meagre", "Spike"),
    61: ("The Fat", "Crow"),
    62: ("The Thick", "Druid"),
    63: ("The Round", "Knight"),
    64: ("The Sweet", "Bandit"),
    65: ("The Boisterous", "Wild Boar"),
    66: ("The Grumpy", "Hunter"),
}


class Inn:
    def __init__(self):
        r = Roller()

        oddity_roll = r.roll("d66")
        for key in inn_table:
            if key <= oddity_roll:
                candidate = key
        self.oddity = inn_table.get(candidate)[0]

        specialty_roll = r.roll("d66")
        for key in inn_table:
            if key <= specialty_roll:
                candidate = key
        self.specialty = inn_table.get(candidate)[1]

        specialty_roll = r.roll("d66")
        for key in inn_table:
            if key <= specialty_roll:
                candidate = key
        self.specialty = inn_table.get(candidate)[1]

        special_guest_roll = r.roll("d66")
        for key in inn_table:
            if key <= special_guest_roll:
                candidate = key
        self.special_guest = inn_table.get(candidate)[2]

        first_roll = r.roll("d66")
        last_roll = r.roll("d66")
        name_type = r.roll("d10")

        for key in inn_name_table:
            if key <= first_roll:
                candidate = key
            if key <= last_roll:
                candidate_last = key
        first = inn_name_table.get(candidate)[0]

        if name_type % 2 == 0:
            last = f"and {inn_name_table.get(candidate_last)[0]}"
        else:
            last = inn_name_table.get(candidate_last)[1]

        self.name = f"{first} {last}"

    def __repr__(self):
        return f"An inn called {self.name} with this oddity: {self.oddity}. Their specialty: {self.specialty}. The special guest: {self.special_guest}."
