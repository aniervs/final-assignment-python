import uuid
import random
import string
from datetime import datetime, timedelta
import json 
from ..models.booking import Booking

BOOKINGS_FILE_PATH = 'flight_booking_system/bookings_data.JSON'  

def load_bookings_from_file():
    try:
        with open(BOOKINGS_FILE_PATH, 'r') as file:
            file_content = file.read()
            if file_content:
                loaded_bookings = json.loads(file_content)
                return {k: Booking(**v) for k, v in loaded_bookings.items()}
            else:
                return {}  
    except FileNotFoundError:
        return {}  


def save_bookings_to_file(bookings):
    with open(BOOKINGS_FILE_PATH, 'w') as file:
        json.dump({k: v.__dict__ for k, v in bookings.items()}, file, indent=4)

bookings = load_bookings_from_file()

def get_all_bookings():
    return list(bookings.values())

def generate_booking_id():
    return ''.join(random.choices(string.digits, k=5))

def generate_booking_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def assign_seats(number_of_passengers):
    seats = []
    rows = range(1, 31)
    columns = 'ABCDEF'
    for _ in range(number_of_passengers):
        seat = f'{random.choice(rows)}{random.choice(columns)}'
        seats.append(seat)
    return seats

def book_flight(origin, destination, passenger_name, number_of_passengers):
    booking_id = generate_booking_id()
    booking_code = generate_booking_code()
    flight_time = datetime.now() + timedelta(days=random.randint(1, 30), hours=random.randint(0, 23))
    seats = assign_seats(number_of_passengers)
    booking = Booking(booking_id=booking_id, origin=origin, destination=destination, 
                      passenger_name=passenger_name, flight_time=flight_time.strftime("%Y-%m-%d %H:%M"), 
                      seats=seats, booking_code=booking_code)
    
    bookings[booking_id] = booking
    save_bookings_to_file(bookings) 

    return {
        "booking_id": booking_id,
        "booking_code": booking_code,
        "flight_time": flight_time.strftime("%Y-%m-%d %H:%M"),
        "seats": seats
    }

def cancel_booking(booking_id):
    if booking_id in bookings:
        del bookings[booking_id]
        save_bookings_to_file(bookings)  
        return True
    return False
