import sqlite3
import sockets
import datetime

def date():
    now = datetime.datetime.now()
    return f"{now.day}.{now.month}.{now.year}"

def time():
    now = datetime.datetime.now()
    return f"{now.hour}.{now.minute}.{now.second}.{now.microsecond}"

def add_msg(sender, message, type="txt"):
    cursor.execute("INSERT INTO messages VALUES (?, ?, ?, ?, ?)", (date(), time(), sender, type, message))
    conn.commit()

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

add_msg(sender="I", message="Hi!")

