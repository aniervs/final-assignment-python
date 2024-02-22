import flight as fl
import data_manager as dm
import custom_exceptions as ce

def add_flight(flight_number, origin, destination, date, capacity):
    flight = fl.Flight(flight_number, origin, destination, date, capacity)
    dm.add_flight_to_csv(flight)

def update_flight(flight_number):
    raise NotImplementedError

def search_flights(departure_city, destination_city, departure_date):
    flights = dm.read_flights_from_csv()
    result = []
    for flight in flights:
        if flight.departure_city == departure_city and flight.departure_date == departure_date and flight.destination_city == destination_city:
            result.append(flight)
    return result

def fetch_flight_by_number(number):
    flights = dm.read_flights_from_csv()
    for flight in flights:
        if flight.flight_number == number:
            return flight
    raise ce.FlightNotFoundError