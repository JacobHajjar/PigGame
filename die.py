''' A single, 6-sided die class. The values range from 1 to 6. '''

import random


def roll_die():
    '''function which rolls the dice'''
    return random.randint(1, 6)
