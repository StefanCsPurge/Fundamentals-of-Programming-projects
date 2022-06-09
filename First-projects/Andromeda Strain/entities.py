class Person:
    def __init__(self,ID,immunization,status):
        self.__ID = ID
        self.__imn = immunization
        self.__status = status
        self.__nrDaysIll = 0
        if self.__status == 'ill':
            self.increase_days_ill()

    def increase_days_ill(self):
        self.__nrDaysIll += 1

    def getID(self):
        return self.__ID

    def getStatus(self):
        return self.__status

    def getImmunization(self):
        return self.__imn

    def setImmunization(self,other):
        self.__imn = other

    def setStatus(self,other):
        self.__status = other

    def getDaysIll(self):
        return self.__nrDaysIll

    def resetDaysIll(self):
        self.__nrDaysIll = 0

    def __eq__(self, other):
        return  self.__ID == other.__ID

    def __str__(self):
        return "ID: "+str(self.__ID)+"\tImmunization status: "+self.__imn+"\t\tStatus: "+self.__status+'\t\tNr days ill: '+str(self.__nrDaysIll)

    @staticmethod
    def fileRead(line):
        parts = line.strip().split(',')
        return Person(int(parts[0]),parts[1],parts[2])

    @staticmethod
    def fileWrite(person):
        return str(person.__ID)+","+person.__imn+","+person.__status