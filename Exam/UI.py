
class ConsoleMenu:
    def __init__(self,examSrv):
        self.__srv = examSrv
        self.__menu = """Press:
        1 to add a student
        2 to give bonuses
        3 to show all students whose name include a given string
        4 to show all students"""

    @staticmethod
    def printStuds(studs):
        for s in studs:
            print(s)

    def option1(self):
        """
        Function that reads the user input for adding the new student.
        The read info is passed to the service for further validation and repo add.
        return: nothing
        """
        ID = int(input("ID: "))
        name = input("Name: ")
        attNr = int(input("Number of attendances: "))
        grade = int(input("Grade: "))
        self.__srv.addStud(ID,name,attNr,grade)

    def option2(self):
        print("Insert the min nr of attendances (p) and and the bonus value (b):")
        p = int(input("p="))
        b = int(input("b="))
        self.__srv.giveBonuses(p,b)

    def option3(self):
        string = input('Insert string: ').strip()
        foundStuds = self.__srv.searchStuds(string)
        self.printStuds(foundStuds)

    def option4(self):
        studs = self.__srv.getAllStuds()
        self.printStuds(studs)

    def run(self):
        options = {1:self.option1,2:self.option2,3:self.option3,4:self.option4}
        while True:
            print(self.__menu)
            try:
                choice = int(input("->"))
                if choice not in range(1,5):
                    raise Exception("Non-existent option!")
                options[choice]()
            except Exception as ex:
                print("Error: "+ str(ex))
