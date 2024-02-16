import sys
sys.path.append('/Users/zainellahi/final-assignment-python')

import streamlit as st
from flight_booking_system.services.flight_service import add_flight, update_flight, flights
from flight_booking_system.models.flight import Flight  
from flight_booking_system.services.booking_service import cancel_booking,book_flight

def main():
    st.title("Flight Booking System")

    option = st.sidebar.selectbox("Select an action", ["View Flights", "Add Flight", "Update Flight", "Book Flight", "Cancel Booking"])

    if option == "View Flights":
        st.subheader("View Flights")
        if not flights:
            st.write("No flights available.")
        else:
            for flight in flights:
                st.write(f"Flight Number: {flight.flight_number}, Capacity: {flight.capacity}")

    elif option == "Add Flight":
        st.subheader("Add Flight")
        flight_number = st.text_input("Flight Number")
        origin = st.text_input("Origin")
        destination = st.text_input("Destination")
        departure_time = st.text_input("Departure Time")
        capacity = st.number_input("Capacity", min_value=1)

        if st.button("Add Flight"):
            new_flight = add_flight(flight_number, origin, destination, departure_time, capacity)
            st.success(f"Flight added: {new_flight.flight_number}")

    elif option == "Update Flight":
        st.subheader("Update Flight")
        flight_number = st.text_input("Enter Flight Number to update")

        if st.button("Update Flight"):
            new_capacity = st.number_input("New Capacity", min_value=1)
            updated_flight = update_flight(flight_number, new_capacity)

            if updated_flight:
                st.success(f"Flight updated: {updated_flight.flight_number}, New Capacity: {updated_flight.capacity}")
            else:
                st.warning(f"Flight with number {flight_number} not found.")

    elif option == "Book a Flight":
        st.subheader("Book a Flight")
        booking_id = st.text_input("Booking ID")
        flight_number = st.text_input("Flight Number")
        passenger_name = st.text_input("Passenger Name")

        if st.button("Book Flight"):
            try:
                booked_flight = book_flight(booking_id, flight_number, passenger_name)
                st.success(f"Booking successful. Passenger: {passenger_name}, Flight: {booked_flight.flight_number}")
            except Exception as e:
                st.error(f"Error: {str(e)}")

    elif option == "Cancel Booking":
        st.subheader("Cancel Booking")
        booking_id = st.text_input("Booking ID")

        if st.button("Cancel Booking"):
            try:
                if cancel_booking(booking_id):
                    st.success(f"Booking with ID {booking_id} canceled .")
                else:
                    st.warning(f"Booking with ID {booking_id} not found.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()