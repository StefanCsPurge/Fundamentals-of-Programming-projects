from UI import UI
from service import Service
from repo import FileRepo
from domain import Room,Reservation,ReservationValidator

if __name__ == "__main__":
    RoomsRepo = FileRepo("rooms.txt",Room.readRoom,Room.writeRoom)
    ReservationsRepo = FileRepo("reservations.txt",Reservation.readReservation,Reservation.writeReservation)
    srv = Service(RoomsRepo,ReservationsRepo,ReservationValidator)
    app_UI = UI(srv)
    app_UI.run()