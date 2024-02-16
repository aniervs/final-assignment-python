import unittest
from services.flight_service import FlightService

class TestFlights(unittest.TestCase):
    def setUp(self):
        self.flight_service = FlightService()
        self.flight_service.add_flight("FL100", "New York", "London", "2024-01-01 10:00", 200)

    def test_add_flight(self):
        self.flight_service.add_flight("FL101", "Tokyo", "Paris", "2024-02-01 15:00", 150)
        self.assertIn("FL101", self.flight_service.flights)
        
    def test_delete_flight(self):
        self.flight_service.delete_flight("FL100")
        self.assertNotIn("FL100", self.flight_service.flights)