from UI import ConsoleMenu
from controller import Service
from repo import FileRepo
from entities import Person

if __name__ ==  '__main__':
    repo = FileRepo("persons.txt",Person.fileRead,Person.fileWrite)
    srv = Service(repo)
    appUI = ConsoleMenu(srv)
    appUI.run()