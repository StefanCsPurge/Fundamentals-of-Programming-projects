from UI import ConsoleMenu
from controller import BusSrv
from repo import FileRepo
from entities import Bus,Route

if __name__ == '__main__':
    BusRepo = FileRepo('buses.txt',Bus.fileRead,Bus.fileWrite)
    RouteRepo = FileRepo('routes.txt',Route.fileRead,Route.fileWrite)
    service = BusSrv(BusRepo,RouteRepo)
    appUI = ConsoleMenu(service)
    appUI.run()