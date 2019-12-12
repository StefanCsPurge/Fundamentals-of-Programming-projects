

def createFestival(name,month,price,artists):
    return {'name':name,'month':month,'price':price,'artists':artists}

def select_fest_by_artist(artist, festList):
    """
    Function that creates a new list of festivals that have the same artist.
    :param artist: str - artist name
    :param festList: list of dictionaries
    :return: nothing
    """
    newFestList = []
    for festival in festList:
        if artist in festival['artists']:
            newFestList.append(festival)
    return newFestList

def select_fest_by_season(season, festList):
    newFestList = []
    seasons = {'spring':(3,4,5),'summer':(6,7,8),'autumn':(9,10,11),'winter':(12,1,2)}
    for festival in festList:
        if festival['month'] in seasons[season]:
            newFestList.append(festival)
    return newFestList

def add_festival(festival, festList):
    """
    Function that adds a new festival to a festival list
    :param festival: dictionary - our new festival
    :param festList: list of dictionaries
    :return: nothing
    """
    if festival['month'] < 1 or festival['month']>12:
        raise ValueError("The month is not in the interval 1-12!")
    for item in festList:
        if item['name'] == festival['name']:
            raise Exception("There is another festival with the same name!")
    festList.append(festival)
