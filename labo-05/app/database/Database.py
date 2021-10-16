import sqlite3

class Database:
    def __init__(self):
        self.connection = None

    # Return cursor as a dict
    def to_dict(self, dict_name, cursor):
        return [dict(dict_name) for dict_name in cursor.fetchall()]

    def get_connection(self):
        """Open database connection. Should be closed after use"""
        if self.connection is None:
            self.connection = sqlite3.connect('app/database/database.db')
            self.connection.row_factory = sqlite3.Row
        return self.connection

    def disconnect(self):
        """Closes the database connection"""
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_books(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT id, title, created_at FROM books ORDER BY title ASC")
        return self.to_dict("books", cursor)

    def get_book_by_id(self, id):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM books WHERE id = ?", [id])
        return self.to_dict("book", cursor)
