##install##
python3 
sqlite3
wts (write to sqlite) "pip install wts" read comments in projetSQL.py for more info

###run##
run main.py with command python3 main.py
p2.sqlite has to be on the same directory as main.py

###/data###
creat_sql.py create an empty sql db named p2.sqlite
animals.sql is a set of data 
add_data.py adds a set of data to the dbnamed p2.sqlite, p2.sqlite has to	be on the same directory as add_data.py, read comments in the code for more info  






###vélages###
user input: Year, month, name (nom de famille)
graphe output: graphe with born dead-born over the month of the selected Year
    ->if no month but year, show the whole year
    ->if no year but month, show month of the last year (2022)
    ->if no famille, choose a random famille