from domain import Student
import random
import names

class Services:
    def __init__(self):
        self.__studList = []
        self.__studListStack = [[]]

    def getStudList(self):
        return self.__studList

    def setStudList(self,other):
        self.__studList = other

    @staticmethod
    def generate_entries():
        EntryList = []
        IDs = [i for i in range(1, 10000)]
        random.shuffle(IDs)
        for i in range(10):
            EntryList.append(Student(IDs[i], names.get_full_name(), random.randint(1, 1000)))
        return EntryList

    def add_student(self, student):
        """
        Function that adds a student to the students list
        :param student: a Student type variable
        :return: nothing
        raise Exception if the student is already in the list
        """
        for current_stud in self.__studList:
            if student.get_ID() == current_stud.get_ID():
                raise Exception("Student already registered!")
        self.__studListStack.append(self.__studList.copy())
        self.__studList.append(student)

    def delete_group(self,group):
        self.__studListStack.append(self.__studList.copy())
        n = len(self.__studList)
        i = 0
        deleted = 0
        while i < n:
            if self.__studList[i].get_group() == group:
                deleted += 1
            else:
                self.__studList[i - deleted] = self.__studList[i]
            i += 1
        del self.__studList[n - deleted:n]
        if not deleted:
            self.__studListStack.pop()
            raise Exception("There are no students from this group!")

    def undo(self):
        self.__studList.clear()
        n = len(self.__studListStack)
        if not n:
            raise Exception("No more undo steps.")
        for stud in self.__studListStack[n - 1]:
            self.__studList.append(stud)
        self.__studListStack.pop()
