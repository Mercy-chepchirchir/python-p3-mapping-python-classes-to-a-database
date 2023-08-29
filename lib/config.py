import sqlite3
# it establishes connection with the database
CONN = sqlite3.connect('music.db')
# it enables us to interact with the database
CURSOR = CONN.cursor() 