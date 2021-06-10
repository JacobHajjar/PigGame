#!/usr/bin/env python3
''' Pig - the greatest die to game ever made, published by John Scarne. '''

from die import roll_die

__author__ = 'Jacob Hajjar'
__email__ = 'hajjarj@csu.fullerton.edu'
__maintainer__ = 'jacobhajjar'


def main():
    ''' The main function for my Pig game '''
    print('Hello world - this is my dice game!')
    input('hit return when you are ready to roll the die.')

    the_roll = roll_die(seed=0)
    print('You just rolled {}' .format(the_roll))


if __name__ == '__main__':
    main()
