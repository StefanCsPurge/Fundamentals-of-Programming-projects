from repo import FileRepo
from controller import ExamSrv
from entities import Student
import unittest

class TestExam(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAddStud(self):
        repo = FileRepo("testStuds.txt",Student.fileRead,Student.fileWrite)
        srv = ExamSrv(repo)
        srv.addStud(12,'Stud1 Stud1',10,9)
        self.assertEqual(len(repo.getAll()),1)
        srv.addStud(13, 'Stud2 Stud2', 10, 9)
        self.assertEqual(len(repo.getAll()), 2)
        repo.clearRepo()

    def testRepoAddStud(self):
        repo = FileRepo("testStuds.txt", Student.fileRead, Student.fileWrite)
        s1 = Student(1,"stud stud",9,9)
        repo.add(s1)
        self.assertEqual(repo.getAll(),[s1])
        repo.clearRepo()