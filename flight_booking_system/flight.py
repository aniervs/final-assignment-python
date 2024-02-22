class Flight:
    def __init__(self, flight_number, departure_city, destination_city, departure_date, capacity, bookings=0):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.departure_date = departure_date
        self.capacity = capacity
        self.bookings = bookings


    def available_seats(self):
        return self.capacity - self.bookings
