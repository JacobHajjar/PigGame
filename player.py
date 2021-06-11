'''human and AI player classes'''

from die import roll_die


class Player:
    '''class for players'''
    curr_score = 0

    def __init__(self, player_num):
        self.player_num = player_num


class ComputerPlayer(Player):
    '''class for computer players'''
