from operations import *
from operator import itemgetter

def print_menu():
    print("""Press:
    1 to add a festival to the list
    2 to show all festivals for a given season
    3 to show the festivals where an artist will perform""")
def printFestivals(festList):
    months = ('January','February','March','April','May','June','July','August','September','October','November','December')
    for festival in festList:
        print("Name: {}, month: {}, ticket cost: {}, artists: {}".format(festival['name'],months[festival['month']-1],festival['price'],', '.join(festival['artists'])))

def listFest_by_artist(artist,festList):
    newFestList = select_fest_by_artist(artist,festList)
    printFestivals(newFestList)

def listFest_by_season(season,festList):
    season_festList = select_fest_by_season(season,festList)
    season_festList = sorted(season_festList, key=itemgetter('month', 'name'))
    printFestivals(season_festList)

def insertArtists():
    artists = []
    print("Insert artists: (enter 'd' when done)")
    ok = True
    while ok:
        a = input()
        a.strip()
        if a!='d':
            artists.append(a)
        else: ok = False
    return artists

def run():
    festivals = [{'name':'Untold','month':8,'price':420,'artists':['Kshmr','Tiesto']},
                 {'name':'w','month':2,'price':0,'artists':['no']},
                 {'name':'s','month':1,'price':0,'artists':['artist']},
                 {'name':'v','month':2,'price':0,'artists':['for','you']},
                 {'name':'a','month':1,'price':0,'artists':['today']}]
    print_menu()
    while True:
        opt = input('->')
        try:
            opt = opt.strip()
            if opt == '1':
                name = input("Insert name: ")
                month = int(input("Insert month: "))
                price = int(input("Insert ticket cost: "))
                artists = insertArtists()
                fest = createFestival(name,month,price,artists)
                add_festival(fest,festivals)
            elif opt == '2':
                season = input("Insert season: ")
                listFest_by_season(season.strip(),festivals)
            elif opt == '3':
                artist = input("Insert artist:")
                listFest_by_artist(artist.strip(),festivals)
            elif opt == '4':
                printFestivals(festivals)
            else:
                raise Exception("Option does not exist!")
        except Exception as ex:
            print(ex)
