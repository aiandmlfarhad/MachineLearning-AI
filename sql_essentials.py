import sqlite3 as sq
con = sq.connect('database.db')
cor = con.cursor()
con.commit()
for row in con.execute('SELECT * FROM accounts WHERE wallet > 300 '):
    print(row)
con.close()