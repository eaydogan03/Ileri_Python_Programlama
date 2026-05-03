import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

sql="SELECT * FROM urunler"

cursor.execute(sql)

# urun=cursor.fetchone()
# print(urun)

urunler=cursor.fetchall()
for u in urunler:
    print(f"ID: {u[0]}, Ürün Adı: {u[1]}, Stok Adedi: {u[3]}")

toplam=0
for urun in urunler:
    toplam += urun[3]
print(toplam)


db.close()
