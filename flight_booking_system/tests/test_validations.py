import unittest
from flight_booking_system.utils.validator import validate_passenger_name, validate_capacity, validate_departure_time

class TestValidations(unittest.TestCase):
    def test_validate_passenger_name(self):
        valid_names = ["John Doe", "Alice", "Mary Ann"]
        for name in valid_names:
            self.assertIsNone(validate_passenger_name(name))
        
        invalid_names = ["", "123", "John@Doe", "John_Doe", "John-Doe"]
        for name in invalid_names:
            with self.assertRaises(ValueError):
                validate_passenger_name(name)

    def test_validate_capacity(self):
        valid_capacities = [1, 10, 100, 1000]
        for capacity in valid_capacities:
            self.assertIsNone(validate_capacity(capacity))

        invalid_capacities = [0, -1, "10", 10.5, None]
        for capacity in invalid_capacities:
            with self.assertRaises(ValueError):
                validate_capacity(capacity)

    def test_validate_departure_time(self):
        valid_times = ["12:00", "00:00", "23:59", "09:30"]
        for time in valid_times:
            self.assertIsNone(validate_departure_time(time))

        invalid_times = ["", "12:60", "24:00", "12:61", "abc", "12:00 PM"]
        for time in invalid_times:
            with self.assertRaises(ValueError):
                validate_departure_time(time)

if __name__ == "__main__":
    unittest.main()
