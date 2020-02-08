from copy import deepcopy

class Board:
    def __init__(self,columns,rows,default=' '):
        self.__board = [[default]*columns for i in range(rows)]

    def getBoard(self):
        return deepcopy(self.__board)