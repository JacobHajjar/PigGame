'''human and AI player classes'''

import time
from die import roll_die
_WIN_SCORE = 100  # global win score for testing


class Player:
    '''class for players'''
    total_score = 0
    turn_score = 0
    curr_roll = 0
    won_game = False

    def __init__(self, player_num):
        self.player_name = "Player " + str(player_num)
        if player_num == -1:
            self.player_name = "Computer"

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
        while True:  # roll or hold decision loop
            print("Press 'r' to roll or 'h' to hold: ", end='')
            game_decision = input()
            if game_decision in ('r', 'R'):  # player chooses to roll
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
                time.sleep(1)
                print("\tEarned this turn: {}".format(self.turn_score))
                time.sleep(1)
                if self.total_score + self.turn_score >= _WIN_SCORE:
                    self.won_game = True
                    break

            elif game_decision in ('h', 'H'):  # player chooses to hold
                self.total_score += self.turn_score
                self.turn_score = 0
                break
            else:
                print("Invalid selection")
                time.sleep(1)


class ComputerPlayer(Player):
    '''class for computer players'''

    def player_roll(self):
        '''overriden function which displays the computer player's roll'''
        curr_roll = roll_die()
        self.curr_roll = curr_roll
        print("Computer rolled: {}".format(curr_roll))
        time.sleep(1)

    def player_turn(self):
        '''overriden function for the computer player's turn'''
        print("Score: {}".format(self.total_score))
        time.sleep(1)
        self.turn_score = 0
        max_rolls = 5
        for _ in range(max_rolls):
            self.player_roll()  # computer always starts with a roll
            self.turn_score += self.curr_roll
            if self.curr_roll == 1:
                self.turn_score = 0
                print("Score: {}".format(self.total_score))
                time.sleep(1)
                break

            print("Score: {}".format(self.total_score + self.turn_score))
            time.sleep(1)
            if self.total_score + self.turn_score >= _WIN_SCORE:
                self.won_game = True
                break


        if _WIN_SCORE - self.total_score + self.turn_score < 10:
            while True:
                if self.total_score + self.turn_score >= _WIN_SCORE:
                    self.won_game = True
                    break
                self.player_roll()
                self.turn_score += self.curr_roll
                if self.curr_roll == 1:
                    self.turn_score = 0
                    print("Score: {}".format(self.total_score))
                    time.sleep(1)
                    break
                print("Score: {}".format(self.total_score + self.turn_score))
                time.sleep(1)

        self.total_score += self.turn_score
        print("End of turn")
        time.sleep(1)
