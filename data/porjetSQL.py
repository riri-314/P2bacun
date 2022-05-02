#!/usr/bin/env python

import sqlite3
from wts import wts
#BY Delphin Blehoussi
# WTS = Write To Sqlite
#installation du package https://pypi.org/project/wts/ donc le github est https://github.com/Chaton-mechant/WTS
#tuto :
# Ecrire dans le terminal : 
#1)url https://bootstrap.pypa.io/get-pip.py -o get-pip.py.
#2)python get-pip.py 
#3)pip --version
#4)pip install wts
#5) Enfin importer le package dans le code :
# from wts import wts
#l'étape 1 à 3 est pâs nécessaire.
#exemple simple :
#from wts import wts
#wts.wts("cows_inserts.sql", "cows.sqlite")
#cows.sqlite and cows_inserts.sql sont ainsi crées
#/!!!ATTENTION!!!\
#Vos commandes doivent être des commandes sql insert valides.
#Vos fichiers sql doivent être dans le même répertoire que le fichier de base de données.

x =  sqlite3.connect('ProjetSQl.sqlite')
# peut acceder à ce fichier grace à la fonction sqlite3.connect()
#return une class connection qui permet d’interagir avec la base de données

cursor = x.cursor()
# Le curseur permettra l'envoi des commandes SQL

# utilisation de la base de données
def CreateTable(n):
    if n != None:
        cursor.execute('''CREATE TABLE familles
        (
        id     INT PRIMARY KEY     NOT NULL,
        nom    TEXT                NOT NULL

        );''')


        cursor.execute('''CREATE TABLE animaux
        (
        id               INT PRIMARY KEY     NOT NULL,
        famille_id       INT                 NOT NULL,
        sexe             TEXT                NOT NULL,
        presence         INT                 NOT NULL,
        apprivoise       INT                 NOT NULL,
        mort_ne          INT                 NOT NULL,
        decede           INT                 NOT NULL,
        FOREIGN KEY (famille_id) REFERENCES familles(id)

        );''')

        cursor.execute('''CREATE TABLE types
        (
        id         INT PRIMARY KEY     NOT NULL,
        type       TEXT                NOT NULL

        );''')


        cursor.execute('''CREATE TABLE animaux_types
        (
        animal_id    INT               NOT NULL,
        type_id      INT               NOT NULL,
        pourcentage  REAL               NOT NULL,
        FOREIGN KEY (type_id) REFERENCES types(id),
        FOREIGN KEY (animal_id) REFERENCES animaux(id),
        PRIMARY KEY (animal_id, type_id)
        );''')


        cursor.execute('''CREATE TABLE velages
        (
        id        INT PRIMARY KEY  NOT NULL,
        mere_id   INT              NOT NULL,
        pere_id   INT              NOT NULL,
        date      TEXT             NOT NULL,
        FOREIGN KEY (mere_id) REFERENCES animaux(id),
        FOREIGN KEY (pere_id) REFERENCES animaux(id)

        );''')

        cursor.execute('''CREATE TABLE animaux_velages
        (
        animal_id INT                 NOT NULL,
        velage_id INT                 NOT NULL,
        FOREIGN KEY (animal_id) REFERENCES animaux(id),
        FOREIGN KEY (velage_id) REFERENCES velages(id),
        PRIMARY KEY (animal_id,velage_id)

        );''')

        cursor.execute('''CREATE TABLE complications
        (
        id             INT PRIMARY KEY     NOT NULL,
        complication   TEXT                NOT NULL

        );''')

        cursor.execute('''CREATE TABLE velages_complications
        (
        velage_id        INT     NOT NULL,
        complication_id  INT     NOT NULL,
        FOREIGN KEY (velage_id) REFERENCES velages(id),
        FOREIGN KEY (complication_id) REFERENCES complications(id),
        PRIMARY KEY (velage_id,complication_id)

        );''')
    else:
        pass




#créer par Delphin Blehoussi
#CreateTable(112)
def Insert(ListInsert):
    #ListInsert est une liste contenant le nom des fichiers SQL
    a = "ProjetSQL.sqlite"
    for x in ListInsert:
        wts.wts(x, "ProjetSQL.sqlite")
     

ListInsert=["insert_familles.sql","insert_animaux.sql","insert_types.sql","insert_animaux_types.sql","insert_velages.sql",
            "insert_animaux_velages.sql","insert_complications.sql","insert_velages_complications.sql"]

x.commit()
# Si on a fait des modifications à la base de données,
#C'est pour forcer l’écriture des modifications.

x.close()
# Toujours fermer la connexion quand elle n'est plus utile
