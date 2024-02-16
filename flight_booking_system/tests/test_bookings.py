import unittest
from datetime import datetime
from flight_booking_system.models.booking import Booking

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.booking_id = "12345"
        self.origin = "CityA"
        self.destination = "CityB"
        self.passenger_name = "John Doe"
        self.flight_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.seats = ["1A", "2B"]
        self.booking_code = "ABCDE"

    def test_booking_creation(self):
        booking = Booking(self.booking_id, self.origin, self.destination,
                          self.passenger_name, self.flight_time, self.seats,
                          self.booking_code)
        
        self.assertEqual(booking.booking_id, self.booking_id)
        self.assertEqual(booking.origin, self.origin)
        self.assertEqual(booking.destination, self.destination)
        self.assertEqual(booking.passenger_name, self.passenger_name)
        self.assertEqual(booking.flight_time, self.flight_time)
        self.assertEqual(booking.seats, self.seats)
        self.assertEqual(booking.booking_code, self.booking_code)

    def test_display_booking_info(self):
        booking = Booking(self.booking_id, self.origin, self.destination,
                          self.passenger_name, self.flight_time, self.seats,
                          self.booking_code)
        
        expected_info = (f"Booking ID: {self.booking_id}, Booking Code: {self.booking_code}, "
                         f"Origin: {self.origin}, Destination: {self.destination}, "
                         f"Passenger Name: {self.passenger_name}, Flight Time: {self.flight_time}, "
                         f"Seats: {', '.join(self.seats)}")
        
        self.assertEqual(booking.display_booking_info(), expected_info)

if __name__ == '__main__':
    unittest.main()
