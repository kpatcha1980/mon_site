from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("inscription.html")

@app.route("/inscription", methods=["POST"])
def inscription():
    nom = request.form["nom"]
    prenom = request.form["prenom"]
    classe = request.form["classe"]
    email = request.form["email"]

    with open("inscrits.txt", "a", encoding="utf-8") as fichier:
        fichier.write(f"{prenom} {nom} - {classe} - {email}\n")

    return f"Merci {prenom} {nom} ! Tu es bien enregistré. <br><a href='/liste'>Voir la liste des inscrits</a>"

@app.route("/liste")
def liste():
    try:
        with open("inscrits.txt", "r", encoding="utf-8") as fichier:
            inscrits = fichier.readlines()
    except FileNotFoundError:
        inscrits = []
    return "<br>".join(inscrits) + "<br><br><a href='/'>Retour</a>"

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)