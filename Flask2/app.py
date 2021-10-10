from database import Database
from flask import Flask, g, render_template, request, redirect

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

@app.route('/personnes')
def personnes():
    personnes = get_db().get_all_persons()
    return render_template('personnes.html', personnes=personnes)
    
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', error='')
    else:
        nom = request.form['champ-nom']
        prenom = request.form['champ-prenom']
        age = request.form['champ-age']

        if nom == "" or prenom == "" or age == "" :
            return render_template('home.html', error="Attention ! Tous les champs sont obligatoires !")
        get_db().add_person(nom, prenom, age)
        return redirect('/personnes')