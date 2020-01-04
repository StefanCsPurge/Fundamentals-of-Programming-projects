
class FileRepo:
    def __init__(self,fileName,readObj,writeObj):
        self.__entities = []
        self.__readObj = readObj
        self.__writeObj = writeObj
        self.__file = open(fileName,'r')
        self.__read_all_from_file()
        self.__file.close()

    def __read_all_from_file(self):
        entities = self.__file.readlines()
        for en in entities:
            obj = self.__readObj(en)
            self.__entities.append(obj)

    #def __write_all_to_file(self): not needed

    def getAll(self):
        return self.__entities[:]

    def getObj(self,ID):
        for obj in self.__entities:
            if obj.getID() == ID:
                return obj
        raise Exception('This ID was not found!')


