# Importer sqlite3
import sqlite3

# Établir une connexion avec la base de données
connection = sqlite3.connect('database.db')

# Établir curseur sql
cursor = connection.cursor()

cursor.execute("select * from artiste")
for row in cursor:
    identifier, name, solo, nb_individus = row
    print(
        f"Ariste n: {identifier}, Nom: {name}, Est solo?: {solo}, Nombre individus: {nb_individus}")


print("Choissisez un ariste en entrant son identifiant")

cursor.execute("SELECT titre, annee FROM album WHERE artiste_id=%d" % choix)
for row in cursor:
    title, year = row
    print(f"Titre: {title}, année de l'album: {year}")


connection.close()
