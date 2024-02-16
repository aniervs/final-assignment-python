from models.flight import Flight
from models.booking import Booking
import aiosqlite
import asyncio

import streamlit as st

async def initiateDB():
     """
     function creates DB 
     """
     
     async with aiosqlite.connect('dbs/Flights.db') as conn:
        cursor = await conn.cursor()
        await cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Flights (
                            flight_number TEXT PRIMARY KEY,
                            origin TEXT,
                            destination TEXT,
                            departure_time TEXT,
                            capacity TEXT,
                            bookings TEXT  
                        )
                    ''')
        await conn.commit()
        global flights
        data = await getData()
        flights = [Flight(*flight_data) for flight_data in data]


async def getData():
    """
     returns data saved in DB
     """
    while True:
        try:
            async with aiosqlite.connect('dbs/Flights.db') as conn:
                cursor = await conn.cursor()
                await cursor.execute("SELECT flight_number, origin, destination, departure_time, capacity, bookings FROM Flights")
                rows = await cursor.fetchall()
                return rows
        except:
            await asyncio.sleep(0.5)

async def update_flight(flight:Flight):
    async with aiosqlite.connect("dbs/Flights.db") as db:
        await db.execute(
            """
            UPDATE Flights 
            SET 
                bookings = ? 
            WHERE 
                flight_number = ?
            """,
            (flight.bookings, flight.flight_number)
        )
        await db.commit()


async def addData(flight: Flight):
    """
     Adds data to DB
     """
    while True:
        try:
            async with aiosqlite.connect('dbs/Flights.db') as conn:
                cursor = await conn.cursor()
                await cursor.execute('''INSERT INTO Flights (flight_number, origin, destination, departure_time, capacity, bookings)
                                      VALUES (?, ?, ?, ?, ?, ?)''',
                                     (flight.flight_number, flight.origin, flight.destination, flight.departure_time, flight.capacity, flight.bookings))
                await conn.commit()
                break
        except Exception as error:
            print(error)

async def main():
    await initiateDB()

    global flights 
    st.title("Flight Booking System")
    

    flight_number_input = st.text_input("Flight Number:")
    if st.button("find by flight"):
        for flight in flights:
            if flight.flight_number == flight_number_input:
                st.write(f"Flight Number: {flight.flight_number}")
                st.write(f"Origin: {flight.origin}")
                st.write(f"Destination: {flight.destination}")
                st.write(f"Departure Time: {flight.departure_time}")
                st.write(f"Capacity: {flight.capacity}")
                st.write(f"Bookings: {flight.bookings}")
                if st.button(f"Book Flight {flight.flight_number}"):
                    
                    if flight.bookings < flight.capacity:
                        flight.bookings += 1
                        st.write("Booking successful!")
                    else:
                        st.write("Sorry, this flight is already fully booked.")
                st.write("---")

                
    origin_input = st.text_input("Origin:")
    if st.button("find by origin"):
        for flight in flights:
            if flight.origin == origin_input:
                st.write(f"Flight Number: {flight.flight_number}")
                st.write(f"Origin: {flight.origin}")
                st.write(f"Destination: {flight.destination}")
                st.write(f"Departure Time: {flight.departure_time}")
                st.write(f"Capacity: {flight.capacity}")
                st.write(f"Bookings: {flight.bookings}")
                if st.button(f"Book Flight {flight.flight_number}"):
                    if flight.bookings < flight.capacity:
                        flight.bookings += 1
                        st.write("Booking successful!")
                    else:
                        st.write("Sorry, this flight is already fully booked.")
                st.write("---")

    destination_input = st.text_input("Destination:")
    if st.button("find by destination"):
        for flight in flights:
            if flight.destination == destination_input:
                    st.write(f"Flight Number: {flight.flight_number}")
                    st.write(f"Origin: {flight.origin}")
                    st.write(f"Destination: {flight.destination}")
                    st.write(f"Departure Time: {flight.departure_time}")
                    st.write(f"Capacity: {flight.capacity}")
                    st.write(f"Bookings: {flight.bookings}")
                    if st.button(f"Book Flight {flight.flight_number}"):
                        if flight.bookings < flight.capacity:
                            flight.bookings += 1
                            st.write("Booking successful!")
                        else:
                            st.write("Sorry, this flight is already fully booked.")
                    st.write("---")

    time_input = st.text_input("Time:")
    if st.button("find by departure time"):
        for flight in flights:
            if flight.departure_time == time_input:
                    st.write(f"Flight Number: {flight.flight_number}")
                    st.write(f"Origin: {flight.origin}")
                    st.write(f"Destination: {flight.destination}")
                    st.write(f"Departure Time: {flight.departure_time}")
                    st.write(f"Capacity: {flight.capacity}")
                    st.write(f"Bookings: {flight.bookings}")
                    if st.button(f"Book Flight {flight.flight_number}"):
                        if flight.bookings < flight.capacity:
                            flight.bookings += 1
                        else:
                            st.write("Sorry, this flight is already fully booked.")
                    st.write("---")

    st.write("---")
    st.write("All flights")
    st.write("---")

    for flight in flights:
        st.write(f"Flight Number: {flight.flight_number}")
        st.write(f"Origin: {flight.origin}")
        st.write(f"Destination: {flight.destination}")
        st.write(f"Departure Time: {flight.departure_time}")
        st.write(f"Capacity: {flight.capacity}")
        st.write(f"Bookings: {flight.bookings}")
        if st.button(f"Book Flight {flight.flight_number}"):
            if int(flight.bookings) < int(flight.capacity):
                flight.bookings = str(int(flight.bookings) + 1)
                await update_flight(flight)
                st.write("Booking successful!")
            else:
                st.write("Sorry, this flight is already fully booked.")
        st.write("---")

    


if __name__ == "__main__":
    asyncio.run(main())