class Booking:
    def __init__(self, booking_id, origin, destination, passenger_name, flight_time, seats, booking_code):
        self.booking_id = booking_id
        self.origin = origin
        self.destination = destination
        self.passenger_name = passenger_name
        self.flight_time = flight_time
        self.seats = seats
        self.booking_code = booking_code

    def __eq__(self, other):
        return self.booking_id == other.booking_id

    def __repr__(self):
        return (f"Booking(booking_id={self.booking_id}, origin={self.origin}, "
                f"destination={self.destination}, passenger_name='{self.passenger_name}', "
                f"flight_time='{self.flight_time}', seats={self.seats}, booking_code='{self.booking_code}')")

    def display_booking_info(self):
        seat_assignments = ', '.join(self.seats)
        return (f"Booking ID: {self.booking_id}, Booking Code: {self.booking_code}, "
                f"Origin: {self.origin}, Destination: {self.destination}, "
                f"Passenger Name: {self.passenger_name}, Flight Time: {self.flight_time}, "
                f"Seats: {seat_assignments}")
