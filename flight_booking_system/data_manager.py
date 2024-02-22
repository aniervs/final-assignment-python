import pandas as pd
import booking as bk
import flight as fl

#clears the files but makes headers
def reset_flights_csv():
    df = pd.DataFrame(columns=["flight_number", "departure_city", "destination_city",
                                     "departure_date", "capacity", "bookings"])
    df.to_csv('flights.csv', index=False)

def reset_bookings_csv():
    df = pd.DataFrame(columns=["flight_number", "departure_city", "destination_city",
                                     "departure_date", "passport"])
    df.to_csv('bookings.csv', index=False)


#returns a list of Flight objs
def read_flights_from_csv():
    df = pd.read_csv("flights.csv")
    flights = []

    for index, row in df.iterrows():
        vals = row.values
        flights.append(fl.Flight(*vals))
    return flights


#gets a Flight obj
def add_flight_to_csv(flight: fl.Flight):
    df = pd.DataFrame(columns=["flight_number", "departure_city", "destination_city",
                                     "departure_date", "capacity", "bookings"])
    
    new_row = {"flight_number":flight.flight_number,
               "departure_city":flight.departure_city,
               "destination_city":flight.destination_city,
               "departure_date":flight.departure_date,
               "capacity":flight.capacity,
               "bookings":flight.bookings}
    
    new_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv("flights.csv", mode='a', header=False, index=False)


#returns a list of Booking objs
def read_bookings_from_csv():

    df = pd.read_csv("bookings.csv")
    bookings = []

    for index, row in df.iterrows():
        vals = row.values
        bookings.append(bk.Booking(*vals))
    return bookings


#gets a Booking obj
def add_booking_to_csv(booking: bk.Booking):
    df = pd.DataFrame(columns=["flight_number", "departure_city", "destination_city",
                                     "date", "passport"])
    
    new_row = {"flight_number":booking.flight_number,
               "departure_city":booking.departure_city,
               "destination_city":booking.destination_city,
               "date":booking.date,
               "passport":booking.passport}
    
    
    new_df = pd.DataFrame([new_row])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv("bookings.csv", mode='a', header=False, index=False)