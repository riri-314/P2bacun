#!/usr/bin/python3

#imports
import tempfile
from flask import Flask, render_template, request
import sqlite3

import flask


# creat app
app = Flask(__name__, template_folder='templates')
# app.debug = False

# cursor to db
conn = sqlite3.connect('p2.sqlite', check_same_thread=False)
cursor = conn.cursor()

def families():
	families_lst = []
	for i in cursor.execute("SELECT nom from familles"):
		families_lst.append(i[0])
	families_lst.sort()
	return families_lst

familles = families()

months = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Décembre"]
years = list(range(1990, 2020))

# fun that count the number of male in the database
def nb_male():
	count = 0
	for x in cursor.execute("SELECT sexe FROM animaux"):
		if x == ('M',):
			count += 1
	return count

def month(month):
	if month == "Janvier":
		return "01"
	elif month == "Février":
		return "02"
	elif month == "Mars":
		return "03"
	elif month == "Avril":
		return "04"
	elif month == "Mai":
		return "05"
	elif month == "Juin":
		return "06"
	elif month == "Juillet":
		return "07"
	elif month == "Aout":
		return "08"
	elif month == "Septembre":
		return "09"
	elif month == "Octobre":
		return "10"
	elif month == "Novembre":
		return "11"
	elif month == "Décembre":
		return "12"
	else:
		return 5
			
# fun for the front page
@app.route("/", methods=('GET','POST'))
def home():
	if flask.request.method == 'POST':
		famille = flask.request.form["famille"]
		mois = month(flask.request.form["mois"])
		année = flask.request.form["annee"]
		graph = flask.request.form["graph"]
		
		#graphe for velages
		if graph == "Nombre de velages":
				tmp_date =[]
				x_axis = []
				y_axis = []
				j = 0
				if famille == "Choisissez une famille":
					if mois == "Choisissez un mois":
						for x in cursor.execute("SELECT date FROM velages WHERE date LIKE '%%/%%/{}'".format(année)):
							#print(x[0])
							tmp_date.append(x[0])
					else:
						for x in cursor.execute("SELECT date FROM velages WHERE date LIKE '%%/{}/{}'".format(mois, année)):
							tmp_date.append(x[0])
				else:
					if mois == "Choisissez un mois":
						for x in cursor.execute("SELECT date FROM velages WHERE date LIKE '%%/%%/{}' AND id IN(SELECT velage_id FROM animaux_velages WHERE animal_id IN (SELECT id FROM animaux WHERE famille_id = (SELECT id FROM familles WHERE nom LIKE '{}')))".format(année, famille)):
							tmp_date.append(x[0])	
					else:
						for x in cursor.execute("SELECT date FROM velages WHERE date LIKE '%%/{}/{}' AND id IN(SELECT velage_id FROM animaux_velages WHERE animal_id IN (SELECT id FROM animaux WHERE famille_id = (SELECT id FROM familles WHERE nom LIKE '{}')))".format(mois, année, famille)):
							tmp_date.append(x[0])
		
				tmp_date.sort()
				#print(tmp_date)

				if len(tmp_date) == 0:
					y_bis = 0
					x_bis = "Pas de vélages sur cette période"
					return x_bis, y_bis
		
				y_axis.append(tmp_date[0])
	
		
				for x in range(len(tmp_date)):
					if tmp_date[x] != tmp_date[x-1]:
						if x != 0:
							y_axis.append(tmp_date[x]) 
						x_axis.append(1)
						j += 1
					else:
						if j == 0:
							x_axis.append(1)
							j += 1
						else:
							x_axis[j-1] += 1 
#				print(x_axis)
#				print(y_axis)
				return flask.render_template("velages.html", x = y_axis, y = x_axis)
		
		if graph == "Pleine Lune":
			print("ToDo")
		
		if graph == "Distribution des races":
			print("ToDo")
		

			
	male = nb_male() #number of males in the db
	return render_template("home.html", familles = familles, months = months, years = years, male=male)

# launch site
if __name__ == '__main__':
    app.run()
