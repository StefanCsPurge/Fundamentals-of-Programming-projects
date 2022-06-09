from repo import FileRepo
from controller import Service
from entities import Assignment
import unittest

class TestExam(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdd(self):
        repo = FileRepo("test.txt",Assignment.fileRead,Assignment.fileWrite)
        srv = Service(repo)
        srv.addAssignment(1,'Ass1','Y.O.L.O.')
        self.assertEqual(len(repo.getAll()),1)
        srv.addAssignment(2, 'Ass2', 'MarianaMaria')
        self.assertEqual(len(repo.getAll()), 2)
        repo.clearRepo()

    def testAddRepo(self):
        repo = FileRepo("test.txt", Assignment.fileRead, Assignment.fileWrite)
        a1 = Assignment(1,'Ass1','Y.O.L.O.')
        a2 = Assignment(2, 'Ass2', 'MarianaMaria')
        repo.add(a1)
        self.assertEqual(repo.getAll(),[a1])
        repo.add(a2)
        self.assertEqual(repo.getAll(),[a1,a2])

