import sqlite3


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/person.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_all_persons(self):
        cursor = self.get_connection().cursor()
        cursor.execute("SELECT lastname, firstname, age FROM person ORDER BY lastname")
        persons = cursor.fetchall()
        return persons

    def add_person(self, nom, prenom, age):
        connection = self.get_connection()
        connection.execute("INSERT INTO person(lastname, firstname, age) " "VALUES(?, ?, ?)", (nom, prenom, age))
        connection.commit()