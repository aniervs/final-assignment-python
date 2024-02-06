from ..models.flight import Flight
from ..database.db_manager import DBManager

def add_flight(flight_number, origin, destination, departure_time, capacity):
    flight = Flight(flight_number, origin, destination, departure_time, capacity)

def update_flight(flight_number):
    raise NotImplementedError
