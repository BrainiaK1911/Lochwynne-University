# Create the class
class Student:
    def __init__(self, name, type, abilities, level, power_ratings, health='==================='):
        # save variables as attributes
        self.name = name
        self.type = type
        self.abilities = abilities
        self.lvl = level
        self.attack = power_ratings['INT'] + power_ratings['STR'] + power_ratings['SPD'] + power_ratings['EGP'] + power_ratings['FHT']
        self.defense = power_ratings['INT'] + power_ratings['SPD'] + power_ratings['DUR'] +power_ratings['FHT']
        self.health = health
        self.bars = 20 # Amount of health bars
