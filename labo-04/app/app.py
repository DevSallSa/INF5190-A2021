import os
import config
from flask import Flask, render_template, request, redirect, url_for


# Initialise l'application Flask
app = Flask(__name__)

# TODO: Afficher la liste de personne dans un tableau
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


# TODO: Route affichant un formulaire avec les champs nécessaires pour créer une personne;

# TODO: Route POST afin d'ajouter une nouvelle personne à la base de données



