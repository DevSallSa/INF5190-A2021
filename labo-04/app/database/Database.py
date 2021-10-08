# TODO: Importer SQLite 3

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

    # TODO: Connect to the database
    def get_connection(self):

    # TODO: Disconnect from the database
    def disconnect(self):

    # TODO: Get all (order by lastname)
    def get_individual_by_lastname(self):

    # TODO: Insert person
    def insert_individual(self, individual):

