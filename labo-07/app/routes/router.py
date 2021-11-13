from flask import Blueprint, jsonify, request, flash, redirect, url_for, render_template, session, g
from utils.authentication import authentication_required
import uuid

router = Blueprint("router", __name__)

@router.route('/')
def home():
    if "profile" in session:
        print(f"session profile is {session['profile']}")
        return render_template("home.html", profile=session['profile'])
    return render_template("home.html"r)


@router.route('/page1')
@authentication_required
def page1():
    return render_template("formulaire1.html")

@router.route('/page2')
@authentication_required
def page2():
    if session['step'] > 1:
        return render_template("formulaire2.html", profile=session['profile'])
    return "Unauthorized", 401

@router.route("/complete_page1", methods=["POST"])
def complete_page1():
    data = request.form['phone']
    print(data)
    print(session['profile'])
    session['profile']['phone'] = data
    session['step'] = 2
    return redirect(url_for("router.page2"))

@router.route("/complete_page2", methods=["POST"])
def complete_page2():
    data = request.form['addresse']
    session['profile']['addresse'] = data
    session['step'] = 3
    return redirect(url_for("router.home"))

@router.route('/login')
def login():
    session.permanent = True
    id_session = uuid.uuid4().hex
    session['id'] = id_session

    return redirect(url_for("router.home", login="success"))


# Helper to parse XML
def create_data():
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
    except Exception as e:
        print("Failed to parse xml from response (%s)" %
              traceback.format_exc())
    return data
