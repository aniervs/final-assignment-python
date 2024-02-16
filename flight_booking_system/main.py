import streamlit as st
from flight_booking_system.services.flight_service import get_all_flights
from flight_booking_system.services.booking_service import book_flight, cancel_booking, get_all_bookings

def main():
    st.title("Flight Booking System")
    app_mode = st.sidebar.selectbox("Choose the action", ["Book a Flight", "View My Bookings", "Cancel a Booking"])

    if app_mode == "Book a Flight":
        book_a_flight()
    elif app_mode == "View My Bookings":
        view_my_bookings()
    elif app_mode == "Cancel a Booking":
        cancel_a_booking()

def view_my_bookings():
    my_bookings = get_all_bookings()
    if my_bookings:
        for booking in my_bookings:
            st.write(f"Booking ID: {booking.booking_id}, Booking Code: {booking.booking_code}, "
                     f"Origin: {booking.origin}, Destination: {booking.destination}, "
                     f"Passenger Name: {booking.passenger_name}, Flight Time: {booking.flight_time}, "
                     f"Seats: {', '.join(booking.seats)}")
    else:
        st.write("No bookings available.")

def book_a_flight():
    with st.form("book_flight_form", clear_on_submit=True):
        origin = st.text_input("Origin City")
        destination = st.text_input("Destination City")
        passenger_name = st.text_input("Passenger Name")
        number_of_passengers = st.number_input("Number of Passengers", min_value=1, max_value=180, value=1)  # Adjust max_value based on your plane's capacity
        submit_button = st.form_submit_button("Book Flight")

        if submit_button:
            booking_details = book_flight(origin, destination, passenger_name, number_of_passengers)
            if booking_details:
                st.success(f"Flight booked successfully! Booking Code: {booking_details['booking_code']}, "
                           f"Booking ID: {booking_details['booking_id']}, Flight Time: {booking_details['flight_time']}, "
                           f"Seats: {', '.join(booking_details['seats'])}")
            else:
                st.error("Failed to book the flight. It might be full or not exist.")

def cancel_a_booking():
    booking_id = st.text_input("Booking ID to cancel")
    if st.button("Cancel Booking"):
        if cancel_booking(booking_id):
            st.success("Booking cancelled successfully.")
        else:
            st.error("Failed to cancel booking. It might not exist.")

if __name__ == "__main__":
    main()

