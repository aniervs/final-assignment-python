import re

def validate_passenger_name(name):
    """Validate the passenger's name. It must not be empty and should only contain alphabetic characters and spaces."""
    if not name or not re.match("^[a-zA-Z\s]+$", name):
        raise ValueError("Invalid passenger name.")

def validate_capacity(capacity):
    """Validate the flight capacity. It must be a positive integer."""
    if not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("Invalid capacity. Capacity must be a positive integer.")

def validate_departure_time(departure_time):
    """Validate the departure time. This example assumes departure_time is a string in 'HH:MM' 24-hour format."""
    if not re.match("^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$", departure_time):
        raise ValueError("Invalid departure time format. Use 'HH:MM' 24-hour format.")
