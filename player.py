'''human and AI player classes'''

import time
from die import roll_die


class Player:
    '''class for players'''
    total_score = 0
    turn_score = 0
    curr_roll = 0

    def __init__(self, player_num):
        self.player_num = player_num

    def player_roll(self):
        '''function which displays the player's roll'''
        curr_roll = roll_die()
        self.curr_roll = curr_roll
        role_exclamation = "Next turn. "
        if 1 < curr_roll <= 3:
            role_exclamation = ""
        elif 3 < curr_roll <= 5:
            role_exclamation = "Great! "
        elif curr_roll == 6:
            role_exclamation = "Wow! The dice is hot! "
        print("Rolling... ")
        time.sleep(1)
        print(role_exclamation + "You rolled a {}".format(curr_roll))
        time.sleep(1)

    def player_turn(self):
        '''function which displays the player's turn'''
        print("Score: {}".format(self.total_score))
        time.sleep(1)
        while True:
            print("Press 'r' to roll or 'h' to hold: ", end='')
            game_decision = input()
            if game_decision in ('r', 'R'):
                self.player_roll()
                if self.curr_roll == 1:
                    self.turn_score = 0
                    print("Score: {}".format(
                        self.total_score + self.turn_score), end='')
                    print("\tNo points earned this turn")
                    time.sleep(1)
                    break

                self.turn_score += self.curr_roll
                print("Score: {}".format(
                    self.total_score + self.turn_score), end='')
                print("\tEarned this turn: {}".format(self.turn_score))
                time.sleep(1)

            elif game_decision in ('h', 'H'):
                self.total_score += self.turn_score
                self.turn_score = 0
                break
            else:
                print("Invalid selection")
                time.sleep(1)


class ComputerPlayer(Player):
    '''class for computer players'''
