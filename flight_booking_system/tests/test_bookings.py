import unittest

from services.flight_service import FlightService
from services.booking_service import BookingService
from exceptions.custom_exceptions import FlightFullException, BookingNotFoundException



class TestBookings(unittest.TestCase):
    def setUp(self):
        self.booking_service = BookingService()
        self.flight_service = FlightService()
        self.flight_service.add_flight("FL102", "San Francisco", "Berlin", "2024-03-01 11:00", 2)
        
    def test_book_flight(self):
        booking_id = "BK001"
        self.booking_service.book_flight(booking_id, "FL102", "John Doe")
        self.assertIn(booking_id, self.booking_service.bookings)

    def test_flight_full_exception(self):
        self.booking_service.book_flight("BK002", "FL102", "Jane Doe")
        self.booking_service.book_flight("BK003", "FL102", "Jim Beam")
        with self.assertRaises(FlightFullException):
            self.booking_service.book_flight("BK004", "FL102", "Jack Daniels")
            
    def test_cancel_booking(self):
        booking_id = "BK005"
        self.booking_service.book_flight(booking_id, "FL102", "Alice Wonderland")
        self.booking_service.cancel_booking(booking_id)
        with self.assertRaises(BookingNotFoundException):
            self.booking_service.cancel_booking(booking_id)

if __name__ == '__main__':
    unittest.main()
