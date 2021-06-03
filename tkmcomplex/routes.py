from flask import render_template ,url_for,flash,redirect
from tkmcomplex import app
from tkmcomplex.data import shops

@app.route("/")
def home():
    logo=url_for('static',filename='images/TKM_logo_icon.png')
    return render_template('home.html',title='Home',shop=shops,logo=logo)

@app.route("/4U")
def fouryou():
    return render_template('4u.html',title='4U')

