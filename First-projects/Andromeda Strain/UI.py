class ConsoleMenu:
    def __init__(self,srv):
        self.__srv = srv
        self.__menu = """Press:
        1 to simulate a new day
        2 to vaccinate a person
        3 to show all persons and the current day
        4 to end simulation"""

    @staticmethod
    def printObjects(objects):
        for obj in objects:
            print(obj)

    def option1(self):
        self.__srv.simulateNewDay()
        self.option3()

    def option2(self):
        ID = int(input("Insert the ID of the person you want to vaccinate: "))
        self.__srv.vaccinatePerson(ID)

    def option3(self):
        persons,day = self.__srv.getPersonsAndDay()
        print('DAY #{}'.format(day))
        self.printObjects(persons)

    def run(self):
        options = {1:self.option1,2:self.option2,3:self.option3}
        while True:
            print(self.__menu)
            try:
                choice = int(input("->"))
                if choice not in range(1,5):
                    raise Exception("Non-existent option!")
                if choice == 4:
                    print("Simulation ended.")
                    break
                options[choice]()
            except Exception as ex:
                print("Error: "+ str(ex))