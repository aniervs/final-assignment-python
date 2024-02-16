class FlightFullException(Exception):
    def __init__(self, message="Flight is full"):
        self.message = message
        super().__init__(self.message)

class BookingNotFoundException(Exception):
    def __init__(self, booking_id, message="Booking not found"):
        self.booking_id = booking_id
        self.message = f"{message}: {booking_id}"
        super().__init__(self.message)
