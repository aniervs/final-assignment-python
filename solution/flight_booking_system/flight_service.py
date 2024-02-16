from models.flight import Flight
#from exceptions import custom_exceptions
currentl={}
def add_flight(flight_number, origin, destination, departure_time, capacity,currently):
    currently[flight_number] = 2 #Flight(flight_number, origin, destination, departure_time, capacity)
    return 
def update_flight(flight_number,currently):
    #if(custom_exceptions.FlightFullException):
        currently[flight_number].upadate_booked()
        return currently
    #else :
        return currently
