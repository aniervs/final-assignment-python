import unittest
from flight_booking_system.services.booking_service import book_flight, cancel_booking, bookings
from flight_booking_system.models.booking import Booking


class TestBookingServices(unittest.TestCase):
    def test_book_flight_successful(self):
        result = book_flight("B001", "ES11", "Zain")
        self.assertIsInstance(result, Booking)

    def test_cancel_booking_successful(self):
        book_flight("B002", "ES12", "Anier")
        result = cancel_booking("B004")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()