import sqlite3 as lite
import sys
con = lite.connect('assignment1.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS ass1_data")
    cur.execute("CREATE TABLE ass1_data(timestamp DATETIME, temperature NUMERIC, humidity NUMERIC)")
