class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.capacity = capacity
        self.bookings = 0
        self.full=False
    def up_booked(self):
        self.bookings +=1
        if self.bookings==self.capacity:
            self.full=True
    def cancel_booked(self):
        if self.bookings==self.capacity:
            self.full=False
        self.bookings -=1
    def available_seats(self):
        return self.capacity - self.bookings
