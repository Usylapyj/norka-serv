import sqlite3
 
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE messages (date, time, sender, type, message)")
