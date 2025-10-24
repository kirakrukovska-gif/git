import os
print(os.path.abspath("AnimalKingdom"))

import sqlite3
 
connection = sqlite3.connect("AnimalKingdom", timeout=5)
cur = connection.cursor()
print(connection)
print(cur)
connection.close()
 
import sqlite3
connection = sqlite3.connect("AnimalKingdom", timeout=5)
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Animals (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, type TEXT);")
connection.commit()
connection.close()


import sqlite3
connection = sqlite3.connect("AnimalKingdom", timeout=5)
cur = connection.cursor()
cur.execute("INSERT INTO Animals (name , type) VALUES ('Лев' , 'Ссавець');")
cur.execute("INSERT INTO Animals (name , type) VALUES ('Крокодил' , 'Плазун');")
cur.execute("INSERT INTO Animals (name , type) VALUES ('Орел' , 'Птах');")
cur.execute("INSERT INTO Animals (name , type) VALUES ('Морська черепаха' , 'Плазун');")
cur.execute("INSERT INTO Animals (name , type) VALUES ('Мавпа' , 'Ссавець');")
connection.commit()
connection.close()

import sqlite3
connection = sqlite3.connect("AnimalKingdom", timeout=5)
cur = connection.cursor()
cur.execute("UPDATE Animals SET name = 'Сокіл' WHERE name ='Орел';")
connection.commit()
connection.close()

import sqlite3
connection = sqlite3.connect("AnimalKingdom", timeout=5)
cur = connection.cursor()
cur.execute("SELECT name, type FROM Animals WHERE type ='Ссавець';")
res = cur.fetchall()
print("Ссавці - " , res)
connection.close()

import sqlite3
connection = sqlite3.connect("AnimalKingdom", timeout=5)
cur = connection.cursor()
cur.execute("SELECT name, type FROM Animals;")
res = cur.fetchall()
print("Усі тварини - " , res)
connection.close()
