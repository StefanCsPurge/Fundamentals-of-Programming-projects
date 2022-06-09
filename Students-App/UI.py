from services import *

class UI:
    def __init__(self):
        self.__services = Services()
        self._menu = """Press:
        1 to add new student to the list
        2 to show the list of students
        3 to delete(filter) the students from a group
        4 to undo
        5 to print this menu again
        x to exit"""

    def printMenu(self):
        print(self._menu)

    def printStudList(self):
        StudList = self.__services.getStudList()
        if not len(StudList):
            raise Exception("There are no students in the list.")
        print("The students are:")
        for student in StudList:
            print(student)
            #print('ID: {}, name: {}, group: {}'.format(student.get_ID(), student.get_name(), student.get_group()))

    @staticmethod
    def __read_numerical(message):
        x = input(message)
        while True:
            try:
                x = int(x)
                if x < 0: raise ValueError
                return x
            except ValueError:
                print("Invalid value!")
                x = input(message)

    def read_add_student(self):
        ID = UI.__read_numerical("Insert ID: ")
        name = input("Insert name: ").strip()
        group = UI.__read_numerical("Insert group: ")
        self.__services.add_student(Student(ID,name,group))

    def read_filter(self):
        group = UI.__read_numerical("Insert group: ")
        self.__services.delete_group(group)

    def call_undo(self):
        self.__services.undo()
        print("Operation reversed")

    def run(self):
        print("STUDENTS APP")
        UI.printMenu(self)
        options = {'1':UI.read_add_student,'2':UI.printStudList,'3':UI.read_filter,'4':UI.call_undo,'5':UI.printMenu}
        self.__services.setStudList(self.__services.generate_entries())
        while True:
            opt = input('->')
            try:
                opt = opt.strip()
                if opt == 'x': exit()
                if not opt.isdigit() or opt not in ('1','2','3','4','5'):
                    raise ValueError("Non-existent option!")
                options[opt](self)
            except Exception as ex:
                print(ex)
