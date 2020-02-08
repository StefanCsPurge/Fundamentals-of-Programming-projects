import datetime

class Room:
    def __init__(self,number,typ):
        self.__nr = number
        self.__type = typ
    def getNr(self):
        return self.__nr
    def getType(self):
        return self.__type
    def __eq__(self, other):
        return self.__nr == other.__nr
    def __str__(self):
        return "Number: " + str(self.__nr)+" Type: " + str(self.__type)
    @staticmethod
    def readRoom(line):
        parts = line.split(",")
        return Room(int(parts[0].strip()),int(parts[1].strip()))
    @staticmethod
    def writeRoom(room):
        return str(room.__ID).zfill(2)+','+str(room.__type)

class Reservation:
    def __init__(self,ID,room,famName,guestsNo,arrival,departure):
        self.__ID = ID
        self.__roomNo = room
        self.__famName = famName
        self.__guestsNo = guestsNo
        self.__arrival = arrival
        self.__departure = departure
    def getID(self):
        return self.__ID
    def getRoomNo(self):
        return self.__roomNo
    def getFam(self):
        return self.__famName
    def getGuestsNo(self):
        return self.__guestsNo
    def getArrival(self):
        return self.__arrival
    def getDeparture(self):
        return self.__departure
    def __eq__(self, other):
        return self.__ID == other.__ID
    def __str__(self):
        return "ID: "+str(self.__ID).zfill(4) + \
               "\tRoom: "+str(self.__roomNo).ljust(2) + \
               "\tFamily: "+self.__famName.ljust(10) + \
               "\tGuest no.: "+str(self.__guestsNo) + \
               "\tArrival: "+str(self.__arrival) + \
               "\t\tDeparture: "+str(self.__departure)

    @staticmethod
    def readReservation(line):
        parts = line.split(",")
        date1parts = parts[4].strip().split('.')
        Year = datetime.date.today().year
        arrivalDate = datetime.date(Year,int(date1parts[1]),int(date1parts[0]))
        date2parts = parts[5].strip().split('.')
        departureDate = datetime.date(Year,int(date2parts[1]),int(date2parts[0]))
        return Reservation(int(parts[0].strip()), int(parts[1].strip()),parts[2].strip(),int(parts[3].strip()),arrivalDate,departureDate)

    @staticmethod
    def writeReservation(res):
        return str(res.__ID).zfill(4) + "," + \
               str(res.__roomNo) + "," + \
               res.__famName + "," + \
               str(res.__guestsNo) + "," + \
               str(res.__arrival.day)+'.'+str(res.__arrival.month) + "," + \
               str(res.__departure.day)+'.'+str(res.__departure.month)


class ReservationValidator:
    def __init__(self):
        self.__errors = None
    def validate(self,res):
        self.__errors = ""
        if not len(res.getFam()):
            self.__errors += "Invalid family name!\n"
        if res.getGuestsNo() not in range(1,5):
            self.__errors += "Invalid number of guests!\n"
        if res.getArrival() > res.getDeparture():
            self.__errors += "Invalid dates!"
        if len(self.__errors):
            raise Exception(self.__errors)