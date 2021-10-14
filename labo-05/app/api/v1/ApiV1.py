from flask import Blueprint, jsonify, render_template
from .Books.BooksApi import books_api

api_v1 = Blueprint("api_v1", __name__, url_prefix='/api')
api_v1.register_blueprint(books_api)
