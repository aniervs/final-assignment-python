import streamlit as st
from datetime import datetime
import random

def main():
    st.title("Flight Booking System")

    if 'orders' not in st.session_state:
        st.session_state.orders = []

    departure_city = st.text_input("Departure City", "")
    destination_city = st.text_input("Destination City", "")


    if departure_city.lower() == destination_city.lower():
        st.error("You cannot fly to the same city! Please select different cities.")
        return

    travel_date = st.date_input("Travel Date")

    if travel_date < datetime.now().date():
        st.error("You lost your flight! Please select a future date.")
        return

    num_passengers = st.number_input("Number of Passengers", min_value=1, value=1)

    airlines = ["American Airlines", "Turkish Airlines", "Vueling", "Singapore Airlines", "Brazil Airlines"]
    selected_airline = st.selectbox("Select Airline", airlines)

    class_options = ["Economy", "Business", "First Class"]
    travel_class = st.selectbox("Select Travel Class", class_options)

    if travel_class.lower() == "economy":
        cost = random.randint(25, 50)
    elif travel_class.lower() == "business":
        cost = random.randint(50, 100)
    elif travel_class.lower() == "first class":
        cost = random.randint(100, 500)

    total_cost = cost * num_passengers

    if st.button("Add to Cart"):
        order_details = {
            "Departure City": departure_city,
            "Destination City": destination_city,
            "Travel Date": travel_date,
            "Number of Passengers": num_passengers,
            "Airline": selected_airline,
            "Travel Class": travel_class,
            "Cost": total_cost
        }
        st.session_state.orders.append(order_details)
        st.success("Order added to the cart!")

    if st.session_state.orders:
        st.subheader("Orders:")
        for i, order in enumerate(st.session_state.orders, start=1):
            st.write(f"Order {i}: {order}")

        order_to_delete = st.selectbox("Select Order to Delete", [f"Order {i}" for i in range(1, len(st.session_state.orders) + 1)], key="delete_order")
        if st.button("Delete Order"):
            order_index = int(order_to_delete.split()[-1]) - 1
            deleted_order = st.session_state.orders.pop(order_index)
            st.warning(f"Deleted Order: {deleted_order}")

if __name__ == "__main__":
    main()