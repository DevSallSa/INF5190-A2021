# Solutnions 

L'enonce de l'exercice se trouve [ici](./enonce.md)

## Version 1
La version 1 du solutionnaire de l'exercice est disponible [ici](./Version1).

Pour réaliser l'exercice la méthode habituelle a été utilisée; utilisation de simples requetes SQL en créant une connexion manuelle avec la base de données.

Deux nouvelles librairies sont utilisées : `flask_bcrypt` er `secret`.

`Bcrypt` est une extension qui fournit des utilitaires de hachage pour l'application.

`secret` permet de generer une chaine de caractères aléatoire, cette dernière sera utilisée comme `secret_key` pour l'application.


## Version 2

La version 2 du solutionnaire de l'exercice est disponible [ici](./Version2).

Pour créer la base de données, on commence par ouvrir la console `python` :

````
> from app import db, User
> db.create_all()
````

Les librairies utilisées dans cette version sont :

- `flask_sqlalchemy` :SQLALchemy est un mappeur objet-relationnel qui offre aux développeurs d'applications toute la puissance et la flexibilité de SQL.<br/>
Il est conçus pour un accès efficace et performant aux bases de données, adaptés dans un langage de domaine simple en python.
- `wtforms` : WTForms est une bibliothèque flexible de validation et de rendu de formulaires pour le développement web en Python.


Des documentations utiles ont été ajoutées (ici)[./https://github.com/elaelheni/INF5190-A2021/blob/Corrections-Ela/README.md]


