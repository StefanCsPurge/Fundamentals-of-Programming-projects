

class BusSrv:
    def __init__(self,BusRepo,RouteRepo): #constructor
        self.__busRepo = BusRepo
        self.__routeRepo = RouteRepo

    def getAllBusesAndRoutes(self):
        """
        Function that gets the routes and the buses from the repository to be printed in the UI.
        return: lists
        """
        return self.__busRepo.getAll(),self.__routeRepo.getAll()

    def getBusesOfRoute(self,routeCode):
        """
        Function that selects the buses that have been used on a given route.
        routeCode: int
        return: list
        """
        foundBuses = []
        for bus in self.__busRepo.getAll():
            if bus.getRouteCode() == routeCode:
                foundBuses.append(bus)
        return foundBuses

    def increaseUsage(self,busID,routeCode):
        """
        Function that increases the usage of a bus on a given route by 1.
        busID: int
        routeCode: int
        """
        ok = 0
        for bus in self.__busRepo.getAll():
            if bus.getID() == busID and bus.getRouteCode() == routeCode:
                bus.increaseUsage()
                ok = 1
                break
        if not ok : raise Exception('There is no bus with the given ID and route code!')
        self.__busRepo.write_all_to_file()

    def MostUsedBuses(self):
        """
        Function that returns the list of buses sorted in decreasing order of the kilometers traveled.
        return: list
        """
        busKM = lambda bus: bus.getTimesUsedRoute() * self.__routeRepo.getObj(bus.getRouteCode()).getLength()
        buses = self.__busRepo.getAll()
        sortedBuses = sorted(buses,key = busKM,reverse=True)
        return sortedBuses

