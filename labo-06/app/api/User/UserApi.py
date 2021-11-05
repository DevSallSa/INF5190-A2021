
from flask import Blueprint, jsonify, request, flash, redirect, url_for, Response
from schemas.shared import db
from schemas.User.UserModel import User
from dicttoxml import dicttoxml
import uuid
import hashlib
users_api = Blueprint("users_api", __name__)

@users_api.get('/api/users')
def get_all_users():
    users = User.query.all()
    users2 = dict()
    users2['key1'] = "value1"
    # return Response(dicttoxml(users2, custom_root="users"), mimetype="application/xml")
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
