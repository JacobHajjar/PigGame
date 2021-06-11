#!/usr/bin/env python3
''' Pig - the greatest die to game ever made, published by John Scarne. '''

from player import Player, ComputerPlayer, time

__author__ = 'Jacob Hajjar'
__email__ = 'hajjarj@csu.fullerton.edu'
__maintainer__ = 'jacobhajjar'


def main():
    ''' The main function for my Pig game '''
    game_menu()


def game_menu():
    '''menu for the player to interact with the game'''

    print("Welcome to Jacob's Pig game!")
    while True:
        print(
            "To play a new game, enter the number of people playing (1-4) or 'q' to quit: ", end = '')
        try:
            player_selection = input()
            if player_selection in ('q', 'Q'):
                break
            number_players = int(player_selection)

            if 1 <= number_players <= 4:
                # game starts, main game conditions met
                play_round(number_players)
            else:
                print("You cannot play with {} players".format(number_players))
        except ValueError:
            print("Invalid input. Try again.")


def play_round(num_players):
    '''function which plays 1 round of pig'''
    p_list = [Player(1)]  # always start with 1 human player
    if num_players == 1:
        p_list.append(ComputerPlayer(2))
    else:
        for i in range(2, num_players+1):
            p_list.append(Player(i))

    highest_score = 0
    while highest_score < 100:
        for player in p_list:
            print("It is player {}'s turn".format(p_list.index(player) + 1))
            time.sleep(1)
            print("Score: {}".format(player.total_score))
            time.sleep(1)
            player.player_turn()

        if num_players == 1:
            print("It is the computer's turn")

        break


if __name__ == '__main__':
    main()
