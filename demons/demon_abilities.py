from roller.roller import Roller

abilities = {
    11: ("Stoneskin", "Armor Rating +6"),
    13: ("Giant", "Strength +2D6"),
    15: ("Burning Body", "Immune to fire."),
    21: ("Made of Ice", "Armor Rating +2"),
    23: ("Mummified Fear", "attack D6+5"),
    25: ("Slimy", "Can move through very small openings."),
    31: ("Unnaturally Beautiful", "+2 Manipulation"),
    33: ("Covered by Sores", "Infectious Touch, Virulence D6+5"),
    35: ("Feathers", "Armor Rating +2"),
    41: ("Wings Can fly", "Movement Rating 3"),
    44: ("Filled by Light" "Fear attack D6+5"),
    46: ("Covered in Vines", "Armor Rating +3"),
    51: ("Transparent", "All attacks get a –3 penalty"),
    54: ("Covered by Eyes", "Draw one extra initiative card, discard the worst one."),
    55: ("No Eyes", "Draw one extra initiative card, discard the best one."),
    56: ("Roll Twice"),
}

r = Roller()


def double_ability():
    """Rolls 2 different abilities. Use this in case the initial roll got the 'Roll Twice' result."""
    first_roll = 66
    while first_roll > 55:
        first_roll = r.roll("d66")
    first_ability = abilities.get(first_roll)

    second_roll = 66
    while second_roll > 55 or second_roll == first_roll:
        second_roll = r.roll("d66")
    second_ability = abilities.get(second_roll)
    return first_ability, second_ability
