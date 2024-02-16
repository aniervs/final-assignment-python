

import streamlit as st

# Initialize flights and bookings in session state if not already present
if 'flights' not in st.session_state:
    st.session_state.flights = {
        "FN132": {
            "Origin": "France",
            "Destination": "Spain",
            "Departure": "Thursday",
            "Available Seats": 15,
            "Bookings": 0  # Initialize bookings to 0
        }
    }

if 'bookings' not in st.session_state:
    st.session_state.bookings = []

class Flight:
    @staticmethod
    def available_seats(flight_number):
        flight = st.session_state.flights.get(flight_number)
        if flight:
            return flight['Available Seats'] - flight.get('Bookings', 0)
        else:
            return None

    @staticmethod
    def update_flight(flight_number, new_departure_time, new_capacity):
        if flight_number in st.session_state.flights:
            st.session_state.flights[flight_number]['Departure'] = new_departure_time
            st.session_state.flights[flight_number]['Available Seats'] = new_capacity
        else:
            raise ValueError("Flight number not found.")

    @staticmethod
    def add_flight(flight_number, origin, destination, departure, available_seats):
        if flight_number in st.session_state.flights:
            raise ValueError("Flight number already exists.")
        st.session_state.flights[flight_number] = {
            "Origin": origin,
            "Destination": destination,
            "Departure": departure,
            "Available Seats": available_seats,
            "Bookings": 0  # Initialize bookings to 0
        }

    @staticmethod
    def validate_flight_number(flight_number):
        if not flight_number.startswith("FN") or len(flight_number) < 3:
            raise ValueError("Invalid flight number format.")

class Booking:
    @staticmethod
    def book_flight(booking_id, flight_number, passenger_name):
        Flight.validate_flight_number(flight_number)
        if flight_number in st.session_state.flights and Flight.available_seats(flight_number) > 0:
            booking = {
                "Booking ID": booking_id,
                "Flight Number": flight_number,
                "Passenger Name": passenger_name
            }
            st.session_state.bookings.append(booking)
            st.session_state.flights[flight_number]['Bookings'] += 1
        else:
            raise Exception("Flight is full or does not exist.")

    @staticmethod
    def cancel_booking(booking_id):
        for i, booking in enumerate(st.session_state.bookings):
            if booking['Booking ID'] == booking_id:
                st.session_state.bookings.pop(i)
                st.session_state.flights[booking['Flight Number']]['Bookings'] -= 1
                return
        raise ValueError("Booking ID not found.")




def main():
    st.title("Flight Booking System")

    # Display available flights
    if st.button('Show Available Flights'):
        for flight_number, details in st.session_state.flights.items():
            st.write(f"Flight Number: {flight_number}, "
                     f"Origin: {details['Origin']}, "
                     f"Destination: {details['Destination']}, "
                     f"Departure: {details['Departure']}, "
                     f"Available Seats: {Flight.available_seats(flight_number)}")

    # Display my bookings
    st.header("Show My Bookings")
    if st.button('Show My Bookings'):
        if st.session_state.bookings:  # Check if there are any bookings
            for booking in st.session_state.bookings:
                st.write(f"Booking ID: {booking['Booking ID']}, "
                         f"Flight Number: {booking['Flight Number']}, "
                         f"Passenger Name: {booking['Passenger Name']}")
        else:
            st.write("You have no bookings.")

    # Booking section
    st.header("Book a Flight")
    booking_id = st.text_input("Booking ID", "")
    flight_number = st.text_input("Flight Number", "")
    passenger_name = st.text_input("Passenger Name", "")
    if st.button('Book Flight'):
        try:
            Booking.book_flight(booking_id, flight_number, passenger_name)
            st.success("Flight booked successfully.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Cancel booking section
    st.header("Cancel a Booking")
    cancel_booking_id = st.text_input("Booking ID to Cancel", "")
    if st.button('Cancel Booking'):
        try:
            Booking.cancel_booking(cancel_booking_id)
            st.success("Booking cancelled successfully.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Update flight section
    st.header("Update a Flight")
    update_flight_number = st.text_input("Flight Number to Update", "")
    new_departure_time = st.text_input("New Departure Time (YYYY-MM-DD HH:MM)", "")
    new_capacity = st.number_input("New Capacity", min_value=1, value=100, step=1)
    if st.button('Update Flight'):
        try:
            Flight.update_flight(update_flight_number, new_departure_time, new_capacity)
            st.success("Flight updated successfully.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

    # Add flight section
    st.header("Add a New Flight")
    new_flight_number = st.text_input("Flight Number", key="new_flight_number")
    new_origin = st.text_input("Origin", key="new_origin")
    new_destination = st.text_input("Destination", key="new_destination")
    new_departure = st.text_input("Departure Time (e.g., 'YYYY-MM-DD HH:MM')", key="new_departure")
    new_available_seats = st.number_input("Available Seats", min_value=1, value=50, step=1, key="new_available_seats")
    if st.button('Add Flight', key="add_flight_button"):
        try:
            Flight.add_flight(new_flight_number, new_origin, new_destination, new_departure, new_available_seats)
            st.success(f"Flight {new_flight_number} added successfully.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()


