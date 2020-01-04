from controller import *
from repo import FileRepo
from entities import *
import unittest

class TestSrv(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    # here are the tests
    def testGetBusesAndRoutes(self):
        BusRepo = FileRepo("testBuses.txt",Bus.fileRead,Bus.fileWrite)
        b1 = Bus(1,1,'b1',2)
        BusRepo.addObj(b1)
        RouteRepo = FileRepo("testRoutes.txt",Route.fileRead,Route.fileWrite)
        r1 = Route(1,12)
        RouteRepo.addObj(r1)
        srv = BusSrv(BusRepo,RouteRepo)
        buses, routes = srv.getAllBusesAndRoutes()
        self.assertEqual(buses,[b1])
        self.assertEqual(routes,[r1])

    def testGetBusesOfRoute(self):
        BusRepo = FileRepo("testBuses.txt", Bus.fileRead, Bus.fileWrite)
        b1 = Bus(1, 1, 'b1', 2)
        BusRepo.addObj(b1)
        RouteRepo = FileRepo("testRoutes.txt", Route.fileRead, Route.fileWrite)
        r1 = Route(1, 12)
        RouteRepo.addObj(r1)
        srv = BusSrv(BusRepo, RouteRepo)
        buses = srv.getBusesOfRoute(1)
        self.assertEqual(buses, [b1])


    def testIncreaseUsage(self):
        BusRepo = FileRepo("testBuses.txt", Bus.fileRead, Bus.fileWrite)
        b1 = Bus(1, 1, 'b1', 2)
        BusRepo.addObj(b1)
        RouteRepo = FileRepo("testRoutes.txt", Route.fileRead, Route.fileWrite)
        srv = BusSrv(BusRepo, RouteRepo)
        srv.increaseUsage(1,1)
        self.assertEqual(b1.getTimesUsedRoute(),3)
        BusRepo.clearRepo()

    def testMostUsedBuses(self):
        BusRepo = FileRepo("testBuses.txt", Bus.fileRead, Bus.fileWrite)
        b1 = Bus(1, 1, 'b1', 2)
        b2 = Bus(2, 1, 'b1', 3)
        BusRepo.addObj(b1)
        BusRepo.addObj(b2)
        RouteRepo = FileRepo("testRoutes.txt", Route.fileRead, Route.fileWrite)
        r1 = Route(1, 12)
        RouteRepo.addObj(r1)
        srv = BusSrv(BusRepo, RouteRepo)
        buses = srv.MostUsedBuses()
        self.assertEqual(buses,[b2,b1])


    #self.assertEqual(2 elements)
    #with self.assertRaises(Exception): something that raises an exception