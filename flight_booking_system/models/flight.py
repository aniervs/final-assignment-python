class Flight:
    def __init__(self, flight_number, origin, destination, departure_time, capacity):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.capacity = capacity
        self.bookings = 0

    def available_seats(self):
        return self.capacity - self.bookings

    def book_seat(self):
        if self.available_seats() > 0:
            self.bookings += 1
            return True
        else:
            return False

    def cancel_booking(self):
        if self.bookings > 0:
            self.bookings -= 1
            return True
        else:
            return False
