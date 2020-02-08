import datetime

class UI:
    def __init__(self,service):
        self.__srv = service
        self.__menu = """Press:  [1] to see the hotel rooms info
        [2] to see the reservations
        [3] to add a reservation
        [4] to delete a reservation
        [5] to show available rooms between 2 dates
        [6] to show the monthly report
        [7] to show the week days report
        [x] to exit"""

    @staticmethod
    def printObjects(objList):
        for obj in objList:
            print(obj)
        print()

    def showHotelRooms(self):
        roomsList = self.__srv.getRooms()
        if not len(roomsList):
            raise Exception("There are no stored rooms!")
        UI.printObjects(roomsList)

    def showReservations(self):
        resList = self.__srv.getReservations()
        if not len(resList):
            raise Exception("There are no stored reservations!")
        UI.printObjects(resList)

    def addReservation(self):
        name = input("Insert family name: ")
        rTyp = int(input("Room type (insert number): "))
        guests = int(input("Insert the number of guests: "))
        y = datetime.date.today().year
        aDay = int(input("Arrival day: "))
        aMonth = int(input("Arrival month: "))
        a = datetime.date(y, aMonth, aDay)
        dDay = int(input("Departure day: "))
        dMonth = int(input("Departure month: "))
        d = datetime.date(y,dMonth,dDay)
        self.__srv.createReservation(name,rTyp,guests,a,d)

    def deleteReservation(self):
        x = int(input("Insert reservation number: "))
        self.__srv.deleteRsv(x)

    def showAvailableRooms(self):
        y = datetime.date.today().year
        dates = input("Insert the interval in the format dd.mm - dd.mm : ").split('-')
        date1str = dates[0].split('.')
        aDay = int(date1str[0])
        aMonth = int(date1str[1])
        a = datetime.date(y, aMonth, aDay)
        date2str = dates[1].split('.')
        dDay = int(date2str[0])
        dMonth = int(date2str[1])
        d = datetime.date(y, dMonth, dDay)
        availableRooms = self.__srv.getAvailableRooms(a,d)
        UI.printObjects(availableRooms)

    def monthlyReport(self):
        orderedMonths = self.__srv.getMonthlyReport()
        for month in orderedMonths:
            print('{} - {} night(s)'.format(month[0],month[1]))
        print()

    def weekDaysReport(self):
        orderedDays = self.__srv.getWeekDaysReport()
        for day in orderedDays:
            print('{} - {} reserved room(s)'.format(day[0],day[1]))
        print()

    def run(self):
        options = {'1': self.showHotelRooms,
                   '2': self.showReservations,
                   '3': self.addReservation,
                   '4': self.deleteReservation,
                   '5': self.showAvailableRooms,
                   '6': self.monthlyReport,
                   '7': self.weekDaysReport}
        while True:
            try:
                print(self.__menu)
                choice = input('-> ').strip()
                if choice not in ('1','2','3','4','5','6','7','x'):
                    raise Exception("Non-existent option!")
                if choice == 'x': return
                options[choice]()
            except Exception as ex:
                print(ex)