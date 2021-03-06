#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#
# name: Jake Bloomfeld
# email: jtbloom@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: N/A
# partner's email: N/A
#

from BoardClass import Board

# Write your Player class below.

class Player:

    def __init__(self, checker):
        """ Constructs a new Player object by initializing the following
            two attributes: An attribute checker – a one-character string
            that represents the gamepiece for the player, as specified by
            the parameter checker. An attribute num_moves – an integer that
            stores how many moves the player has made so far. This
            attribute should be initialized to zero to signify that the
            Player object has not yet made any Connect Four moves.
        """
        assert(checker == 'X' or checker == 'O')

        self.checker = checker
        self.num_moves = 0


    def __repr__(self):
        """ Returns a string representing a Player object.
        """
        return 'Player ' + self.checker


    def opponent_checker(self):
        """ Returns a one-character string representing the checker of the
            Player object’s opponent.
        """
        if self.checker == 'X':
            return 'O'
        return 'X'


    def next_move(self, board):
        """ Accepts a Board object as a parameter and returns the column
            where the player wants to make the next move.
        """

        while True:
            col_num = int(input('Enter a column:'))
            if board.can_add_to(col_num) == True:
                self.num_moves += 1
                return col_num
            else:
                print('Try again!')
            
                
                
                
            
