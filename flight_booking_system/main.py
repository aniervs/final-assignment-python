import streamlit as st
from models.booking import Booking
from models.flight import Flight

def main():
    st.title("Flight Booking System")

    flights = {
        "Flight 1": Flight('1', 'Barcelona', 'Madrid', '12:00', 50, 10),
        "Flight 2": Flight('2', 'Moscow', 'St.Petersburg', '9:00', 100, 30),
        "Flight 3": Flight('3', 'Dubai', 'Istanbul', '20:00', 180, 180)
    }
    name = st.text_input("Enter your name:")

    selected_flight = st.selectbox("Select a flight:", flights)

    st.write("### Flight Details:")
    st.write(f"From: {flights[selected_flight].origin} to {flights[selected_flight].destination}")
    st.write(f"Departure Time: {flights[selected_flight].departure_time}")
    st.write(f"Seats Available: {flights[selected_flight].capacity - flights[selected_flight].bookings}")
    st.write(f"Booked Seats: {flights[selected_flight].bookings}")

    if st.button("Book a Seat"):
        if flights[selected_flight].capacity - flights[selected_flight].bookings > 0  :
            flights[selected_flight].bookings -= 1
            st.success("Seat booked successfully!")
        else:
            st.warning("No available seats for booking.")

if __name__ == "__main__":
    main()
