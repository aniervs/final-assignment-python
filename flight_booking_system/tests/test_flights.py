import unittest
from flight_booking_system.models.flight import Flight

class TestFlight(unittest.TestCase):
    def test_available_seats(self):
        flight = Flight("F123", "Origin", "Destination", "2024-02-20 08:00", 100)
        self.assertEqual(flight.available_seats(), 100)

    def test_book_seat(self):
        flight = Flight("F123", "Origin", "Destination", "2024-02-20 08:00", 100)
        for _ in range(100):
            self.assertTrue(flight.book_seat())
        self.assertFalse(flight.book_seat())

    def test_cancel_booking(self):
        flight = Flight("F123", "Origin", "Destination", "2024-02-20 08:00", 100)
        for _ in range(50):
            flight.book_seat()
        for _ in range(50):
            self.assertTrue(flight.cancel_booking())
        self.assertFalse(flight.cancel_booking())
        self.assertEqual(flight.available_seats(), 100)

if __name__ == "__main__":
    unittest.main()
