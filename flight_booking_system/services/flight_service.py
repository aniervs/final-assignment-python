from models.flight import Flight

class FlightService:
    def __init__(self):
        self.flights = {}
    
    def add_flight(self, flight_number, origin, destination, departure_time, capacity):
        if flight_number in self.flights:
            raise ValueError(f"Flight number {flight_number} already exists.")
        self.flights[flight_number] = Flight(flight_number, origin, destination, departure_time, capacity)
        return self.flights[flight_number]
    
    def update_flight(self, flight_number, origin=None, destination=None, departure_time=None, capacity=None):
        if flight_number not in self.flights:
            raise ValueError(f"Flight number {flight_number} does not exist.")
        flight = self.flights[flight_number]
        if origin:
            flight.origin = origin
        if destination:
            flight.destination = destination
        if departure_time:
            flight.departure_time = departure_time
        if capacity:
            flight.capacity = capacity
        return flight
    
    def delete_flight(self, flight_number):
        if flight_number in self.flights:
            del self.flights[flight_number]
        else:
            raise ValueError(f"Flight number {flight_number} does not exist.")
