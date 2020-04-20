# Program Header
# Course: CIS 117 Python Programming
# Name:   Gerardo Perez
# Description: Python program that creates a database: a
# table and insert data. After creation of database, a series of
# sqlite statements will be executed using the created database.
#
# Lab #9: sqlite3: Creating and Using a Database 
#
#
# Development Environment: IDLE(Python 3.7 32-bit)
# Version: Python 3.7.3
# Solution File: gerardoPerezlab10.py
# Date:  04/23/2019
#################################################


# Programs Source Statements


import sqlite3

# Creates database using sqlite3
con = sqlite3.connect('perez.db')

# Esatablishes handle to the database connection
cur = con.cursor()

# Creates table with 2 columns
cur.execute('CREATE TABLE PopByRegion(Region TEXT, Population INTEGER)')

# Data entry for database 
cur.execute('INSERT INTO PopByRegion VALUES("Central Africa", 330993)')
cur.execute('INSERT INTO PopByRegion VALUES("Southeastern Africa", 743112)')
cur.execute('INSERT INTO PopByRegion VALUES("Japan", 100562)')


# Commit changes
con.commit()

# Close Connection
con.close()


# Program Output (Commented out)

"""
>>> import sqlite3
>>> con = sqlite3.connect('perez.db')
>>> cur = con.cursor()
>>> cur.execute('SELECT Region, Population FROM PopByRegion')
<sqlite3.Cursor object at 0x10674d960>
>>> cur.fetchall()
[('Central Africa', 330993), ('Southeastern Africa', 743112), ('Japan', 100562)]
>>> cur.execute('SELECT Region, Population FROM PopByRegion ORDER by Region')
<sqlite3.Cursor object at 0x10674d960>
>>> cur.fetchall()
[('Central Africa', 330993), ('Japan', 100562), ('Southeastern Africa', 743112)]
>>> cur.execute('SELECT Region FROM PopByRegion')
<sqlite3.Cursor object at 0x10674d960>
>>> cur.fetchall()
[('Central Africa',), ('Southeastern Africa',), ('Japan',)]
>>> cur.execute ('SELECT Region FROM PopbyRegion WHERE Population > 400000')
<sqlite3.Cursor object at 0x10674d960>
>>> cur.fetchall()
[('Southeastern Africa',)]
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x10674d960>
>>> cur.fetchone()
('Japan', 100562)
>>> cur.execute('''UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan"''')
<sqlite3.Cursor object at 0x10674d960>
>>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
<sqlite3.Cursor object at 0x10674d960>
>>> cur.fetchone()
('Japan', 100600)
>>> cur.execute('DELETE FROM PopByRegion WHERE Region < "S"')
<sqlite3.Cursor object at 0x10674d960>
>>> cur.execute('SELECT * FROM PopByRegion')
<sqlite3.Cursor object at 0x10674d960>
>>> cur.fetchall()
[('Southeastern Africa', 743112)]
>>> cur.close()
>>> con.close()
"""
