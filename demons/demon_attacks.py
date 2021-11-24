from roller.roller import Roller


attacks_table = {
    # Rolled d66 value: ('name', 'base dice', 'damage (sometimes requires a roll)', 'reach'),
    11: ("Claws", "D6+4", {1: 1, 3: 2, 6: 3}, "Arm’s Length"),
    16: ("Teeth", "D6+5", {1: 1, 3: 2, 6: 3}, "Arm’s Length"),
    23: ("Horn", "d6+6", {1: 2, 5: 3}, "Arm's Length"),
    26: ("Tentacles", "d6+4", {1: 2, 3: 2}, "Near"),
    33: (
        "Fire",
        "d6+6",
        """The victim continues to take 1
point of damage every round until
the fire is put out with a MOVE roll.""",
        "Near",
    ),
    36: ("Cold", "D6+5", "The victim also instantly becomes COLD", "Near"),
    42: ("Roar", "d3+6", "Fear attack", "Near"),
    46: ("Killing gaze", "d6+5", "Fear attack", "Near"),
    52: (
        "Heavy weapon",
        "d6+5",
        {
            1: "Longsword",
            2: "Two handed sword",
            3: "Heavy Warhammer",
            4: "Morningstar",
            5: "Two-handed Axe",
            6: "Trident",
        },
        "Arm's Length",
    ),
    61: "Roll Three Times",
    66: "Roll Four Times",
}


class Attack:
    def __init__(self, name, base_dice, dmg, reach):
        r = Roller()

        self.name = name
        self.base_dice = r.roll(base_dice)
        if type(dmg) == dict:
            roll = r.roll("d6")
            for key in dmg:
                if key <= roll:
                    candidate = key
            self.dmg = dmg.get(candidate)
        else:
            self.dmg = dmg
        self.reach = reach

    def __repr__(self):
        return f"{self.name}. Base Dice: {self.base_dice}. Damage: {self.dmg}. Range: {self.reach}."


def roll_multiple_attacks(n):
    "Rolls for 3 or 4 attacks"
    r = Roller()
    rolled_attacks = []
    previous_rolls = []
    for _ in range(n):
        roll = 66
        while roll > 60 and roll not in previous_rolls:
            roll = r.roll("d66")
        previous_rolls.append(roll)
        for key in attacks_table.keys():
            if key <= roll:
                candidate = key
        rolled_attacks.append(Attack(*attacks_table.get(candidate)))
    return rolled_attacks


def roll_attacks():
    rolled_attacks = []
    r = Roller()
    first_roll = r.roll("d66")
    for key in attacks_table.keys():
        if key <= first_roll:
            candidate = key
    if candidate < 61:
        rolled_attacks.append(Attack(*attacks_table.get(candidate)))
    elif candidate < 66:
        # make a roll twice func that returns 3 different attacks
        rolled_attacks.extend(roll_multiple_attacks(3))
    else:
        rolled_attacks.extend(roll_multiple_attacks(4))
    second_roll = r.roll("d66")
    for key in attacks_table.keys():
        if key <= second_roll:
            candidate = key
    if candidate < 61:
        rolled_attacks.append(Attack(*attacks_table.get(candidate)))
    elif candidate < 66:
        # make a roll twice func that returns 3 different attacks
        rolled_attacks.extend(roll_multiple_attacks(3))
    else:
        rolled_attacks.extend(roll_multiple_attacks(4))

    return list(set(rolled_attacks))
