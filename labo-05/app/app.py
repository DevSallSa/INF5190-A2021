import os
from flask import Flask, render_template, request, redirect, url_for, g, jsonify
from .database.Database import Database
from .api.v1.ApiV1 import api_v1

# DATETIME POUR LE TP1
from datetime import datetime


# Initialise l'application Flask
app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key = "toto"
app.register_blueprint(api_v1)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database

@app.errorhandler(404)
@app.errorhandler(405)
def _handle_api_error(error):
    if request.path.startswith("/api/"):
        return jsonify(error=str(error)), error.code
    else:
        return error

@app.route("/", methods=["GET"])
def home():
    books = get_db().get_books()

    return render_template("home.html", books=books)


if __name__ == "__main__":
    app.run()
