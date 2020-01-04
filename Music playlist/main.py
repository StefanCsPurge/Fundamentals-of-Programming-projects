from ui import ConsoleMenu
from srv import SongService
from repo import FileRepo
from entities import Song

if __name__ == '__main__':
    repository = FileRepo("songs.txt",Song.fileRead,Song.fileWrite)
    appUI = ConsoleMenu(SongService(repository))
    appUI.run()
