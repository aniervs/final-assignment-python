import streamlit as st
from flight_service import add_flight
from services.booking_service import book_flight,cancel_booking
from countires import country
curr={}
def main():
    k=[]
    st.title("Flight Booking System")
    user_input = st.text_input("number of flight that you want for booking")
    st.title(""" #choose one of the options : """)
    key1=st.button("booking a flight") 
    key2=st.button("cancel a booked flight")
    key3=st.button("add a new flight ")
    key4=st.button("delet a flight ")
    if (key3):
        with st.form(key='my_form'):
            flight_number = st.number_input("flight_number : ",min_value=1, max_value=100000)
            origin = st.selectbox("origin :", options=[i for i in country.countries])
            destination = st.number_input("destination : ", min_value=10, max_value=10000)
            departure_time= st.number_input("departure_time (min): ",min_value=10, max_value=5000)
            capacity=st.number_input("capacity : " , min_value=5, max_value=1000)
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                curr=add_flight(flight_number,origin,destination,departure_time,capacity,curr)
                print(curr.keys())
    elif(key1):
            with st.form(key='my_form'):
                flight_number = st.selectbox("flight_number from (availbe_Flights): ",options=[i for i in curr.keys()])
                booking_id = st.text_input("booking_id :")
                passenger_name = st.text_input("passenger_name :")
                submit_button = st.form_submit_button(label='Submit')
                if submit_button:
                    book_flight(booking_id, flight_number, passenger_name)
    st.write("""*Avaible Flights : *""")
    for i in curr.keys():
        k.append(st.button("Flight Number : "+str(curr[i])))  
if __name__ == "__main__":
     main()