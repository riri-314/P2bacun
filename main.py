#!/usr/bin/python3

#imports
from flask import Flask, render_template, request
import sqlite3


# creat app
app = Flask(__name__, template_folder='templates')
# app.debug = False

# cursor to db
conn = sqlite3.connect('ProjetSQl.sqlite', check_same_thread=False)
cursor = conn.cursor()

def families():
	families_lst = []
	for i in cursor.execute("SELECT nom from familles"):
		families_lst.append(i)
	return families_lst

familles = families()


months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
years = list(range(1990, 2020))

# fun that count the number of male in the database
def nb_male():
	count = 0
	for x in cursor.execute("SELECT sexe FROM animaux"):
		#print(x)
		if x == ('M',):
			count += 1
	return count
#print(nb_male())
# fun for the front page
@app.route("/")
def home():
    male = nb_male() #number of males in the db
    return render_template("home.html", familles = familles, months = months, years = years, male=male)

# launch site
if __name__ == '__main__':
    app.run()
