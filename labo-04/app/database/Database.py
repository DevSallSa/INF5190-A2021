import sqlite3


"""
Définir une classe pour la base de donnée. Vous aurez besoin de :
- Un constructeur
- Une fonction initialisant la connection à la BD.
- Une fonction pour terminer la connection à la BD.
- BONUS: Une fonction qui map le résultat de query SQL a un dictionnaire python.
"""

class Database:
    def __init__(self):
        self.connection = None

    # Return cursor as a dict
    def to_dict(self, dict_name, cursor):
        return [dict(dict_name) for dict_name in cursor.fetchall()]

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('database/database.db')
            self.connection.row_factory = sqlite3.Row
        return self.connection

    # TODO: Disconnect from the database
    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_individual_by_lastname(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM individual ORDER BY lastname ASC")
        return self.to_dict("individual", cursor)

    def insert_individual(self, individual):
        connection = self.get_connection()
        cursor = connection.cursor()

        cursor.execute("INSERT INTO individual(lastname, firstname, age) values (?, ?, ?)", [individual['lastname'], individual['firstname'], individual['age']])
        connection.commit()
        return 1
