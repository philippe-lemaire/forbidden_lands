import random

class Roller:
    def roll(self, dice):
        if str(dice).endswith('66'):
            tens = random.randint(1,6)
            units = random.randint(1,6)
            return 10*tens + units
        if '+' in dice:
            d, mod = dice.split('+')
            d = int(d[1:])
            mod = int(mod)
        else:
            d = int(dice[1:])
            mod = 0
        return random.randint(1,d) + mod