import time
import numpy as np
import sys


def delay_print(s):
    # print one character at a time
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

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


def fight(Student1, Student2):
    # Allow two Students to fight each other

    # Print fight information
    print("-----Lochwynne University-----")
    print(f"\n{Student1.name}")
    print("TYPE:", Student1.type)
    print("ATTACK:", Student1.attack)
    print("DEFENSE:", Student1.defense)
    print("LVL:", Student1.lvl)
    print("\nVS")
    print(f"\n{Student2.name}")
    print("TYPE:", Student2.type)
    print("ATTACK:", Student2.attack)
    print("DEFENSE:", Student2.defense)
    print("LVL:", Student2.lvl)

    time.sleep(2)

    # Consider type advantages
    version = ['Cerebral','Phytogaia','Zoomor','Mantrador','Null']
    for i,k in enumerate(version):
        if Student1.type == k:
            # Both are same type
            if Student2.type == k:
                string_1_attack = '\nIts not very effective...'
                string_2_attack = '\nIts not very effective...'

            # Student2 is STRONG
            if Student2.type == version[(i+1)%3]:
                Student2.attack *= 2
                Student2.defense *= 2
                Student1.attack /= 2
                Student1.defense /= 2
                string_1_attack = '\nIts not very effective...'
                string_2_attack = '\nIts super effective!'

            # Student2 is WEAK
            if Student2.type == version[(i+2)%3]:
                Student1.attack *= 2
                Student1.defense *= 2
                Student2.attack /= 2
                Student2.defense /= 2
                string_1_attack = '\nIts super effective!'
                string_2_attack = '\nIts not very effective...'


    # Now for the actual fighting...
    # Continue while Student still have health
    while (Student1.bars > 0) and (Student2.bars > 0):
        # Print the health of each Student
        print(f"\n{Student1.name}\t\tHLTH\t{Student1.health}")
        print(f"{Student2.name}\t\tHLTH\t{Student2.health}\n")

        print(f"Go {Student1.name}!")
        for i, x in enumerate(Student1.abilities):
            print(f"{i+1}.", x)
        index = int(input('Pick a move: '))
        delay_print(f"\n{Student1.name} used {Student1.abilities[index-1]}!")
        time.sleep(1)
        delay_print(string_1_attack)

        # Determine damage
        Student2.bars -= Student1.attack
        Student2.health = ""

        # Add back bars plus defense boost
        for j in range(int(Student2.bars+.1*Student2.defense)):
            Student2.health += "="

        time.sleep(1)
        print(f"\n{Student1.name}\t\tHLTH\t{Student1.health}")
        print(f"{Student2.name}\t\tHLTH\t{Student2.health}\n")
        time.sleep(.5)

        # Check to see if Student fainted
        if Student2.bars <= 0:
            delay_print("\n..." + Student2.name + ' fainted.')
            break

        # Student2s turn

        print(f"Go {Student2.name}!")
        for i, x in enumerate(Student2.abilities):
            print(f"{i+1}.", x)
        index = int(input('Pick a move: '))
        delay_print(f"\n{Student2.name} used {Student2.abilities[index-1]}!")
        time.sleep(1)
        delay_print(string_2_attack)

        # Determine damage
        Student1.bars -= Student2.attack
        Student1.health = ""

        # Add back bars plus defense boost
        for j in range(int(Student1.bars+.1*Student1.defense)):
            Student1.health += "="

        time.sleep(1)
        print(f"{Student1.name}\t\tHLTH\t{Student1.health}")
        print(f"{Student2.name}\t\tHLTH\t{Student2.health}\n")
        time.sleep(.5)

        # Check to see if Student fainted
        if Student1.bars <= 0:
            delay_print("\n..." + Student1.name + ' fainted.')
            break
    
    # Rank increases
    new_level = Student2.lvl + 1
    delay_print(f"\nYour new level is {new_level}.\n")






if __name__ == '__main__':
    #Create Student
    Raja = Student('Raja', 'Phytogaia', ['Water Whip', 'Bubble', 'Wave', 'Water Drill'], 3, {'INT':3, 'STR':3, 'SPD':3, 'DUR':4, 'EGP':3, 'FHT':5})
    
    Gia = Student('Gia', 'Phytogaia', ['Earth Gauntlet', 'Rock Armor', 'Earthquake', 'Sand Spout'], 3, {'INT':3, 'STR':5, 'SPD':3, 'DUR':5, 'EGP':4, 'FHT':3})
    

    fight(Raja, Gia) # Get them to fight
