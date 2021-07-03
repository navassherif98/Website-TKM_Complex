from flask import render_template ,url_for,flash,redirect,send_from_directory
from tkmcomplex import app
from tkmcomplex.data import shops

@app.route("/")
def home():
    logo=url_for('static',filename='images/TKM_logo_icon.png')
    return render_template('home.html',title='Home',shop=shops,logo=logo)

@app.route("/.well-known/brave-rewards-verification.txt")
def brave():
    return send_from_directory("static",".well-known/brave-rewards-verification.txt")