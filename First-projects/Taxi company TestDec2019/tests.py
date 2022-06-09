from repo import FileRepo
from controller import Service
from entities import Address
import unittest

class TestExam(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testGetNearAdr(self):
        repo = FileRepo("test.txt",Address.fileRead,Address.fileWrite)
        a1 = Address(1,'adr1',1,4,0)
        a2 = Address(2,'adr2',4,5,0)
        repo.add(a1)
        repo.add(a2)
        srv = Service(repo)
        fAdr = srv.getNearAdr(0,0,10)
        self.assertEqual(len(fAdr),2)
        self.assertEqual(fAdr[0][0],a1)
        self.assertEqual(fAdr[1][0],a2)

    def testEuclidDist(self):
        repo = FileRepo("test.txt", Address.fileRead, Address.fileWrite)
        srv = Service(repo)
        d = srv.EuclidDist(6,6,2,3)
        self.assertEqual(d,5)