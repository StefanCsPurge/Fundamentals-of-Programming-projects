class Student:
    def __init__(self,ID,name,attCount,grade):
        self.__ID = ID
        self.__name = name
        self.__attCount = attCount
        self.__grade = grade

    def getName(self):
        return self.__name

    def getAttendanceCount(self):
        return self.__attCount

    def addBonus(self,b):
        self.__grade += b
        if self.__grade>10:
            self.__grade = 10

    def __eq__(self, other):
        return  self.__ID == other.__ID

    def __str__(self):
        return "ID: "+str(self.__ID)+"\tName: "+self.__name+"\tAttendance count: "+str(self.__attCount)+"\tGrade: "+str(self.__grade)

    @staticmethod
    def fileRead(line):
        parts = line.strip().split(',')
        return Student(int(parts[0]),parts[1],int(parts[2]),int(parts[3]))

    @staticmethod
    def fileWrite(stud):
        return str(stud.__ID)+","+stud.__name+","+str(stud.__attCount)+","+str(stud.__grade)
