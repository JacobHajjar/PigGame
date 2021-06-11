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
            "To play a new game, enter the number of people playing (1-4) or 'q' to quit: ", end='')
        try:
            player_selection = input()
            if player_selection in ('q', 'Q'):
                break
            number_players = int(player_selection)

            if 1 <= number_players <= 4:
                # game starts, main game conditions met
                print("New game started with {} player(s)".format(number_players))
                time.sleep(1)
                play_round(number_players)
            else:
                print("You cannot play with {} players".format(number_players))
                time.sleep(1)
        except ValueError:
            print("Invalid input. Try again.")
            time.sleep(1)


def play_round(num_players):
    '''function which plays 1 round of pig'''
    p_list = [Player(1)]  # always start with 1 human player
    if num_players == 1:
        p_list.append(ComputerPlayer(2))
    else:
        for i in range(2, num_players+1):
            p_list.append(Player(i))

    game_ongoing = True
    while game_ongoing:
        for player in p_list:
            player_number = p_list.index(player) + 1
            print("It is player {}'s turn".format(player_number))
            time.sleep(1)
            player.player_turn()
            if player.won_game:
                game_ongoing = False
                print("Congratulations player {}, you have won!".format(player_number))
                break
        if num_players == 1:
            print("It is the computer's turn")
            time.sleep(1)
            if player.won_game:
                print("Too bad! You lost!")
                break


if __name__ == '__main__':
    main()
