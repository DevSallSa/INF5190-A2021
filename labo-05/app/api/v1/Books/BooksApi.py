from flask import Blueprint, jsonify

books_api = Blueprint("books_api", __name__)

@books_api.route("/books")
def get_all_books():
    return { "message": "List of books as JSON"}, 200

@books_api.route("/book/<int:id>")
def get_book_by_id(id):
    return { "message": f"The book with ID {id} as JSON"}, 200
