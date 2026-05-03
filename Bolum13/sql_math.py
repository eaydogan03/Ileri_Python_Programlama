import sqlite3

db=sqlite3.connect("btk_akademi.db")
cursor=db.cursor()

# sql="SELECT SUM(stok_adedi), AVG(fiyat) FROM urunler"
# cursor.execute(sql)
# toplam_stok, ortalama_fiyat = cursor.fetchone()

# print(f"Toplam Stok: {toplam_stok}")
# print(f"Ortalama Fiyat: {ortalama_fiyat}")

sql="SELECT MIN(fiyat), MAX(fiyat) FROM urunler"
cursor.execute(sql)

min_fiyat, max_fiyat = cursor.fetchone()

print(f"En düşük Fiyat: {min_fiyat}")
print(f"En yüksek Fiyat: {max_fiyat}")

db.close()



