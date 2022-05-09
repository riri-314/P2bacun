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
				tmp_date =[]
				y_axis = []
				j = 0
				full_moon_dates = ['11/01/1990', '09/02/1990', '11/03/1990', '10/04/1990', '09/05/1990', '08/06/1990', '08/07/1990', '08/08/1990', '05/09/1990', '04/10/1990', '02/11/1990', '02/12/1990', '31/12/1990', '30/01/1991', '28/02/1991', '30/03/1991', '28/04/1991', '28/05/1991', '27/06/1991', '26/07/1991', '25/08/1991', '23/09/1991', '23/10/1991', '21/11/1991', '21/12/1991', '19/01/1992', '18/02/1992', '18/03/1992', '17/04/1992', '16/05/1992', '15/06/1992', '14/07/1992', '13/08/1992', '12/09/1992', '11/10/1992', '10/11/1992', '09/12/1992', '08/01/1993', '06/02/1993', '11/03/1993', '06/04/1993', '06/05/1993', '04/06/1993', '03/07/1993', '02/08/1993', '01/09/1993', '30/09/1993', '30/10/1993', '29/11/1993', '28/12/1993', '27/01/1994', '26/02/1994', '27/03/1994', '25/04/1994', '25/05/1994', '23/06/1994', '22/07/1994', '21/08/1994', '19/09/1994', '19/10/1994', '18/11/1994', '18/12/1994', '16/01/1995', '15/02/1995', '17/03/1995', '15/04/1995', '14/05/1995', '13/06/1995', '12/07/1995', '10/08/1995', '09/09/1995', '08/10/1995', '07/11/1995', '07/12/1995', '05/01/1996', '04/02/1996', '05/03/1996', '04/04/1996', '03/05/1996', '01/06/1996', '01/07/1996', '30/07/1996', '28/08/1996', '27/09/1996', '26/10/1996', '25/11/1996', '24/12/1996', '23/01/1997', '22/02/1997', '24/03/1997', '22/04/1997', '22/05/1997', '20/06/1997', '20/07/1997', '18/08/1997', '16/09/1997', '16/10/1997', '14/11/1997', '14/12/1997', '12/01/1998', '11/02/1998', '13/03/1998', '11/04/1998', '11/05/1998', '10/06/1998', '09/07/1998', '08/08/1998', '06/09/1998', '05/10/1998', '04/11/1998', '03/12/1998', '02/01/1999', '31/01/1999', '02/03/1999', '31/03/1999', '30/04/1999', '30/05/1999', '28/06/1999', '28/07/1999', '26/08/1999', '25/09/1999', '24/10/1999', '23/11/1999', '22/12/1999', '21/01/2000', '19/02/2000', '20/03/2000', '18/04/2000', '18/05/2000', '16/06/2000', '16/07/2000', '15/08/2000', '13/09/2000', '13/10/2000', '11/11/2000', '11/12/2000', '09/01/2001', '08/02/2001', '09/03/2001', '08/04/2001', '07/05/2001', '06/06/2001', '05/07/2001', '04/08/2001', '02/10/2001', '01/11/2001', '30/11/2001', '30/12/2001', '28/01/2002', '27/02/2002', '28/03/2002', '27/04/2002', '26/05/2002', '24/06/2002', '24/07/2002', '22/08/2002', '21/09/2002', '21/10/2002', '20/11/2002', '19/12/2002', '18/01/2003', '16/02/2003', '18/03/2003', '16/04/2003', '16/05/2003', '14/06/2003', '13/07/2003', '12/08/2003', '10/09/2003', '10/10/2003', '09/11/2003', '08/12/2003', '07/01/2004', '06/02/2004', '06/03/2004', '05/04/2004', '04/05/2004', '03/06/2004', '02/07/2004', '31/07/2004', '30/08/2004', '28/09/2004', '28/10/2004', '26/11/2004', '26/12/2004', '25/01/2005', '24/02/2005', '25/03/2005', '24/04/2005', '23/05/2005', '22/06/2005', '21/07/2005', '19/08/2005', '18/09/2005', '17/10/2005', '16/11/2005', '15/12/2005', '14/01/2006', '13/02/2006', '14/03/2006', '13/04/2006', '13/05/2006', '11/06/2006', '11/07/2006', '09/08/2006', '07/09/2006', '07/10/2006', '05/11/2006', '05/12/2006', '03/01/2007', '02/02/2007', '03/03/2007', '02/04/2007', '02/05/2007', '01/06/2007', '30/06/2007', '30/07/2007', '28/08/2007', '26/09/2007', '26/10/2007', '24/11/2007', '24/12/2007', '22/01/2008', '21/02/2008', '21/03/2008', '20/04/2008', '20/05/2008', '18/06/2008', '18/07/2008', '16/08/2008', '15/09/2008', '14/10/2008', '13/11/2008', '12/12/2008', '11/01/2009', '09/02/2009', '11/03/2009', '09/04/2009', '09/05/2009', '07/06/2009', '07/07/2009', '06/08/2009', '04/09/2009', '04/10/2009', '02/11/2009', '02/12/2009', '31/12/2009', '30/01/2010', '28/02/2010', '30/03/2010', '28/04/2010', '27/05/2010', '26/06/2010', '26/07/2010', '24/08/2010', '23/09/2010', '23/10/2010', '21/11/2010', '21/12/2010', '19/01/2011', '18/02/2011', '19/03/2011', '18/04/2011', '17/05/2011', '15/06/2011', '15/07/2011', '13/08/2011', '12/09/2011', '12/10/2011', '10/11/2011', '10/12/2011', '09/01/2012', '07/02/2012', '08/03/2012', '06/04/2012', '06/05/2012', '04/06/2012', '03/07/2012', '02/08/2012', '31/08/2012', '30/09/2012', '29/10/2012', '28/11/2012', '27/01/2013', '25/02/2013', '27/03/2013', '25/04/2013', '25/05/2013', '23/26/2013', '22/07/2013', '21/08/2013', '19/09/2013', '18/10/2013', '17/11/2013', '17/12/2013', '16/01/2014', '14/02/2014', '16/03/2014', '15/04/2014', '14/05/2014', '13/06/2014', '12/07/2014', '10/08/2014', '09/09/2014', '08/10/2014', '06/11/2014', '06/12/2014', '05/01/2015', '03/02/2015', '05/03/2015', '04/04/2015', '04/05/2015', '02/06/2015', '02/07/2015', '31/07/2015', '29/08/2015', '28/09/2015', '27/10/2015', '25/11/2015', '25/12/2015', '24/01/2016', '22/02/2016', '23/03/2016', '22/04/2016', '21/05/2016', '20/06/2016', '19/07/2016', '18/08/2016', '16/09/2016', '16/10/2016', '14/11/2016', '14/12/2016', '12/01/2017', '11/02/2017', '12/03/2017', '11/04/2017', '10/05/2017', '09/06/2017', '09/07/2017', '07/08/2017', '06/09/2017', '05/10/2017', '04/11/2017', '03/12/2017', '02/01/2018', '31/01/2018', '02/03/2018', '31/03/2018', '30/04/2018', '29/05/2018', '28/06/2018', '27/07/2018', '26/08/2018', '25/09/2018', '24/10/2018', '23/11/2018', '22/12/2018', '21/01/2019', '29/02/2019', '21/03/2019', '19/04/2019', '18/05/2019', '17/06/2019', '16/07/2019', '15/08/2019', '14/09/2019', '13/10/2019', '12/11/2019', '12/12/2019', '10/01/2020', '09/02/2020', '09/03/2020', '08/04/2020', '07/05/2020', '05/06/2020', '05/07/2020', '03/08/2020', '02/09/2020', '01/10/2020', '31/10/2020', '30/11/2020', '30/12/2020']

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

				for x in tmp_date:
					for y in full_moon_dates:
						if y == x:
							#print("velage full moon: ", x)
							j += 1
				y_axis.append(j)
				y_axis.append(len(tmp_date)-j)

				return flask.render_template("moon.html", y = y_axis)
		
		if graph == "Distribution des races":
			print("ToDo")
		

			
	male = nb_male() #number of males in the db
	return render_template("home.html", familles = familles, months = months, years = years, male=male)

# launch site
if __name__ == '__main__':
    app.run()
