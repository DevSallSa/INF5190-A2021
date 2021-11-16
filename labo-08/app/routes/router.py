from flask import Blueprint, jsonify, request, flash, redirect, url_for, render_template, session, g
from utils.authentication import authentication_required
import uuid

router = Blueprint("router", __name__)

@router.route('/')
def home():
    if "profile" in session:
        return render_template("home.html", profile=session['profile'])
    return render_template("home.html")
