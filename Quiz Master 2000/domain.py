class Question:
    def __init__(self,ID,text,a,b,c,correct,difficulty):
        self.__ID = ID
        self.__text = text
        self.__a = a
        self.__b = b
        self.__c = c
        self.__correct = correct
        self.__diff = difficulty

    def getDifficulty(self):
        return self.__diff
    def getChoices(self):
        return [self.__a,self.__b,self.__c]
    def getCorrectAns(self):
        return self.__correct

    def __str__(self):
        return '\n'+self.__text+'?\na) '+self.__a+'\nb) '+self.__b+'\nc) '+self.__c+'\n'

    @staticmethod
    def readQ(line):
        parts = line.split(';')
        return Question(int(parts[0]),parts[1].strip(),parts[2].strip(),parts[3].strip(),parts[4].strip(),parts[5].strip(),parts[6].strip())
    @staticmethod
    def writeQ(q):
        return str(q.__ID)+';'+q.__text+';'+q.__a+';'+q.__b+';'+q.__c+';'+q.__correct+';'+q.__diff