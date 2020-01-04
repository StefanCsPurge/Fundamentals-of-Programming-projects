from math import sqrt
from entities import *

class Service:
    def __init__(self,repo):
        self.__repo = repo

    def getAllAdr(self):
        return self.__repo.getAll()

    def addAdr(self,ID,name,nr,x,y):
        if ID<0: raise Exception("Invalid ID!")
        if len(name)<3: raise Exception("Invalid name!")
        if nr>100 or nr<0: raise Exception("Invalid number!")
        adr = Address(ID,name,nr,x,y)
        self.__repo.add(adr)

    @staticmethod
    def EuclidDist(x1,y1,x2,y2):
        """
        Function that computes the Euclidean distance between 2 points in a x y plane.
        x1, x2, y1, y2: all int
        """
        x1 = float(x1)
        y1 = float(y1)
        return float(sqrt((x1-x2)**2 + (y1-y2)**2))

    def getNearAdr(self,x,y,d):
        """
        Function that selects the addresses that have the distance at most 'd' from the given (x,y)
        x,y,d: all int
        """
        foundAdr = []
        for adr in self.__repo.getAll():
            dist = self.EuclidDist(adr.getX(),adr.getY(),x,y)
            if dist<=d:
                foundAdr.append((adr,format(dist, '.3f')))
        return foundAdr
