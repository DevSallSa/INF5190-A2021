import os
from flask import Flask, render_template, request, redirect, url_for, g, flash
from flask_bootstrap import Bootstrap
from .database.Database import Database
from app.individual.Individual import Individual

# DATETIME POUR LE TP1
from datetime import datetime


# Initialise l'application Flask
app = Flask(__name__, static_folder="static", template_folder="views", static_url_path="/toto")
app.secret_key = "toto"
Bootstrap(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


# TODO: Afficher la liste de personne dans un tableau
@app.route("/", methods=["GET"])
def home():

    # DATETIME UTILS
    today = datetime.now().strftime("%Y-%m-%d")

    individuals = get_db().get_individual_by_lastname()
    return render_template("home.html", individuals=individuals)


# TODO: Route affichant un formulaire avec les champs nécessaires pour créer une personne;
@app.route("/personne", methods=["POST"])
def create_invidivual():
    error = False
    errors = dict()
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    age = request.form['age']

    if firstname == "":
        errors['firstname'] = "Le champ prénom n'est pas rempli"
        error = True


    if error is True:
        individuals = get_db().get_individual_by_lastname()
        return render_template('home.html', firstname=firstname, lastname=lastname, age=age, errors=errors, individuals=individuals)
    individual = Individual(firstname, lastname, age)
    get_db().insert_individual(individual.to_dict())

    return redirect(url_for("home"))


