from models.booking import Booking
from exceptions.custom_exceptions import BookingNotFoundException

class BookingService:
    def __init__(self):
        self.bookings = {}
    
    def book_flight(self, booking_id, flight_number, passenger_name):
        if booking_id in self.bookings:
            raise ValueError(f"Booking ID {booking_id} already exists.")

        self.bookings[booking_id] = Booking(booking_id, flight_number, passenger_name)
        return self.bookings[booking_id]
    
    def cancel_booking(self, booking_id):
        if booking_id not in self.bookings:
            raise ValueError(f"Booking ID {booking_id} does not exist.")
        if booking_id not in self.bookings:
            raise BookingNotFoundException(booking_id)
        del self.bookings[booking_id]
        
    def get_all_bookings(self):
        return list(self.bookings.values())