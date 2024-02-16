import json
from flight_booking_system.models.flight import Flight

FLIGHT_DATA_FILE = 'flight_booking_system/flights_data.JSON'

def load_flights_from_json():
    """Load flights from a JSON file."""
    try:
        with open(FLIGHT_DATA_FILE, 'r') as file:
            flight_dicts = json.load(file)
            return {fn: Flight(**fd) for fn, fd in flight_dicts.items()}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  

def save_flights_to_json(flights):
    """Save the flights dictionary to a JSON file."""
    with open(FLIGHT_DATA_FILE, 'w') as file:
        json.dump({fn: flight.__dict__ for fn, flight in flights.items()}, file, indent=4)

flights = load_flights_from_json()

def add_flight(flight_number, origin, destination, departure_time, capacity):
    flight = Flight(flight_number, origin, destination, departure_time, capacity)
    flights[flight_number] = flight
    save_flights_to_json(flights)  
    return flight

def fetch_flights_from_database():
    return list(load_flights_from_json().values())

def get_all_flights():
    return fetch_flights_from_database()

def update_flight(flight_number, origin=None, destination=None, departure_time=None, capacity=None):
    if flight_number in flights:
        flight = flights[flight_number]
        if origin is not None:
            flight.origin = origin
        if destination is not None:
            flight.destination = destination
        if departure_time is not None:
            flight.departure_time = departure_time
        if capacity is not None:
            flight.capacity = capacity
        save_flights_to_json(flights)  
        return True
    else:
        return False
