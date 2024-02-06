import sqlite3
from flight_booking_system.config import DATABASE_PATH

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_PATH)

    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        return cursor
