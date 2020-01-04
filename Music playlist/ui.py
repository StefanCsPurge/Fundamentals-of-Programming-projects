class ConsoleMenu:
    def __init__(self,songSrv):
        self.__songSrv = songSrv
        self.__menu = "\nPress: [1] to search songs by name\n" \
                      "[2] to show the songs with the same genre as a given song"
    @staticmethod
    def printSongs(songs):
        for song in songs:
            print(song)

    def showAll(self):
        theSongs = self.__songSrv.getAllSongs()
        self.printSongs(theSongs)

    def searchSongsByName(self):
        searchStr = input("Search: ").strip()
        results = self.__songSrv.nameSearch(searchStr)
        print("The results are:")
        self.printSongs(results)

    def showSameGenre(self):
        try:
            sID = int(input("Insert the ID of the song: "))
            if sID < 0:
                raise ValueError
        except ValueError:
            raise Exception('The ID is not a natural number!')
        genre = self.__songSrv.getGenre(sID)
        print('The searched genre: {}'.format(genre))
        results = self.__songSrv.genreSearch(genre)
        self.printSongs(results)

    def run(self):
        options = {1:self.searchSongsByName,2:self.showSameGenre,0:self.showAll}
        while True:
            print(self.__menu)
            try:
                choice = int(input("->"))
                if choice == 3: exit()
                if choice not in (1,2,0):
                    raise Exception('Non-existent option!')
                options[choice]()
            except Exception as ex:
                print("Error: " + str(ex))