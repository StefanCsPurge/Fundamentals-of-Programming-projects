class ConsoleMenu:
    def __init__(self,srv):
        self.__srv = srv
        self.__menu = """Press:
        1 to add an address
        2 to display all addresses
        3 to get addresses good for taxi stations"""

    @staticmethod
    def printObjects(objects):
        for obj in objects:
            print(obj)

    def option1(self):
        ID = int(input("ID: "))
        name = input("Name: ").strip()
        nr = int(input("Number: "))
        x = int(input("x: "))
        y = int(input("y: "))
        self.__srv.addAdr(ID,name,nr,x,y)

    def option2(self):
        addresses = self.__srv.getAllAdr()
        self.printObjects(addresses)

    def option3(self):
        x = float(input("x: "))
        y = float(input("y: "))
        d = float(input("Max distance: "))
        foundAdrDist = self.__srv.getNearAdr(x,y,d)
        for adrD in foundAdrDist:
            print("{}; Distance: {}".format(adrD[0],adrD[1]))

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