from database import Database
from flask import Flask, g, render_template

app = Flask(__name__)

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

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

#TODO : Ajout d'une route pour afficher le formulaire et récuperer les données pour les ajouter dans la base données


#TODO : Ajout d'une route pour afficher toutes les personnes contenues dans la base de données