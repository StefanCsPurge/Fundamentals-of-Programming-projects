class Song:
    def __init__(self,ID,title,artist,genre):
        self.__ID = ID
        self.__title = title
        self.__artist = artist
        self.__genre = genre

    def getID(self):
        return self.__ID
    def getTitle(self):
        return self.__title
    def getGenre(self):
        return self.__genre

    def __eq__(self, other):
        return self.__ID == other.__ID

    def __str__(self):
        return "ID: " + str(self.__ID) + "  ~  TITLE: " + self.__title + "  ~  ARTIST: " + self.__artist + " ~ GENRE: " + self.__genre

    @staticmethod
    def fileRead(line):
        parts = line.strip().split(';')
        return Song(int(parts[0]),parts[1],parts[2],parts[3])
    @staticmethod
    def fileWrite(song):
        return str(song.__ID) + ";" + song.__title + ";" + song.__artist + ";" + song.__genre

