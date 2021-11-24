from roller.roller import Roller

special_abilities = {
    11: ("Immune to weapons", "Only unarmed attacks and spells can hurt the demon."),
    15: ("Immune to fire", "Cannot be hurt by fire."),
    23: ("Immune to cold", "Cold has no effect."),
    26: ("Lightning fast", "Draws two initiative cards and gets to act on both turns"),
    33: ("Immune to physical attacks ", "Physical attacks are ineffective."),
    35: (
        "Parasite",
        "By touching its victim, the demon can take control over it. This works as the PUPPETEER  spell with Power Level 3.",
    ),
    41: ("Regenerative", "Regains D3 Strength every round."),
    44: (
        "Paralyzing",
        "A victim touched by the demon is affected by a paralyzing poison with Potency D6+5.",
    ),
    46: (
        "Poisonous",
        "A victim touched by the demon is affected by a lethal poison with Potency D6+5.",
    ),
    52: (
        "Shapeshifter",
        "Can change shape into any creature. The copy is perfect except for one small detail (such as eye color).",
    ),
    55: ("Immaterial", "Can move through solid matter."),
    61: (
        "Floating",
        "Does not touch the ground. Can float up to 10 meters from the ground.",
    ),
    63: (
        "Teleportation",
        "Can instantly teleport to anywhere within LONG range every other round.",
    ),
    65: ("Roll twice on this table"),
}

r = Roller()


def double_special_ability():
    """Rolls 2 different abilities. Use this in case the initial roll got the 'Roll Twice' result."""
    first_roll = 66
    while first_roll > 55:
        first_roll = r.roll("d66")

    for key in special_abilities.keys():
        if key <= first_roll:
            candidate = key
    first_ability = special_abilities.get(candidate)

    second_roll = 66
    while second_roll > 55 or second_roll == first_roll:
        second_roll = r.roll("d66")
    for key in special_abilities.keys():
        if key <= second_roll:
            candidate = key
    second_ability = special_abilities.get(candidate)

    return first_ability, second_ability
