# Streamlit Flight Booking System

This project is a Streamlit-based web application designed to manage flight bookings. It allows users to view available flights, book flights, view current bookings, and manage (add and delete) flights through a simple and interactive UI.

## Features

- **View Available Flights**: Lists all available flights with details such as flight number, origin, destination, departure time, and available seats.
- **Book Flights**: Users can book flights by providing their name and selecting an available flight.
- **View Current Bookings**: Displays all current flight bookings, including booking ID, flight number, and passenger name.
- **Manage Flights**: Administrators can add new flights or delete existing flights from the system.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.6 or later
- Streamlit

You can install Streamlit using pip:

```bash
pip install streamlit
```

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/datamucho/flight-booking-system.git
cd flight-booking-system
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, navigate to the project directory and use the following command:

```bash
streamlit run main.py
```

The command will start the Streamlit server, and you should be able to access the application by navigating to `http://localhost:8501` in your web browser.

## Usage

- Upon launching the app, you will see a list of available flights.
- To book a flight, fill in your name in the "Book a Flight" section and select an available flight from the dropdown menu. Click "Book Flight" to confirm.
- To view current bookings, simply scroll to the "Current Bookings" section.
- Administrators can add a new flight by filling in the flight details in the "Flight Management" section and clicking "Add Flight". Similarly, flights can be deleted by selecting a flight number and clicking "Delete Flight".

## Development

This project is developed using Python and Streamlit. The backend logic for managing flights and bookings is contained within the `services` directory. The Streamlit UI is defined in `main.py`.

## Contributing

Contributions to the Flight Booking System are welcome. Please follow the standard fork-and-pull request workflow on GitHub to submit your contributions.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
