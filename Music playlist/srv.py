class SongService:
    def __init__(self,songRepo):
        self.__repo = songRepo

    def nameSearch(self,sStr):
        foundSongs = []
        for song in self.__repo.getAll():
            if sStr.casefold() in song.getTitle().casefold():
                foundSongs.append(song)
        if not len(foundSongs):
            raise Exception("No songs were found!")
        return foundSongs

    def genreSearch(self,genre):
        foundSongs = []
        for song in self.__repo.getAll():
            if genre == song.getGenre():
                foundSongs.append(song)
        if not len(foundSongs):
            raise Exception("No songs were found!")
        return foundSongs

    def getGenre(self,ID):
        song = self.__repo.getObj(ID)
        return song.getGenre()

    def getAllSongs(self):
        return self.__repo.getAll()

