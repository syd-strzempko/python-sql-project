import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO entries (title, lat, long, author) VALUES (?, ?, ?, ?)",
            ('Southwest', 0, 0, 'Syd')
            )

cur.execute("INSERT INTO entries (title, lat, long, author) VALUES (?, ?, ?, ?)",
            ('Northeast', 1, 1, 'Syd')
            )

cur.execute("INSERT INTO entries (title, lat, long, author) VALUES (?, ?, ?, ?)",
            ('Southeast', 0, 1, 'Syd')
            )

cur.execute("INSERT INTO entries (title, lat, long, author) VALUES (?, ?, ?, ?)",
            ('Northwest', 1, 0, 'Brandon')
            )

connection.commit()
connection.close()