from texttable import Texttable

class Console:
    def __init__(self,controller):
        self.__srv = controller

    @staticmethod
    def printBoard(board):
        table = Texttable()
        for i in range(6):
            table.add_row([board[i][j] for j in range(6)])
        print(table.draw() + '\n')

    def readMove(self,message):
        while True:
            try:
                moveList = input(message).strip().split()
                if not (len(moveList) == 3 and moveList[0].isdigit() and moveList[1].isdigit() and moveList[2].isalpha()):
                    raise Exception
                if self.__srv.validBoardMove((int(moveList[0]) - 1, int(moveList[1]) - 1, moveList[2].upper())):
                    return int(moveList[0]) - 1, int(moveList[1]) - 1, moveList[2].upper()
            except Exception as exception:
                print("Invalid move! " + str(exception))

    def runGame(self):
        print("The empty board:")
        self.printBoard(self.__srv.getBoard())
        while True:
            try:
                # Order turn
                move = self.__srv.getOrderMove()
                print('Order moved: {} {} {}'.format(move[0] + 1,move[1] + 1,move[2]))
                self.printBoard(self.__srv.getBoard())
                if self.__srv.checkOrderWin():
                    print("Order won!")
                    break
                # Chaos turn
                self.__srv.chaosMove(self.readMove("Enter chaos move (eg: 4 2 X): "))
                self.printBoard(self.__srv.getBoard())
                if self.__srv.checkChaosWin():
                    print("Chaos won!")
                    break
            except Exception as exception:
                print(exception)