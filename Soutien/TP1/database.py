import sqlite3

class Database:

    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection =sqlite3.connect('db/articles.db')
        return self.connection

    def disconnet(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    # TODO
    # methode qui permet d'effectuer une recherche dans la bd pour recuperer les 
    # 5 derniers articles en date du jour
    # Indices : 
    # date_aj = date.today()
    # cursor.execute("select * from article where date_publication <= ? limit 5", (date_aj,))
    