import sqlite3

class Database:
    # Definir le constructeur de la classe
    def __init__(self):
        self.connection = None

    # Definir une connexion avec la base de données
    # Dans notre cas c'est la base de données créée à partir du script sql donné
    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/musique.db')
        return self.connection

    # Deconnexion de la base de données
    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_all_artistes(self):
        # On commence par defenir un curseur pour etablir la connextion
        # avec la base de données et effectuer les requettes necessaires
        cursor = self.get_connection().cursor()
        # On execute la requete de recherche
        cursor.execute("select * from artiste")
        # On range toutes les données dans des variables
        for row in cursor:
            identifier, nom, est_solo, combien = row
            # On affiche le résultat à la console
            print("Artiste n: %d Nom : %s\n" %(identifier,nom))

    def get_artiste(self, id):
        cursor = self.get_connection().cursor()
        # WHERE permet de selectionner l'album de l'artiste avec l'id donné
        cursor.execute("select titre, annee from album where artiste_id=%d" %id)
        for row in cursor:
            # On range le titre et l'année récupérés dans des variables
            titre,annee = row
            # On affiche le résultat à la console
            print ("%s %d\n" %(titre, annee))

    def insert_album(self, nom_artiste, nom_album, annee_publication):
        # On sépare la connexion et le curseur
        # Le connexion servira a commité les changement dans la base de données 
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute("select * from artiste where nom like ?", ('%'+nom_artiste+'%',))
        # On fetch les artistes qui matchent (si ils existent)
        existe =cursor.fetchall()
        if existe:
            # On récupere l'id
            artiste_id = cursor.fetchone()
            # On update les donnees de l'artiste correspondant a artiste_id en ajoutant le nouvel album à la table album
            cursor.execute(("insert into album(titre,annee,artiste_id)" "values(?,?,?)"),(nom_album, annee_publication, artiste_id))
            # On commmit les changements
            connection.commit()
        else:
            # On insère le nouvel artiste dans la table artiste
            cursor.execute(("insert into artiste(nom, est_solo, nombre_individus)" "values(?,?,?)"), (nom_artiste,0,1))
            # On récupere l'id du dernier artiste ajouté
            cursor.execute("select last_insert_rowid()")
            last_id = cursor.fetchone()[0]
            connection.commit()
            # A partir de l'id du dernier artiste ajouté on ajoute son album a la table album
            cursor.execute(("insert into album(titre,annee,artiste_id)" "values(?,?,?)"),(nom_artiste, annee_publication, last_id))
            connection.commit()

