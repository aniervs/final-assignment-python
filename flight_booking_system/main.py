import streamlit as st
from datetime import date

import booking_service
import flight_service
import custom_exceptions as ce
import data_manager as dm
import flight as fl
import time

european_capitals = [
    "Amsterdam", "Athens", "Belgrade", "Berlin", "Bern", "Bratislava", "Brussels",
    "Bucharest", "Budapest", "Copenhagen", "Dublin", "Helsinki", "Lisbon", "Ljubljana",
    "London", "Luxembourg", "Madrid", "Oslo", "Paris", "Podgorica", "Prague", "Riga",
    "Rome", "Sarajevo", "Skopje", "Sofia", "Stockholm", "Tallinn", "Tirana", "Vienna",
    "Vilnius", "Warsaw", "Zagreb"
]


#! issues
#? destination date: str and datetime obj (SOLVED)
# booking counts: call update func
# implement functionality for deleting and updating flights
# implement booking and cancelling
# not all errors implemented

# Function to display user page
def user_page():
    st.title("Flight Booking System")

    with st.form("flight_details"):
        st.write("Enter your flight details:")
        departure_city = st.selectbox("Departure City", european_capitals)
        destination_city = st.selectbox("Destination City", european_capitals)
        departure_date = st.date_input("Departure Date", min_value=date.today()).strftime("%Y-%m-%d")
        passport = st.text_input("Passport number")
        search_button = st.form_submit_button("Search Flights")

    if search_button:

        try:

            if departure_city == None or destination_city == None or departure_date == None or passport == None:
                raise ce.IncompleteFormError
            if departure_city == destination_city:
                raise ce.SameCitiesError

            # Filter flights based on selected criteria
            filtered_flights = flight_service.search_flights(departure_city, destination_city, departure_date)
            if filtered_flights == []:
                raise ce.NoFlightsError
            st.write("Available Flights:")
            for flight in filtered_flights:
                st.write(f"Flight number: {flight.flight_number}")
                st.write(f"Departure City: {flight.departure_city}")
                st.write(f"Destination City: {flight.destination_city}")
                st.write(f"Departure Date: {flight.departure_date}")
                st.write(f"Available Seats: {flight.available_seats()}")
                st.write("---")

            with st.form("book-flight"):
                flight_to_book = st.text_input("Enter the number of flight you want to book:")
                book_button = st.form_submit_button("Book!")
                if book_button:
                    chosen_flight = flight_service.fetch_flight_by_number(flight_to_book)
                    if chosen_flight.available_seats() == 0:
                        raise ce.FlightFullException
                    booking_service.book_flight(chosen_flight)
                    st.success("The flights was succesfully booked!")   
                    time.sleep(5)


        except Exception as e:
            st.error(str(e))
    st.header("Current Bookings")
    bookings = dm.read_bookings_from_csv()
    if bookings:
        st.write("Here are your current bookings:")
        for booking in bookings:
            st.write(f"Departure City: {booking['departure_city']}")
            st.write(f"Destination City: {booking['destination_city']}")
            st.write(f"Departure Date: {booking['departure_date']}")
            st.write(f"Passengers: {booking['passengers']}")
            st.write("---")
    else:
        st.error("You have no current bookings.")



def admin_page():
    st.title("Admin Page - Flight Management")

    password = st.text_input("Enter Admin Password", type="password")
    if password == "1111":
        action = st.radio("Select Action", ["Add Flight", "Update Flight", "Delete Flight"])
        if action == "Add Flight":
            with st.form("flight_details"):
                st.write("Enter flight details:")
                flight_number = st.text_input("Flight number")
                origin = st.selectbox("Departure City", european_capitals)
                destination = st.selectbox("Destination City", european_capitals)
                departure_date = st.date_input("Departure Date", min_value=date.today()).strftime("%Y-%m-%d")
                capacity = st.number_input("Number of seats",min_value=1, step=1)
                add_button = st.form_submit_button("Add")

                if add_button:
                    flight_service.add_flight(flight_number, origin, destination, departure_date, capacity)
                    st.success("The flight is successfully added!")


        elif action == "Update Flight":
            # Update flight functionality
            pass


        elif action == "Delete Flight":
            # Delete flight functionality
            pass


        
        reset_flights = st.button("Delete all existing flights")
        if reset_flights:
            dm.reset_flights_csv()
            st.success("All flights were succesfully deleted.")

        reset_bookings = st.button("Delete all existing bookings")
        if reset_bookings:
            dm.reset_bookings_csv()
            st.success("All bookings were succesfully deleted.")
    elif password != '':
        st.error("Incorrect Password")


# Main function to display the user page
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["User Page", "Admin Page"])

    if page == "User Page":
        user_page()
    elif page == "Admin Page":
        admin_page()

if __name__ == "__main__":
    main()
