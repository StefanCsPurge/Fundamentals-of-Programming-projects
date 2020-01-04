from entities import Student

class ExamSrv:
    def __init__(self,studRepo):
        self.__studRepo = studRepo

    def getAllStuds(self):
        return self.__studRepo.getAll()

    def addStud(self,ID,name,attNr,grade):
        """
        Function that adds a student to the student repository.
        ID - int, name - str, attNr - int, grade - int
        """
        if ID < 0: raise Exception("Invalid ID!")
        parts = name.split(' ')
        if len(parts) < 2: raise Exception('Invalid name!')
        for part in parts:
            if len(part)<3: raise Exception('Invalid name!')
        if attNr < 0: raise Exception('Invalid number of attendances!')
        if grade not in range(0,11): raise Exception('Invalid grade!')
        self.__studRepo.add(Student(ID,name,attNr,grade))

    def giveBonuses(self,p,b):
        for s in self.__studRepo.getAll():
            if s.getAttendanceCount()>=p:
                s.addBonus(b)
        self.__studRepo.write_all_to_file()

    def searchStuds(self,string):
        foundStuds = []
        for stud in self.__studRepo.getAll():
            if string.casefold() in stud.getName().casefold():
                foundStuds.append(stud)
        sortedStuds = sorted(foundStuds,key=lambda s: s.getName())
        return sortedStuds
