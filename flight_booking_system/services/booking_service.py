from ..models.booking import Booking

def book_flight(booking_id, flight_number, passenger_name):
    booking = Booking(booking_id, flight_number, passenger_name)

def cancel_booking(booking_id):
    raise NotImplementedError
