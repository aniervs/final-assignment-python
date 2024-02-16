from ..models.booking import Booking
from ..exceptions.custom_exceptions import BookingNotFoundException,FlightFullException

from .flight_service import flights  

bookings=[]
def book_flight(booking_id, flight_number, passenger_name):
    booking = Booking(booking_id, flight_number, passenger_name)

    flight_exists = False
    for flight in flights:
        if flight.flight_number == flight_number:
            flight_exists = True
            break

    if not flight_exists:
        raise ValueError(f"Flight with number {flight_number} does not exist.")

    for flight in flights:
        if flight.flight_number == flight_number and flight.available_seats() == 0:
            raise FlightFullException(f"Flight with number {flight_number} is full. Cannot book more seats.")

    bookings.append(booking)

    for flight in flights:
        if flight.flight_number == flight_number:
            flight.bookings += 1


def cancel_booking(booking_id):
        for i, booking in enumerate(bookings):
         if booking.booking_id == booking_id:
            del bookings[i]
            return True  
         raise BookingNotFoundException("Booking not found")


