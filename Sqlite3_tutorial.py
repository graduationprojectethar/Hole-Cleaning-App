import sqlite3

con = sqlite3.connect('tryy.db')
cursor = con.cursor()

# cursor.execute("DROP TABLE users")
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
)""")
cursor.execute("INSERT INTO users(name,age) VALUES('hassan',27)")
cursor.execute("INSERT INTO users(name,age) VALUES('mahmood',22)")
data = cursor.execute("SELECT * FROM users")
for row in data:
    print(row)
con.commit()
con.close()

# sqlite3 movies.db .dump > movies.sql
