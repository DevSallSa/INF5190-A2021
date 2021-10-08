import sqlite3
from person import Person


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

    #TODO : Une methode qui permet de récuperer les personnes dans la base de données - les personnes sont triés par ordre alphabetique de noms de familles

    #TODO : Une methode qui permet d'ajouter une personne à la base de données