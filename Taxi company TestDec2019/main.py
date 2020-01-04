from UI import ConsoleMenu
from controller import Service
from repo import FileRepo
from entities import Address

if __name__ ==  '__main__':
    repo = FileRepo("addresses.txt",Address.fileRead,Address.fileWrite)
    srv = Service(repo)
    appUI = ConsoleMenu(srv)
    appUI.run()