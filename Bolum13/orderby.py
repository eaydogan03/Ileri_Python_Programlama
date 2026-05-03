import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

sql="SELECT * FROM urunler ORDER BY fiyat DESC"

cursor.execute(sql)

sonuclar=cursor.fetchall()

for s in sonuclar:
    print(s)

db.close()