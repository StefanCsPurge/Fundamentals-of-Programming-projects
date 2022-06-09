
class Service:
    def __init__(self,repo):
        self.__repo = repo
        self.__day = 1

    def getPersonsAndDay(self):
        return self.__repo.getAll(),self.__day

    def simulateNewDay(self):
        """
        Function that simulates a new day.
        No parameters, has effect on repo and updates the repo file.
        """
        self.__day += 1
        # 2.
        self.updateIllness()
        ok = 0
        for person in self.__repo.getAll():
            if person.getStatus()=='ill':
                ok = 1
                break
        if ok:
            for person in self.__repo.getAll():
                if person.getStatus()=='healthy' and person.getImmunization()=='nonvaccinated':
                    person.setStatus('ill')
                    person.increase_days_ill()
                    break
            #update file
            self.__repo.write_all_to_file()

    def updateIllness(self):
        for person in self.__repo.getAll():
            if person.getStatus()=='ill':
                person.increase_days_ill()
                if person.getDaysIll()>3:
                    person.resetDaysIll()
                    person.setStatus('healthy')

    def vaccinatePerson(self,ID):
        person = self.__repo.getObj(ID)
        if person.getStatus() == 'ill':
            raise Exception("The person you want to vaccinate is ill!")
        person.setStatus('healthy')
        person.setImmunization('vaccinated')
        person.resetDaysIll()
        # update file
        self.__repo.write_all_to_file()



