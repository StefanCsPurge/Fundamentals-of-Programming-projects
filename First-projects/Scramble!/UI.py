
class Console:
    def __init__(self,service):
        self.__srv = service

    def UISwapLetters(self,cmd):
        parts = cmd.split('-')
        left = parts[0].split()
        right = parts[1].split()
        if len(left) != 2 or len(right) != 2:
            raise Exception("Incorrect command!")
        word1 = int(left[0])
        let1 = int(left[1])
        word2 = int(right[0])
        let2 = int(right[1])
        self.__srv.swapLetters(word1,let1,word2,let2)
        self.__srv.addSwapToHistory(word1,let1,word2,let2)

    def undoSwap(self):
        self.__srv.undo()

    def run(self):
        while True:
            try:
                score = self.__srv.getScore()
                scrambled = ' '.join(self.__srv.getScrambled())
                print(f"{scrambled} [score is: {score}]")
                if self.__srv.checkVictory():
                    print('Victory!')
                    break
                if score == 0:
                    print('Defeat!')
                    break
                cmd = input(">").split()
                if cmd[0] == 'swap':
                    self.UISwapLetters(' '.join(cmd[1:]))
                    self.__srv.decreaseScore()
                elif cmd[0] == 'undo':
                    self.undoSwap()
                else:
                    raise Exception("Non-existent command!")
            except Exception as ex:
                print(ex)