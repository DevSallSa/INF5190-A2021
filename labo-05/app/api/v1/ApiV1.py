from flask import Blueprint, jsonify, render_template
from .Books.BooksApi import books_api
from .Users.UsersApi import users_api

api_v1 = Blueprint("api_v1", __name__, url_prefix='/api/v1')
api_v1.register_blueprint(books_api)
api_v1.register_blueprint(users_api)
