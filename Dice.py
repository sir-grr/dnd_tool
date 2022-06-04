import random

class Dice:
    def __init__(self,sidesIn):
        self.sides = sidesIn
        
    def roll(self):
        return random.choice(self.sides)
    