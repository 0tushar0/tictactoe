# model stores board position and checks win condition

import numpy as np

class Model():
    def __init__(self):
        self.__board = np.array([['1','2','3'],['4','5','6'],['7','8','9']])

    def update(self, row, col, pos):
        if self.__board[row][col] != 'x' and \
                self.__board[row][col] != 'o':
            self.__board[row][col] = pos
            return True
        return False

    def getBoard(self):
        return self.__board

    def win(self):
        if  (self.__board[0][0] == self.__board[0][1] and \
             self.__board[0][1] == self.__board[0][2]) or \
            (self.__board[1][0] == self.__board[1][1] and \
             self.__board[1][1] == self.__board[1][2]) or \
            (self.__board[2][0] == self.__board[2][1] and \
             self.__board[2][1] == self.__board[2][2]) or \
            (self.__board[0][0] == self.__board[1][0] and \
             self.__board[1][0] == self.__board[2][0]) or \
            (self.__board[0][1] == self.__board[1][1] and \
             self.__board[1][1] == self.__board[2][1]) or \
            (self.__board[0][2] == self.__board[1][2] and \
             self.__board[1][2] == self.__board[2][2]) or \
            (self.__board[0][0] == self.__board[1][1] and \
             self.__board[1][1] == self.__board[2][2]) or \
            (self.__board[0][2] == self.__board[1][1] and \
             self.__board[1][1] == self.__board[2][0]):
            return True
            
        return False

    def draw(self):
        if( self.__board[0][0] != '1' and \
            self.__board[0][1] != '2' and \
            self.__board[0][2] != '3' and \
            self.__board[1][0] != '4' and \
            self.__board[1][1] != '5' and \
            self.__board[1][2] != '6' and \
            self.__board[2][0] != '7' and \
            self.__board[2][1] != '8' and \
            self.__board[2][2] != '9'):
            return True
        return False

    def end(self):
        if self.win():
            print("Winner!")
            return True
        elif self.draw():
            print("Draw")
            return True
        return False
