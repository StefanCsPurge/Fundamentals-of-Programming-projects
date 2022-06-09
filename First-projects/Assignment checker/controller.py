from entities import Assignment

class Service:
    def __init__(self,repo):
        self.__repo = repo

    def getAllAssigns(self):
        return self.__repo.getAll()

    def addAssignment(self,ID,sName,sol):
        """
        Function that takes the assigment data from the UI, creates a new Assignment obj with it and adds it to the repo.
        ID: int, sName: str, sol: str
        """
        if len(sName)<3: raise Exception("Student name is to short!")
        assign = Assignment(ID,sName,sol)
        self.__repo.add(assign)

    @staticmethod
    def commonWordsPercent(words1,words2):
        n = len(words2)
        c = 0
        for w in words1:
            if w in words2:
                c += 1
        return c*100//n

    def checkDishonesty(self):
        assigns = self.__repo.getAll()
        n = len(assigns)
        report = []
        for i in range(0,n):
            for j in range(0,n):
                if i!=j:
                    p = self.commonWordsPercent(assigns[i].getSol().strip().split(),assigns[j].getSol().strip().split())
                    if p>=20: report.append((assigns[i].getSName(),assigns[j].getSName(),p))
        return report
