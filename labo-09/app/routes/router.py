from flask import Blueprint, jsonify, request, flash, redirect, url_for, render_template, session, g
from utils.authentication import authentication_required
from shared import mail
import uuid

router = Blueprint("router", __name__)

@router.route('/')
def home():
    if "profile" in session:
        return render_template("home.html", profile=session['profile'])
    return render_template("home.html")


@router.route('/activation/<token>')
def activer_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('Invalid token')
    # user = db.query.user.filter_by(email)
    if user.confirmed:
        flash("Account was already confirmed")
        return redirect(url_for('home'))
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash('Account validated')
    return redirect(url_for('home'))

