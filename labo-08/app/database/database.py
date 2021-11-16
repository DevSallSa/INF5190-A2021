import sqlite3
from base64 import b64decode

# Class that handle database connection and query with sqlite3
class Database:
    def __init__(self):
        self.connection = None

    # Return cursor as a dict
    def to_dict(self, dict_name, cursor):
        return [dict(dict_name) for dict_name in cursor.fetchall()]

    # Connect to the database
    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('database/database.db')
            self.connection.row_factory = sqlite3.Row
        return self.connection

    # Disconnect
    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
