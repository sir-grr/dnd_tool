import random

class Dice:
    def __init__(self,sidesIn):
        self.sides = sidesIn

    def roll(self,*count):
        if count:
            result = 0
            for i in range(count):
                result += random.choice(self.sides)
            return result
        else:
            return random.choice(self.sides)
    