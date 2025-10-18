import os
print(os.path.abspath("itstep_DB.sl3"))

import sqlite3
 
connection = sqlite3.connect("itstep_DB.sl3", timeout=5)
cur = connection.cursor()
print(connection)
print(cur)
connection.close()
 
import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", timeout=5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Nick');")
connection.commit()
connection.close()


import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", timeout=5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Ann');")
cur.execute("INSERT INTO first_table (name) VALUES ('Kats');")
cur.execute("INSERT INTO first_table (name) VALUES ('John');")
connection.commit()
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()

import sqlite3
connection = sqlite3.connect("itstep_DB.sl3", timeout=5)
cur = connection.cursor()
cur.execute("DELETE FROM first_table WHERE rowid=4;")
# connection.commit()
cur.execute("SELECT rowid, name FROM first_table WHERE rowid=3;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()
 
 
 