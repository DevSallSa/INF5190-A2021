import re
from database import Database
from datetime import date
# Bcrypt est une extension qui fournit des utilitaires de hachage pour l'application
from flask_bcrypt import Bcrypt
from flask import Flask, g, redirect, render_template, flash, request

app = Flask(__name__)


#Generé avec : import secrets, secrets.token_hex(16)
app.config['SECRET_KEY'] = "269cfb2a4f0246b006b4640b11152f21"
bcrypt = Bcrypt(app)

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
TODO - Ajout des méthodes de validations :
1. Vérifier si le courriel entré existe déjà dans la base de données.
2. Valider que les champs 'courriel' et 'validation courriel' sont identiques
3. Valider que le mot de passe a le bon format :
    - minimum de 8 caractères;
    - au moins une lettre majuscule et une lettre minuscule;
    - au moins un chiffre;
    - au moins un caractère de ponctuation.
"""
def validate_courriel(courriel, validation_courriel):
    return courriel == validation_courriel

def courriel_existe (courriel):
    return get_db().mail_exists(courriel)

regex = r'[A-Za-z0-9@#$%+=]{8,}'
match_mdp = re.compile(regex).match

def validate_mdp(str):
    try:
        if match_mdp(str) is not None:
            return True
    except:
        pass
    return False

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        nom = request.form["nom"]
        courriel = request.form["courriel"]
        validation_courriel = request.form["validation-courriel"]
        mdp = request.form["mdp"]

        if nom == "" or courriel == "" or validation_courriel == "" or mdp == "":
            flash("ERREUR! Tous les champs sont obligatoires.", "error")
            return render_template('home.html')
        if validate_courriel(courriel, validation_courriel) is False:
            return render_template('home.html', mail_error="Attention les deux adresses courriel sont différentes!")
        if courriel_existe(courriel):
            return render_template('home.html', mail_error="L'adresse courriel existe déjà")
        if validate_mdp(mdp) is False:
            return render_template("home.html", mdp_error="Le mot de passe n'a pas le bon format")
        
        hashed_password = bcrypt.generate_password_hash(mdp).decode('utf-8')
        date_inscription = date.today()
        get_db().insert_user(nom, courriel, date_inscription, hashed_password)
        flash("Felicitations vous etes maintenant inscrit!", "success")
        return redirect('/confirmation')


@app.route('/confirmation')
def confirnation():
    return render_template('confirmation.html')






