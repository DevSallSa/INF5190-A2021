from database import Database
from flask import Flask, g, render_template, request, Response

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

@app.route('/')
def home():
    get_db().add_person("Charlotte", 2, 23, "Montéal")
    get_db().add_person("James", 1 , 50, "Bruxelles")
    get_db().add_person("Bob", 9, 28, "Paris")

    persons = get_db().get_all_persons()
    return render_template("home.html", persons=persons)

@app.route('/get-info/<int:id>')
def get_info(id):
    p = get_db().get_person_by_id(id)
    if p is None:
        return Response(status=404)
    return render_template ("infos.html", p=p[0])