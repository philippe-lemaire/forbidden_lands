from roller.roller import Roller
from demons.demon_forms import forms
from demons.demon_abilities import abilities, double_ability
from demons.demon_attacks import roll_attacks


class Demon:
    r = Roller()

    def __init__(self):
        r = Roller()
        form_roll = r.roll("d66")
        # find the proper value in forms.keys()
        for key in forms.keys():
            if key <= form_roll:
                candidate = key
        # grab the form from the dict
        form = forms.get(candidate)

        # populate values from the form
        self.form = form[0]
        self.strength = r.roll(form[1])
        self.agility = form[2]
        self.wits = form[3]
        self.empathy = form[4]
        self.armor = r.roll(form[5])
        self.effect = form[6]
        # roll for first ability
        self.abilities = []
        abilities_roll = r.roll("d66")
        for key in abilities.keys():
            if key <= abilities_roll:
                candidate = key
        if candidate < 56:
            self.abilities.append(abilities.get(candidate))
        else:
            self.abilities.extend(double_ability())
        # roll of attacks
        self.attacks = roll_attacks()
        self.special_abitily = ""
        self.weakness = ""

    def __repr__(self):
        return f"""A {self.form} demon.
    STR: {self.strength}
    AGI: {self.agility}
    WITS: {self.wits}
    EMP: {self.empathy}
    AR: {self.armor}
    {self.effect}.
    Abilities: {self.abilities}
    Attacks: {self.attacks}
    Special ability: {self.special_abitily}
    Weakness: {self.weakness}."""
