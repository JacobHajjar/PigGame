#!/usr/bin/env python3
''' Pig - the greatest die to game ever made, published by John Scarne. '''

from die import roll_die
from player import Player, ComputerPlayer

__author__ = 'Jacob Hajjar'
__email__ = 'hajjarj@csu.fullerton.edu'
__maintainer__ = 'jacobhajjar'


def main():
    ''' The main function for my Pig game '''
    the_roll = roll_die()
    # print(the_roll)
    game_menu()


def game_menu():
    '''menu for the player to interact with the game'''

    print("Welcome to Jacob's Pig game!")
    while True:
        print(
            "To play a new game, enter the number of people playing (1-4) or 'q' to quit: ")
        try:
            player_selection = input()
            if player_selection == 'q' or player_selection == 'Q':
                break
            number_players = int(player_selection)

            if number_players <= 4 and number_players >= 1:
                # game starts, main game conditions met
                play_round(number_players)
            else:
                print("You cannot play with {} players".format(number_players))
        except ValueError:
            print("Invalid input. Try again.")


def play_round(num_players):
    '''function which plays 1 roung of pig'''
    p_list = [Player(1)]  # always start with 1 human player
    if num_players == 1:
        p_list.append(ComputerPlayer(2))
    else:
        for i in range(2, num_players+1):
            p_list.append(Player(i))

    highest_score = 0
    while highest_score < 100:
        for i in range(len(p_list)):
            print(i)
        break


if __name__ == '__main__':
    main()
