from UI import ConsoleMenu
from controller import ExamSrv
from repo import FileRepo
from entities import Student

if __name__ ==  '__main__':
    studRepo = FileRepo("students.txt",Student.fileRead,Student.fileWrite)
    examContr = ExamSrv(studRepo)
    appUI = ConsoleMenu(examContr)
    appUI.run()

