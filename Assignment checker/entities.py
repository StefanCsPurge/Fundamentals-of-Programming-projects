class Assignment:
    def __init__(self,ID,studName,solution):
        self.__ID = ID
        self.__studName = studName
        self.__sol = solution

    def getID(self):
        return self.__ID

    def getSol(self):
        return self.__sol

    def getSName(self):
        return self.__studName

    def __eq__(self, other):
        return  self.__ID == other.__ID

    def __str__(self):
        return "ID: "+str(self.__ID)+"\tStudent name: "+self.__studName+"\t\tSolution: "+self.__sol

    @staticmethod
    def fileRead(line):
        parts = line.strip().split(',')
        return Assignment(int(parts[0]),parts[1],parts[2])

    @staticmethod
    def fileWrite(assign):
        return str(assign.__ID)+","+assign.__studName+','+assign.__sol