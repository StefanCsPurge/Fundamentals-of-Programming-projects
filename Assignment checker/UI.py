class ConsoleMenu:
    def __init__(self,srv):
        self.__srv = srv
        self.__menu = """Press:
        1 to add and assignment
        2 to show all assignments
        3 to check dishonesty"""

    @staticmethod
    def printObjects(objects):
        for obj in objects:
            print(obj)

    def option1(self):
        ID = int(input("Assignment ID: "))
        sName = input("Student name: ")
        sol = input("Solution: ")
        self.__srv.addAssignment(ID,sName,sol)

    def option2(self):
        assigns = self.__srv.getAllAssigns()
        self.printObjects(assigns)

    def option3(self):
        reportedPairs = self.__srv.checkDishonesty()
        if not len(reportedPairs):
            print("Everybody is honest!"); return
        for pair in reportedPairs:
            print("{} -> {} ({}% of {}'s solution)".format(pair[0],pair[1],pair[2],pair[1]))

    def run(self):
        options = {1:self.option1,2:self.option2,3:self.option3}
        while True:
            print(self.__menu)
            try:
                choice = int(input("->"))
                if choice not in range(1,4):
                    raise Exception("Non-existent option!")
                options[choice]()
            except Exception as ex:
                print("Error: "+ str(ex))