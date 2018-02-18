from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import datetime
import os
app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'bank'

mysql.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

t@app.route('/home2')
def home2():
    return render_template('home2.html')


@app.route('/munten')
def munten():
    return render_template('munten.html')

@app.route('/transacties')
def transacties():
    return render_template('transacties.html')

@app.route('/overzichten')
def overzichten():
    return render_template('overzichten.html')

@app.route('/klanten')
def klanten():
    return render_template('klanten.html')

@app.route('/klanten_reg')
def klanten_reg():
    return render_template('klanten_reg.html')


class KlantRegistratie(Form):
    voornaam = StringField('voornaam',[validators.length(min=1, max=50)])
    achternaam = StringField('achternaam', [validators.length(min=1, max=50)])
    adres = StringField('adres', [validators.length(min=1, max=50)])
    telefoon = StringField('telefoon', [validators.length(min=6, max=20)])
    rek_num = StringField('rek_num', [validators.length(min=6, max=7)])

@app.route('/klant_reg', methods=['GET', 'POST'])
def registreer():
    form = KlantRegistratie(request.form)
    if request.method == 'POST' and form.validate():
        voornaam = form.voornaam.data
        achternaaam = form.achternaam.data
        adres = form.adres.data
        telefoon = form.telefoon.data
        rek_num = form.rek_num.data

        #create cursor
        cur = mysql.connection.cursor()

        #execute query
        cur.execute("INSERT INTO klanten(voornaam, achternaam, adres, telefoon, rek_num) VALUES(%s, %s, %s, %s, %s)", (voornaam, achternaaam, adres, telefoon, rek_num))

        #commit to database
        mysql.connection.commit()

        #close connection
        cur.close()

        #flash('klant is toegevoegd', 'success')

    #return render_template('klanten.html')
    return render_template('klant.html', form=form)


@app.route('/validatie', methods=['POST'])
def validatie():
    naam = str(request.form['naam'])
    wachtwoord = str(request.form['wachtwoord'])

    try:
        cursor = mysql.connect.cursor()
        cursor.execute("SELECT * FROM users WHERE naam='"+ naam+"' AND wachtwoord= '"+ wachtwoord + "'")
        user = cursor.fetchone()

        if user[1] == 1:
            return redirect(url_for('home'))
        elif user[1] == 2:
            return redirect(url_for('home2'))
        else:
            return "fout geconstateerd"

    except Exception as e:
        return e

if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)