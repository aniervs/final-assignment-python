from models.booking import Booking
from models.flight import Flight 
from flight_service import currentl
book={}
def book_flight(booking_id, flight_number, passenger_name):
    book[booking_id]=flight_number
    booking = Booking(booking_id, flight_number, passenger_name)
    
def cancel_booking(booking_id):
    if (booking_id in book):
        currentl[book[booking_id]].cancel_booked()
        del book[booking_id]
        return "canceling completed succesfuly!"
    else : 
        return "booking id is invalid!"
    raise NotImplementedError
