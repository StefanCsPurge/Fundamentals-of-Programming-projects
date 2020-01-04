class Address:
    def __init__(self,ID,name,nr,x,y):
        self.__ID = ID
        self.__name = name
        self.__nr = nr
        self.__x = x
        self.__y = y

    def getID(self):
        return self.__ID

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def __eq__(self, other):
        return  self.__ID == other.__ID

    def __str__(self):
        return "ID: "+str(self.__ID)+"\tName: "+self.__name+"\t\tNumber: "+str(self.__nr)+'\tx: '+str(self.__x)+"\ty: "+str(self.__y)

    @staticmethod
    def fileRead(line):
        parts = line.strip().split(',')
        return Address(int(parts[0]),parts[1],int(parts[2]),int(parts[3]),int(parts[4]))

    @staticmethod
    def fileWrite(obj):
        return str(obj.__ID)+","+obj.__name+","+str(obj.__nr)+","+str(obj.__x)+","+str(obj.__y)