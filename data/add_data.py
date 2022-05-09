# import
import sqlite3

# connect to db
conn = sqlite3.connect('p2.sqlite', check_same_thread=False)
cursor = conn.cursor()

# found on the internet
# input: list of files containing data to add to db
def incerte_data(files):
    for i in files :
        file = open(i,'r',encoding='utf-8') #open the file 
        lignes=file.readlines() # read a line in the file
        file.close() # close file
        tmp=[]
        for j in lignes :
                tmp.append(j.strip()) # remove space at start and end

        for i in tmp :
                cursor.execute(i) # add the line to the db


files = ["insert_velages_complications.sql", "insert_velages.sql", "insert_types.sql", "insert_familles.sql", "insert_complications.sql", "insert_animaux_velages.sql", "insert_animaux_types.sql", "insert_animaux.sql"]
incerte_data(files)

conn.commit()
conn.close()

