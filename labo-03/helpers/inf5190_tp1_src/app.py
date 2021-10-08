from flask import Flask


# Initialise l'application Flask
app = Flask(__name__)


# Ceci sera vrai seulement si le fichier
# app.py est utilisé comme point d'entrée de l'interpréteur.
if __name__ == "__main__":
    app.run()
