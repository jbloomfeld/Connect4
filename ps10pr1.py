# Jake Bloomfeld
# jtbloom@bu.edu

# Problem Set 10
# Problem 1

class Board:

    def __init__(self, height, width):
        """ The constructor for objects of type Board. """
        self.height = height
        self.width = width
        self.slots = [[' '] * width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string representing a Board object. """
        s = ''         

        for row in range(self.height):
            s += '|'   

            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'  

        for col in range(self.width):
            s += ('-')*2
        s+= '-'
        s+='\n'

        for col in range(self.width):
            s += ' ' + str(col%10)

        return s


    def add_checker(self, checker, col):
        """ Accepts two inputs: Checker, a one-character string that
            specifies the checker to add to the board (either 'X' or 'O').
            Col, an integer that specifies the index of the column to which
            the checkershould be added and that adds checker to the
            appropriate row in column col of the board.
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)

        row = 0
        while self.slots[row][col] == ' ':
            row += 1 
            if row == (self.height):
               break
        self.slots[row-1][col] = checker


    def clear(self):
        """ Clears the Board object on which it is called by setting all
            slots to contain a space character.
        """
        self.slots = [[' '] * self.width for row in range(self.height)]


    def add_checkers(self, columns):
        """ Takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in columns:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


    def can_add_to(self, col):
        """ Returns True if it is valid to place a checker in the column col
            on the calling Board object. Otherwise, it should return False.
        """
        if col not in range(self.width):
            return False
        if self.slots[0][col] == 'X':
            return False
        if self.slots[0][col] == 'O':
            return False
        else:
            return True


    def is_full(self):
        """ Returns True if the called Board object is completely full of
            checkers, and returns False otherwise.
        """
        if self.can_add_to(self.width-1) == True:
            return False
        else: 
            return True


    def remove_checker(self, col):
        """ Removes the top checker from column col of the called Board
            object. If the column is empty, then the method should do
            nothing.
        """
        for i in range(self.height):
            if self.slots[i][col] in 'XO':
                self.slots[i][col] = ' '
                break


    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False


    def is_vertical_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no vertical wins
        return False


    def is_down_diagonal_win(self, checker):
        """ Checks for a down-diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for an up-diagonal win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and \
                    self.slots[row - 3][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False


    def is_win_for(self, checker):
        """ Accepts a parameter checker that is either 'X' or 'O', and
            returns True if there are four consecutive slots containing
            checker on the board. Otherwise, it should return False.
        """
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
        
         
        
        
    
