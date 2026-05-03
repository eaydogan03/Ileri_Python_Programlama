import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

sql="SELECT * FROM urunler WHERE fiyat >= ? AND stok_adedi > 0"

cursor.execute(sql, (50000,))

sonuclar=cursor.fetchall()

for s in sonuclar:
    print(s)

db.close()