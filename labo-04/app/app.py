import os
import config
from flask import Flask, render_template, request, redirect, url_for


# Initialise l'application Flask
app = Flask(__name__)

# Default route
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")
