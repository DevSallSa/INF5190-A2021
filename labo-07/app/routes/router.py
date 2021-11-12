from flask import Blueprint, jsonify, request, flash, redirect, url_for, render_template, session, g
import uuid

router = Blueprint("router", __name__)

@router.route('/')
def home():
    if "id" in session:
        print(f"session id is {session['id']}")
    return render_template("home.html")

@router.route('/login')
def login():
    session.permanent = True
    id_session = uuid.uuid4().hex
    session['id'] = id_session

    return redirect(url_for("router.home", login="success"))
