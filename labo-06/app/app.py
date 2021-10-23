from flask import Flask, request, flash, redirect, url_for, render_template
from api.User.UserApi import users_api
from schemas.shared import db
from schemas.User.UserModel import User
import os
import hashlib
import uuid

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = 'secret'

# Configure SQLITE connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(BASE_DIR, 'database/database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

# Register blueprint for the API
app.register_blueprint(users_api)


# Create database if doesnt exist yet
with app.app_context():
    db.create_all()

@app.route('/', methods=["GET"])
def home():
    users = User.query.all()
    return render_template('home.html', users=users)
