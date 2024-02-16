from ..models.flight import Flight

flights=[]

def add_flight(flight_number, origin, destination, departure_time, capacity):
     new_flight = Flight(flight_number, origin, destination, departure_time, capacity)
     flights.append(new_flight)
     return new_flight

def update_flight(flight_number,new_capacity):
    for flight in flights:
        if flight.flight_number == flight_number:
            flight.capacity = new_capacity
            return flight
    return None