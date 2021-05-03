import sqlite3
conn=sqlite3.connect('numbers_database.db')
c=conn.cursor()

output = conn.execute("SELECT * FROM numbers_table")
for i in output:
    print(i)

c.close()