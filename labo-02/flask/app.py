from flask import Flask, render_template, request, redirect, url_for

# Initialise l'application Flask
app = Flask(__name__)

# Default route
@app.route("/", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def authenticate():
    """
    Gère les requêtes uniquement de type POST sur la route '/' de l'application.
    """
    firstname = request.form['prenom']
    name = request.form['nom']

    if firstname == "" or name == "":
        # Retourner un message d'erreur avec status BAD REQUEST
        # Ne redirige pas l'utilisateur (Ne crée pas le patron POST REDIRECT GET)
        return render_template('login.html', error="Il manque des choses"), 400

    file = open("log.txt", "w")
    file.write(f"{firstname}{name}")
    file.close()

    # Redirige l'utilisateur (POST REDIRECT GET !!!)
    # url_for retourne la route pour la fonction home (ligne 33)
    return redirect(url_for("home", firstname=firstname))

@app.route("/home", methods=["GET"])
def home():
    """Greets the user when logged in"""
    firstname = request.args["firstname"]
    return render_template("home.html", firstname=firstname)

# Ceci sera vrai seulement si le fichier
# app.py est utilisé comme point d'entrée de l'interpréteur.
if __name__ == "__main__":
    app.run()
