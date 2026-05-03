import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

sql="INSERT INTO urunler (urun_adi, fiyat, stok_adedi) VALUES (?, ?, ?)"

#values=("IPHONE 15", 65000, 7)

#cursor.execute(sql, values)

liste=[
    ("Mouse", 1500, 10),
    ("Monitor",10000, 5),
    ("Klavye", 2000, 9)
]

cursor.executemany(sql, liste)

db.commit()

db.close()


