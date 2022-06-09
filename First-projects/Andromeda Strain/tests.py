from repo import FileRepo
from controller import Service
from entities import Person
import unittest

class TestExam(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testSimulateNewDay(self):
        repo = FileRepo("test.txt",Person.fileRead,Person.fileWrite)
        srv = Service(repo)
        p1 = Person(1,'nonvaccinated','ill')
        p2 = Person(2,'nonvaccinated','healthy')
        p3 = Person(3,'nonvaccinated','healthy')
        repo.add(p1)
        repo.add(p2)
        repo.add(p3)
        srv.simulateNewDay()
        self.assertEqual(p2.getStatus(),'ill')
        srv.simulateNewDay()
        self.assertEqual(p3.getStatus(),'ill')
        with self.assertRaises(AssertionError):
            assert p1.getStatus() == 'healthy'
        repo.clearRepo()
