class Booking:
    def __init__(self, flight_number, departure_city, destination_city, date, passport):
        self.flight_number = flight_number
        self.passport = passport
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.date = date
