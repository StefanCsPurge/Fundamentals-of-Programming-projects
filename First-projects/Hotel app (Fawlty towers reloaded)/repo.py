
class Repo:
    def __init__(self):
        self._list = []
    def getAll(self):
        """
        Object list getter.
        :return: complete list of objects.
        """
        return self._list[:]
    def getObj(self,ID):
        for obj in self._list:
            if obj.getID() == ID:
                return obj
        raise Exception("This ID does not exist!")
    def add(self,obj):
        """
        Method that adds a given object to the repository.
        :param obj: the given object
        :return: nothing
        """
        if obj in self._list:
            raise Exception("Already stored!")
        self._list.append(obj)
    def remove(self,obj):
        """
        Method that removes a given object from the repository.
        :param obj: the given object
        :return: nothing
        """
        if obj not in self._list:
            raise Exception("Non-existent item!")
        self._list.remove(obj)
    def cleanRepo(self):
        self._list.clear()

class FileRepo(Repo):
    def __init__(self,file,readObj,writeObj):
        self.__file = file
        self.__readObj = readObj
        self.__writeObj = writeObj
        Repo.__init__(self)
        self.read_all_from_file()

    def read_all_from_file(self):
        """
        Method that gets all the objects stored in a given file.
        :return: nothing
        """
        with open(self.__file,"r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    obj = self.__readObj(line)
                    self._list.append(obj)
        f.close()

    def write_all_to_file(self):
        """
        Method that stores all the objects in a given file.
        :return: nothing
        """
        with open(self.__file,"w") as f:
            for obj in self._list:
                line = self.__writeObj(obj)
                f.write(line+"\n")
        f.close()

    def add(self,obj):
        """
        Method that adds an object to the repository (by using the inherited Repo class)
        and stores it in the given file.
        :param obj: the given object
        :return: nothing
        """
        Repo.add(self,obj)
        self.write_all_to_file()

    def remove(self,obj):
        """
        Method that removes an object from the repository (by using the inherited Repo class)
        and also deletes it from the given file.
        :param obj: the given object
        :return: nothing
        """
        Repo.remove(self,obj)
        self.write_all_to_file()

    def cleanRepo(self):
        Repo.cleanRepo(self)
        self.write_all_to_file()