import streamlit as st
from services.flight_service import FlightService
from services.booking_service import BookingService

flight_service = FlightService()
booking_service = BookingService()

flight_service.add_flight("FL100", "New York", "London", "2024-01-01 10:00", 200)
flight_service.add_flight("FL101", "Barcelona", "Tbilisi", "2024-02-01 12:00", 175)
flight_service.add_flight("FL102", "Tokyo", "Paris", "2024-02-01 15:00", 150)

def display_bookings():
    st.header("Current Bookings")
    bookings = booking_service.get_all_bookings()
    for booking in bookings:
        st.write(f"Booking ID: {booking.booking_id}, Flight Number: {booking.flight_number}, Passenger Name: {booking.passenger_name}")

def add_flight_ui():
    with st.form("add_flight"):
        flight_number = st.text_input("Flight Number")
        origin = st.text_input("Origin")
        destination = st.text_input("Destination")
        departure_time = st.text_input("Departure Time")
        capacity = st.number_input("Capacity", min_value=1, value=100, step=1)
        submit_button = st.form_submit_button("Add Flight")
        
        if submit_button:
            try:
                flight_service.add_flight(flight_number, origin, destination, departure_time, capacity)
                st.success("Flight added successfully.")
            except ValueError as e:
                st.error(e)

def delete_flight_ui():
    flight_number = st.selectbox("Select Flight Number to Delete", options=[flight.flight_number for flight in flight_service.flights.values()])
    if st.button("Delete Flight"):
        try:
            flight_service.delete_flight(flight_number)
            st.success("Flight deleted successfully.")
        except ValueError as e:
            raise ValueError(e)


def display_flights():
    flights = flight_service.flights.values()
    for flight in flights:
        st.write(f"Flight Number: {flight.flight_number}, Origin: {flight.origin}, Destination: {flight.destination}, Departure: {flight.departure_time}, Capacity: {flight.capacity}, Available Seats: {flight.available_seats()}")

def book_flight_ui():
    with st.form("book_flight"):
        name = st.text_input("Name")
        flight_number = st.selectbox("Flight Number", options=[flight.flight_number for flight in flight_service.flights.values()])
        submit_button = st.form_submit_button("Book Flight")
        
        if submit_button:
            booking_id = "BK" + str(len(booking_service.bookings) + 1)  # Generate a simple booking_id
            booking_service.book_flight(booking_id, flight_number, name)
            st.success(f"Flight booked successfully! Your booking ID is {booking_id}.")

def cancel_booking_ui():
    booking_id = st.text_input("Enter Booking ID to cancel")
    if st.button("Cancel Booking"):
        try:
            booking_service.cancel_booking(booking_id)
            st.success("Booking cancelled successfully.")
        except ValueError as e:
            st.error(e)

def main():
    st.title("Flight Booking System")

    # Display functionalities
    display_flights()
    book_flight_ui()
    display_bookings()
    cancel_booking_ui()
    
    st.header("Flight Management")
    add_flight_ui()
    delete_flight_ui()

if __name__ == "__main__":
    main()
