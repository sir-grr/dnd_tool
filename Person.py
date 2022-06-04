import random
import fantasynames as names
from matplotlib.pyplot import delaxes
from Dice import Dice

class Person:
    def __init__(self):
        self.name = names.human("male")
        die = Dice([8,9,10,10,11])
        self.stats = {}
        for stat in ["STR","DEX","CON","INT","WIS","CHA"]:
            self.stats.update({stat:die.roll()})

    def show(self):
        print()
        print(self.name)
        print()
        for stat in self.stats.keys():
            print(stat + " : " + str(self.stats.get(stat)))

    