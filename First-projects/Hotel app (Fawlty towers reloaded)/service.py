from domain import Room,Reservation
import random
import datetime
import calendar
import unittest

class Service:
    def __init__(self,roomRepo,reservationRepo,reservationValidator):
        self.__roomRepo = roomRepo
        self.__resRepo = reservationRepo
        self.__resValid = reservationValidator()

    def getRooms(self):
        return self.__roomRepo.getAll()

    def getReservations(self):
        return self.__resRepo.getAll()

    def checkAvailableRoom(self,roomNo,arrival,departure):
        """
        Method that checks if the room (with a given number) is available during the given reservation dates.
        :param roomNo: int - the unique room number
        :param arrival: date - complete arrival date
        :param departure: date - complete departure date
        :return: True/False
        """
        for res in self.__resRepo.getAll():
            if res.getRoomNo() == roomNo and arrival < res.getDeparture() and departure > res.getArrival():
                return False
        return True

    def createReservation(self,famName,roomType,guestsNo,arrival,departure):
        """
        Method that creates a new reservation, after validating the user input data.
        :param famName: string - the given family name
        :param roomType: int - 1 (single), 2 (double), 4 (family)
        :param guestsNo: int - from 1 to 4
        :param arrival: date - complete arrival date
        :param departure: date - complete departure date
        :return: nothing
        """
        self.__resValid.validate(Reservation(None,None,famName,guestsNo,arrival,departure))
        roomNumber = False
        for room in self.__roomRepo.getAll():
            if room.getType() == roomType:
                if self.checkAvailableRoom(room.getNr(),arrival,departure):
                    roomNumber = room.getNr()
                    break
        if not roomNumber:
            raise Exception("There are no available rooms of the desired type during the reservation dates!")
        resID = random.randint(1000, 9999)
        while Reservation(resID,None,None,None,None,None) in self.__resRepo.getAll():
            resID = random.randint(1000,9999)
        self.__resRepo.add(Reservation(resID,roomNumber,famName,guestsNo,arrival,departure))

    def deleteRsv(self,ID):
        """
        Method that removes a reservation using its given ID, by calling the repo remove method.
        :param ID: int - the unique number of the reservation
        :return: nothing
        """
        self.__resRepo.remove(Reservation(ID,None,None,None,None,None))

    def getAvailableRooms(self,date1,date2):
        if date1 > date2:
            raise Exception("First date is after the second date!")
        avRooms = []
        for room in self.__roomRepo.getAll():
            if self.checkAvailableRoom(room.getNr(),date1,date2):
                avRooms.append(room)
        return avRooms

    def getMonthlyReport(self):
        monthsNights = [0]*13
        y = datetime.date.today().year
        for res in self.__resRepo.getAll():
            a = res.getArrival()
            d = res.getDeparture()
            m1 = a.month
            m2 = d.month
            nights = (d-a).days
            if m1 == m2:
                monthsNights[m1] += nights
            else:
                m2first = datetime.date(y,m2,1)
                m2Nights = (d-m2first).days
                monthsNights[m2] += m2Nights
                monthsNights[m1] += (nights-m2Nights)
        finalMonthsNights = []
        for i in range(1,13):
            finalMonthsNights.append([calendar.month_name[i],monthsNights[i]])
        finalMonthsNights.sort(key=lambda x: x[1], reverse=True)
        return finalMonthsNights

    def getWeekDaysReport(self):
        daysFrequency = {}
        for res in self.__resRepo.getAll():
            a = res.getArrival()
            d = res.getDeparture()
            for i in range((d-a).days):
                day = calendar.day_name[(a+datetime.timedelta(i)).weekday()]
                daysFrequency[day] = daysFrequency[day] + 1 if day in daysFrequency else 1
        finalDaysFrequency = list(map(list,daysFrequency.items()))
        finalDaysFrequency.sort(key=lambda x: x[1], reverse=True)
        return finalDaysFrequency

class TestReservations(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        from repo import FileRepo
        from domain import ReservationValidator
        self.RoomsRepo = FileRepo("rooms.txt", Room.readRoom, Room.writeRoom)
        self.ResRepo = FileRepo("test.txt",Reservation.readReservation,Reservation.writeReservation)
        self.srv = Service(self.RoomsRepo,self.ResRepo,ReservationValidator)
        self.y = datetime.date.today().year

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testCheckAvailableRoom(self):
        self.assertTrue(self.srv.checkAvailableRoom(3,datetime.date(self.y,3,3),datetime.date(self.y,4,4)))
        self.assertFalse(self.srv.checkAvailableRoom(1,datetime.date(self.y,1,2),datetime.date(self.y,1,12)))

    def testCreateReservation(self):
        self.srv.createReservation('Test',4,4,datetime.date(self.y,11,11),datetime.date(self.y,11,12))
        reservations = self.srv.getReservations()
        lastRes = reservations[-1]
        self.assertEqual(lastRes.getFam(),'Test')
        self.srv.deleteRsv(lastRes.getID())

    def testDeleteReservation(self):
        firstRes = self.srv.getReservations()[0]
        ID = firstRes.getID()
        self.srv.deleteRsv(ID)
        self.assertTrue(firstRes not in self.srv.getReservations())
        self.ResRepo.add(firstRes)
