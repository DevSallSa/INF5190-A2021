from database import Database
from flask import Flask, g

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

# TODO
#@app.route('/')
#def home()
#afficher toutes les données sur les articles récupérés à partir de la bd 
