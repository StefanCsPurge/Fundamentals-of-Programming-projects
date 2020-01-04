from UI import ConsoleMenu
from controller import Service
from repo import FileRepo
from entities import Assignment

if __name__ ==  '__main__':
    repo = FileRepo("assignments.txt",Assignment.fileRead,Assignment.fileWrite)
    srv = Service(repo)
    appUI = ConsoleMenu(srv)
    appUI.run()