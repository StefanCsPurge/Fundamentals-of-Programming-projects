class Student:

    def __init__(self, ID, name, group):
        if ID < 0 or group < 0:
            raise ValueError("ID and group must be positive integers!")
        self.__ID = ID
        self.__name = str(name)
        self.__group = group

    def get_ID(self):
        return self.__ID

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def set_id(self,newID):
        self.__ID = newID

    def set_name(self,newName):
        self.__name = newName

    def set_group(self,newGroup):
        self.__group = newGroup

    def __str__(self):
        return "ID: " + str(self.__ID) + ", name: " + self.__name + ", group: " + str(self.__group)

    def __eq__(self,other):
        return self.__ID == other.__ID and self.__name == other.__name and self.__group == other.__group

