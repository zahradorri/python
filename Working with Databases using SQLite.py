Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
... 
... # Connecting to SQLite database
... conn = sqlite3.connect('example.db')
... cursor = conn.cursor()
... 
... # Creating a table
... cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
... 
... # Inserting data
... cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('John', 25))
... conn.commit()
... 
... # Querying data
... cursor.execute('''SELECT * FROM users''')
... result = cursor.fetchall()
... print(result)
... 
... # Closing the connection
