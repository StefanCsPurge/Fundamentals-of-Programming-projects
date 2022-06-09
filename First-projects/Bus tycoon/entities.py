class Bus:
    def __init__(self,ID,routeCode,model,timesUsedRoute):
        self.__id = ID
        self.__rCode = routeCode
        self.__model = model
        self.__timesUsedR = timesUsedRoute

    def getID(self):
        return self.__id
    def getRouteCode(self):
        return self.__rCode
    def getTimesUsedRoute(self):
        return self.__timesUsedR
    def increaseUsage(self):
        self.__timesUsedR += 1

    def __str__(self):
        return 'ID: ' + str(self.__id) + '\tRoute code: '+ str(self.__rCode) + '\tModel: '+self.__model+'\tTimes used on this route: ' + str(self.__timesUsedR)

    @staticmethod
    def fileRead(line):
        parts = line.strip().split(',')
        return Bus(int(parts[0]),int(parts[1]),parts[2],int(parts[3]))

    @staticmethod
    def fileWrite(bus):
        return str(bus.__id) + ',' + str(bus.__rCode) + ',' + bus.__model + ',' + str(bus.__timesUsedR)

class Route:
    def __init__(self,code,length):
        self.__code = code
        self.__length = length

    def getLength(self):
        return self.__length

    def getID(self):
        return self.__code

    def __str__(self):
        return 'Route code: '+ str(self.__code) + '\tLength: ' + str(self.__length) + ' KM'

    @staticmethod
    def fileRead(line):
        parts = line.strip().split(',')
        return Route(int(parts[0]), int(parts[1]))

    @staticmethod
    def fileWrite(route):
        return str(route.__code) + ',' + str(route.__length)
