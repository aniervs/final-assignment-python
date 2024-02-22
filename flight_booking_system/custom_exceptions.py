class FlightFullException(Exception):
    def __init__(self):
        super().__init__("There are no available places on this flight.")
        
class NoFlightsError(Exception):
    def __init__(self):
        super().__init__("There are no flights with selected options.")

class IncompleteFormError(Exception):
    def __init__(self):
        super().__init__("Please, fill in all the fields.")


class SameCitiesError(Exception):
    def __init__(self):
        super().__init__('Departure and destination cities cannot be the same.')


class FlightNotFoundError(Exception):
    def __init__(self):
        super().__init__('Error occured: this flight is not found.')
