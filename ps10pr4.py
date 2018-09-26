#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# An AI Player for Connect Four
#
# name: Jake Bloomfeld  
# email: jtbloom@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from ps10pr3 import *
import random

class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        """ Constructs a new AIPlayer object.
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        Player.__init__(self, checker)

        self.tiebreak = tiebreak
        self.lookahead = lookahead


    def __repr__(self):
        """ Returns a string representing an AIPlayer object.
        """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'


    def max_score_column(self, scores):
        """ Takes a list scores containing a score for each column of the
            board, and that returns the index of the column with the
            maximum score.
        """
        max_score = max(scores)
        max_indicies = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                max_indicies += [i]
        if self.tiebreak == 'LEFT':
            return max_indicies[0]
        elif self.tiebreak == 'RIGHT':
            return max_indicies[-1]


    def scores_for(self, board):
        """ Takes a Board object board and determines the called AIPlayer‘s
            scores for the columns in board.
        """
        scores = []
        
            
            
        
        
        
        

        
        
        
        
        
        

        
        
        
        

    

        

        
        


