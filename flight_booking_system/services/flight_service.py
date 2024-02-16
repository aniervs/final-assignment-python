from ..models.flight import Flight

def add_flight(flight_number, origin, destination, departure_time, capacity):
    flight = Flight(flight_number, origin, destination, departure_time, capacity)

def update_flight(flight_number):
    raise NotImplementedError
