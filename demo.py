from app import *
from student import *
import time
import numpy as np
import sys



if __name__ == '__main__':
    #Create Student
    Raja = Student('Raja', 'Phytogaia', ['Water Whip', 'Bubble', 'Wave', 'Water Drill'], 3, {'INT':3, 'STR':3, 'SPD':3, 'DUR':4, 'EGP':3, 'FHT':5})
    
    Gia = Student('Gia', 'Phytogaia', ['Earth Gauntlet', 'Rock Armor', 'Earthquake', 'Sand Spout'], 3, {'INT':3, 'STR':5, 'SPD':3, 'DUR':5, 'EGP':4, 'FHT':3})
    App().run(Raja, Gia)
    
