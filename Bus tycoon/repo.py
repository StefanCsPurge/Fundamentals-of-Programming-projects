class FileRepo:
    def __init__(self,filename,readObj,writeObj):
        self.__objects = []
        self.__readObj = readObj
        self.__writeObj = writeObj
        self.__fileName = filename
        self.__read_all_from_file()

    def __read_all_from_file(self):
        f = open(self.__fileName,'r')
        lines = f.readlines()
        for line in lines:
            obj = self.__readObj(line)
            self.__objects.append(obj)
        f.close()

    def write_all_to_file(self):
        f = open(self.__fileName,'w')
        for obj in self.__objects:
            line = self.__writeObj(obj)
            f.write(line+'\n')
        f.close()

    def getObj(self,ID):
        for obj in self.__objects:
            if obj.getID() == ID:
                return obj
        raise Exception('This ID was not found!')

    def getAll(self):
        return self.__objects[:]

    def addObj(self,obj):
        self.__objects.append(obj)

    def clearRepo(self):
        self.__objects.clear()
        self.write_all_to_file()

