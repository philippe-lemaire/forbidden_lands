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

    def __repr__(self):
        return f"An inn with this oddity: {self.oddity}. Their specialty: {self.specialty}. The special guest: {self.special_guest}."
