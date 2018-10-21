import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# To create auto-incrementing primary keys, the type MUST be the full word, INTEGER 
create_users_table = """
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    username text, 
    password text
  )
"""

cursor.execute(create_users_table)

connection.commit()
connection.close()