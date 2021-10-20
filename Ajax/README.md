# Solutions

L'enoncé de l'exercice est disponible [ici](./enonce.md)

## Version 1

La version 1 de la solution de l'exercice est disponible [ici](./Version1).

Pour réaliser l'exercice la méthode habituelle a été utilisée; utilisation de simples requetes SQL en créant une connexion manuelle avec la base de données.

## Version 2

La version 2 de la solution de l'exercice est disponible [ici](./Version2).

### Manipulations console Python:
Pour créer la table de la base de données et y ajouter des données :


1. Ouvrir la console Python
2.
```
> from app import db, Person
> db.create_all()
> p = Person(name="Charlotte", sex=2, age=23, country="Canada", birth_town="Montreal")
> db.session.add(p)
> db.session.commit()
> exit()

```

### Manipulations console SQLite3:
1. Pour vérifier que la table a été créé :
```
sqlite3 database.db
> .tables
> .exit
```
2. Pour afficher le contenu de la table : 
```
sqlite3 database.db
> select * from person;
> .exit
```