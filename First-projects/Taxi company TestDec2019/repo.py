class FileRepo:
    def __init__(self,file,readObj,writeObj):
        self.__objects = []
        self.__file = file
        self.__readObj = readObj
        self.__writeObj = writeObj
        self.read_all_from_file()

    def getAll(self):
        return self.__objects[:]

    def getObj(self, ID):
        for obj in self.__objects:
            if obj.getID() == ID:
                return obj
        raise Exception('This ID was not found!')

    def read_all_from_file(self):
        f = open(self.__file,'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            obj = self.__readObj(line)
            self.__objects.append(obj)


    def add(self,obj):
        """
        Function that adds the object to the repository if the an object with the same id doesn't exist.
        """
        if obj in self.__objects:
            raise Exception("This ID is already used!")
        self.__objects.append(obj)
