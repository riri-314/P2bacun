#!/usr/bin/python3

#imports
from flask import Flask, render_template, request
import sqlite3

# creat app
app = Flask(__name__, template_folder='templates')
# app.debug = False

# cursor to db
conn = sqlite3.connect('p2.sqlite', check_same_thread=False)
cursor = conn.cursor()

# fun that count the number of male in the database
def nb_male():
	count = 0
	for x in cursor.execute("SELECT sexe FROM animaux"):
		#print(x)
		if x == ('M',):
			count += 1
	return count
print(nb_male())
# fun for the front page
@app.route("/")
def home():
    male = nb_male() #number of males in the db
    return render_template("home.html", male=male)

# launch site
if __name__ == '__main__':
    app.run()
