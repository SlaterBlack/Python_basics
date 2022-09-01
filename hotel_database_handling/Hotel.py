import sqlite3

con = sqlite3.connect('hotel.db')
cursor = con.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

cursor.execute("SELECT * FROM Hotel;")
print(cursor.fetchall())

names = list(map(lambda x : x[0], cursor.description))
print(names)

cursor.execute("SELECT * FROM Hotel WHERE city = 'Brisbane';")
print(cursor.fetchall()) 

cursor.execute("SELECT guestName, guestAddress FROM Guest ORDER BY guestName;")
print(cursor.fetchall())

cursor.execute("SELECT price, roomtype FROM Room,Hotel;")
print(cursor.fetchall())