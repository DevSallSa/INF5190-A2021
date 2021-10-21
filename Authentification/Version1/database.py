import sqlite3


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/database.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    """
    TODO - Insertion d'un utilisateur dans la base de données
    """


    """
    TODO - Verifier si un utilisateur existe dans la bd à partir de son courriel
    """

    
    
