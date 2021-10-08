# Importer sqlite3
import sqlite3

# Établir une connexion avec la base de données
connection = sqlite3.connect('database.db')

# Définir curseur sql
cursor = connection.cursor()

"""Implémenter une fonction qui permet de lire le fichier
et insérer les données dans la BD"""
def write_album():
    try:
        with open('input.txt', 'r') as file:
            # TODO: read file
            for line in file:
                artist, album, year = line.strip('\n').split('|')
                cursor.execute(
                    "SELECT * FROM artiste WHERE nom LIKE ?", ('%'+artist+'%',))

                exist = cursor.fetchall()
                if exist:
                    artist_id = exist[0][0]
                    cursor.execute(
                        ("INSERT INTO ALBUM(titre, annee, artiste_id)" "values(?,?,?)"), (artist, year, artist_id))

                    connection.commit()

                else:
                    # TODO: creer un nouvel artiste avec des valeurs bidon
                    print("TODO")

                    # Utiliser curseur pour inserer un nouvel artiste
                    """
                    Utiliser curseur pour créer un album avec l'id de l'artiste précédemment créé.
                    """
            file.close()

    except:
        print("Problème lors de la lecture du fichier")


write_album()
connection.close()
