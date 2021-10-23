
from flask import Blueprint, jsonify, request, flash, redirect, url_for
from schemas.shared import db
from schemas.User.UserModel import User
import uuid
import hashlib
users_api = Blueprint("users_api", __name__)

@users_api.get('/api/users')
def get_all_users():
    users = User.query.all()
    return jsonify(users)

@users_api.route('/api/users/create', methods=["POST"])
def create_user():
    password = request.form['password']
    username = request.form['username']
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(str(password + salt).encode('utf-8')).hexdigest()

    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Vous avez créer un user !', 'success')
    return redirect(url_for('home'))
