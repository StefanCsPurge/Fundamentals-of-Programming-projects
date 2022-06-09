import random

class Service:
    def __init__(self,wordsRepo):
        self.__wordsRepo = wordsRepo
        self.__score = 0
        self.__initialWords = []
        self.__newWords = []
        self.gameStart()
        self.__undoStack = []

    def gameStart(self):
        entry = random.choice(self.__wordsRepo.getAll())
        self.__initialWords = entry.split()
        letters = []
        for word in self.__initialWords:
            self.__score += len(word)
            innerLetters = list(word[1:-1])
            letters.extend(innerLetters)
        random.shuffle(letters)  # now we have the shuffled letters
        index = 0
        for word in self.__initialWords:
            inLetNo = len(word)-2
            innerW = ''.join(letters[index:index+inLetNo])
            index += inLetNo
            new = word[0] + innerW + word[-1]
            self.__newWords.append(new)

    def decreaseScore(self):
        self.__score -= 1

    def getScore(self):
        return self.__score

    def getScrambled(self):
        return self.__newWords

    def swapLetters(self,w1,let1_index,w2,let2_index):
        if not self.validSwap(w1,let1_index,w2,let2_index):
            raise Exception("Invalid indices!")
        letter1 = self.__newWords[w1][let1_index]
        letter2 = self.__newWords[w2][let2_index]
        word1 = list(self.__newWords[w1])
        word1[let1_index] = letter2
        self.__newWords[w1] = ''.join(word1)  # changed the first word
        word2 = list(self.__newWords[w2])
        word2[let2_index] = letter1
        self.__newWords[w2] = ''.join(word2)  # changed the second word

    def addSwapToHistory(self,w1,let1_index,w2,let2_index):
        self.__undoStack.append((w1, let1_index, w2, let2_index))

    def undo(self):
        if not len(self.__undoStack):
            raise Exception('No more undo!')
        lastAction = self.__undoStack.pop()
        w1 = lastAction[0]
        let1 = lastAction[1]
        w2 = lastAction[2]
        let2 = lastAction[3]
        self.swapLetters(w2,let2,w1,let1)

    def checkVictory(self):
        for i in range(len(self.__initialWords)):
            if self.__initialWords[i] != self.__newWords[i]:
                return False
        return True

    def validSwap(self,w1,let1,w2,let2):
        n = len(self.__initialWords)
        if w1 not in range(n) or w2 not in range(n):
            return False
        if let1 not in range(1,len(self.__newWords[w1])-1) or let2 not in range(1,len(self.__newWords[w2])-1):
            return False
        return True