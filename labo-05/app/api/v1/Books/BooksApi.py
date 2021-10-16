from flask import Blueprint, jsonify, g
from app.database.Database import Database

books_api = Blueprint("books_api", __name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database

@books_api.route("/books")
def get_all_books():
    return { "message": "List of books as JSON"}, 200

@books_api.route("/book/<int:id>")
def get_book_by_id(id):
    book = get_db().get_book_by_id(id)

    return jsonify(book[0]), 200
