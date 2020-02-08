from domain import Board
import random

class Service:
    def __init__(self):
        self.__board = Board(6, 6).getBoard()
        # the next list represents the directions: up, down, right, left and every diagonal
        self.__directions = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
        self.__usedCells = []  # the list that keeps the occupied cells

    def getBoard(self):
        return self.__board

    def chaosMove(self,move):
        cell = (move[0], move[1])
        self.__usedCells.append(cell)
        self.__board[move[0]][move[1]] = move[2]

    def validBoardMove(self,move):
        cell = (move[0], move[1])
        if not (cell[0] in range(6) and cell[1] in range(6) and move[2] in ('X', 'O')) or cell in self.__usedCells:
            raise Exception
        return True

    def mostFrequentSymbol(self):
        symbols = {'X':0,'O':0}  # initialize the frequencies
        for i in range(6):
            for j in range(6):
                sym = self.__board[i][j]
                if sym != ' ':
                    symbols[sym] += 1
        if symbols['X'] > symbols['O']:
            return 'X'
        return 'O'

    def countCellNeighbours(self,i,j,sym):
        found = 0
        for d in self.__directions:
            if i+d[0] in range(6) and j+d[1] in range(6) and self.__board[i+d[0]][j+d[1]] == sym:
                found += 1
        return found

    def cellWithMaxNeighbours(self,sym):
        row = col = maxi = 0
        for i in range(6):
            for j in range(6):
                if self.__board[i][j] == ' ':
                    neighboursNumber = self.countCellNeighbours(i, j, sym)
                    if neighboursNumber > maxi:
                        maxi = neighboursNumber
                        row = i
                        col = j
        return row,col

    def findOrderWinningMove(self):
        for i in range(6):
            for j in range(6):
                symbol = self.__board[i][j]
                if symbol != ' ':
                    for d in self.__directions:
                        move = self.checkDirection(i+d[0], j+d[1], d[0], d[1], symbol, 4)
                        # this time we used checkDirection to see if there are 4 consecutive symbols, so the order would have a winning move with the 5th
                        if move: return move
        return False

    def getOrderMove(self):
        if not len(self.__usedCells):  # when we first start the game, place randomly
            row = random.randint(0, 5)
            col = random.randint(0, 5)
            symbol = random.choice(['X', 'O'])
        else:
            move = self.findOrderWinningMove()
            if move:
                row = move[0]
                col = move[1]
                symbol = move[2]
            else:
                symbol = self.mostFrequentSymbol()
                row, col = self.cellWithMaxNeighbours(symbol)
        self.__board[row][col] = symbol
        self.__usedCells.append((row, col))
        return row, col, symbol

    def checkDirection(self,i,j,di,dj,sym,req=5):
        """
        Method that checks if there are enough consecutive cells with a given symbol in the given direction.
        :param i: (int) start row
        :param j: (int) start column
        :param di: (int) direction for row
        :param dj: (int) direction for column
        :param sym: (str) 'X' or 'O' the elements of the board
        :param req: (int) by default we are required 5 consecutive symbols
        :return: (bool) True or False  /  order winning move (tuple) or False in case req = 4
        """
        found = 1
        while 0 <= i < 6 and 0 <= j < 6 and found < req and self.__board[i][j] == sym:
            # print(self.__board[i][j],i,j, ' ', di,dj)
            found += 1
            i += di
            j += dj
        if found == req:
            if req == 5:
                return True
            elif req == 4 and i in range(0,6) and j in range(0,6):
                sym = self.__board[i-di][j-dj]
                if i in range(0,6) and j in range(0,6) and self.__board[i][j] == ' ':
                    return i, j, sym  # we had 4 consecutive symbols so order got a winning move
        return False

    def checkFiveOrdered(self,row,col):
        """
        Method that checks if there are five cells with the same symbol starting from the given position.
        :param row: int - the given board row
        :param col: int - the given board column
        :return: (bool) True or False
        """
        symbol = self.__board[row][col]
        for d in self.__directions:
            if self.checkDirection(row + d[0], col + d[1], d[0], d[1], symbol):  # check if we have 4 more consecutive in that direction
                return True
        return False

    def checkOrderWin(self):
        """
        Function that checks if order has won, by searching five consecutive ordered symbols on the board.
        :return: (bool) True if order won, False otherwise
        """
        for i in range(6):
            for j in range(6):
                if self.__board[i][j] != ' ' and self.checkFiveOrdered(i, j):
                    return True
        return False

    def checkChaosWin(self):
        for i in range(6):
            for j in range(6):
                if self.__board[i][j] == ' ':
                    return False
        return True