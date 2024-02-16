import sys
sys.path.append('/Users/zainellahi/final-assignment-python')

import unittest
from flight_booking_system.services.flight_service import add_flight, update_flight
from flight_booking_system.models.flight import Flight

class TestFlightServices(unittest.TestCase):
    def test_add_flight(self):
        result = add_flight("ES11", "Origin1", "Destination1", "09:00", 50)
        self.assertIsInstance(result, Flight)
        
    def test_update_flight(self):
        add_flight("FN002", "Origin2", "Destination2", "12:00", 30)
        result = update_flight("ES12", 40)
        self.assertIsInstance(result, Flight)
        self.assertEqual(result.capacity, 40)

if __name__ == "__main__":
    unittest.main()
