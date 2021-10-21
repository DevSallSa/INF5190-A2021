import re
from database import Database
from datetime import date
# Bcrypt est une extension qui fournit des utilitaires de hachage pour l'application
from flask_bcrypt import Bcrypt
from flask import Flask, g, redirect, render_template, flash, request

app = Flask(__name__)



"""
TODO - Ajout des méthodes de validations :
1. Vérifier si le courriel entré existe déjà dans la base de données.
2. Valider que les champs 'courriel' et 'validation courriel' sont identiques
3. Valider que le mot de passe a le bon format :
    - minimum de 8 caractères;
    - au moins une lettre majuscule et une lettre minuscule;
    - au moins un chiffre;
    - au moins un caractère de ponctuation.
"""


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()

"""
TODO - Ajout de la route principale;
Afficher le formulaire d'inscription;
Récuperation et validation des données
Hachage du mot de passe;
Insertion du user dans la base de données
"""

"""
TODO - Route pour la confirmation en cas de succès
"""




