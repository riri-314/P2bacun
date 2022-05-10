##install## 
python3 ; Included in python IDE
sqlite3 ; command to install on terminal 'pip install pysqlite3' 
Flask ; command to install on terminal 'pip install Flask'

###run##
run main.py with command python3 main.py
p2.sqlite has to be on the same directory as main.py


##TreeStructure##
Main folder{
  main.py; contains @app.route that runs the website, as well as, interior functions that helps calculate or run the code for simplicity. 
}

data Folder{
  creat_sql; creates a db named p2.sqlite in the main folder. 
  add_data.py adds a set of data to the dbnamed p2.sqlite, p2.sqlite has to be on the same directory as add_data.py, read comments in the code for more info   
}

templates Folder{
  home.html; is referenced back in main and is run by Flask in order to display as said in the html file. 
  menue.html; contains the 'Accueil' button that helps run back to the home page incase of unexpected errors.
  moon_test.html, races_test.html, velages_test.html; all contain the Chart.js and are adjusted to function as required based on their title.
}

static Folder{
  home.css; is the graphic design aspect of the page, except for color.
}


