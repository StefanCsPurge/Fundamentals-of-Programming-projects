class ConsoleMenu:
    def __init__(self,BusSrv):
        self.__srv = BusSrv
        self.__menu = """Press:
        1 to display all buses travelling across a certain route
        2 to increase the usage of a bus
        3 to display all buses in decreasing order of kilometers traveled
        4 to display all routes & buses"""

    @staticmethod
    def printObjects(objects):
        for obj in objects:
            print(obj)

    def option1(self):
        routeCode = int(input("Insert the route code: "))
        foundBuses = self.__srv.getBusesOfRoute(routeCode)
        self.printObjects(foundBuses)

    def option2(self):
        busID = int(input("Insert the bus ID: "))
        routeCode = int(input("Insert the route code: "))
        if busID<0 or routeCode<0:
            raise Exception('Invalid bus ID or route code!')
        self.__srv.increaseUsage(busID,routeCode)

    def option3(self):
        sortedBuses = self.__srv.MostUsedBuses()
        self.printObjects(sortedBuses)

    def option4(self):
        buses,routes = self.__srv.getAllBusesAndRoutes()
        print('The routes are: ')
        self.printObjects(routes)
        print('The buses are:')
        self.printObjects(buses)
        input('Press any key to continue ...')

    def run(self):
        options = {1:self.option1,2:self.option2,3:self.option3,4:self.option4}
        while True:
            print(self.__menu)
            try:
                choice = int(input('->'))
                if choice not in range(1,5):
                    raise Exception("Non-existent option!")
                options[choice]()
            except Exception as ex:
                print('Error: ' + str(ex))